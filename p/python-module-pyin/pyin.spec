%define oname pyin

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt1.git20150211
Summary: Perform Python operations on every line streamed from stdin
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/geowurster/pyin.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-click-tests python-module-coverage
BuildPreReq: python-module-nose python-module-str2type
BuildPreReq: python-module-derive python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-click-tests python3-module-coverage
BuildPreReq: python3-module-nose python3-module-str2type
BuildPreReq: python3-module-derive
%endif

%py_provides %oname
%py_requires click str2type derive

%description
Perform Python operations on every line read from `stdin`. Every line is
evaluated individually and available via a variable called `line`.

%package -n python3-module-%oname
Summary: Perform Python operations on every line streamed from stdin
Group: Development/Python3
%py3_provides %oname
%py3_requires click str2type derive

%description -n python3-module-%oname
Perform Python operations on every line read from `stdin`. Every line is
evaluated individually and available via a variable called `line`.

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

%check
python setup.py test
nosetests --with-coverage
%if_with python3
pushd ../python3
python3 setup.py test
#nosetests3 --with-coverage
popd
%endif

%files
%doc *.md tests.py sample-data
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md tests.py sample-data
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150211
- Version 0.3.3

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150203
- Version 0.2.1

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150202
- Initial build for Sisyphus

