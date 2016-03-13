%define mname sphinxcontrib
%define oname %mname-spelling

%def_with python3

Name: python-module-%oname
Version: 2.1.1
Release: alt2.1.1

Summary: Sphinx "spelling" extension
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-spelling

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-enchant
#BuildPreReq: python-module-setuptools python-module-pbr
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-enchant
#BuildPreReq: python3-module-setuptools python3-module-pbr
%endif

%py_provides %mname.spelling
Requires: python-module-%mname = %EVR

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pbr python3-module-html5lib python3-module-pbr rpm-build-python3 time

%description
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

This package contains documentation for %oname.

%package -n python-module-%mname
Summary: Core package of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core package of %mname.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx "spelling" extension
Group: Development/Python3
%py3_provides %mname.spelling
Requires: python3-module-%mname = %EVR

%description -n python3-module-%oname
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

This package contains tests for %oname.

%package -n python3-module-%mname
Summary: Core package of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core package of %mname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS ChangeLog README
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/__init__.py*
%dir %python_sitelibdir/%oname
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/*/*/tests

%files docs
%doc docs/build/html/*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS ChangeLog README
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt2.1
- NMU: Use buildreq for BR.

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt2
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

