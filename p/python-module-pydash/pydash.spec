%define oname pydash

%def_with python3

Name: python-module-%oname
Version: 3.0.1
Release: alt1.git20150225.1
Summary: The kitchen sink of Python utility libraries for doing "stuff" in a functional way
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pydash/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dgilland/pydash.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tox python-module-pytest-cov
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-sphinx_rtd_theme
#BuildPreReq: python-module-sphinxcontrib-napoleon
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tox python3-module-pytest-cov
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: bzr python-base python-devel python-module-Paver python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-coverage python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mimeparse python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sphinxcontrib python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-coverage python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest-cov python-module-setuptools-tests python-module-sphinxcontrib-napoleon python-module-tox python3-module-pytest-cov python3-module-setuptools-tests python3-module-tox rpm-build-python3 time

%description
The kitchen sink of Python utility libraries for doing "stuff" in a
functional way. Based on the Lo-Dash Javascript library.

%package -n python3-module-%oname
Summary: The kitchen sink of Python utility libraries for doing "stuff" in a functional way
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The kitchen sink of Python utility libraries for doing "stuff" in a
functional way. Based on the Lo-Dash Javascript library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python
Requires: %name = %EVR

%description pickles
The kitchen sink of Python utility libraries for doing "stuff" in a
functional way. Based on the Lo-Dash Javascript library.

This package contains pickles for %oname.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
%make pytest
%if_with python3
pushd ../python3
sed -i 's|py.test|py.test-%_python3_version|' makefile
%make pytest
popd
%endif

%files
%doc *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0.1-alt1.git20150225.1
- NMU: Use buildreq for BR.

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20150225
- Initial build for Sisyphus

