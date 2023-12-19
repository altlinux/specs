%define _unpackaged_files_terminate_build 1
%define pypi_name asyncpg

%def_with check

Name: python3-module-%pypi_name
Version: 0.29.0
Release: alt2

Summary: A fast PostgreSQL Database Client Library for Python/asyncio
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/asyncpg/
Vcs: https://github.com/MagicStack/asyncpg

Source0: %name-%version.tar
Source1: submodules.tar
Source2: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
BuildRequires: libpq5-devel
BuildRequires: postgresql15-server
BuildRequires: postgresql15-contrib
%endif

%description
asyncpg is a database interface library designed specifically for PostgreSQL
and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL
server binary protocol for use with Python's asyncio framework.

asyncpg requires Python 3.8 or later and is supported for PostgreSQL
versions 9.5 to 16. Older PostgreSQL versions or other databases implementing
the PostgreSQL protocol may work, but are not being actively tested.

%prep
%setup -a1
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# Don't append current directory to sys.path to
# avoid 'ModuleNotFoundError' error, becase
# the package has modules which need compiling.
%pyproject_run -- pytest -vra ./tests

%files
%doc README.rst LICENSE AUTHORS
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Dec 19 2023 Anton Zhukharev <ancieg@altlinux.org> 0.29.0-alt2
- Fixed building with cython>3.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.29.0-alt1
- Updated to 0.29.0.

* Mon Jul 24 2023 Anton Zhukharev <ancieg@altlinux.org> 0.28.0-alt1
- Updated to 0.28.0.

* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.27.0-alt1
- New version.

* Sun Aug 07 2022 Anton Zhukharev <ancieg@altlinux.org> 0.26.0-alt1
- initial build for Sisyphus

