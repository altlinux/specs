%define oname sphinxjp.themes.basicstrap

Name: python-module-%oname
Version: 0.3.0
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

%package -n python-module-sphinxjp.themes
Summary: Core package of sphinxjp.themes
Group: Development/Python
Requires: python-module-sphinxjp

%description -n python-module-sphinxjp.themes
Core package of sphinxjp.themes.

%prep
%setup

%build
%python_build

%install
%python_install

touch %buildroot%python_sitelibdir/sphinxjp/__init__.py
touch %buildroot%python_sitelibdir/sphinxjp/themes/__init__.py

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/sphinxjp/themes/__init__.py*
%exclude %python_sitelibdir/sphinxjp/__init__.py*

%files -n python-module-sphinxjp.themes
%python_sitelibdir/sphinxjp/themes/__init__.py*

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

