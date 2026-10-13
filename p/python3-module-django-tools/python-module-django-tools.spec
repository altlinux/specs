%define oname django-tools
%define modname django_tools

Name: python3-module-django-tools
Version: 0.59.0
Release: alt1

Summary: Miscellaneous tools for django

License: GPL-3.0-or-later
Group: Development/Python3
Url: https://pypi.org/project/django-tools

# upstream git: https://github.com/jedie/django-tools
# Source-url: %__pypi_url %modname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)

%description
Miscellaneous tools for django.


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
%pyproject_build

%install
%pyproject_install
# test project for upstream development only
rm -v %buildroot%_bindir/django_tools_project
rm -rv %buildroot%python3_sitelibdir/django_tools_project/
# tests need the test project above
find %buildroot%python3_sitelibdir/%modname -depth -type d -name tests -exec rm -rv {} +

%files
%doc README.md
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.59.0-alt1
- new version 0.59.0
- switch to pyproject build (hatchling)
- fix License (GPL-3.0-or-later)
- drop the development test project from the package

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.48.3-alt2
- switch to build from tarball, real build 0.48.3

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.48.3-alt1
- new version 0.48.3 (with rpmrb script)
- make pip require optional

* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.32.7-alt2
- Porting to python3.

* Wed Mar 15 2017 Lenar Shakirov <snejok@altlinux.ru> 0.32.7-alt1
- Initial build for ALT

