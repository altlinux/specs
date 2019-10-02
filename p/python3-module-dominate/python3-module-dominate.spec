%define _unpackaged_files_terminate_build 1
%define oname dominate

Name: python3-module-%oname
Version: 2.4.0
Release: alt1
Summary: Library for creating and manipulating HTML documents using an elegant DOM API
License: LGPLv3
Group: Development/Python3
Url: https://github.com/Knio/dominate
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Dominate is a Python library for creating and manipulating HTML documents using
an elegant DOM API. It allows you to write HTML pages in pure Python very
concisely, which eliminates the need to learn another template language, and
lets you take advantage of the more powerful features of Python.

%prep
%setup

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%python3_sitelibdir/%oname/tests
install -m 0644 tests/*  %buildroot%python3_sitelibdir/%oname/tests

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%{_python3_version}.egg-info
%doc LICENSE.txt README.md

%changelog
* Wed Oct 02 2019 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.0-alt1
- Initial build for ALT
