%define _unpackaged_files_terminate_build 1
%define oname wheel
%define system_wheels_path %(%__python3 -c 'import os, sys, system_seed_wheels; sys.stdout.write(os.path.dirname(system_seed_wheels.__file__))')

%def_with check
%def_without bootstrap

Name: python3-module-%oname
Version: 0.37.1
Release: alt1
Summary: A built-package format for Python3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/wheel/
Packager: Python Development Team <python@packages.altlinux.org>

# Source-url: https://github.com/pypa/wheel.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
%endif

# dependencies for build wheel
%if_without bootstrap
BuildRequires: python3(system_seed_wheels)
%endif

# hide provides of bundled packages
%add_findprov_skiplist %python3_sitelibdir/wheel/vendored/*

%description
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%if_without bootstrap
%package wheel
Summary: %summary
Group: Development/Python3
%py3_requires system_seed_wheels

%description wheel
Provides the seed package for virtualenv(packaged as wheel).
%endif

%prep
%setup
%autopatch -p1

# never unbundle vendored packages
# built wheel being installed into virtualenv will lack of unbundled packages

%build
%python3_build

%install
%python3_install

# since we package python modules as arch dependent
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%if_without bootstrap
# point to just built and installed wheel package
export PYTHONPATH=%buildroot%python3_sitelibdir
%{python3_setup:} bdist_wheel --dist-dir %buildroot%system_wheels_path/
%endif

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --no-deps -vvr

%files
%doc *.txt
%_bindir/wheel
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%if_without bootstrap
%files wheel
%system_wheels_path/wheel-%version-*.whl
%endif

%changelog
* Thu Jan 13 2022 Stanislav Levin <slev@altlinux.org> 0.37.1-alt1
- 0.37.0 -> 0.37.1.

* Fri Sep 10 2021 Stanislav Levin <slev@altlinux.org> 0.37.0-alt1
- 0.36.2 -> 0.37.0.

* Fri Apr 23 2021 Stanislav Levin <slev@altlinux.org> 0.36.2-alt1
- 0.34.2 -> 0.36.2.
- Enabled testing.
- Built wheel package(for virtualenv).

* Sat Apr 11 2020 Alexey Shabalin <shaba@altlinux.org> 0.34.2-alt1
- 0.34.2

