%define oname sphinxcontrib-spelling

Name: python-module-%oname
Version: 1.4
Release: alt1

Summary: Sphinx "spelling" extension
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxcontrib-spelling

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-enchant
BuildPreReq: python-module-setuptools

Requires: python-module-sphinxcontrib = %EVR

%description
This package contains sphinxcontrb.spelling, a spelling checker for
Sphinx-based documentation. It uses PyEnchant to produce a report
showing misspelled words.

%package -n python-module-sphinxcontrib
Summary: Core package of sphinxcontrib
Group: Development/Python

%description -n python-module-sphinxcontrib
Core package of sphinxcontrib.

%prep
%setup

%build
%python_build_debug

%install
%python_install

touch %buildroot%python_sitelibdir/sphinxcontrib/__init__.py

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.py*

%files -n python-module-sphinxcontrib
%python_sitelibdir/*/__init__.py*

%changelog
* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

