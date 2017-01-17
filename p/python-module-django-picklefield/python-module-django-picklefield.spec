%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define module_name django-picklefield

%def_with python3

Name: python-module-%module_name
Version: 0.3.2
#Release: alt1.git20131115.1
Group: Development/Python
License: BSD License
Summary: django-picklefield provides an implementation of a pickled object field
URL: http://github.com/gintas/django-picklefield.git
Source0: https://pypi.python.org/packages/9c/22/602e6d010248786d72b70c7ca16b0d19ec513897a39861a957a092a77b08/%{module_name}-%{version}.tar.gz

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%endif

%description
django-picklefield provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

%package -n python3-module-%module_name
Summary: django-picklefield provides an implementation of a pickled object field
Group: Development/Python

%description -n python3-module-%module_name
django-picklefield provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

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
%doc README.rst PKG-INFO
%python_sitelibdir/django_picklefield*
%python_sitelibdir/picklefield*

%if_with python3
%files -n python3-module-%module_name
%doc README.rst PKG-INFO
%python3_sitelibdir/django_picklefield*
%python3_sitelibdir/picklefield*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20131115.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20131115.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20131115
- Version 0.3.1
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.1-alt1
- build for ALT
