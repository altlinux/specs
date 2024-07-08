%define _unpackaged_files_terminate_build 1
%define pypi_name leb128
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.8
Release: alt1

Summary: LEB128 or Little Endian Base 128
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/leb128/
Vcs: https://github.com/mohanson/leb128

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
LEB128 or Little Endian Base 128 is a form of variable-length code compression
used to store an arbitrarily large integer in a small number of bytes.
LEB128 is used in the DWARF debug file format and the WebAssembly binary
encoding for all integer literals.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 08 2024 Anton Zhukharev <ancieg@altlinux.org> 1.0.8-alt1
- Updated to 1.0.8.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 1.0.7-alt1
- Updated to 1.0.7.

* Thu Mar 07 2024 Anton Zhukharev <ancieg@altlinux.org> 1.0.5-alt1
- Built for ALT Sisyphus.

