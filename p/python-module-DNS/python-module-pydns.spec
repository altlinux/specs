Summary: Python DNS library
Version: 2.3.6
Release: alt2

%setup_python_module DNS
%add_python_req_skip _winreg

Name: %packagename
Source0: %modulename-%version.tar
License: Python Software Foundation License
Group: Development/Python
URL: http://pydns.sourceforge.net/

Conflicts: python-module-pydns < %EVR
Obsoletes: python-module-pydns < %EVR
Provides: python-module-pydns = %EVR

%description
PyDNS provides a module for performing DNS queries from python applications.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib=%python_sitelibdir

%files
%doc README-guido.txt README.txt CREDITS.txt
%python_sitelibdir/*

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.6-alt2
- Owned %python_sitelibdir/DNS (inspired by ldv@)

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.6-alt1
- Version 2.3.6

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.3-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1.1
- Rebuilt with python 2.6

* Sun May 03 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt1
- Initial build for ALT Linux
