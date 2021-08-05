Summary: The ``zope`` package is a pure namespace package
Version: 3.3.0
Release: alt9
License: ZPL
Group: Development/Python3

%define modulename zope
%define oname zope
Name: python3-module-%modulename

BuildRequires(pre): rpm-build-python3
Requires: python3-module-zope.interface
Requires: python3-module-zc

%description
%summary

%install
mkdir -p %buildroot/%python3_sitelibdir/%modulename
cat <<EOF > %buildroot/%python3_sitelibdir/%modulename/__init__.py
##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
#
# This file is necessary to make this directory a package.

try:
    # Declare this a namespace package if pkg_resources is available.
    import pkg_resources
    pkg_resources.declare_namespace('zope')
except ImportError:
    pass
EOF

%files
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/__init__.py*
%dir %python3_sitelibdir/%oname/__pycache__
%python3_sitelibdir/%oname/__pycache__/__init__.*

%changelog
* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt9
- Drop python2 support.

* Fri Apr 05 2019 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt8.5
- Rebuild for python3.7.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.0-alt8.4
- (.spec) simplified the use of macros (It is better for girar-nmu, too).

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.0-alt8.3
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.0-alt8.2
- Added requirement on python3-module-zope.interface

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.0-alt8.1
- Removed requirement on python3-module-zope.interface
  (bootstrap for Python 3.3)

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt8
- Added requirement on python3-module-zope.interface

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt7
- Avoid requirement for python-module-zope on python3-module-zc

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt6
- Added module for Python 3 (bootstrap)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.0-alt5.1
- Rebuild with Python-2.7

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt5
- Added requirement on python-module-zc

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt4
- Rebuilt as archdep (for others zope modules

* Mon Nov 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt3
- Rebuilt as noarch package

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 3.3.0-alt1.1
- Rebuilt with python-2.5.

* Sun Feb 18 2007 Ivan Fedorov <ns@altlinux.ru> 3.3.0-alt1
- Initial build for ALT Linux.
