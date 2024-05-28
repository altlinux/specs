%define _unpackaged_files_terminate_build 1
%define pypi_name libcst
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: A Concrete Syntax Tree (CST) parser and serializer library for Python
License: MIT and Python-2.0 and Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/libcst/
Vcs: https://github.com/Instagram/LibCST
Source0: %name-%version.tar
Source1: vendor_rust.tar
Source2: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
Patch3500: 3500-Update-target-lexicon-version-in-Cargo.lock.patch
Patch3501: 3501-target-lexicon-loongarch64.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter fixit
%add_pyproject_deps_check_filter hypothesmith
%add_pyproject_deps_check_filter jupyter
%add_pyproject_deps_check_filter prompt-toolkit
%add_pyproject_deps_check_filter pyre-check
%add_pyproject_deps_check_filter slotscheck
%add_pyproject_deps_check_filter sphinx-rtd-theme
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check
%endif
# rust stuff
BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo

%description
LibCST parses Python source code as a CST tree that keeps all formatting
details (comments, whitespaces, parentheses, etc). It's useful for building
automated refactoring (codemod) applications and linters.

LibCST creates a compromise between an Abstract Syntax Tree (AST) and a
traditional Concrete Syntax Tree (CST). By carefully reorganizing and naming
node types and fields, we've created a lossless CST that looks and feels like
an AST.

%prep
%setup -a1
%autopatch -p1
echo >> .cargo/config.toml
cat < vendor_cargoconf.toml >> .cargo/config.toml
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
find %buildroot%python3_sitelibdir -type d -name tests | \
    xargs -I {} rm -rf "{}"

# don't remove libcst/codemod/_testing.py and libcst/testing/
# contains CodemodTest class which provides testing facility for Codemods

%check
export NO_PYRE=yes
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
cd %mod_name
export LIBCST_PARSER_TYPE=native
python -m %mod_name.tests

export LIBCST_PARSER_TYPE=pure
python -m %mod_name.tests
ENDTESTS

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 24 2024 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.1 -> 1.4.0.

* Mon Apr 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.3.1-alt2
- NMU: fixed FTBFS on LoongArch (updated target-lexicon crate).

* Thu Apr 04 2024 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.2.0 -> 1.3.1.

* Wed Feb 21 2024 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Wed Nov 22 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt3
- Bootstrap for python3.12.

* Tue Oct 31 2023 Anton Vyatkin <toni@altlinux.org> 1.1.0-alt2
- NMU: Dropped dependency on distutils.

* Fri Oct 06 2023 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 0.4.10 -> 1.0.1.

* Fri May 26 2023 Grigory Ustinov <grenka@altlinux.org> 0.4.10-alt2
- Build without check for python3.11.

* Wed May 24 2023 Stanislav Levin <slev@altlinux.org> 0.4.10-alt1
- 0.4.9 -> 0.4.10.

* Fri May 05 2023 Stanislav Levin <slev@altlinux.org> 0.4.9-alt1
- 0.4.7 -> 0.4.9.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 0.4.7-alt1
- 0.4.1 -> 0.4.7.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.3.18 -> 0.4.1.

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 0.3.18-alt1
- Initial build for Sisyphus.
