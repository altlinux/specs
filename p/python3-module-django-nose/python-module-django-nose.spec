%global oname django-nose
%def_with bootstrap

Name:           python3-module-django-nose
Version:        1.4.7
Release:        alt1

Summary:        Django test runner that uses nose

Group:          Development/Python3
License:        BSD
URL:            http://github.com/jbalogh/django-nose

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch:      noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires:  python3-module-setuptools
Requires:       python3-module-nose
Requires:       python3-module-django
%if_with bootstrap
%add_python3_req_skip django.db.backends.creation
%endif

%description
Django test runner that uses nose.

%prep
%setup

# remove egg-info
rm -rf django_nose.egg-info

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/testapp/

%files
%doc LICENSE README.rst
%{python3_sitelibdir}/django_nose
%{python3_sitelibdir}/django_nose-%{version}-py?.?.egg-info

%changelog
* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt1
- new version 1.4.7 (with rpmrb script)

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt2
- build python3 module separately

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt1
- new version 1.4.6 (with rpmrb script)

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Fixed for Django 18+

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2-alt1
- First build for ALT (based on Fedora 1.2-2.fc21.src)

