Name: calcure
Version: 3.3
Release: alt1
License: MIT

Summary: Modern TUI calendar and task manager

Group: Office

Url: https://github.com/anufrievroman/calcure
Vcs: https://github.com/anufrievroman/calcure.git

Source: %name-%version.tar

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

Requires: python3(holidays)

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version.dist-info
%_man1dir/*.1.*

%changelog
* Thu Jul 16 2026 Kirill Unitsaev <fiersik@altlinux.org> 3.3-alt1
- new version 3.3

* Sun Jun 15 2025 Kirill Unitsaev <fiersik@altlinux.org> 3.2.1-alt1
- Initial build
