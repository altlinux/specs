%define modulename pybeam

Name: python3-module-%modulename
Summary: Python module to parse Erlang BEAM files
Version: 0.7
Release: alt1
Group: Development/Python3
License: MIT
URL: https://github.com/matwey/pybeam
Source: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%description
%summary.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Fri Aug 06 2021 Alexey Shabalin <shaba@altlinux.org> 0.7-alt1
- Initial build for ALT
