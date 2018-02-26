%define modulename cherrypy

%def_with python3

Name: python-module-%modulename
Version: 3.2.2
Release: alt1.hg20120408

%setup_python_module %modulename

Summary: CherryPy is a pythonic, object-oriented web development framework
License: BSD
Group: Development/Python

URL: http://www.cherrypy.org
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>
BuildArch: noarch

# hg clone https://bitbucket.org/cherrypy/cherrypy
Source: http://download.cherrypy.org/cherrypy/%version/%name-%version.tar

Conflicts: python-module-cherrypy2 >= 2.3.0-alt1

BuildPreReq: %py_dependencies setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%add_python_req_skip win32api
%add_python_req_skip win32con
%add_python_req_skip win32event
%add_python_req_skip win32service
%add_python_req_skip win32serviceutil

%description
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

%if_with python3
%package -n python3-module-%modulename
Summary: CherryPy is a pythonic, object-oriented web development framework (Python 3)
Group: Development/Python3
%add_python3_req_skip win32api
%add_python3_req_skip win32con
%add_python3_req_skip win32event
%add_python3_req_skip win32service
%add_python3_req_skip win32serviceutil
%add_python3_req_skip sqlobject

%description -n python3-module-%modulename
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

%package -n python3-module-%modulename-tests
Summary: Tests for CherryPy (Python 3)
Group: Development/Python3
Requires: python3-module-%modulename = %version-%release

%description -n python3-module-%modulename-tests
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

This package contains tests for CherryPy (Python 3).
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i ||:
done
sed -i 's|%_bindir/python|%_bindir/python3|' \
	cherrypy/process/servers.py cherrypy/test/sessiondemo.py
sed -i 's|%_bindir/env python|%_bindir/env python3|' cherrypy/cherryd
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/cherryd %buildroot%_bindir/cherryd3
%endif
%python_install

%files
%doc cherrypy/tutorial
%_bindir/cherryd
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%doc cherrypy/tutorial
%_bindir/cherryd3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%modulename-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.2-alt1.hg20120408
- Version 3.2.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.2-alt1.1
- Rebuild with Python-2.7

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt1
- update to svn tag 3.1.2
- pack cherryd script

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt2
- Rebuilt with python 2.6

* Mon Apr 06 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.1.1-alt1
- 3.1.1 (Closes: #15276)
- Add conflict with python-module-cherrypy2

* Sat Apr 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.3.0-alt1
- 2.3.0

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.1.0-alt1.1
- Rebuilt with python-2.5.

* Sun Oct 30 2005 Maxim Bodyansky <maximbo@altlinux.ru> 2.1.0-alt1
- Initial build for Sisyphus
