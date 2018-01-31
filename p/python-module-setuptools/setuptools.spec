%define _unpackaged_files_terminate_build 1
%define mname setuptools

Name: python-module-%mname
Epoch: 1
Version: 38.4.0
Release: alt1%ubt

Summary: Easily download, build, install, upgrade, and uninstall Python packages
License: MIT
Group: Development/Python
# Source-git: https://github.com/pypa/setuptools.git
Url: http://pypi.python.org/pypi/setuptools

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-six
BuildRequires: python3-module-six
# for test
BuildRequires: git-core
BuildRequires: python-module-pytest
BuildRequires: python-module-virtualenv
BuildRequires: python-module-path
BuildRequires: python-module-mock
BuildRequires: python-module-pip
BuildRequires: python-module-wheel
BuildRequires: python-module-contextlib2
BuildRequires: python-module-pytest-fixture-config
BuildRequires: python-module-tox
BuildRequires: python-module-pytest-flake8
BuildRequires: python3-module-pytest
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-path
BuildRequires: python3-module-mock
BuildRequires: python3-module-pip
BuildRequires: python3-module-wheel
BuildRequires: python3-module-contextlib2
BuildRequires: python3-module-pytest-fixture-config
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest-flake8
#

BuildArch: noarch
Provides: python-module-distribute = %EVR
Obsoletes: python-module-distribute <= 0.6.35-alt1

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

%package -n python3-module-%mname
Summary: Python Distutils Enhancements
Group: Development/Python3
Provides: python3-module-distribute = %EVR
# skip self requires
%add_python3_req_skip pkg_resources.extern.pyparsing
%add_python3_req_skip pkg_resources.extern.packaging.markers
%add_python3_req_skip pkg_resources.extern.packaging.requirements
%add_python3_req_skip pkg_resources.extern.packaging.specifiers
%add_python3_req_skip pkg_resources.extern.packaging.version
%add_python3_req_skip pkg_resources.extern.six
%add_python3_req_skip pkg_resources.extern.six.moves
%add_python3_req_skip pkg_resources.extern.six.moves.urllib
%add_python3_req_skip %mname.extern.six
%add_python3_req_skip %mname.extern.six.moves

%description -n python3-module-%mname
Setuptools is a collection of enhancements to the Python3 distutils
that allow you to more easily build and distribute Python3 packages,
especially ones that have dependencies on other packages.

%prep
%setup
%patch0 -p1

# Remove bundled exes
rm -f setuptools/*.exe

# do not generate version like release.postdate, we need release one
sed -i '/^tag_build =.*/d;/^tag_date = 1/d' setup.cfg

rm -rf ../python3
cp -a . ../python3

%build
python bootstrap.py
%python_build_debug

pushd ../python3
python3 bootstrap.py
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

rm -f %buildroot%_bindir/easy_install
ln -s easy_install-%_python_version %buildroot%_bindir/easy_install
ln -s easy_install-%_python3_version %buildroot%_bindir/easy_install3

%check
export PIP_INDEX_URL=http://host.invalid./
export PYTHONPATH=`pwd`:%python_sitelibdir_noarch:%_libdir/python%_python_version/site-packages
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py27 -v -- -v

pushd ../python3
export PYTHONPATH=`pwd`:%python3_sitelibdir_noarch:%_libdir/python%_python3_version/site-packages
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py35 -v -- -v
popd

%files
%doc LICENSE *.rst
%_bindir/easy_install
%_bindir/easy_install-%_python_version
%python_sitelibdir/pkg_resources
%python_sitelibdir/%mname
%python_sitelibdir/easy_install.*
%python_sitelibdir/%mname-%version-*.egg-info

%files docs
%doc docs/*.txt

%files -n python3-module-%mname
%_bindir/easy_install3
%_bindir/easy_install-%_python3_version
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/pkg_resources
%python3_sitelibdir/%mname
%python3_sitelibdir/easy_install.*
%python3_sitelibdir/%mname-%version-*.egg-info

%changelog
* Mon Jan 22 2018 Stanislav Levin <slev@altlinux.org> 1:38.4.0-alt1%ubt
- 38.2.3 -> 38.4.0

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
