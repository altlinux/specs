%define oname sphinxjp.themecore

Name: python-module-%oname
Version: 0.1.3
Release: alt1
Summary: A sphinx theme plugin support extension
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxjp.themecore
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

Requires: python-module-sphinxjp = %EVR

%description
A sphinx theme plugin support extension.

%package -n python-module-sphinxjp
Summary: Core package of sphinxjp
Group: Development/Python

%description -n python-module-sphinxjp
Core package of sphinxjp.

%prep
%setup

%build
%python_build

%install
%python_install

touch %buildroot%python_sitelibdir/sphinxjp/__init__.py

%files
%doc src/*.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.py*

%files -n python-module-sphinxjp
%python_sitelibdir/*/__init__.py*

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

