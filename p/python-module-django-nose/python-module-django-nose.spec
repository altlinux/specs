%global pkgname django-nose
%def_with python3
%def_with bootstrap

Name:           python-module-django-nose
Version:        1.4.6
Release:        alt1

Summary:        Django test runner that uses nose

Group:          Development/Python
License:        BSD
URL:            http://github.com/jbalogh/django-nose

# Source-url: https://github.com/django-nose/django-nose/archive/v%version.tar.gz
Source:         %name-%version.tar

BuildArch:      noarch
BuildRequires:  python-devel python-module-setuptools
Requires:       python-module-nose
Requires:       python-module-django
BuildRequires(pre): rpm-build-python3

%description
Django test runner that uses nose.

%if_with python3
%package -n python3-module-%{pkgname}
Summary:        Django test runner that uses nose
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3 python3-module-setuptools
Requires:       python3-module-nose
Requires:       python3-module-django
%if_with bootstrap
%add_python3_req_skip django.db.backends.creation
%endif

%description -n python3-module-%{pkgname}
Django test runner that uses nose.

%endif

%prep
%setup

# remove egg-info
rm -rf django_nose.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
rm -rf %buildroot%python_sitelibdir/testapp/

%if_with python3
pushd ../python3
%python3_install
popd
rm -rf %buildroot%python3_sitelibdir/testapp/
%endif

%files
%doc LICENSE README.rst
%{python_sitelibdir}/django_nose
%{python_sitelibdir}/django_nose-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pkgname}
%doc LICENSE README.rst
%{python3_sitelibdir}/django_nose
%{python3_sitelibdir}/django_nose-%{version}-py?.?.egg-info
%endif

%changelog
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

