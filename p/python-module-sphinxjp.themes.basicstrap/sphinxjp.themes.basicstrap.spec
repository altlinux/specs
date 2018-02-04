%define sname sphinxjp
%define mname %sname.themes
%define oname %mname.basicstrap

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt1.1.1.1
Summary: A sphinx theme for Basicstrap style
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxjp.themes.basicstrap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-sphinxjp.themecore
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-sphinx-devel python3-module-sphinxjp.themecore
#BuildPreReq: python-tools-2to3
%endif

Requires: python-module-%sname
Requires: python-module-%mname = %EVR
%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-sphinxjp python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python-module-sphinxjp.themecore python3-module-html5lib python3-module-nose python3-module-setuptools python3-module-sphinx python3-module-sphinxjp.themecore rpm-build-python3 time

%description
Basicstrap style theme for Sphinx. Using Twitter Bootstrap.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Basicstrap style theme for Sphinx. Using Twitter Bootstrap.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Basicstrap style theme for Sphinx. Using Twitter Bootstrap.

This package contains documentation for %oname.

%package -n python-module-%mname
Summary: Core package of %mname
Group: Development/Python
Requires: python-module-%sname
%py_provides %mname

%description -n python-module-%mname
Core package of %mname.

%if_with python3
%package -n python3-module-%oname
Summary: A sphinx theme for Basicstrap style
Group: Development/Python3
Requires: python3-module-%sname
Requires: python3-module-%mname = %EVR
%py3_provides %oname

%description -n python3-module-%oname
Basicstrap style theme for Sphinx. Using Twitter Bootstrap.

%package -n python3-module-%mname
Summary: Core package of %mname
Group: Development/Python3
Requires: python3-module-%sname
%py3_provides %mname

%description -n python3-module-%mname
Core package of %mname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
install -p -m644 src/%sname/__init__.py \
	%buildroot%python_sitelibdir/%sname/
install -p -m644 src/%sname/themes/__init__.py \
	%buildroot%python_sitelibdir/%sname/themes/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 src/%sname/__init__.py \
	%buildroot%python3_sitelibdir/%sname/
install -p -m644 src/%sname/themes/__init__.py \
	%buildroot%python3_sitelibdir/%sname/themes/
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname

%files
%doc *.rst
%python_sitelibdir/%sname/themes/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%sname/themes/__init__.py*
%dir %python_sitelibdir/%oname
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%files -n python-module-%mname
%dir %python_sitelibdir/%sname/themes
%python_sitelibdir/%sname/themes/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%sname/themes/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%sname/themes/__init__.py
%exclude %python3_sitelibdir/%sname/themes/__pycache__/__init__.*

%files -n python3-module-%mname
%dir %python3_sitelibdir/%sname/themes
%dir %python3_sitelibdir/%sname/themes/__pycache__
%python3_sitelibdir/%sname/themes/__init__.py
%python3_sitelibdir/%sname/themes/__pycache__/__init__.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.1
- NMU: Use buildreq for BR.

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Verson 0.4.2
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Version 0.3.2

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Version 0.3.1

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

