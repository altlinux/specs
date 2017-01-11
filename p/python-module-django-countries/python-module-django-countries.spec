%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define module_name django-countries

%def_with python3

Name: python-module-%module_name
Version: 4.0
#Release: alt1.git20141027.1
Group: Development/Python
License: BSD License
Summary: Provides a country field for Django models.
URL: https://pypi.python.org/pypi/django-countries
# https://github.com/SmileyChris/django-countries.git
Source0: https://pypi.python.org/packages/91/88/c99df63539deafc9306158e65965e1774eebf3a9f39c8bb2314369fb79a8/%{module_name}-%{version}.tar.gz

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
%setup -q -n %{module_name}-%{version}

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

%if "%_target_libdir_noarch" != "%_libdir"
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.git20141027.1.1
- (AUTO) subst_x86_64.

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
