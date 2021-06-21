%define  modulename runtests

Name:    python3-module-%modulename
Version: 0.0.28
Release: alt1

Summary: Running pytest tests with incremental builds and optional MPI support
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/bccp/runtests

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source: %modulename-%version.tar

%description
A simple tools for incrementally building packages, then testing against
installed version.

The idea came from runtests.py in numpy and scipy projects:

* incremental build is fast: encouraging developers to test frequently;
* existing installation of the software package is not overwritten;
* binaries are properly compiled -- and optionally in debug mode.

Testing of MPI application is also supported via the [mpi] feature. We use
runtests in nbodykit and a variety of packages.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 0.0.28-alt1
- Initial build for Sisyphus
