%define oname jedi

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.0
Release: alt1.git20150623.1.1
Summary: An autocompletion tool for Python that can be used for text editors
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jedi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davidhalter/jedi.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-docopt python-modules-sqlite3
#BuildPreReq: python-module-sphinx-devel graphviz
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-docopt python3-modules-sqlite3
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python3-module-pytest rpm-build-python3 time

%description
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

%package -n python3-module-%oname
Summary: An autocompletion tool for Python that can be used for text editors
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Jedi is an autocompletion tool for Python that can be used in
IDEs/editors. Jedi works. Jedi is fast. It understands all of the basic
Python syntax elements including many builtin functions.

Additionaly, Jedi suports two different goto functions and has support
for renaming as well as Pydoc support and some other IDE features.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|env python|env python3|' \
	../python3/sith.py ../python3/scripts/*.py
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
install -d %buildroot%_bindir

%python_install
install -p -m755 sith.py scripts/*.py %buildroot%_bindir/

%if_with python3
pushd ../python3
%python3_install
install -p -m755 sith.py %buildroot%_bindir/sith.py3
pushd scripts
for i in $(ls); do
	install -p -m755 $i %buildroot%_bindir/${i}3
done
popd
popd
%endif

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
python setup.py test
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.txt *.rst *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150623.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150623.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150623
- Version 0.9.0

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.final0.git20150102
- Initial build for Sisyphus

