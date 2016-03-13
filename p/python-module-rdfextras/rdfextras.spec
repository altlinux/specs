%define oname rdfextras

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0
Release: alt1.dev.git20130519.1.1
Summary: RDFExtras provide tools, extra stores and such for RDFLib
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/rdfextras/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RDFLib/rdfextras.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-rdflib python-module-pyparsing
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-SPARQLWrapper
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-rdflib python3-module-pyparsing
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-SPARQLWrapper
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-isodate python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pyparsing python-module-pytz python-module-rdflib python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pyparsing python3-module-rdflib python3-module-setuptools
BuildRequires: python-module-alabaster python-module-coverage python-module-docutils python-module-html5lib python-module-nose python-module-objects.inv python-module-pytest python-module-rdflib_jsonld python3-module-coverage python3-module-nose python3-module-pytest python3-module-rdflib_jsonld rpm-build-python3 time

%description
RDFExtras is a collection of packages providing extras based on RDFLib.
These include a tools package and several "non-core-rdflib" store
implementations.

%package -n python3-module-%oname
Summary: RDFExtras provide tools, extra stores and such for RDFLib
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
RDFExtras is a collection of packages providing extras based on RDFLib.
These include a tools package and several "non-core-rdflib" store
implementations.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
RDFExtras is a collection of packages providing extras based on RDFLib.
These include a tools package and several "non-core-rdflib" store
implementations.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
RDFExtras is a collection of packages providing extras based on RDFLib.
These include a tools package and several "non-core-rdflib" store
implementations.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
export PYTHONPATH=%buildroot%python_sitelibdit
python setup.py test
./run_tests.py
%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdit
pushd ../python3
python3 setup.py test
./run_tests_py3.sh
popd
%endif

%files
%doc CONTRIBUTORS *.txt *.md
#_bindir/*
#if_with python3
#exclude %_bindir/*.py3
#endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CONTRIBUTORS *.txt *.md
#_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.dev.git20130519.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt1.dev.git20130519.1
- NMU: Use buildreq for BR.

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.dev.git20130519
- Initial build for Sisyphus

