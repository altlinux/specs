%define _unpackaged_files_terminate_build 1
%define oname ipdb

%def_with python3

Name: python-module-%oname
Version: 0.10.1
Release: alt1
Summary: IPython-enabled pdb
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ipdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gotcha/ipdb.git
Source0: https://pypi.python.org/packages/eb/0a/0a37dc19572580336ad3813792c0d18c8d7117c2d66fc63c501f13a7a8f8/%{oname}-%{version}.tar.gz
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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.dev0.git20130919.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.dev0.git20130919
- Initial build for Sisyphus

