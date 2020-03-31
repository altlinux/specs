%define _unpackaged_files_terminate_build 1
%define oname forex-python

Name: python3-module-%oname
Version: 1.5
Release: alt1

Summary: Foreign exchange rates, Bitcoin price index and currency conversion using ratesapi.io
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/forex-python
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
The currency module of the Tryton application platform.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.rst PKG-INFO MANIFEST.in
%python3_sitelibdir/*

%changelog
* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt1
- Initial build.

