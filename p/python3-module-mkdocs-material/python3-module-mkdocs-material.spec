%define _unpackaged_files_terminate_build 1
%define pypi_name mkdocs-material

%define _docsdir %_datadir/docs

Name: python3-module-%pypi_name
Version: 8.4.1
Release: alt1

Summary: Documentation that simply works
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mkdocs-material

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

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
* Fri Aug 26 2022 Anton Zhukharev <ancieg@altlinux.org> 8.4.1-alt1
- initial build for Sisyphus
