%define oname zc.isithanging

%def_disable check

Name: python3-module-%oname
Version: 0.3.0
Release: alt2

Summary: A zc.monitor plugin for testing whether function hangs
License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/zc.isithanging/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires zc

BuildRequires: python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-unittest2 python3-module-zc.thread python3-module-zope.testing


%description
Somtimes, computation stops and it can be hard to find out why. Tools
like strace can be helpful, but are very low level. If a call hangs
calling external network services, all you might see is a select or poll
call and not what serveice was being called.

Isithanging provides a simple registry and a helper function for
registering and unregistering calls.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing zc.thread

%description tests
Somtimes, computation stops and it can be hard to find out why. Tools
like strace can be helpful, but are very low level. If a call hangs
calling external network services, all you might see is a select or poll
call and not what serveice was being called.

Isithanging provides a simple registry and a helper function for
registering and unregistering calls.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
cp README.rst src/zc/isithanging/
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/zc/*/tests.*
%exclude %python3_sitelibdir/zc/*/*/tests.*

%files tests
%python3_sitelibdir/zc/*/tests.*
%python3_sitelibdir/zc/*/*/tests.*


%changelog
* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt1.2
- Rebuild with python3.7.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

