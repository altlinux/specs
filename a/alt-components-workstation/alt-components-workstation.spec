%define _unpackaged_files_terminate_build 1
%def_enable check

Name: alt-components-workstation
Version: 11.2.1
Release: alt1
Summary: ALT Workstation edition and components
Group: System/Configuration/Other
License: GPL-3.0-or-later
Url: https://altlinux.space/armatik/alt-components-workstation
Vcs: https://altlinux.space/armatik/alt-components-workstation

BuildArch: noarch

Source0: %name-%version.tar

Requires: alterator-backend-component

BuildRequires(pre): rpm-macros-meson rpm-macros-alterator
BuildRequires: meson
BuildRequires: cmark
BuildRequires: alterator-entry

%description
Components and categories for ALT Workstation distribution.
Provides component definitions, descriptions and categories
for the alterator component manager (alt-components / alteratorctl).

%package -n alt-edition-workstation
Summary: ALT Workstation edition definition for alterator
Group: System/Configuration/Other
Requires: %name = %EVR
Requires: alterator-backend-edition

%description -n alt-edition-workstation
Edition definition for ALT Workstation distribution.
Provides the edition configuration for the alterator component manager.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md README.ru.md
%dir %_alterator_datadir/components
%dir %_alterator_datadir/components/categories
%_alterator_datadir/components/workstation-*/
%_alterator_datadir/components/categories/*/

%files -n alt-edition-workstation
%dir %_alterator_datadir/editions
%_alterator_datadir/editions/edition_workstation/

%changelog
* Tue Apr 08 2026 Semen Fomchenkov <armatik@altlinux.org> 11.2.1-alt1
- Initial build.
