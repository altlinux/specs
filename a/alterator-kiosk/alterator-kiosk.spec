Name: alterator-kiosk
Version: 1.20
Release: alt1

Source: %name-%version.tar
Source1: activate-kiosk.sh
Source2: kiosk.service

Summary: alterator module for managing kiosk mode
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: alterator
Requires: kiosk

%description
alterator module for managing kiosk mode

%package -n kiosk-profiles
Summary: profiles for kiosk
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch
Requires: alterator-kiosk = %EVR

%description -n kiosk-profiles
profiles for kiosk

%prep
%setup -q

%install
%makeinstall
install -Dm 0755 %SOURCE1 %buildroot%_bindir/activate-kiosk.sh
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/kiosk.service

%triggerin -n kiosk-profiles -- kiosk-profiles < 1.18-alt1
# update symlinks to keep profiles enabled
if [ -L /etc/alterator/kiosk/profiles_enabled/user-startup ]; then
    rm -f /etc/alterator/kiosk/profiles_enabled/user-startup
    ln -s /etc/alterator/kiosk/{profiles,profiles_enabled}/kde-startup
fi
if [ -L /etc/alterator/kiosk/profiles_enabled/user-shutdown ]; then
    rm -f /etc/alterator/kiosk/profiles_enabled/user-shutdown
    ln -s /etc/alterator/kiosk/{profiles,profiles_enabled}/kde-shutdown
fi

%post
%post_service kiosk

%preun
%preun_service kiosk

%files
%_sysconfdir/alterator/kiosk/
%exclude %_sysconfdir/alterator/kiosk/profiles/
%_datadir/alterator/applications/*
%_libexecdir/alterator/backend3/*
%_datadir/alterator/ui/*
%_unitdir/kiosk.service
%_bindir/activate-kiosk.sh

%files -n kiosk-profiles
%_sysconfdir/alterator/kiosk/profiles/
%_man5dir/kiosk-profiles.5.xz

%changelog
* Fri May 22 2026 Oleg Solovyov <mcpain@altlinux.org> 1.20-alt1
- fix "kiosk enabled" flag, patch from antohami@ (Closes: #59304)

* Tue Mar 03 2026 Oleg Solovyov <mcpain@altlinux.org> 1.19-alt1
- update man page

* Fri Sep 26 2025 Oleg Solovyov <mcpain@altlinux.org> 1.18-alt1
- rename user-startup/user-shutdown profiles

* Thu Sep 11 2025 Oleg Solovyov <mcpain@altlinux.org> 1.17-alt1
- profiles: add maliit-keyboard (Closes: #55946)

* Mon Aug 18 2025 Oleg Solovyov <mcpain@altlinux.org> 1.16-alt1
- update profiles: run systemd without enforcing security

* Wed Apr 16 2025 Oleg Solovyov <mcpain@altlinux.org> 1.15-alt1
- update profiles: add chromium

* Thu Mar 06 2025 Oleg Solovyov <mcpain@altlinux.org> 1.14-alt1
- update profiles: add Wayland

* Wed Mar 05 2025 Oleg Solovyov <mcpain@altlinux.org> 1.13-alt1
- update profiles

* Mon Apr 22 2024 Oleg Solovyov <mcpain@altlinux.org> 1.12-alt1
- profiles: require alterator-kiosk

* Tue Nov 07 2023 Oleg Solovyov <mcpain@altlinux.org> 1.11-alt1
- update profiles

* Wed May 04 2022 Oleg Solovyov <mcpain@altlinux.org> 1.10-alt1
- add manpage about profiles

* Thu Feb 24 2022 Oleg Solovyov <mcpain@altlinux.org> 1.9-alt1
- fix chromium-gost launch

* Fri Feb 18 2022 Oleg Solovyov <mcpain@altlinux.org> 1.8-alt1
- extend apps-common profile

* Mon Feb 07 2022 Oleg Solovyov <mcpain@altlinux.org> 1.7-alt1
- update profiles for LDE startup and shotdown

* Tue Sep 21 2021 Ivan Razzhivin <underwit@altlinux.org> 1.6-alt1
- add okular and projectlibre to profiles

* Fri Aug 28 2020 Oleg Solovyov <mcpain@altlinux.org> 1.5-alt2
- require kiosk-profiles

* Tue Aug 25 2020 Oleg Solovyov <mcpain@altlinux.org> 1.5-alt1
- add chromium to profiles
- make a new package with profiles

* Wed Jul 08 2020 Ivan Razzhivin <underwit@altlinux.org> 1.4-alt1
- remove kiosk mode

* Mon Jun 22 2020 Oleg Solovyov <mcpain@altlinux.org> 1.3-alt1
- KDE: fix profiles
- enable service when committing changes

* Mon Jun 22 2020 Oleg Solovyov <mcpain@altlinux.org> 1.2-alt2
- add service

* Fri Jun 19 2020 Oleg Solovyov <mcpain@altlinux.org> 1.2-alt1
- remove system restrictions

* Wed Mar 25 2020 Oleg Solovyov <mcpain@altlinux.org> 1.1-alt1
- remove altha from error message

* Mon Jan 27 2020 Ivan Razzhivin <underwit@altlinux.org> 1.0-alt1
- init


