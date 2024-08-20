%define _unpackaged_files_terminate_build 1
%define pypi_name wheel
%define system_wheels_path %(%__python3 -c 'import os, sys, system_seed_wheels; sys.stdout.write(os.path.dirname(system_seed_wheels.__file__))' 2>/dev/null || echo unknown)

%def_with check

Name: python3-module-%pypi_name
Version: 0.44.0
Release: alt1
Summary: A built-package format for Python3
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/wheel/
VCS: https://github.com/pypa/wheel.git

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manage deps with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

# namespace package for system seed wheels which will be used within venv
# created by virtualenv
BuildRequires: python3(system_seed_wheels)

%if_with check
%pyproject_builddeps_metadata_extra test
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

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
install -m0644 -t "%buildroot%system_wheels_path/" "./dist/$built_wheel"

%check
%pyproject_run_pytest -ra

%files
%doc *.txt
%_bindir/wheel
%python3_sitelibdir/wheel/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files wheel
%system_wheels_path/%{pep427_name %pypi_name}-%version-*.whl

%changelog
* Mon Aug 19 2024 Stanislav Levin <slev@altlinux.org> 0.44.0-alt1
- 0.43.0 -> 0.44.0.

* Tue Mar 12 2024 Stanislav Levin <slev@altlinux.org> 0.43.0-alt1
- 0.42.0 -> 0.43.0.

* Thu Dec 07 2023 Stanislav Levin <slev@altlinux.org> 0.42.0-alt1
- 0.41.3 -> 0.42.0.

* Thu Nov 02 2023 Stanislav Levin <slev@altlinux.org> 0.41.3-alt1
- 0.41.2 -> 0.41.3.

* Tue Sep 26 2023 Stanislav Levin <slev@altlinux.org> 0.41.2-alt1
- 0.41.1 -> 0.41.2.

* Mon Aug 07 2023 Stanislav Levin <slev@altlinux.org> 0.41.1-alt1
- 0.41.0 -> 0.41.1.

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 0.41.0-alt1
- 0.40.0 -> 0.41.0.

* Thu Apr 20 2023 Stanislav Levin <slev@altlinux.org> 0.40.0-alt1
- 0.38.4 -> 0.40.0.

* Fri Nov 11 2022 Stanislav Levin <slev@altlinux.org> 0.38.4-alt1
- 0.37.1 -> 0.38.4.

* Fri Aug 12 2022 Stanislav Levin <slev@altlinux.org> 0.37.1-alt2
- Modernized packaging.

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

