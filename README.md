# Batch Connect - HCC MATLAB

[![pipeline status](https://git.unl.edu/hcc/bc-hcc-matlab/badges/master/pipeline.svg)](https://git.unl.edu/hcc/bc-hcc-matlab/-/commits/master)
[![GitHub License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A Batch Connect app designed for OSC OnDemand that launches MATLAB within an
SLURM batch job.

## Prerequisites

This Batch Connect app requires the following software be available on the
**compute nodes** that the batch job is intended to run on (**NOT** the
OnDemand node):

- [MATLAB] R2016b+
- [Singularity]
- [Lmod]

[MATLAB]: https://www.mathworks.com
[Singularity]: https://sylabs.io/singularity/
[Xfce Desktop]: https://xfce.org/
[Lmod]: https://www.tacc.utexas.edu/research-development/tacc-projects/lmod

## Build/Install

Gitlab CI will automatically build both CentOS 7 and 8 RPMs.
They can be installed directly via `yum` for testing.
For production, add to the per-cluster common repos and require via puppet.

## Contributing

1. Fork it ( https://git.unl.edu/hcc/bc-hcc-matlab )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License

* Documentation, website content, and logo is licensed under
  [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
* Code is licensed under MIT (see LICENSE.txt)
* MATLAB's logo is a trademark or registered trademark of MathWorks, Inc.
