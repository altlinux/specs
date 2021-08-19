%define oname django-tools
%define modname django_tools

Name: python3-module-django-tools
Version: 0.48.3
Release: alt2

Summary: Miscellaneous tools for django

License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-tools

# package from pypi missed django_tools_test_project, but it is prepared to build without poetry
# Source-url: https://github.com/jedie/django-tools/archive/refs/tags/v%version.tar.gz
# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-django

# missed in a module from pypi
%add_python3_req_skip django_tools_test_project.django_tools_test_app.models

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
# need only for developing and tests
rm -v %modname/publish.py

%build
%python3_build

%install
%python3_install
%python3_prune
# strange tools
rm -v %buildroot%_bindir/{dev_server,publish,update_rst_readme}

%files
%python3_sitelibdir/%modname
%python3_sitelibdir/*.egg-info
#exclude %python3_sitelibdir/%modname/unittest_utils/
#exclude %python3_sitelibdir/%modname/selenium/

#files tests
#python3_sitelibdir/%modname/unittest_utils/


%changelog
* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 0.48.3-alt2
- switch to build from tarball, real build 0.48.3

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.48.3-alt1
- new version 0.48.3 (with rpmrb script)
- make pip require optional

* Tue Feb 18 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.32.7-alt2
- Porting to python3.

* Wed Mar 15 2017 Lenar Shakirov <snejok@altlinux.ru> 0.32.7-alt1
- Initial build for ALT

