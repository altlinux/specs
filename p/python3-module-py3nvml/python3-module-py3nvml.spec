%define  modulename py3nvml

Name:    python3-module-%modulename
Version: 0.2.7
Release: alt1

Summary: Python 3 Bindings for NVML library. Get NVIDIA GPU status inside your program.
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/fbcotter/py3nvml

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Python 3 compatible bindings to the NVIDIA Management Library. Can be used to
query the state of the GPUs on your system. This was ported from the NVIDIA
provided python bindings nvidia-ml-py, which only supported python 2. I have
forked from version 7.352.0. The old library was itself a wrapper around the
NVIDIA Management Library.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%_bindir/py3smi
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Jun 06 2022 Andrey Cherepanov <cas@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus.
