%define _unpackaged_files_terminate_build 1
%define snake_case_name alt_source_generator

Name: alt-source-generator
Version: 0.1.1
Release: alt1

Summary: Generator of .source files for the source control module (Alterator)
License: GPLv3+
Group: Other
Url: https://altlinux.space/alterator/alt-source-generator
BuildArch: noarch

BuildRequires: rpm-build-python3, python3(hatchling)
BuildRequires: python3(colorama), python3(toml)

Source0: %name-%version.tar

%description
A console utility that interactively creates a descriptor file <repo-name>.source,
which is used by the source management module.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%files -f %name.lang
%python3_sitelibdir/%snake_case_name
%python3_sitelibdir/%snake_case_name-%version.dist-info
%_bindir/%name

%changelog
* Wed Jun 17 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.1-alt1
- Updated for alterator-entry 0.4.13:
  + Removed the requires key
  + Added support for required components (the required key)

* Thu May 14 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.0-alt1
- First build for Sisyphus.
