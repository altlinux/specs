%define _unpackaged_files_terminate_build 1

Name: proxsave
Version: 0.26.0
Release: alt1

Summary: Backup tool for Proxmox PBS & PVE System Files
License: MIT
Group: Archiving/Backup

Url: https://github.com/tis24dev/proxsave
Vcs: https://github.com/tis24dev/proxsave

ExcludeArch: i586

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires: golang

%description
ProxSave is a project created by enthusiasts, with the aim of simplifying
recovery in critical moments.

Restoring a PVE or PBS server after a disaster (or even just a migration)
is always a process that requires skill, time, and patience, ProxSave
allows you to save your entire environment and restore it at any time,
allowing you to prepare the new installation to accommodate your personal
data with as few manual changes as possible.

ProxSave allows you to save and restore, integrating advanced features:
automatic backups, multi-path saves, intelligent retention, encryption of
backups, integrated Telegram and email notifications (cloud relay or
Proxmox Notifications), and compatibility with webhooks, Gotify, and Prometheus.

%package doc
Summary: Documentation for the %name
Group: Books/Other
BuildArch: noarch
%description doc
Documentation for the %name

%prep
%setup -a1
subst 's|0.0.0-dev|%version|' Makefile

%build
%make_build

%install
install -Dm0755 build/%name %buildroot%_bindir/%name

%files
%doc *.md LICENSE NOTICE 
%_bindir/%name

%files doc
%doc docs

%changelog
* Fri Jun 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.26.0-alt1
- 0.25.0 -> 0.26.0

* Sun Jun 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.25.0-alt1
- automatic build: 0.24.0 -> 0.25.0

* Fri Jun 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.24.0-alt1
- automatic build: 0.23.1 -> 0.24.0

* Tue Jun 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.23.1-alt1
- 0.23.0 -> 0.23.1

* Tue Jun 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.23.0-alt1
- 0.22.1 -> 0.23.0

* Wed May 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.22.1-alt1
- 0.22.0 -> 0.22.1

* Tue May 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.22.0-alt1
- 0.21.0 -> 0.22.0

* Wed May 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.21.0-alt1
- 0.20.0 -> 0.21.0

* Thu May 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.20.0-alt1
- 0.19.0 -> 0.20.0

* Sun Apr 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.19.0-alt1
- 0.18.1 -> 0.19.0

* Tue Mar 31 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.18.1-alt1
- 0.18.0 -> 0.18.1

* Mon Mar 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.18.0-alt1
- 0.17.0 -> 0.18.0

* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.17.0-alt1
- 0.16.0 -> 0.17.0

* Thu Mar 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.16.0-alt1
- 0.15.1 -> 0.16.0

* Fri Feb 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.15.1-alt1
- 0.15.0 -> 0.15.1

* Thu Feb 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.15.0-alt1
- 0.14.1 -> 0.15.0

* Mon Feb 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.14.1-alt1
- 0.14.0 -> 0.14.1

* Sun Feb 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.14.0-alt1
- 0.13.6 -> 0.14.0

* Wed Feb 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.6-alt1
- 0.13.5 -> 0.13.6

* Tue Feb 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.5-alt1
- 0.13.4 -> 0.13.5

* Fri Feb 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.4-alt1
- 0.13.3 -> 0.13.4

* Thu Feb 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.3-alt1
- 0.13.1 -> 0.13.3

* Wed Feb 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.1-alt1
- 0.13.0 -> 0.13.1

* Tue Feb 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.0-alt1
- 0.12.8 -> 0.13.0

* Thu Jan 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.12.8-alt1
- Initial build for ALT Linux.

