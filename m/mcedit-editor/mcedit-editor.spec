%ifndef _environmentdir
%define _environmentdir /lib/environment.d
%endif

Name: mcedit-editor
Version: 0.3.1
Release: alt1

Group: System/Configuration/Other
Summary: Set EDITOR environment variable to mcedit by default
License: GPL

BuildArch: noarch

Requires: /usr/bin/mcedit

Source0: mcedit-editor.sh
Source1: mcedit-editor.csh
Source2: mcedit-editor.conf


%description
Set EDITOR environment variable to mcedit by default

%prep

%install
install -D -m 0755 %SOURCE0 %buildroot/%_sysconfdir/profile.d/mcedit-editor.sh
install -D -m 0755 %SOURCE1 %buildroot/%_sysconfdir/profile.d/mcedit-editor.csh
mkdir -p %buildroot/%_environmentdir
install -m 0644 %SOURCE2 %buildroot/%_environmentdir/30-mcedit-editor.conf

%files
%config(noreplace) %_sysconfdir/profile.d/mcedit-editor.sh
%config(noreplace) %_sysconfdir/profile.d/mcedit-editor.csh
%_environmentdir/30-mcedit-editor.conf

%changelog
* Thu Jan 25 2024 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- fix systemd support for wayland

* Tue Jan 16 2024 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- add systemd support for wayland

* Thu Jan 21 2021 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- fix editor program

* Wed Dec 16 2020 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
