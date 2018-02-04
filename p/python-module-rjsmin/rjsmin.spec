%define oname rjsmin

%def_with python3

Name: python-module-%oname
Version: 1.0.12
Release: alt1.1
Summary: Javascript Minifier
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/rjsmin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ndparker/rjsmin.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-epydoc python-modules-xml
BuildPreReq: python-modules-logging python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
rJSmin is a javascript minifier written in python.

%package -n python3-module-%oname
Summary: Javascript Minifier
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
rJSmin is a javascript minifier written in python.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
epydoc --config=epydoc.conf
popd

%files
%doc %_docdir/%oname
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc %_docdir/%oname
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.12-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.10-alt3.git20141116.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 28 2016 Denis Medvedev <nbr@altlinux.org> 1.0.10-alt3.git20141116
- Python compilation for 3.5.

* Thu Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.10-alt2.git20141116
- Documentation creation disabled

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.git20141116
- Initial build for Sisyphus

