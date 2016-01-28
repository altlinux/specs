%define modulename setuptools

%def_with python3

Name: python-module-%modulename
Epoch: 1
Version: 18.1
Release: alt2

Summary: Python Distutils Enhancements
License: PSF/ZPL
Group: Development/Python
URL: http://pypi.python.org/pypi/setuptools

Source0: %modulename.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel

Provides: python-module-distribute = %epoch:%version-%release

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
Setuptools is a collection of enhancements to the Python distutils
that allow you to more easily build and distribute Python packages,
especially ones that have dependencies on other packages.

%package tests
Summary: Tests for Setuptools
Group: Development/Python
Requires: %name = %EVR

%description tests
Setuptools is a collection of enhancements to the Python distutils
that allow you to more easily build and distribute Python packages,
especially ones that have dependencies on other packages.

This package contains tests for Setuptools.

%package docs
Summary: Documentation for Setuptools
Group: Development/Documentation
Provides: python-module-distribute-docs = %epoch:%version-%release

%description docs
Distribute is intended to replace Setuptools as the standard method for
working with Python module distributions.

This package contains documentation for Distribute.

%if_with python3
%package -n python3-module-%modulename
Summary: Python Distutils Enhancements
Group: Development/Python3
Provides: python3-module-distribute = %epoch:%version-%release

%description -n python3-module-%modulename
Setuptools is a collection of enhancements to the Python distutils
that allow you to more easily build and distribute Python packages,
especially ones that have dependencies on other packages.

%package  -n python3-module-%modulename-tests
Summary: Tests for Setuptools
Group: Development/Python3
Requires: python3-module-%modulename = %EVR

%description  -n python3-module-%modulename-tests
Setuptools is a collection of enhancements to the Python distutils
that allow you to more easily build and distribute Python packages,
especially ones that have dependencies on other packages.

This package contains tests for Setuptools.
%endif

%prep
%setup -n %modulename

#mv "setuptools/script template.py" \
#	setuptools/script_template.py
#mv "setuptools/script template (dev).py" \
#	"setuptools/script_template_(dev).py"

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
%python_install --optimize=2 --record=INSTALLED_FILES

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

%files
%doc *.txt
%_bindir/easy_install
%_bindir/easy_install-%_python_version
%python_sitelibdir/*
%exclude %python_sitelibdir/%modulename/command/test.py*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/%modulename/command/test.py*
%python_sitelibdir/*/tests

%files docs
%doc docs/*.txt

%if_with python3
%files -n python3-module-%modulename
%_bindir/easy_install3
%_bindir/easy_install-%_python3_version
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%modulename/command/test.py*
%exclude %python3_sitelibdir/%modulename/command/*/test.*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%modulename-tests
%python3_sitelibdir/%modulename/command/test.py*
%python3_sitelibdir/%modulename/command/*/test.*
%python3_sitelibdir/*/tests
%endif

%changelog
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
