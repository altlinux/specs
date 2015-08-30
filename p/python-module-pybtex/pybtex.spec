%define oname pybtex

%def_with python3

Name: python-module-%oname
Version: 0.18
Release: alt1.git20150807
Summary: A BibTeX-compatible bibliography processor in Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pybtex
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/pybtex-devs/pybtex
Source: %name-%version.tar
Source1: conf.py

BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-yaml python-module-nose
BuildPreReq: python-module-docutils python-module-jinja2
BuildPreReq: python-module-Pygments
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-yaml python3-module-nose
BuildPreReq: python3-module-docutils python3-module-jinja2
BuildPreReq: python3-module-Pygments
%endif

%py_provides %oname
%py_requires yaml docutils jinja2 pygments

%description
Pybtex reads citation information from a file and produces a formatted
bibliography. BibTeX style files are supported. Alternatively it is
possible to write styles in Python.

%if_with python3
%package -n python3-module-%oname
Summary: A BibTeX-compatible bibliography processor in Python
Group: Development/Python3
%py3_provides %oname
%py3_requires yaml docutils jinja2 pygments

%description -n python3-module-%oname
Pybtex reads citation information from a file and produces a formatted
bibliography. BibTeX style files are supported. Alternatively it is
possible to write styles in Python.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Pybtex reads citation information from a file and produces a formatted
bibliography. BibTeX style files are supported. Alternatively it is
possible to write styles in Python.

This package contains tests for %oname.
%endif

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Pybtex reads citation information from a file and produces a formatted
bibliography. BibTeX style files are supported. Alternatively it is
possible to write styles in Python.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Pybtex reads citation information from a file and produces a formatted
bibliography. BibTeX style files are supported. Alternatively it is
possible to write styles in Python.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Pybtex reads citation information from a file and produces a formatted
bibliography. BibTeX style files are supported. Alternatively it is
possible to write styles in Python.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

install -p -m644 %SOURCE1 docs/rst/
%prepare_sphinx docs
ln -s ../objects.inv docs/rst/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

export PYTHONPATH=$PWD
pushd docs
./generate.py
sphinx-build -b pickle -d build/doctrees rst build/pickle
popd

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
sed -i 's|from . import io|import io|' \
	%buildroot%python3_sitelibdir/%oname/io.py
%endif

%python_install

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/
install -d %buildroot%_man1dir
install -m644 docs/man1/*.1 %buildroot%_man1dir/

%check
python setup.py test -v
export PYTHONPATH=$PWD
nosetests -vv --with-doctest %oname
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD
#nosetests3 -vv --with-doctest %oname
popd
%endif

%files
%doc CHANGES README
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/custom_fixers
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%_man1dir/*

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/html

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/custom_fixers
%exclude %python3_sitelibdir/*/tests
%_man1dir/*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.git20150807
- Initial build for Sisyphus

