%define oname sphinxcontrib-epydoc
Name: python-module-%oname
Version: 0.4.1
Release: alt1
Summary: Sphinx extension epydoc
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/sphinxcontrib-epydoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
A Sphinx extension to cross-reference epydoc-generated documentation.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.rst README
%python_sitelibdir/*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Version 0.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

