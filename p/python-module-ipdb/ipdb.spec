%define oname ipdb

%def_with python3

Name: python-module-%oname
Version: 0.8.1
Release: alt1.dev0.git20130919.1
Summary: IPython-enabled pdb
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ipdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gotcha/ipdb.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: ipython3
%endif

%description
ipdb exports functions to access the IPython debugger, which features
tab completion, syntax highlighting, better tracebacks, better
introspection with the same interface as the pdb module.

%package -n python3-module-%oname
Summary: IPython-enabled pdb
Group: Development/Python3

%description -n python3-module-%oname
ipdb exports functions to access the IPython debugger, which features
tab completion, syntax highlighting, better tracebacks, better
introspection with the same interface as the pdb module.

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

%check
PYTHONPATH=%buildroot%python_sitelibdir python setup.py test
%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%_bindir/%oname
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/%{oname}3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.dev0.git20130919.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.dev0.git20130919
- Initial build for Sisyphus

