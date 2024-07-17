%define modulename cherrypy

%def_with check

Name: python3-module-%modulename
Version: 18.10.0
Release: alt1

Summary: CherryPy is a pythonic, object-oriented web development framework

License: BSD-3-Clause
Group: Development/Python3
URL: http://www.cherrypy.org
BuildArch: noarch

# git clone https://github.com/cherrypy/cherrypy
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-cheroot
BuildRequires: python3-module-portend
BuildRequires: python3-module-zc.lockfile
BuildRequires: python3-module-jaraco.collections
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-cheroot-tests
BuildRequires: python3-module-path
BuildRequires: python3-module-pytest-services
%endif

# win32 depends on pywin32
# note: don't remove win32 module because other packages may rely on it
%add_findreq_skiplist %python3_sitelibdir/%modulename/process/win32.py

%description
Your CherryPy powered web applications are in fact stand-alone Python
applications embedding their own multi-threaded web server. You can deploy
them anywhere you can run Python applications. Apache is not required,
but it's possible to run a CherryPy application behind it.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install
mv %buildroot%_bindir/cherryd %buildroot%_bindir/cherryd3

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%tox_check_pyproject

%files
%doc cherrypy/tutorial
%_bindir/cherryd3
%python3_sitelibdir/%modulename
%python3_sitelibdir/CherryPy-%version.dist-info
%exclude %python3_sitelibdir/%modulename/test

%changelog
* Tue Jul 16 2024 Grigory Ustinov <grenka@altlinux.org> 18.10.0-alt1
- Automatically updated to 18.10.0.
- Built with check.

* Wed Dec 13 2023 Grigory Ustinov <grenka@altlinux.org> 18.9.0-alt1
- Automatically updated to 18.9.0.

* Mon Jun 12 2023 Grigory Ustinov <grenka@altlinux.org> 18.8.0-alt1
- Automatically updated to 18.8.0 (Closes: #46442).

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 18.6.1-alt1
- 18.6.0 -> 18.6.1.

* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 18.6.0-alt1
- New version.

* Fri Jan 24 2020 Grigory Ustinov <grenka@altlinux.org> 18.5.0-alt2
- Got rid of python2 support (Closes: #37898).
- Build with docs.
- Fix license.

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
