%define _unpackaged_files_terminate_build 1
%define pypi_name sqlite-vec
%define mod_name sqlite_vec

%def_with check

Name: python3-module-sqlite-vec
Version: 0.1.9
Release: alt2

Summary: A vector search SQLite extension that runs anywhere
License: Apache-2.0 OR MIT
Group: Development/Python3
Url: https://alexgarcia.xyz/sqlite-vec/
Vcs: https://github.com/asg017/sqlite-vec

Source0: %name-%version.tar
Source1: %name-%version-python.tar
Source2: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: pkgconfig(sqlite3)
%if_with check
BuildRequires: python3-modules-sqlite3
%endif

%description
%summary.

%prep
%setup -a1
%autopatch -p1

cd alt
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%make sqlite-vec.h
cd alt
%pyproject_build

%install
cd alt
%pyproject_install

%check
cd alt
rm -r %mod_name
%pyproject_run -- python3 test.py

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 01 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.9-alt2
- Set check requirements explicitly.

* Mon Aug 31 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.9-alt1
- Packaged for ALT Sisyphus.
