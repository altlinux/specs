%define oname colander

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.dev.git20141126.1.1.1
Summary: A serialization/deserialization/validation library for strings, mappings and lists
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/colander/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/colander.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
#BuildPreReq: python-module-iso8601 python-module-translationstring
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-iso8601 python3-module-translationstring
%endif

%py_provides %oname
%py_requires iso8601

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: pylons_sphinx_theme python-module-alabaster python-module-docutils python-module-html5lib python-module-iso8601 python-module-objects.inv python-module-setuptools python-module-translationstring python3-module-iso8601 python3-module-setuptools python3-module-translationstring rpm-build-python3 time

%description
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A serialization/deserialization/validation library for strings, mappings and lists
Group: Development/Python3
%py3_provides %oname
%py3_requires iso8601

%description -n python3-module-%oname
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A simple schema-based serialization and deserialization library.

An extensible package which can be used to:

* deserialize and validate a data structure composed of strings,
  mappings, and lists.
* serialize an arbitrary data structure to a data structure composed of
  strings, mappings, and lists.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/
cp -fR %_datadir/pylons_sphinx_theme docs/_themes

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.dev.git20141126.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.dev.git20141126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt1.dev.git20141126.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev.git20141126
- Version 1.1dev
- Enabled testing

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b1.git20140910
- Initial build for Sisyphus

