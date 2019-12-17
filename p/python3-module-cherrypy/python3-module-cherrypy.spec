%define modulename cherrypy

Name: python3-module-%modulename
Version: 18.5.0
Release: alt1
Summary: CherryPy is a pythonic, object-oriented web development framework
License: BSD
Group: Development/Python

URL: http://www.cherrypy.org
BuildArch: noarch

# git https://github.com/cherrypy/cherrypy
Source: %name-%version.tar
Patch0: python3-module-cherrypy-disable-codecov_button.patch
Patch1: python3-module-cherrypy-python3-shebang.patch
Patch2: %name-%version-%release.patch

Conflicts: python-module-cherrypy2 >= 2.3.0-alt1
Conflicts: python-module-cherrypy <= 14.2.0-alt1.1

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-graphviz
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-simplejson
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-cov-core
BuildRequires: python3-module-objgraph
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-sugar
BuildRequires: python3-module-pytest-services >= 1.3.1
BuildRequires: python3-module-rst.linker
BuildRequires: python3-module-jaraco.packaging
BuildRequires: python3-module-jaraco.collections
BuildRequires: python3-module-memcached
BuildRequires: python3-module-cheroot-tests
BuildRequires: python3-module-routes
BuildRequires: python3(tox)
BuildRequires: python3(pip)
BuildRequires: python3(portend)
BuildRequires: python3(path)
BuildRequires: python3(zc)
BuildRequires: python3(requests_toolbelt)
BuildRequires: python3(cheroot)
BuildRequires: python3(zc.lockfile)
# proc and memcached for tests
BuildRequires: memcached
BuildRequires: /proc
BuildRequires: time

%add_python3_req_skip win32api
%add_python3_req_skip win32con
%add_python3_req_skip win32event
%add_python3_req_skip win32service
%add_python3_req_skip win32serviceutil
%add_python3_req_skip sqlobject

%description
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

%package tests
Summary: Tests for CherryPy
Group: Development/Python
Requires: %name = %EVR

%description tests
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

This package contains tests for CherryPy.

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

%prep
%setup 
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i "s/f'/'/;s/f\"/\"/" docs/conf.py

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build
cp ./CherryPy.egg-info/PKG-INFO .

# TODO - enable documentation 
PYTHONPATH=. python3 /usr/bin/sphinx-build-3 -b html -d build/doctrees docs/ build/html

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install
rm -rf %buildroot%python3_sitelibdir/*/tutorial

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -v

%files
%_bindir/cherryd
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files docs
# TODO - build documentation
%doc build/html/*
%doc cherrypy/tutorial

%files tests
%python3_sitelibdir/*/test

%changelog
* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 18.5.0-alt1
- 18.5.0
- enabled tests

* Sun Oct 06 2019 Anton Farygin <rider@altlinux.ru> 18.3.0-alt2
- fixed build with cheroot 7.0.0-alt1

* Thu Oct 03 2019 Anton Farygin <rider@altlinux.ru> 18.3.0-alt1
- 18.3.0
- added conflicts with python-module-cherrypy for python-2.7 (closes: #37292)
- enabled build of the documentation

* Sat Sep 21 2019 Anton Farygin <rider@altlinux.ru> 18.2.0-alt1
- 18.2.0
- removed python-2.7 support
- temporarily disabled the documentation build through sphinx due to
  need to update sphinx
- enabled tests

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
