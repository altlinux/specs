%define _unpackaged_files_terminate_build 1
%define pypi_name xxhash
%define mod_name %pypi_name

%def_with check

# %%python3_set_limited_api is not supported yet

Name: python3-module-%pypi_name
Version: 3.8.0
Release: alt1
Summary: Binding for xxHash
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/xxhash/
VCS: https://github.com/ifduyue/python-xxhash.git

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libxxhash-devel
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
xxhash is a Python binding for the xxHash library.

%prep
%setup
%patch -p1

# remove bundled libs
rm -r deps

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
# make use of system xxhash library
export XXHASH_LINK_SO=1
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
# skip benchmark tests
rm tests/test_benchmark.py
%pyproject_run -- bash -s <<-'ENDUNITTEST'
set -eu
cd tests
python -m unittest -v
ENDUNITTEST

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 29 2026 Stanislav Levin <slev@altlinux.org> 3.8.0-alt1
- 3.7.0 -> 3.8.0

* Tue Apr 28 2026 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.0 -> 3.7.0.

* Tue Dec 16 2025 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.5.0 -> 3.6.0.

* Wed Sep 25 2024 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 3.4.1 -> 3.5.0.

* Thu Oct 05 2023 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1
- 3.3.0 -> 3.4.1.

* Wed Aug 09 2023 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 3.1.0 -> 3.3.0.

* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 2.0.2 -> 3.1.0.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 2.0.2-alt1
- 1.4.3 -> 2.0.2.

* Fri Jan 17 2020 Stanislav Levin <slev@altlinux.org> 1.4.3-alt1
- 1.3.0 -> 1.4.3 (Closes: #37849).

* Sun Feb 17 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- Initial build.
