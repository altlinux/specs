Name: alt-workstation-addon
Version: 11.2
Release: alt2

Summary: Additional requires for ALT Workstation
License: ALT-Public-Domain
Group: System/Configuration/Other
Url: http://www.altlinux.org/

Requires: gnome-software-plugin-fwupd
Requires: gnome-software-plugin-flatpak
Requires: flatpak

BuildArch: noarch

%description
%summary.

%files

%changelog
* Sun Jan 04 2026 Semen Fomchenkov <armatik@altlinux.org>  11.2-alt2
- Add GNOME Software flatpak plugin and flatpak.

* Thu Nov 20 2025 Semen Fomchenkov <armatik@altlinux.org> 11.2-alt1
- Add GNOME Software fwupd plugin.

* Mon Jul 14 2025 Semen Fomchenkov <armatik@altlinux.org> 11.1-alt1
- Initial build.
