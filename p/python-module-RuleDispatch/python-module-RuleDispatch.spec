%define version 0.5a1.dev
%define release alt3.r2506.2.1
%setup_python_module RuleDispatch

Name: %packagename
Version:%version
Release: %release

Summary: Rule-based Dispatching and Generic Functions

License: MIT/X11
Group: Development/Python
Url: http://peak.telecommunity.com
Packager: Denis Klimov <zver@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: python-module-distribute

Provides: python-module-ruledispatch = %version-%release
Obsoletes: python-module-ruledispatch <= 0.5a0-alt0.1.1

%description
Rule-based Dispatching and Generic Functions.

%prep
%setup -n %modulename-%version

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/dispatch
%python_sitelibdir/%modulename-*.egg-info

%changelog
* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5a1.dev-alt3.r2506.2.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5a1.dev-alt3.r2506.2
- Fixed build

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5a1.dev-alt3.r2506.1
- Rebuilt for debuginfo

* Tue Jul 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5a1.dev-alt3.r2506
- Rebuild with python 2.6

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 0.5a1.dev-alt2.r2506
- add provides and obsoletes

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 0.5a1.dev-alt1.r2506
- Initial build for ALT Linux


