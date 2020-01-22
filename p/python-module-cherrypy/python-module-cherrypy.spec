%define modulename cherrypy

%def_without python2
%def_with python3
%def_without docs

Name: python-module-%modulename
Version: 18.5.0
Release: alt1

%setup_python_module %modulename

Summary: CherryPy is a pythonic, object-oriented web development framework
License: BSD
Group: Development/Python

URL: http://www.cherrypy.org
BuildArch: noarch

# git clone https://github.com/cherrypy/cherrypy
Source: %modulename-%version.tar
Patch: disable-codecov_button.patch

Conflicts: python-module-cherrypy2 >= 2.3.0-alt1

BuildRequires: python-module-setuptools_scm

%if_with python3
BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires: python3-module-setuptools
%endif
BuildRequires: python3-module-setuptools_scm
BuildRequires: python-module-alabaster
BuildRequires: python-module-coverage
BuildRequires: python-module-docutils
BuildRequires: python-module-html5lib
BuildRequires: python-module-nose
BuildRequires: python-module-objects.inv
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-rst.linker
BuildRequires: python3-module-jaraco.packaging
BuildRequires: python3-module-cheroot
BuildRequires: time
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

%package tests
Summary: Tests for CherryPy
Group: Development/Python
Requires: %name = %version-%release

%description tests
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

This package contains tests for CherryPy.

%package pickles
Summary: Pickles for CherryPy
Group: Development/Python

%description pickles
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

This package contains pickles for CherryPy.

%package docs
Summary: Documentation for CherryPy
Group: Development/Documentation
BuildArch: noarch

%description docs
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

This package contains documentation for CherryPy.

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
%setup -n %modulename-%version
%patch -p1
sed -i "s/f'/'/;s/f\"/\"/" docs/conf.py
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%if_with python2
%python_build
%endif
%if_with python3
pushd ../python3
subst 's|%_bindir/python|%_bindir/python3|' \
      cherrypy/process/servers.py cherrypy/test/sessiondemo.py
%python3_build
popd
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/cherryd %buildroot%_bindir/cherryd3
%endif
%if_with python2
%python_install
%endif

%if_with docs
export PYTHONPATH=%_builddir/python3
pushd docs
%if_with python2
python3 /usr/bin/sphinx-build -b pickle -d build/doctrees . build/pickle
%endif
python3 /usr/bin/sphinx-build -b html -d build/doctrees . build/html
popd
%endif

%if_with python2
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%modulename/
%endif

%if_with python2
%files
%doc cherrypy/tutorial
%_bindir/cherryd
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/pickle
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/test

%files pickles
%python_sitelibdir/%modulename/pickle

%files tests
%python_sitelibdir/*/test
%endif

%if_with docs
%files docs
%doc docs/build/html/*
%endif

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
* Wed Jan 22 2020 Andrey Cherepanov <cas@altlinux.org> 18.5.0-alt1
- New version (ALT #37898).
- Build without docs.

* Wed Apr 24 2019 Andrey Cherepanov <cas@altlinux.org> 14.2.0-alt2
- Build without python2 support.

* Sat May 26 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.0-alt1
- New version.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.5.1-alt1.hg20140627.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.1-alt1.hg20140627.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.5.1-alt1.hg20140627.1
- NMU: Use buildreq for BR.

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1.hg20140627
- Version 3.5.1

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.4-alt2.hg20131113
- Moved tests into separate package

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.4-alt1.hg20131113
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.4-alt1.hg20130409
- Version 3.2.4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.2.2-alt1.hg20120408.1
- Rebuild with Python-3.3

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
