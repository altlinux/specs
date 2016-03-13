%define module_name bundle

%def_with python3

Name: python-module-%module_name
Version: 1.1.2
Release: alt2.1
Group: Development/Python
License: BSD License
Summary: Manages installed Bundle packages
URL: https://github.com/ask/bundle.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Manages installed Bundle packages

%package -n python3-module-%module_name
Summary: Manages installed Bundle packages
Group: Development/Python3

%description -n python3-module-%module_name
Manages installed Bundle packages

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
%doc AUTHORS Changelog LICENSE README.rst TODO
%python_sitelibdir/bundle*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS Changelog LICENSE README.rst TODO
%python3_sitelibdir/bundle*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Added module for Python 3

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.2-alt1
- build for ALT
