%def_disable check

%define oname mpltools

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt2.git20150224.1.1
Summary: Tools for Matplotlib
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mpltools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tonysyu/mpltools.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools xvfb-run
BuildPreReq: python-module-matplotlib 
BuildPreReq: python-module-pygobject3
BuildPreReq: python-module-pycairo python-module-mock
BuildPreReq: python-module-nose python-module-pytz
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-matplotlib 
BuildPreReq: python3-module-pygobject3
BuildPreReq: python3-module-pycairo python3-module-mock
BuildPreReq: python3-module-nose python3-module-pytz
%endif

%py_provides %oname
%py_requires matplotlib configobj future gi cairo

%description
As the name implies, mpltools provides tools for working with
matplotlib. For the most part, these tools are only loosely-connected in
functionality, so the best way to get started is to look at the example
gallery: http://tonysyu.github.com/mpltools/auto_examples/index.html .

%package -n python3-module-%oname
Summary: Tools for Matplotlib
Group: Development/Python3
%py3_provides %oname
%py3_requires matplotlib configobj future gi cairo

%description -n python3-module-%oname
As the name implies, mpltools provides tools for working with
matplotlib. For the most part, these tools are only loosely-connected in
functionality, so the best way to get started is to look at the example
gallery: http://tonysyu.github.com/mpltools/auto_examples/index.html .

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
As the name implies, mpltools provides tools for working with
matplotlib. For the most part, these tools are only loosely-connected in
functionality, so the best way to get started is to look at the example
gallery: http://tonysyu.github.com/mpltools/auto_examples/index.html .

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
As the name implies, mpltools provides tools for working with
matplotlib. For the most part, these tools are only loosely-connected in
functionality, so the best way to get started is to look at the example
gallery: http://tonysyu.github.com/mpltools/auto_examples/index.html .

This package contains documentation for %oname.

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
export PYTHONPATH=$PWD
python setup.py test
python examples/plot_all_styles.py
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
python3 examples/plot_all_styles.py
popd
%endif

%files
%doc *.rst examples/*.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples/*.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2.git20150224.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt2.git20150224.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 0.2.0-alt2.git20150224
- turn off docs generation and tests

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150224
- Initial build for Sisyphus

