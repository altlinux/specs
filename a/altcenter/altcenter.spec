%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: altcenter
Version: 1.0
Release: alt0.39
Epoch: 1
Summary: Application for show information and configure system

License: GPL-3.0+
Group: Graphical desktop/Other
URL: http://www.altlinux.org/altcenter

Source0: %name-%version.tar

%if "%altbranch" == "sisyphus" || "%altbranch" == "p11"
BuildArch: noarch
%else
ExcludeArch: ppc64le armh
%endif

BuildRequires(pre): rpm-build-python3

%add_python3_req_skip mainwindow my_utils my_utils_pyqt5

Requires: inxi
Requires: alteratorctl

%description
This is the grapical plugin-based application for show information and
configure system.

Available plugins:
- about
- license
- documentation
- hardware
- settings
- useful
- components
- policies
- journal

%prep
%setup

%install
%makeinstall_std

%files
%doc README.md TODO.md
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_sysconfdir/xdg/autostart/%name.desktop

%changelog
* Mon Jun 22 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.39
- Policy: added user console blocking.
- Policy: added Podman policy and package availability check.
- Policy: added ptrace tracing restriction.
- Policy: added SysRq key blocking.
- Components: enabled apply on checkbox changes.
- Policy: added network services startup control.

* Fri Jun 12 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.38
- Components: filtered obsolete egrep warning.
- Auditd logs settings: added system power audit rule.
- Components: shown installed component packages.
- Components: used apt-get for component installation (ALT #59410).

* Wed Jun 03 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.37
- policies: added wireless access policies.
- policies: added removable media policies.

* Wed May 27 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.36
- Fixed bugs (ALT #59265, #54844).

* Tue May 19 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.35
- Fixed bugs (ALT #58310, #58742).

* Wed May 06 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.34
- Ported plugins to PyQt6.

* Wed Apr 29 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.33
- Mainwindow: fixed bug (ALT #58836).
- Policies: added "Disallow remote SSH access as root" policy.
- Policies: removing the "Disable remote graphical sessions" policy.
- Policies: added a condition for displaying the policy.

* Wed Apr 22 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.32
- QtWebEngine has been removed.

* Wed Apr 22 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.31
- Useful Information: QtWebEngine has been converted to QTextBrowser.
- Policies: added a condition for displaying the policy.
- Added an explanation to the console.
- Policies: added policy exception.
- Exit "Expert mode" after 20 minutes.

* Mon Apr 20 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.30
- Removed requirements of polkit-rule-packagekit-allow-install (ALT #58807).

* Thu Apr 16 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.29
- Fixed bugs (ALT #58547, 58542, 58545, 58549, 58664, 58702, 58630, 58583,
  58384).

* Wed Apr 08 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.28
- Fixed bugs (ALT #58106, #58308, #58558, #58579, #58577).

* Mon Apr 06 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.27
- auditd: do not require to fill all fields (ALT #58387).

* Thu Apr 02 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.26
- Updated auditd logs settings.

* Wed Mar 18 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.25
- Added new plugin auditd_settings.

* Mon Mar 16 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.24
- Added Expert mode and admin rights to plugins.

* Fri Feb 27 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.23
- journal: added saving to file and audit support.

* Mon Jan 26 2026 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.22
- journal settings updated.

* Wed Dec 24 2025 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.21
- Added new plugin journal.
- policies: added new entries.

* Tue Dec 02 2025 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.20
- Components: transition to the new alterator API.
- Added new plugin policies.

* Mon Sep 29 2025 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.19
- Settings: used DE-specific application magazine (ALT #55289).

* Sun Sep 28 2025 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt0.18
- Useful: added links to useful articles (ALT #55198).
- Components: fixed freezing during download.

* Tue Sep 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.17
- Required polkit-rule-packagekit-allow-install to install packages (ALT #54844).

* Sun Jul 13 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.16
- App Install plugin has been removed
- Documentation: added a button to go to OS manual
- Settings: moved install applications buttons from components
- Componnets: the console show button has been moved to another container
- Components: indicate continues process by mouse cursor

* Thu Jul 03 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.15
- Components: optimizing packages for plasma-discover
- Components: handling if the component has no comment
- Components: added close console button
- Components: added localization of buttons
- Use xcb in Wayland

* Sun Jun 22 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.14
- altcenter.desktop: used consistent Russian translation of application name (ALT #54822).

* Thu Jun 19 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.13
- Documentation: localized link fixed.
- Added translation of context menu.

* Tue Jun 17 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.12
- components: fixed install and uninstall.

* Wed Jun 11 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.11
- settings: fixed KDE detection on Wayland.

* Mon Jun 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.10
- Required inxi.
- Required alterator 2.0.

* Thu Jun 05 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.9
- Added "Components" section.

* Fri Apr 25 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.8
- hardware: running hw-probe and inxi as non-blocking process.

* Fri Apr 18 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.7
- hardware: added the ability to hardware probe.
- about: showed URL specified for product and product logo specified in
  /etc/os-release
- Used logo from icon theme.

* Fri Feb 07 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.6
- about: added info about DE + redesigned plugin.
- settings: fix DE like Alt-GNOME:GNOME (ALT #52873).

* Tue Jan 28 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.5
- Open the desired plugin via command line parameter.
- Remove unused code.

* Fri Jan 24 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.4
- Used correct user settings program for current DE (ALT #52797).
- Unset minimal size for mobile device (ALT #52798).

* Thu Jan 23 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.3
- about: fixed using float for setPointSize.

* Thu Jan 23 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.2
- Made unify spec for sisyphus and p11.
- Put application to autostart.

* Wed Jan 22 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt0.1
- Initail build for Sisyphus.
