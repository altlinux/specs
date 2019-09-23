%define _unpackaged_files_terminate_build 1
%define oname simplediff

Name: python3-module-%oname
Version: 1.0
Release: alt1
Summary: Simple diff function implemented in Python
License: zlib
Group: Development/Python3
Url: https://github.com/paulgb/simplediff/tree/master/python
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
A Python module to annotate two versions of a list with the values that have
been changed between the versions, similar to unix's diff but with a dead-simple
Python interface.

%prep
%setup

%build
%python3_build

%install
%python3_install
install -m 0644 test.py %buildroot%python3_sitelibdir

%files
%python3_sitelibdir/*
%doc LICENSE README.*

%changelog
* Mon Sep 23 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.0-alt1
- Initial build for ALT
