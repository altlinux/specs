%define module_name django-notification

%def_with python3

Name: python-module-%module_name
Version: 0.2.1
Release: alt1.git20140207.1
Group: Development/Python
License: MIT License
Summary: User notification management for the Django web framework
URL: http://github.com/Star2Billing/django-notification
Source: %name-%version.tar

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
User notification management for the Django web framework

%package -n python3-module-%module_name
Summary: User notification management for the Django web framework
Group: Development/Python3

%description -n python3-module-%module_name
User notification management for the Django web framework

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc AUTHORS CHANGELOG LICENSE README docs/*
%python_sitelibdir/django_notification*
%python_sitelibdir/notification*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS CHANGELOG LICENSE README docs/*
%python3_sitelibdir/django_notification*
%python3_sitelibdir/notification*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20140207.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20140207
- Version 0.2.1
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1
- build for ALT
