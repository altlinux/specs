%define modulename weasyprint

%def_with check

Name:    python3-module-%modulename
Version: 62.1
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
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-cffi
BuildRequires: libpango
BuildRequires: python3-module-pyphen
BuildRequires: python3-module-fonttools
BuildRequires: python3-module-pydyf
BuildRequires: fonts-ttf-dejavu
BuildRequires: ghostscript
BuildRequires: python3-module-pytest-xdist
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
