%define _unpackaged_files_terminate_build 1
%define pypi_name zensical
%define mod_name zensical

%python3_set_limited_api

Name: python3-module-%pypi_name
Version: 0.0.30
Release: alt1

Summary: A modern static site generator by the Material for MkDocs team
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/zensical/
Vcs: https://github.com/zensical/zensical

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %pyproject_deps_config_name
Source3: config.toml
Patch0: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3-dev

%description
Write your documentation in Markdown and create a professional static
site for your Open Source or commercial project in minutes - searchable,
customizable, more than 60 languages, for all devices.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE3 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
rm -v %buildroot/%python3_sitelibdir/LICENSE.md

%files
%_bindir/zensical
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 31 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.30-alt1
- Updated to 0.0.30.

* Thu Mar 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.29-alt1
- Updated to 0.0.29.

* Mon Mar 23 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.28-alt1
- Packaged for ALT Sisyphus.
