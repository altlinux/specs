%define oname sphinxjp.themes.basicstrap

Name: python-module-%oname
Version: 0.3.2
Release: alt1
Summary: A sphinx theme for Basicstrap style
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxjp.themes.basicstrap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
BuildPreReq: python-module-sphinx-devel python-module-sphinxjp.themecore

Requires: python-module-sphinxjp
Requires: python-module-sphinxjp.themes = %EVR

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

%package -n python-module-sphinxjp.themes
Summary: Core package of sphinxjp.themes
Group: Development/Python
Requires: python-module-sphinxjp

%description -n python-module-sphinxjp.themes
Core package of sphinxjp.themes.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%install
%python_install

touch %buildroot%python_sitelibdir/sphinxjp/__init__.py
touch %buildroot%python_sitelibdir/sphinxjp/themes/__init__.py

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/sphinxjp/themes/__init__.py*
%exclude %python_sitelibdir/sphinxjp/__init__.py*
%dir %python_sitelibdir/%oname
%exclude %python_sitelibdir/%oname/pickle

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%files -n python-module-sphinxjp.themes
%python_sitelibdir/sphinxjp/themes/__init__.py*

%changelog
* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Version 0.3.2

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Version 0.3.1

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

