%define oname zc
%define version 1.0.0
%define release alt7

Summary: The ``zc`` package is a pure namespace package
Name: python3-module-%oname
Version: %version
Release: %release
License: ZPL
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>

# need for links with some Zope modules
Requires: python3-module-z3c
BuildRequires(pre): rpm-build-python3

### Don't set BuildArch to noarch - other zc packages arch-dependent.

%description
%summary

%install
mkdir -p %buildroot/%python3_sitelibdir/%oname
cat <<EOF > %buildroot/%python3_sitelibdir/%oname/__init__.py
try:
    # Declare this a namespace package if pkg_resources is available.
    import pkg_resources
    pkg_resources.declare_namespace('zc')
except ImportError:
    pass
EOF

%files
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/__init__.py*
%dir %python3_sitelibdir/%oname/__pycache__
%python3_sitelibdir/%oname/__pycache__/__init__.*

%changelog
* Wed Sep 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt7
- Drop python2 support.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt6.2
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.0-alt6.1
- Rebuild with Python-3.3

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6
- Added requirement on python3-module-z3c

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt5
- Added module for Python 3 (bootstrap)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt4.1
- Rebuild with Python-2.7

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt4
- Really added requirement on python-module-z3c

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3
- Added requirement on python-module-z3c

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 1.0.0-alt1.1
- Rebuilt with python-2.5.

* Wed Feb 21 2007 Ivan Fedorov <ns@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux.
