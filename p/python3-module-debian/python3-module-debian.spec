%define _unpackaged_files_terminate_build 1
%define pymodname debian

Name:    python3-module-%pymodname
Version: 0.1.36
Release: alt1

Summary: Modules for Debian-related data formats
License: GPLv2+ and GPLv3+
Group:   Development/Python3
Url:     https://pypi.org/project/python-debian/
Source:  %name-%version.tar

BuildArch: noarch
BuildRequires: python3-devel

%description
The `debian` Python modules work with Debian-related data formats,
providing a means to read data from files involved in Debian packaging,
and the distribution of Debian packages. The ability to create or edit
the files is also available for some formats.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/debian/
%python3_sitelibdir/debian_bundle/
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/python_debian-*-py%_python3_version.egg-info/
%python3_sitelibdir/deb*.py*
%doc README.rst

%changelog
* Thu Mar 12 2020 Slava Aseev <ptrnine@altlinux.org> 0.1.36-alt1
- Update to upstream version 0.1.36
- Disable build for python2

* Tue Jan 29 2019 Slava Aseev <ptrnine@altlinux.org> 0.1.34-alt1
- Initial build for ALT
