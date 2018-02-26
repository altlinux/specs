%define oname regex
Name: python-module-%oname
Version: 0.1.20111223
Release: alt1.1
Summary: Alternate regular expression module, to replace re
License: PSFL
Group: Development/Python
Url: http://pypi.python.org/pypi/regex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
This new regex implementation is intended eventually to replace Python's
current re module implementation.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.20111223-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20111223-alt1
- Version 0.1.20111223

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20111103-alt1
- Version 0.1.20111103

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.20110524-alt1.1
- Rebuild with Python-2.7

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20110524-alt1
- Initial build for Sisyphus

