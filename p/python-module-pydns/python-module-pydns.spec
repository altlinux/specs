Summary: Python DNS library
Version: 2.3.3
Release: alt1.1.1

%setup_python_module pydns
%add_python_req_skip _winreg

Name: %packagename
Source0: %modulename-%version.tar
License: Python Software Foundation License
Group: Development/Python
URL: http://pydns.sourceforge.net/
Packager: Andriy Stepanov <stanv@altlinux.ru>

%description
PyDNS provides a module for performing DNS queries from python applications.

%prep
%setup -q -n %modulename-%version

%build
%__python setup.py build

%install
%__python setup.py install --root=$RPM_BUILD_ROOT --install-lib=%python_sitelibdir  --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README-guido.txt README.txt CREDITS.txt

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.3-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.3-alt1.1
- Rebuilt with python 2.6

* Sun May 03 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt1
- Initial build for ALT Linux
