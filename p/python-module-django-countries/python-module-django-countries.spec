%define module_name django-countries

%def_with python3

Name: python-module-%module_name
Version: 2.1.2
Release: alt1.git20140829
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

%description
Provides a country field for Django models.

%package -n python3-module-%module_name
Summary: Provides a country field for Django models
Group: Development/Python3

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
* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.git20140829
- Version 2.1.2
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- build for ALT
