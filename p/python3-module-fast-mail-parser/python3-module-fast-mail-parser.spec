%define _unpackaged_files_terminate_build 1
%define pypi_name fast-mail-parser
%define mod_name fast_mail_parser

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: Very fast Python library for .eml files parsing
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/fast-mail-parser/
Vcs: https://github.com/namecheap/fast_mail_parser

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Source3: %pyproject_deps_config_name

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: python3-dev
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary.

%prep
%setup -a1
install -v %SOURCE2 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
rm -rf fast_mail_parser  # remove to not use in tests (no compiled part)
%pyproject_run_pytest -vra

%files
%doc Readme.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Mar 06 2026 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- Packaged for ALT Sisyphus.
