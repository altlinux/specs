%define modname sphinx-autodoc-typehints
%define pypi_name sphinx_autodoc_typehints
%def_disable check

Name: python3-module-%modname
Version: 3.12.1
Release: alt1

Summary: Type hints (PEP 484) support for the Sphinx autodoc extension
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/%modname

Vcs: https://github.com/tox-dev/sphinx-autodoc-typehints.git

#Source: https://github.com/tox-dev/%modname/archive/%version/%modname-%version.tar.gz
Source: https://pypi.io/packages/source/s/%modname/%pypi_name-%version.tar.gz

BuildArch: noarch
Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(hatchling) python3(hatch-vcs)
%{?_enable_check:BuildRequires: python3-module-tox >= 4.23.2
BuildRequires: python3-module-sphinx-tests python3-module-snowballstemmer >= 2.0
BuildRequires: python3-module-diff-cover
BuildRequires: python3-module-pytest-cov python3-module-sphobjinv
BuildRequires: python3-module-coverage python3-module-covdefaults
BuildRequires: python3-module-twine python3-module-nptyping}

%description
This Sphinx extension allows to use Python 3 annotations for
documenting acceptable argument types and return value types of
functions.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*


%changelog
* Mon Jul 06 2026 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Jun 29 2026 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Jun 15 2026 Yuri N. Sedunov <aris@altlinux.org> 3.11.0-alt1
- 3.11.0

* Sat Jun 06 2026 Yuri N. Sedunov <aris@altlinux.org> 3.10.5-alt1
- 3.10.5

* Mon Jun 01 2026 Yuri N. Sedunov <aris@altlinux.org> 3.10.4-alt1
- 3.10.4

* Thu May 14 2026 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Thu Apr 09 2026 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Apr 03 2026 Yuri N. Sedunov <aris@altlinux.org> 3.9.11-alt1
- 3.9.11

* Tue Mar 24 2026 Yuri N. Sedunov <aris@altlinux.org> 3.9.10-alt1
- 3.9.10

* Thu Mar 19 2026 Yuri N. Sedunov <aris@altlinux.org> 3.9.8-alt1
- 3.9.8

* Fri Mar 06 2026 Yuri N. Sedunov <aris@altlinux.org> 3.9.7-alt1
- 3.9.7

* Wed Mar 04 2026 Yuri N. Sedunov <aris@altlinux.org> 3.9.6-alt1
- 3.9.6

* Mon Mar 02 2026 Yuri N. Sedunov <aris@altlinux.org> 3.9.3-alt1
- 3.9.3

* Thu Feb 26 2026 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Feb 24 2026 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt1
- 3.7.0

* Wed Feb 18 2026 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Sat Jan 03 2026 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Dec 09 2025 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sun Oct 19 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.2-alt1
- 3.5.2

* Fri Oct 10 2025 Yuri N. Sedunov <aris@altlinux.org> 3.5.1-alt1
- 3.5.1

* Sat Apr 26 2025 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Feb 22 2025 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Sat Jan 18 2025 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sat Jan 04 2025 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Oct 10 2024 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Thu Sep 19 2024 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Fri Sep 13 2024 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Sep 09 2024 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Fri Aug 30 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Wed Jul 17 2024 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Sun Jun 23 2024 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Fri Jun 21 2024 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Jun 12 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Thu Apr 18 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Tue Apr 16 2024 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Fri Jan 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.25.3-alt1
- 1.25.3

* Wed Jan 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.25.2-alt1
- 1.25.2

* Mon Jul 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.23.3-alt1
- 1.23.3

* Sat Jun 17 2023 Yuri N. Sedunov <aris@altlinux.org> 1.23.2-alt1
- 1.23.2

* Fri Jun 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.23.1-alt1
- 1.23.1

* Thu Apr 20 2023 Yuri N. Sedunov <aris@altlinux.org> 1.23.0-alt1
- 1.23.0

* Tue Nov 15 2022 Yuri N. Sedunov <aris@altlinux.org> 1.19.5-alt1
- 1.19.5

* Tue Aug 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1.19.2-alt1
- 1.19.2

* Mon Aug 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1.19.1-alt1
- 1.19.1

* Fri Jul 29 2022 Yuri N. Sedunov <aris@altlinux.org> 1.19.0-alt1
- 1.19.0
- ported to %%pyproject* macros

* Tue Jun 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Fri May 06 2022 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Fri Jan 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Thu Jan 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.15.3-alt1
- 1.15.3

* Mon Jan 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.15.1-alt1
- 1.15.1

* Wed Jan 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.13.1-alt1
- 1.13.1 (supported Python 3.10)

* Thu Apr 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Sun Mar 07 2021 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- first build for Sisyphus




