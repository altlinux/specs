%define oname django-tools
%define modname django_tools

Name: python3-module-%oname
Version: 0.32.7
Release: alt2

Summary: Miscellaneous tools for django.
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-tools
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django

%py3_requires pip
%add_python3_req_skip filer pip._vendor.packaging.version


%description
%summary

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Miscellaneous tools for django.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modname
%python3_sitelibdir/%{modname}_test_project
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%{modname}_tests

%files tests
%python3_sitelibdir/%{modname}_tests


%changelog
* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.32.7-alt2
- Porting to python3.

* Wed Mar 15 2017 Lenar Shakirov <snejok@altlinux.ru> 0.32.7-alt1
- Initial build for ALT

