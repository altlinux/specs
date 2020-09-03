%define _unpackaged_files_terminate_build 1
%define oname erf

Name: python3-module-%oname
Version: 1.0.1
Release: alt2
Summary: A pure-Python implementation of the error function and inverse error function.
License: GPLv3
Group: Development/Python3
BuildArch: noarch
Url: https://github.com/dougthor42/pyerf

# https://github.com/dougthor42/pyerf.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-hypothesis

%description
pyerf is a pure-Python implementation of the error function
and inverse error function using the same functions that SciPy uses
(namely parts of the Cephes math library, cprob/ndtr.c and cprob/ndtri.c).

This is a useful package for when you need to calculate some error fuctions
but you don't want to install all of the SciPy/NumPy stuff.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Thu Sep 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Transfer on python3.

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
