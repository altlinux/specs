%define module_name django-socketio

%def_with python3

Name: python-module-%module_name
Version: 0.3.9
Release: alt1.git20140105.1
Group: Development/Python
License: BSD License
Summary: Application that allow you to use WebSockets seamlessly with any Django project
URL: https://github.com/stephenmcd/django-socketio.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Application that brings together a variety of features that allow you to
use WebSockets seamlessly with any Django project

%package -n python3-module-%module_name
Summary: Application that allow you to use WebSockets seamlessly with any Django project
Group: Development/Python3

%description -n python3-module-%module_name
Application that brings together a variety of features that allow you to
use WebSockets seamlessly with any Django project

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
%doc LICENSE README.rst docs/*.rst
%python_sitelibdir/django_socketio*

%if_with python3
%files -n python3-module-%module_name
%doc LICENSE README.rst docs/*.rst
%python3_sitelibdir/django_socketio*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.9-alt1.git20140105.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.git20140105
- Version 0.3.9
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.4-alt1
- build for ALT
