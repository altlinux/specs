%define _unpackaged_files_terminate_build 1
%define modulename zope

# The purpose of this package is the ownership of xxx/site-packages/zope/
# namespace root directories. Other zope packages will be installed on those
# paths, but the packages can't own the root paths.

Name: python3-module-%modulename
Version: 3.3.0
Release: alt10
Summary: The ``zope`` package is a pure namespace package
License: ZPL-2.1
Group: Development/Python3
%py3_provides %modulename
BuildRequires(pre): rpm-build-python3

%description
%summary

%install
# Note: implicit namespace package can't contain __init__.py in namespace root
mkdir -p -m0755 %buildroot%python3_sitelibdir/%modulename/
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
mkdir -p -m0755 %buildroot%python3_sitelibdir_noarch/%modulename/
%endif

%files
%python3_sitelibdir/%modulename/
# for fixing: warning: File listed twice
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
%python3_sitelibdir_noarch/%modulename/
%endif

%changelog
* Thu Aug 07 2025 Stanislav Levin <slev@altlinux.org> 3.3.0-alt10
- Switched to native namespace scheme.
- Dropped excessive runtime dependencies.

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
