%define oname setuptools

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 38.2.3
Release: alt1%ubt

Summary: Python Distutils Enhancements
License: PSF/ZPL
Group: Development/Python
URL: http://pypi.python.org/pypi/setuptools

Source: %oname.tar

Patch0: 0001-Don-t-remove-setuptools.tests-from-the-installed-pac.patch
Patch1: 0002-dist.py-skip-checking-the-existence-of-system-PKG-IN.patch
Patch2: %oname-%version-alt-pth-generator.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python rpm-build-ubt
BuildRequires: python-devel
BuildRequires: python2.7(packaging) python2.7(pyparsing) python2.7(six) python2.7(appdirs)
BuildRequires: python-module-pytest python2.7(mock) python2.7(pytest_fixture_config) python2.7(pytest_virtualenv)
BuildRequires: python2.7(path) python2.7(contextlib2) python-module-virtualenv python-module-pip
# For more precise reqs:
%python_req_hier

Provides: python-module-distribute = %EVR

Provides: %name-tests = %EVR
Obsoletes: %name-tests <= 1:18.1-alt4
Obsoletes: python-module-distribute <= 0.6.35-alt1
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(packaging) python3(pyparsing) python3(six) python3(appdirs)
BuildRequires: python3-module-pytest python3(mock) python3(pytest_fixture_config) python3(pytest_virtualenv)
BuildRequires: python3(path) python3(contextlib2) python3-module-virtualenv python3-module-pip
# For more precise reqs:
%python3_req_hier
%endif

%description
Setuptools is a collection of enhancements to the Python distutils
that allow you to more easily build and distribute Python packages,
especially ones that have dependencies on other packages.

%package docs
Summary: Documentation for Setuptools
Group: Development/Documentation
Provides: python-module-distribute-docs = %EVR

%description docs
Distribute is intended to replace Setuptools as the standard method for
working with Python module distributions.

This package contains documentation for Distribute.

%if_with python3
%package -n python3-module-%oname
Summary: Python Distutils Enhancements
Group: Development/Python3
Provides: python3-module-distribute = %EVR

Provides: python3-module-%oname-tests = %EVR
Obsoletes: python3-module-%oname-tests <= 1:18.1-alt4

%description -n python3-module-%oname
Setuptools is a collection of enhancements to the Python distutils
that allow you to more easily build and distribute Python packages,
especially ones that have dependencies on other packages.
%endif

%prep
%setup -n %oname
%patch0
%patch1 -p2
%patch2 -p2

# don't use bundled packages
rm -rf pkg_resources/extern pkg_resources/_vendor setuptools/extern

find . -name '*.py' -type f | xargs sed -i \
	-e "s:from pkg_resources\.extern ::g" \
	-e "s:from pkg_resources\.extern\.:from :g" \
	-e "s:'pkg_resources\.extern\.:':g" \
	-e "s:from setuptools\.extern ::g" \
	-e "s:from setuptools\.extern\.:from :g"

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
#python setup.py test

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
mkdir -p %buildroot%python_sitelibdir
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -f %buildroot%_bindir/easy_install
ln -s easy_install-%_python_version %buildroot%_bindir/easy_install
%if_with python3
ln -s easy_install-%_python3_version %buildroot%_bindir/easy_install3
%endif

%check
# TODO: fix or disable remaining failing tests
PYTHONPATH=$(pwd) py.test -v ||:

%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3 -v ||:
popd
%endif

%files
%doc *.rst
%_bindir/easy_install
%_bindir/easy_install-%_python_version
%python_sitelibdir/pkg_resources/
%dir %python_sitelibdir/%oname/
%python_sitelibdir/%oname/*.*
%python_sitelibdir/%oname/command/
%python_sitelibdir/%oname/tests/
%python_sitelibdir/easy_install.*
%python_sitelibdir/%oname-%version-*.egg-info

%files docs
%doc docs/*.txt

%if_with python3
%files -n python3-module-%oname
%_bindir/easy_install3
%_bindir/easy_install-%_python3_version
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/pkg_resources/
%dir %python3_sitelibdir/%oname/
%python3_sitelibdir/%oname/__pycache__/
%python3_sitelibdir/%oname/*.*
%python3_sitelibdir/%oname/command/
%python3_sitelibdir/%oname/tests/
%python3_sitelibdir/easy_install.*
%python3_sitelibdir/%oname-%version-*.egg-info
%endif

%changelog
* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:38.2.3-alt1%ubt
- Updated to upstream version 38.2.3.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:36.6.0-alt1%ubt
- Updated to upstream version 36.6.0.
- Fixed issue with generated .pth files.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:36.5.0-alt1%ubt
- Updated to new version.

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1:18.5-alt1
- new version 18.5 (with rpmrb script)
- add obsoletes python-module-distribute (ALT bug #32546)

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1:18.4-alt1
- new version 18.4 (with rpmrb script)

* Wed Jun 14 2017 Lenar Shakirov <snejok@altlinux.ru> 1:18.1-alt5
- Merge %name-tests into %name (pbr new version requires it)

* Thu Jul 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:18.1-alt4
- %%python{,3}_req_hier for more precise safer reqs

* Wed Jul 27 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:18.1-alt3.2
- rebuild with rpm-build-python{,3} where the incomplete packaging of
  __pycache__/* files has been fixed (due to unlink/compile ordering).

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:18.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Wed Mar 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:18.1-alt3
- Avoid the self-dependency often generated by buildreq when
  setuptools are used (by not checking the existence of system PKG-INFO
  for new Distribution instances during rpmbuild).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:18.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:18.1-alt2
- command/test.py: added hack to skip search for install_requires and
  tests_require during rpmbuild.

* Wed Aug 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:18.1-alt1
- Version 18.1

* Sat Jul 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:18.0.1-alt1
- Version 18.0.1

* Mon Jun 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:17.1-alt1
- Version 17.1

* Fri May 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:17.0-alt1
- Version 17.0

* Fri May 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:16.0-alt1
- Version 16.0

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:15.2-alt1
- Version 15.2

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:15.1-alt1
- Version 15.1

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:14.3.1-alt1
- Version 14.3.1

* Mon Mar 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:14.3-alt1
- Version 14.3

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:14.2-alt1
- Version 14.2

* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:14.0-alt1
- Version 14.0

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:13.0.1-alt1
- Version 13.0.1

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:12.4-alt1
- Version 12.4

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:12.3-alt1
- Version 12.3

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:12.2-alt1
- Version 12.2

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:12.1-alt1
- Version 12.1

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:12.0.5-alt1
- Version 12.0.5

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:12.0.4-alt1
- Version 12.0.4

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:12.0.3-alt1
- Version 12.0.3

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:12.0.1-alt1
- Version 12.0.1

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:11.3.1-alt1
- Version 11.3.1

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:11.3-alt2
- Moved all tests into tests subpackages

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:11.3-alt1
- Version 11.3

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:11.0-alt1
- Version 11.0

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:10.1-alt1
- Version 10.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:9.1-alt1
- Version 9.1

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:9.0-alt1
- Version 9.0

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:8.3-alt1
- Version 8.3

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:8.2.1-alt1
- Version 8.2.1

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:8.0.4-alt1
- Version 8.0.4

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:8.0.2-alt1
- Version 8.0.2

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.4.1-alt1
- Version 5.4.1

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.4.2-alt1
- Version 1.4.2

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.5-alt2
- Fixed dependencies

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.5-alt1
- Version 1.1.5

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6-alt1.c11
- Version 0.6c11
- Extracted tests into separate package

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6-alt1.c9.1
- Rebuilt with python 2.6

* Sat Nov 29 2008 Ivan Fedorov <ns@altlinux.org> 1:0.6-alt1.c9
- fixed #18041
- 0.6c9
  + Minor changes for Jython compatibility, including skipping tests
    that can't work on Jython.
  + Support Subversion 1.5

  + Removed use of deprecated ``md5`` module if ``hashlib`` is available

  + Fixed ``bdist_wininst upload`` trying to upload the ``.exe`` twice

  + Fixed ``bdist_egg`` putting a ``native_libs.txt`` in the source
    package's ``.egg-info``, when it should only be in the built egg's
    ``EGG-INFO``.

  + Ensure that _full_name is set on all shared libs before extensions
    are checked for shared lib usage. (Fixes a bug in the experimental
    shared library build support.)

  + Fix to allow unpacked eggs containing native libraries to fail more
    gracefully under Google App Engine (with an ``ImportError`` loading
    the C-based module, instead of getting a ``NameError``).

* Fri May 23 2008 Ivan Fedorov <ns@altlinux.org> 1:0.6-alt1.c8
- 0.6c8
- Fixed a missing files problem when using Windows source distributions on
  non-Windows platforms, due to distutils not handling manifest file line
  endings correctly.

- Updated Pyrex support to work with Pyrex 0.9.6 and higher.

- Minor changes for Jython compatibility

- Fixed not installing eggs in ``install_requires`` if they were also used for
  ``setup_requires`` or ``tests_require``.

- Fixed not fetching eggs in ``install_requires`` when running tests.

- Allow ``ez_setup.use_setuptools()`` to upgrade existing setuptools
  installations when called from a standalone ``setup.py``.

- Added a warning if a namespace package is declared, but its parent package
  is not also declared as a namespace.

* Thu Oct 25 2007 Ivan Fedorov <ns@altlinux.org> 1:0.6-alt1.c7
- 0.6c7
- Fixed ``distutils.filelist.findall()`` crashing on broken symlinks,
  and ``egg_info`` command failing on new, uncommitted SVN directories.
- Fix import problems with nested namespace packages installed via
  ``--root`` or ``--single-version-externally-managed``, due to the
  parent package not having the child package as an attribute.

* Fri Jul 13 2007 Ivan Fedorov <ns@altlinux.org> 1:0.6-alt1.c6
- 0.6c6
- Added --egg-path option to develop command, allowing you to force
  .egg-link files to use relative paths (allowing them to be shared
  across platforms on a networked drive).
- Fix not building binary RPMs correctly.
- Fix "eggsecutables" (such as setuptools' own egg) only being runnable
  with bash-compatible shells.
- Fix #! parsing problems in Windows .exe script wrappers, when there
  was whitespace inside a quoted argument or at the end of the #! line
  (a regression introduced in 0.6c4).
- Fix test command possibly failing if an older version of the project
  being tested was installed on sys.path ahead of the test source
  directory.
- Fix find_packages() treating ez_setup and directories with . in their
  names as packages.

* Tue Mar 20 2007 Ivan Fedorov <ns@altlinux.ru> 1:0.6-alt2.c5
- build from git
- unpack %%SOURCE0

* Tue Feb 20 2007 Ivan Fedorov <ns@altlinux.ru> 1:0.6-alt1.c5
- 0.6c5

* Tue Jan 30 2007 Ivan Fedorov <ns@altlinux.ru> 1:0.6-alt1.c3
- 0.6c3
- remove %%_bindir/easy_install.py

* Sun Jul 16 2006 Grigory Batalov <bga@altlinux.ru> 1:0.6-alt1.b4
- 0.6b4

* Fri May 19 2006 Ivan Fedorov <ns@altlinux.ru> 1:0.6-alt1.b1
- 0.6b1

* Thu Apr 13 2006 Ivan Fedorov <ns@altlinux.ru> 1:0.6-alt1.a11
- 0.6a11

* Sun Feb 26 2006 Ivan Fedorov <ns@altlinux.ru> 1:0.6-alt1.a10
- 0.6a10

* Sun Jan 08 2006 Ivan Fedorov <ns@altlinux.ru> 0.6a9-alt1
- 0.6a9
- spec modified to conform altlinux python policy

* Thu Dec 29 2005 Grigory Batalov <bga@altlinux.ru> 0.6a8-alt1
- Build for ALT Linux

* Sun Nov 13 2005 Michael Scherer <misc@mandriva.org> 0.6a7-1mdk
- initial package ( description stolen from debian, thanks  Matthias Klose )
