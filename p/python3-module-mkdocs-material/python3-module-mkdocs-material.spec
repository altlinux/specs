%define _unpackaged_files_terminate_build 1
%define pypi_name mkdocs-material

Name: python3-module-%pypi_name
Version: 9.1.4
Release: alt1

Summary: Documentation that simply works
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mkdocs-material

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(hatchling)
BuildRequires: python3(hatch_nodejs_version)
BuildRequires: python3(hatch_requirements_txt)

BuildArch: noarch

%description
Write your documentation in Markdown and create a professional static site for
your Open Source or commercial project in minutes - searchable, customizable,
more than 50 languages, for all devices.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc CHANGELOG LICENSE README.md
%python3_sitelibdir/material
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 9.1.4-alt1
- New version.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 8.5.3-alt1
- 8.4.1 -> 8.5.3
- clean up spec

* Fri Aug 26 2022 Anton Zhukharev <ancieg@altlinux.org> 8.4.1-alt1
- initial build for Sisyphus
