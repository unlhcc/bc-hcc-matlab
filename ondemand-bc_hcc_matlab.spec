# Disable debuginfo as it causes issues with bundled gems that build libraries
%global debug_package %{nil}
%global repo_name bc-hcc-matlab
%global app_name bc_hcc_matlab
%{!?package_version: %define package_version %{major}.%{minor}.%{patch}}
%{!?package_release: %define package_release 1}
%{!?git_tag: %define git_tag v%{package_version}}
%define git_tag_minus_v %(echo %{git_tag} | sed -r 's/^v//')

Name:     ondemand-%{app_name}
Version:  %{package_version}
Release:  %{package_release}%{?dist}
Summary:  Batch Connect - HCC MATLAB

Group:    System Environment/Daemons
License:  MIT
URL:      https://git.unl.edu/hcc/bc-hcc-matlab
Source0:  bc-hcc-matlab.tar.gz

Requires: ondemand

# Disable automatic dependencies as it causes issues with bundled gems and
# node.js packages used in the apps
AutoReqProv: no

%description
A Batch Connect app designed to launch the MATLAB GUI with a batch job.

%prep
%setup -q -n %{repo_name}-%{git_tag_minus_v}


%build


%install
export PASSENGER_APP_ENV=production
export PASSENGER_BASE_URI=/pun/sys/%{app_name}
mkdir -p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}
if [ -x bin/setup ]; then
    bin/setup
fi
cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/


%files
%defattr(-,root,root)
%{_localstatedir}/www/ood/apps/sys/%{app_name}
%{_localstatedir}/www/ood/apps/sys/%{app_name}/manifest.yml


%changelog
%changelog
* Tue Jul 06 2021 Adam Caprez <acaprez2@unl.edu> v%{version}-%{release}
- initial version based off of https://github.com/OSC/bc_osc_matlab/blob/master/packaging/ondemand-bc_osc_matlab.spec
