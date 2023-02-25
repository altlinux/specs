Name:     sddm-sugar-light-theme
Version:  1.0
Release:  alt1.2
BuildArch: noarch

%define sname sddm-sugar-light-theme
%define mname sugar-light
%define sddm_user sddm
%define sddm_conf %_sysconfdir/X11/sddm/sddm.conf

Requires: libkf5plasmaquick sed sddm

Summary:  SDDM Sugar light theme
License:  GPLv3
Group:    Graphical desktop/KDE
Url:      https://framagit.org/MarianArlt/sddm-sugar-light

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:   %name-%version-%release.tar
Source1:  %mname.conf
Source2:  VirtualKeyboard.qml
Patch1:   sddm-sugar-light-theme-vk-1.0.patch

%description
Sugar light login theme for SDDM

%prep
%setup -n %sname
%patch1 -p1

install -m 644  %SOURCE2 %_builddir/sddm-sugar-light-theme/Components/

%install
install -d %buildroot%_datadir/sddm/themes/%mname/
cp -ar .  %buildroot%_datadir/sddm/themes/%mname
install -d  %buildroot%_sysconfdir/sddm.conf.d/
install -D  %SOURCE1  %buildroot%_sysconfdir/sddm.conf.d/


%files
%_datadir/sddm/themes/%mname/
%attr(0640,root,%sddm_user) %_sysconfdir/sddm.conf.d/%mname.conf

%changelog
* Sat Feb 25 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1.2
- Fix bug (ALT #45177)

* Thu Feb 16 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1.1
- Correct bug

* Thu Feb 02 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1
-  Init Build for Sisyphus
