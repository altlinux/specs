%define _unpackaged_files_terminate_build 1
%define pypi_name mkdocs-material
%define mod_name material

Name: python3-module-%pypi_name
Version: 9.4.2
Release: alt1

Summary: Documentation that simply works
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mkdocs-material/
Vcs: https://github.com/squidfunk/mkdocs-material

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Write your documentation in Markdown and create a professional static site for
your Open Source or commercial project in minutes - searchable, customizable,
more than 50 languages, for all devices.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc CHANGELOG LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 9.4.2-alt1
- Updated to 9.4.2.

* Tue Sep 12 2023 Anton Zhukharev <ancieg@altlinux.org> 9.3.1-alt1
- Updated to 9.3.1.

* Tue Sep 05 2023 Anton Zhukharev <ancieg@altlinux.org> 9.2.8-alt1
- Updated to 9.2.8.

* Sun Sep 03 2023 Anton Zhukharev <ancieg@altlinux.org> 9.2.7-alt1
- Updated to 9.2.7.

* Fri Sep 01 2023 Anton Zhukharev <ancieg@altlinux.org> 9.2.6-alt1
- Updated to 9.2.6.

* Mon Aug 28 2023 Anton Zhukharev <ancieg@altlinux.org> 9.2.5-alt1
- Updated to 9.2.5.

* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 9.2.2-alt1
- Updated to 9.2.2.

* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 9.2.1-alt1
- Updated to 9.2.1.

* Fri Aug 18 2023 Anton Zhukharev <ancieg@altlinux.org> 9.1.21-alt1
- Updated to 9.1.21.

* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 9.1.4-alt1
- New version.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 8.5.3-alt1
- 8.4.1 -> 8.5.3
- clean up spec

* Fri Aug 26 2022 Anton Zhukharev <ancieg@altlinux.org> 8.4.1-alt1
- initial build for Sisyphus
