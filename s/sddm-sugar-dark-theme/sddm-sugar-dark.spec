Name:     sddm-sugar-dark-theme
Version:  1.2
Release:  alt1
BuildArch: noarch

%define sname sddm-sugar-dark-theme
%define mname sugar-dark
%define sddm_user sddm
%define sddm_conf %_sysconfdir/X11/sddm/sddm.conf

Requires: libkf5plasmaquick sed sddm

Summary:  SDDM Sugar dark theme
License:  GPLv3
Group:    Graphical desktop/KDE
Url:      https://framagit.org/MarianArlt/sddm-sugar-dark

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:   %name-%version-%release.tar
Source1:  %mname.conf
Source2:  VirtualKeyboard.qml

%description
Sugar dark login theme for SDDM

%prep
%setup -n %sname
install -m 644  %SOURCE2 %_builddir/sddm-sugar-dark-theme/Components/

%install
install -d %buildroot%_datadir/sddm/themes/%mname/
cp -ar .  %buildroot%_datadir/sddm/themes/%mname
install -d  %buildroot%_sysconfdir/sddm.conf.d/
install -D  %SOURCE1  %buildroot%_sysconfdir/sddm.conf.d/

#%post
#cp %sddm_conf %sddm_conf.save
#subst s/\^Current/\#Current/ %sddm_conf

#%postun
#cp %sddm_conf %sddm_conf.save
#subst s/\#Current/Current/ %sddm_conf

%files
%_datadir/sddm/themes/%mname/
%attr(0640,root,%sddm_user) %_sysconfdir/sddm.conf.d/%mname.conf

%changelog
* Thu Feb 02 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1.2-alt1
-  Init Build for Sisyphus
