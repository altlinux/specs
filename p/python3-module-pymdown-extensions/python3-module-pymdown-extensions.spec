%define _unpackaged_files_terminate_build 1
%define pypi_name pymdown-extensions
%define mod_name pymdownx

%def_with check

Name: python3-module-%pypi_name
Version: 12.1
Release: alt1

Summary: Extensions for Python Markdown
License: MIT and BSD
Group: Development/Python3
URL: https://pypi.org/project/pymdown-extensions/
VCS: https://github.com/facelessuser/pymdown-extensions

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-markdown
BuildRequires: python3-module-yaml
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Oct 02 2026 Alexander Burmatov <thatman@altlinux.org> 12.1-alt1
- New 12.1 version.

* Tue Mar 31 2026 Anton Zhukharev <ancieg@altlinux.org> 10.21.2-alt1
- Updated to 10.21.2.

* Thu Oct 30 2025 Anton Zhukharev <ancieg@altlinux.org> 10.16.1-alt1
- Updated to 10.16.1.

* Mon Jun 23 2025 Anton Zhukharev <ancieg@altlinux.org> 10.16-alt1
- Updated to 10.16.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 10.15-alt1
- Updated to 10.15.

* Tue Feb 04 2025 Anton Zhukharev <ancieg@altlinux.org> 10.14.3-alt1
- Updated to 10.14.3.

* Sun Oct 13 2024 Anton Zhukharev <ancieg@altlinux.org> 10.11.2-alt1
- Updated to 10.11.2.

* Mon Sep 30 2024 Anton Zhukharev <ancieg@altlinux.org> 10.11.1-alt1
- Updated to 10.11.1.

* Thu Sep 26 2024 Anton Zhukharev <ancieg@altlinux.org> 10.10.2-alt1
- Updated to 10.10.2.

* Tue Sep 24 2024 Anton Zhukharev <ancieg@altlinux.org> 10.10.1-alt1
- Updated to 10.10.1.

* Sun Jul 28 2024 Anton Zhukharev <ancieg@altlinux.org> 10.9-alt1
- Updated to 10.9.

* Thu May 16 2024 Anton Zhukharev <ancieg@altlinux.org> 10.8.1-alt1.gitf1e2fad
- Updated to 10.8.1 (f1e2fad).

* Thu Apr 11 2024 Anton Zhukharev <ancieg@altlinux.org> 10.7.1-alt1.git509e93d
- Updated to 10.7.1 (509e93d).

* Sun Dec 31 2023 Anton Zhukharev <ancieg@altlinux.org> 10.7-alt1
- Updated to 10.7.

* Wed Dec 27 2023 Anton Zhukharev <ancieg@altlinux.org> 10.6-alt1
- Updated to 10.6.

* Mon Dec 11 2023 Anton Zhukharev <ancieg@altlinux.org> 10.5-alt1
- Updated to 10.5.

* Wed Nov 15 2023 Anton Zhukharev <ancieg@altlinux.org> 10.4-alt1
- Updated to 10.4.

* Thu Oct 19 2023 Anton Zhukharev <ancieg@altlinux.org> 10.3.1-alt1
- Updated to 10.3.1.

* Sun Sep 03 2023 Anton Zhukharev <ancieg@altlinux.org> 10.3-alt1
- Updated to 10.3.

* Wed Aug 30 2023 Anton Zhukharev <ancieg@altlinux.org> 10.2.1-alt1
- Updated to 10.2.1.

* Tue Aug 29 2023 Anton Zhukharev <ancieg@altlinux.org> 10.2-alt1
- Updated to 10.2.

* Fri Aug 18 2023 Anton Zhukharev <ancieg@altlinux.org> 10.1-alt1
- Updated to 10.1.

* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 9.5-alt1
- initial build for Sisyphus
