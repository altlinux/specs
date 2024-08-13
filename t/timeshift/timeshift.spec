%define _unpackaged_files_terminate_build 1
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%IF_ver_gteq %ubt_id M110
%def_disable use_xvt
%else
%def_enable use_xvt
%endif

Name: timeshift
Version: 24.06.3
Summary: System restore tool for Linux
Release: alt1
License: GPLv3
Group: Archiving/Backup
URL: https://github.com/linuxmint/timeshift
Source: %name-%version.tar
Source1: firsttime-snapshot.sh
Patch1: alt-use-xvt.patch
Patch2: alt-fix-41711.patch
Patch3: alt-fix-41055.patch
Patch4: alt-fix-46917.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake
BuildRequires: meson
BuildRequires: vala
BuildRequires: libgee0.8-devel
BuildRequires: libjson-glib-devel
BuildRequires: libvte3-devel
BuildRequires: libxapps-devel
BuildRequires: help2man
Requires: rsync

%description
System restore tool for Linux. Creates filesystem snapshots using
rsync+hardlinks, or BTRFS snapshots. Supports scheduled snapshots, multiple back
up levels, and exclude filters. Snapshots can be restored while system is
running or from Live CD/USB.

%prep
%setup
%if_enabled use_xvt
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1

%build
%meson
%meson_build

%install
%meson_install
#firsttime script, start with zz, as it should be executed as late as possible
install -m755 -pD %SOURCE1 %buildroot%_sysconfdir/firsttime.d/zz-firsttime-snapshot.sh
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-gtk
%_bindir/%name-launcher
%_datadir/%name
%_sysconfdir/%name
%_desktopdir/%name-gtk.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/metainfo/%name.appdata.xml
%_pixmapsdir/%name.png
%_datadir/polkit-1/actions/in.teejeetech.pkexec.timeshift.policy
%_sysconfdir/firsttime.d/zz-firsttime-snapshot.sh
%_man1dir/%name-gtk.1.xz
%_man1dir/%name.1.xz
%doc README.md

%changelog
* Tue Aug 13 2024 Alexander Makeenkov <amakeenk@altlinux.org> 24.06.3-alt1
- Updated to version 24.06.3.

* Sat Jul 06 2024 Alexander Makeenkov <amakeenk@altlinux.org> 24.06.2-alt1
- Updated to version 24.06.2.

* Fri Jun 07 2024 Anastasia Osmolovskaya <lola@altlinux.org> 24.06.1-alt1
- Updated to version 24.06.1.

* Wed Jan 17 2024 Alexander Makeenkov <amakeenk@altlinux.org> 24.01.1-alt2
- Fixed post-install unowned files.

* Wed Jan 17 2024 Alexander Makeenkov <amakeenk@altlinux.org> 24.01.1-alt1
- Updated to version 24.01.1.

* Fri Jan 12 2024 Alexander Makeenkov <amakeenk@altlinux.org> 23.12.2-alt2
- Do not apply alt-fix-46917.patch.

* Tue Jan 02 2024 Alexander Makeenkov <amakeenk@altlinux.org> 23.12.2-alt1
- Updated to version 23.12.2.

* Wed Dec 20 2023 Alexander Makeenkov <amakeenk@altlinux.org> 23.12.1-alt2
- Fixed removing of temporary directories (closes: #46917).

* Tue Dec 05 2023 Alexander Makeenkov <amakeenk@altlinux.org> 23.12.1-alt1
- Updated to version 23.12.1.

* Sun Jul 09 2023 Alexander Makeenkov <amakeenk@altlinux.org> 23.07.1-alt1
- Updated to version 23.07.1.

* Mon Jun 19 2023 Alexander Makeenkov <amakeenk@altlinux.org> 23.06.2-alt3
- Fixed opening of browse snapshots window (closes: #41055).

* Thu Jun 15 2023 Alexander Makeenkov <amakeenk@altlinux.org> 23.06.2-alt2
- Fixed system users detection (closes: #41711)

* Thu Jun 08 2023 Alexander Makeenkov <amakeenk@altlinux.org> 23.06.2-alt1
- Updated to version 23.06.2

* Sun Jun 04 2023 Alexander Makeenkov <amakeenk@altlinux.org> 23.06.1-alt1
- Updated to version 23.06.1

* Thu Mar 16 2023 Alexander Makeenkov <amakeenk@altlinux.org> 22.11.1-alt4
- Use xvt instead x-terminal-emulator (closes: #45553)

* Tue Mar 07 2023 Oleg Solovyov <mcpain@altlinux.org> 22.11.1-alt3
- do not take first boot snapshot if there are any
- use /etc/os-release info

* Mon Feb 20 2023 Oleg Solovyov <mcpain@altlinux.org> 22.11.1-alt2
- First boot: take BtrFS snapshot before logging in

* Sun Nov 27 2022 Alexander Makeenkov <amakeenk@altlinux.org> 22.11.1-alt1
- Updated to version 22.11.1
- Switched to new upstream

* Fri Nov 11 2022 Alexander Makeenkov <amakeenk@altlinux.org> 22.06.6-alt1
- Updated to version 22.06.6

* Mon May 30 2022 Alexander Makeenkov <amakeenk@altlinux.org> 22.06.1-alt1
- Updated to version 22.06.1

* Tue Sep 28 2021 Alexander Makeenkov <amakeenk@altlinux.org> 21.09.1-alt1
- Updated to version 21.09.1

* Tue Nov 24 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20.11.1-alt1
- Updated to version 20.11.1

* Sun Mar 08 2020 Alexander Makeenkov <amakeenk@altlinux.org> 20.03-alt1
- New version

* Tue Nov 05 2019 Alexander Makeenkov <amakeenk@altlinux.org> 19.08.1-alt1
- New version 19.08.1
- Fixed build

* Tue Feb 12 2019 Mikhail Savostyanov <mik@altlinux.org> 19.01-alt1
- New version 19.01

* Wed Apr 18 2018 Mikhail Savostyanov <mik@altlinux.org> 18.4-alt1
- New version 18.4

* Fri Feb 9 2018 Mikhail Savostyanov <mik@altlinux.org> 18.2-alt1
- initial build for ALT
