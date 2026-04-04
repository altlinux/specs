%define nameS pyside6_fluent_widgets
%define nameL qfluentwidgets

Name: python3-module-PySide6-Fluent-Widgets
Version: 1.11.2
Release: alt1

Summary: A fluent design widgets library based on PySide6

License: GPL-3.0-only
Group: Development/Python3

URL: https://pypi.org/project/PySide6-Fluent-Widgets

ExcludeArch: i586

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%python3_sitelibdir
mv %buildroot%_prefix/lib/python3/site-packages/* %buildroot%python3_sitelibdir/
rm -r %buildroot%_prefix/lib

%files
%python3_sitelibdir/%nameL/
%python3_sitelibdir/%{pyproject_distinfo %nameS}/
%doc *.md LICENSE

%changelog
* Sun Apr 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.11.2-alt1
- 1.11.1 -> 1.11.2

* Sun Feb 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.11.1-alt1
- 1.11.0 -> 1.11.1

* Mon Jan 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.11.0-alt1
- 1.10.5 -> 1.11.0

* Mon Dec 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.10.5-alt1
- 1.10.4 -> 1.10.5

* Mon Dec 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.10.4-alt1
- 1.10.2 -> 1.10.4

* Wed Dec 10 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.10.2-alt1
- 1.9.2 -> 1.10.2

* Thu Nov 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.9.2-alt1
- 1.9.1 -> 1.9.2

* Thu Oct 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.9.1-alt1
- Initial build for ALT Linux.
