%define module_name django-piston

%def_with python3

Name: python-module-%module_name
Version: 0.2.3
Release: alt1.hg20120330.1

Summary: Piston is a Django mini-framework creating APIs

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/django-piston

# hg clone https://bitbucket.org/jespern/django-piston
Source: %module_name-%version.tar

BuildArch: noarch

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %module_name

%description
Piston is a Django mini-framework creating APIs

%package -n python3-module-%module_name
Summary: Piston is a Django mini-framework creating APIs
Group: Development/Python3

%description -n python3-module-%module_name
Piston is a Django mini-framework creating APIs

%prep
%setup -n %module_name-%version

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
cp piston/__init__.py %buildroot%python_sitelibdir/piston/

%if_with python3
pushd ../python3
%python3_install
cp piston/__init__.py %buildroot%python3_sitelibdir/piston/
popd
%endif

%files
%doc *.txt examples
%python_sitelibdir/django_piston-*
%python_sitelibdir/piston*

%if_with python3
%files -n python3-module-%module_name
%doc *.txt examples
%python3_sitelibdir/django_piston-*
%python3_sitelibdir/piston*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.hg20120330.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.hg20120330
- Snapshot from mercurial
- Added module for Python 3

* Thu Apr 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.3-alt1
- Initial build for ALT Linux
