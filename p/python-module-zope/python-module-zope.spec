%define oname zope
%define version 3.3.0
%define release alt8

%def_with python3

%setup_python_module %oname

Summary: The ``zope`` package is a pure namespace package
Name: %packagename
Version: %version
Release: %release
License: ZPL
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>
Requires: python-module-zope.interface >= 3.3.0-alt2
Requires: python-module-zc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
%summary

%if_with python3
%package -n python3-module-%oname
Summary: The ``zope`` package is a pure namespace package (Python 3)
Group: Development/Python3
Requires: python3-module-zope.interface
Requires: python3-module-zc

%description -n python3-module-%oname
%summary
%endif

%install
mkdir -p %buildroot/%python_sitelibdir/%modulename
cat <<EOF > %buildroot/%python_sitelibdir/%modulename/__init__.py
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

%if_with python3
install -d %buildroot/%python3_sitelibdir/%oname
install -m644 %buildroot/%python_sitelibdir/%modulename/__init__.py \
	%buildroot/%python3_sitelibdir/%oname/
%endif

%files
%dir %python_sitelibdir/%modulename
%python_sitelibdir/%modulename/__init__.py*

%if_with python3
%files -n python3-module-%oname
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/__init__.py*
%dir %python3_sitelibdir/%oname/__pycache__
%python3_sitelibdir/%oname/__pycache__/__init__.*
%endif

%changelog
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
