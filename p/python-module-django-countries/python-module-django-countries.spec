%define module_name django-countries

%def_with python3

Name: python-module-%module_name
Version: 3.0.1
Release: alt1.git20141027.1
Group: Development/Python
License: BSD License
Summary: Provides a country field for Django models.
URL: https://pypi.python.org/pypi/django-countries
# https://github.com/SmileyChris/django-countries.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides django_countries

%description
Provides a country field for Django models.

%package -n python3-module-%module_name
Summary: Provides a country field for Django models
Group: Development/Python3
%py3_provides django_countries

%description -n python3-module-%module_name
Provides a country field for Django models.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc *.rst
%python_sitelibdir/django_countries*

%if_with python3
%files -n python3-module-%module_name
%doc *.rst
%python3_sitelibdir/django_countries*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.git20141027.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20141027
- Version 3.0.1

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.git20140829
- Version 2.1.2
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- build for ALT
