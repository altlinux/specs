%define _unpackaged_files_terminate_build 1
%define oname cssutils

%def_with check

Name: python3-module-%oname
Version: 2.3.0
Release: alt2

Summary: CSS Cascading Style Sheets library for Python

Group: Development/Python3
License: LGPL-3.0
Url: https://pypi.org/project/cssutils/

# Source-git: https://github.com/jaraco/cssutils.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(lxml)
BuildRequires: python3(cssselect)
BuildRequires: python3(mock)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

# optional
%add_python3_req_skip google.appengine.api

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not
any rendering facilities!

%prep
%setup
%autopatch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
export NO_INTERNET=YES
export TOX_TESTENV_PASSENV='NO_INTERNET'
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false -- -vra

%files
%_bindir/csscapture
%_bindir/csscombine
%_bindir/cssparse
%python3_sitelibdir/%oname/
%python3_sitelibdir/encutils/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 2.3.0-alt2
- Fixed FTBFS (Python3.10).

* Fri Jan 14 2022 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 1.0.2 -> 2.3.0.

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt2
- build python3 package only

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- switch to build from tarball
- enable python3 module
- new version (1.0.2) with rpmgs script

* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt2
- exclude tests from package

* Tue Jul 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7b1-alt1.1
- Rebuild with Python-2.7

* Tue Jun 01 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.9.7b1-alt1
- 1st build for ALTLinux
- thanks to real@ fr spec skeleton
