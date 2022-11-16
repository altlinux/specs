%define _unpackaged_files_terminate_build 1
%define pypi_name setuptools
%define system_wheels_path %(%__python3 -c 'import os, sys, system_seed_wheels; sys.stdout.write(os.path.dirname(system_seed_wheels.__file__))' 2>/dev/null || echo unknown)

%def_with check

# bootstrap note: it doesn't work for now
# see https://github.com/pypa/setuptools/issues/2986

Name: python3-module-%pypi_name
Epoch: 1
Version: 65.5.1
Release: alt1

Summary: Easily download, build, install, upgrade, and uninstall Python packages
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pypa/setuptools.git
Url: https://pypi.org/project/setuptools/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# deps of self-hosted build backend
BuildRequires: python3(wheel)

%if_with check
BuildRequires: /dev/shm
BuildRequires: python3(jaraco.envs)
BuildRequires: python3(jaraco.path)
BuildRequires: python3(pip)
BuildRequires: python3(build)
BuildRequires: python3(filelock)
BuildRequires: python3(pip_run)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_xdist)
BuildRequires: python3(pytest_virtualenv)
BuildRequires: python3(pytest_enabler)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(tomli)
BuildRequires: python3(virtualenv)
BuildRequires: python3(wheel)
BuildRequires: python3-module-ini2toml-lite

# For the tests of the setuptools commands to do binary builds:
BuildPreReq: python3-dev
%endif

# namespace package for system seed wheels which will be used within venv
# created by virtualenv
BuildRequires: python3(system_seed_wheels)

Provides: python3-module-distribute = %EVR
Requires: python3-module-pkg_resources = %EVR
# setuptools has commands for doing binary builds; for them to work always:
Requires: python3-dev
# skip requires of self
%filter_from_requires /python3\(\.[[:digit:]]\)\?(pkg_resources\.extern\..*)/d
%filter_from_requires /python3\(\.[[:digit:]]\)\?(setuptools\.extern\..*)/d

# switch to 'local' copy of distutils
%filter_from_requires /python3(distutils\(\..*\)\?)/d

# hide bundled packages
%add_findprov_skiplist %python3_sitelibdir/setuptools/_vendor/*

# don't allow vendored distributions have deps other than stdlib
%add_findreq_skiplist %python3_sitelibdir/setuptools/_vendor/*

# ms windows compilers (some packages want to import these modules)
%add_findreq_skiplist %python3_sitelibdir/setuptools/_distutils/*msvc*compiler*.py*
%add_findprov_skiplist %python3_sitelibdir/setuptools/_distutils/*msvc*compiler*.py*

%package -n python3-module-pkg_resources
Summary: Package Discovery and Resource Access for Python3 libraries
Group: Development/Python3
# Not separated yet:
Conflicts: python3-module-%pypi_name < 39.2.0-alt3

# hide bundled packages
%add_findprov_skiplist %python3_sitelibdir/pkg_resources/_vendor/*

# don't allow vendored distributions have deps other than stdlib
%add_findreq_skiplist %python3_sitelibdir/pkg_resources/_vendor/*

%description
Setuptools is a collection of enhancements to the Python3 distutils
that allow you to more easily build and distribute Python3 packages,
especially ones that have dependencies on other packages.

%global pkg_resources_desc The "pkg_resources" module distributed with "setuptools" provides an API\
for Python libraries to access their resource files, and for extensible\
applications and frameworks to automatically discover plugins.  It also\
provides runtime support for using C extensions that are inside zipfile-format\
eggs, support for merging packages that have separately-distributed modules or\
subpackages, and APIs for managing Python's current "working set" of active\
packages.\
\
Any Python code can make use of pkg_resources at runtime (unlike setuptools,\
whose purpose is preparing packages).

%description -n python3-module-pkg_resources
%pkg_resources_desc

This package contains pkg_resources for Python3.

%package wheel
Summary: %summary
Group: Development/Python3
%py3_requires system_seed_wheels

%description wheel
Provides the seed package for virtualenv(packaged as wheel).

%prep
%setup
%autopatch -p1

# never unbundle vendored packages
# built wheel being installed into virtualenv will lack of unbundled packages

# Remove bundled exes
# today's paths containing *.exe
# setuptools/
# setuptools/_distutils/command/
find -type f -name '*.exe' -delete

# do not generate version like release.postdate, we need release one
sed -i '/^tag_build =.*/d;/^tag_date = 1/d' setup.cfg

# Make sure distutils looks at the right pyconfig.h file
# See https://bugzilla.redhat.com/show_bug.cgi?id=201434
# Similar for sysconfig: sysconfig.get_config_h_filename tries to locate
# pyconfig.h so it can be parsed, and needs to do this at runtime in site.py
# when python starts up (see https://bugzilla.redhat.com/show_bug.cgi?id=653058)
#
# Split this out so it goes directly to the pyconfig-32.h/pyconfig-64.h
# variants:
%ifarch x86_64 %ix86
%ifarch x86_64
%define _pyconfig_h pyconfig-64.h
%else
%define _pyconfig_h pyconfig-32.h
%endif

sed -i "s@'pyconfig.h'@'%_pyconfig_h'@" setuptools/_distutils/sysconfig.py
%endif

%build
%pyproject_build

%install
%pyproject_install

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

# package a built wheel (will be used within venv created by virtualenv)
built_wheel=$(cat ./dist/.wheeltracker) || \
        { echo Make sure you built a pyproject ; exit 1 ; }
mkdir -p "%buildroot%system_wheels_path"
cp -t "%buildroot%system_wheels_path/" "./dist/$built_wheel"

%check
export TOX_TESTENV_PASSENV='PIP_NO_BUILD_ISOLATION NO_INTERNET'
%tox_check_pyproject -- -vra

%files
%doc LICENSE *.rst
%python3_sitelibdir/_distutils_hack/
%python3_sitelibdir/distutils-precedence.pth
%python3_sitelibdir/setuptools

%files -n python3-module-pkg_resources
%doc LICENSE
%python3_sitelibdir/pkg_resources
# People write "setuptools" in *.egg-info/requires.txt (or in setup.py's requires)
# even if they use only the pkg_resources part;
# if setuptools-*.egg-info is not present, pkg_resources.load_entry_point() fails
# (for no real reason). Unfortunately, they have nothing better to write there...
# So we fool this mechanism by putting this file even
# if having incomplete setuptools code.
# Our autoreqs will take over the duty of tracking the real dependencies.
# (In future, we could patch their requires.txt.)
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files wheel
%system_wheels_path/setuptools-%version-*.whl

%changelog
* Fri Nov 11 2022 Stanislav Levin <slev@altlinux.org> 1:65.5.1-alt1
- 65.5.0 -> 65.5.1.

* Fri Oct 14 2022 Stanislav Levin <slev@altlinux.org> 1:65.5.0-alt1
- 65.4.1 -> 65.5.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 1:65.4.1-alt1
- 65.3.0 -> 65.4.1.

* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 1:65.3.0-alt1
- 64.0.3 -> 65.3.0.

* Sat Aug 13 2022 Stanislav Levin <slev@altlinux.org> 1:64.0.3-alt1
- 62.0.0 -> 64.0.3.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 1:62.0.0-alt1
- 61.3.0 -> 62.0.0.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 1:61.3.0-alt1
- 60.10.0 -> 61.3.0.

* Fri Mar 18 2022 Stanislav Levin <slev@altlinux.org> 1:60.10.0-alt1
- 60.9.3 -> 60.10.0.

* Tue Feb 22 2022 Stanislav Levin <slev@altlinux.org> 1:60.9.3-alt1
- 60.8.1 -> 60.9.3.

* Tue Feb 08 2022 Stanislav Levin <slev@altlinux.org> 1:60.8.1-alt1
- 60.5.4 -> 60.8.1.

* Tue Jan 18 2022 Stanislav Levin <slev@altlinux.org> 1:60.5.4-alt1
- 59.6.0 -> 60.5.4 (closes: #41643).

* Wed Dec 15 2021 Stanislav Levin <slev@altlinux.org> 1:59.6.0-alt1
- 58.4.0 -> 59.6.0.

* Mon Nov 01 2021 Stanislav Levin <slev@altlinux.org> 1:58.4.0-alt1
- 58.3.0 -> 58.4.0.

* Mon Oct 25 2021 Stanislav Levin <slev@altlinux.org> 1:58.3.0-alt1
- 58.2.0 -> 58.3.0.

* Fri Oct 15 2021 Stanislav Levin <slev@altlinux.org> 1:58.2.0-alt1
- 58.1.0 -> 58.2.0.

* Mon Sep 27 2021 Stanislav Levin <slev@altlinux.org> 1:58.1.0-alt1
- 58.0.4 -> 58.1.0.

* Fri Sep 10 2021 Stanislav Levin <slev@altlinux.org> 1:58.0.4-alt1
- 57.4.0 -> 58.0.4.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 1:57.4.0-alt1
- 57.0.0 -> 57.4.0.

* Mon May 24 2021 Stanislav Levin <slev@altlinux.org> 1:57.0.0-alt1
- 56.1.0 -> 57.0.0.

* Fri May 07 2021 Stanislav Levin <slev@altlinux.org> 1:56.1.0-alt1
- 56.0.0 -> 56.1.0.

* Sat Apr 24 2021 Stanislav Levin <slev@altlinux.org> 1:56.0.0-alt2
- Built wheel package(for virtualenv).

* Wed Apr 14 2021 Stanislav Levin <slev@altlinux.org> 1:56.0.0-alt1
- 54.2.0 -> 56.0.0.

* Fri Mar 26 2021 Stanislav Levin <slev@altlinux.org> 1:54.2.0-alt1
- 46.1.3 -> 54.2.0.

* Wed Oct 28 2020 Stanislav Levin <slev@altlinux.org> 1:46.1.3-alt2
- Fixed FTBFS(virtualenv 20.1.0).

* Tue Apr 21 2020 Stanislav Levin <slev@altlinux.org> 1:46.1.3-alt1
- 41.4.0 -> 46.1.3.

* Mon Oct 07 2019 Stanislav Levin <slev@altlinux.org> 1:41.4.0-alt1
- 41.2.0 -> 41.4.0.

* Mon Aug 26 2019 Stanislav Levin <slev@altlinux.org> 1:41.2.0-alt1
- 41.0.1 -> 41.2.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 1:41.0.1-alt3
- Fixed testing against Pytest 5.

* Mon Jun 03 2019 Stanislav Levin <slev@altlinux.org> 1:41.0.1-alt2
- Allowed testing against Pytest4.x.

* Tue May 14 2019 Stanislav Levin <slev@altlinux.org> 1:41.0.1-alt1
- 40.8.0 -> 41.0.1.

* Mon May 13 2019 Stanislav Levin <slev@altlinux.org> 1:40.8.0-alt2
- Fixed the testing against `virtualenv` 16.5.0.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1:40.8.0-alt1
- 40.6.3 -> 40.8.0.

* Thu Jan 10 2019 Stanislav Levin <slev@altlinux.org> 1:40.6.3-alt1
- 40.5.0 -> 40.6.3.

* Thu Nov 01 2018 Stanislav Levin <slev@altlinux.org> 1:40.5.0-alt1
- 40.4.3 -> 40.5.0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:40.4.3-alt1.qa1
- NMU: applied repocop patch

* Sun Oct 07 2018 Stanislav Levin <slev@altlinux.org> 1:40.4.3-alt1
- 39.2.0 -> 40.4.3.

* Mon Jul 02 2018 Ivan Zakharyaschev <imz@altlinux.org> 1:39.2.0-alt5
- (.spec) our setup.py won't require external setuptools,
  so we override this dep from rpm-build-python*. (Useful for bootstrap.)

* Fri Jun 29 2018 Ivan Zakharyaschev <imz@altlinux.org> 1:39.2.0-alt4
- put *.egg-info even in the uncomplete pkg_resources subpkg
  to fool the checking mechanism. (People declare that they use "setuptools",
  but actually they often just use pkg_resources. They shouldn't get an error.
  In future, we could patch their requires.txt.)
- Requires: python*-dev (for commands for binary builds to work
  always)

* Thu Jun 28 2018 Ivan Zakharyaschev <imz@altlinux.org> 1:39.2.0-alt3
- pkg_resources packaged separately (needed at runtime; unlike setuptools)

* Thu Jun 28 2018 Ivan Zakharyaschev <imz@altlinux.org> 1:39.2.0-alt2
- (.spec) cleanup (for maintainer's convenience)

* Thu May 31 2018 Stanislav Levin <slev@altlinux.org> 1:39.2.0-alt1
- 39.0.1 -> 39.2.0

* Thu Mar 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:39.0.1-alt2
- Marked docstrings with backslashes as raw strings.

* Sat Mar 24 2018 Stanislav Levin <slev@altlinux.org> 1:39.0.1-alt1
- 38.4.0 -> 39.0.1

* Sat Mar 24 2018 Stanislav Levin <slev@altlinux.org> 1:38.4.0-alt4
- Fix test command

* Thu Mar 22 2018 Grigory Ustinov <grenka@altlinux.org> 1:38.4.0-alt3
- Add patch for skipping some requires from glebfm@, adapted for new code.
  It restores feature from commit 362ea68 in 1:18.1-alt2 release. (Closes: #34658)

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:38.4.0-alt2.S1
- Updated build dependencies.

* Mon Jan 22 2018 Stanislav Levin <slev@altlinux.org> 1:38.4.0-alt1.S1
- 38.2.3 -> 38.4.0

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:38.2.3-alt1.S1
- Updated to upstream version 38.2.3.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:36.6.0-alt1.S1
- Updated to upstream version 36.6.0.
- Fixed issue with generated .pth files.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:36.5.0-alt1.S1
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
