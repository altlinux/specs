%define oname czjson
Name: python-module-%oname
Version: 1.0.8
Release: alt2.1.1
Summary: Fast JSON encoder/decoder for Python(fix bug for python-cjson)
License: LGPL
Group: Development/Python
Url: http://pypi.python.org/pypi/czjson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
Fast JSON encoder/decoder for Python(fix bug for python-cjson).

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build

%install
%python_install

%files
%doc ChangeLog LICENSE README
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.8-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.8-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2
- Avoid strict-aliasing rules

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Initial build for Sisyphus

