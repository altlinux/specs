%define oname mincss

%def_with python3

Name: python-module-%oname
Version: 0.8.4
Release: alt1.git20150203
Summary: Clears the junk out of your CSS
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mincss/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/peterbe/mincss.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-lxml
BuildPreReq: python-module-cssselect
BuildPreReq: python-modules-multiprocessing
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-lxml
BuildPreReq: python3-module-cssselect
%endif

%py_provides %oname
%py_requires lxml cssselect

%description
Clears the junk out of your CSS by finding out which selectors are
actually not used in your HTML.

%package -n python3-module-%oname
Summary: Clears the junk out of your CSS
Group: Development/Python3
%py3_provides %oname
%py3_requires lxml cssselect

%description -n python3-module-%oname
Clears the junk out of your CSS by finding out which selectors are
actually not used in your HTML.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Clears the junk out of your CSS by finding out which selectors are
actually not used in your HTML.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Clears the junk out of your CSS by finding out which selectors are
actually not used in your HTML.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst example proxy
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst example proxy
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.git20150203
- Initial build for Sisyphus

