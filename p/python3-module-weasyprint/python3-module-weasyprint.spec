%define modulename weasyprint

%def_with check

Name:    python3-module-%modulename
Version: 69.0
Release: alt1

Summary: WeasyPrint converts web documents to PDF
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/Kozea/WeasyPrint

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-tinycss2
BuildRequires: python3-module-cssselect2
BuildRequires: python3-module-tinyhtml5
BuildRequires: python3-module-cffi
BuildRequires: libpango
BuildRequires: python3-module-pyphen
BuildRequires: python3-module-fonttools
BuildRequires: python3-module-pydyf
BuildRequires: fonts-ttf-dejavu
BuildRequires: ghostscript
BuildRequires: python3-module-pytest-xdist
BuildRequires: fonts-ttf-google-noto-emoji
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -n auto

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo %modulename}
%_bindir/%modulename
%doc README.rst LICENSE

%changelog
* Wed Jun 03 2026 Anton Vyatkin <toni@altlinux.org> 69.0-alt1
- New version 69.0 (Fixes: CVE-2026-49452).

* Fri Feb 06 2026 Anton Vyatkin <toni@altlinux.org> 68.1-alt1
- New version 68.1.

* Tue Jan 20 2026 Anton Vyatkin <toni@altlinux.org> 68.0-alt1
- New version 68.0 (Fixes: CVE-2025-68616).

* Wed Dec 03 2025 Anton Vyatkin <toni@altlinux.org> 67.0-alt1
- New version 67.0.

* Thu Jul 24 2025 Anton Vyatkin <toni@altlinux.org> 66.0-alt1
- New version 66.0.

* Thu Jul 10 2025 Anton Vyatkin <toni@altlinux.org> 65.1-alt2
- Fixed FTBFS.

* Sun Apr 13 2025 Anton Vyatkin <toni@altlinux.org> 65.1-alt1
- New version 65.1.

* Mon Mar 17 2025 Anton Vyatkin <toni@altlinux.org> 65.0-alt1
- New version 65.0.

* Fri Feb 21 2025 Anton Vyatkin <toni@altlinux.org> 64.1-alt1
- New version 64.1.

* Sat Feb 01 2025 Anton Vyatkin <toni@altlinux.org> 64.0-alt1
- New version 64.0.

* Wed Dec 11 2024 Anton Vyatkin <toni@altlinux.org> 63.1-alt1
- New version 63.1.

* Tue Oct 29 2024 Anton Vyatkin <toni@altlinux.org> 63.0-alt1
- New version 63.0.

* Sat Jun 22 2024 Anton Vyatkin <toni@altlinux.org> 62.3-alt1
- New version 62.3.

* Wed Jun 05 2024 Anton Vyatkin <toni@altlinux.org> 62.2-alt1
- New version 62.2.

* Tue May 07 2024 Anton Vyatkin <toni@altlinux.org> 62.1-alt1
- New version 62.1.

* Thu May 02 2024 Anton Vyatkin <toni@altlinux.org> 62.0-alt1
- New version 62.0.

* Mon Mar 11 2024 Anton Vyatkin <toni@altlinux.org> 61.2-alt1
- New version 61.2.

* Tue Feb 27 2024 Anton Vyatkin <toni@altlinux.org> 61.1-alt1
- New version 61.1.

* Mon Feb 12 2024 Anton Vyatkin <toni@altlinux.org> 61.0-alt1
- New version 61.0.

* Tue Dec 12 2023 Anton Vyatkin <toni@altlinux.org> 60.2-alt1
- New version 60.2.

* Fri Sep 29 2023 Anton Vyatkin <toni@altlinux.org> 60.1-alt1
- New version 60.1.

* Tue Sep 26 2023 Anton Vyatkin <toni@altlinux.org> 60.0-alt1
- New version 60.0.

* Thu May 11 2023 Anton Vyatkin <toni@altlinux.org> 59.0-alt1
- New version 59.0.

* Wed May 10 2023 Anton Vyatkin <toni@altlinux.org> 58.1-alt2
- Fix FTBFS

* Tue Mar 21 2023 Anton Vyatkin <toni@altlinux.org> 58.1-alt1
- New version 58.1.

* Tue Feb 07 2023 Anton Vyatkin <toni@altlinux.org> 57.2-alt1
- new version 57.2

* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 47-alt1
- Initial build for Sisyphus
