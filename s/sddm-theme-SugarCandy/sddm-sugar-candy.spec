Name:     sddm-theme-SugarCandy
Version:  1.5
Release:  alt2
BuildArch: noarch

%define sname sddm-sugar-candy-theme
%define mname sugar-candy
%define sddm_user sddm
%define sddm_conf %_sysconfdir/X11/sddm/sddm.conf

Requires: libkf5plasmaquick sed sddm

Summary:  SDDM Sugar Candy theme
License:  GPLv3
Group:    Graphical desktop/KDE
Url:      https://framagit.org/MarianArlt/sddm-sugar-candy

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:   %name-%version-%release.tar
Source1:  %mname.conf
Source2:  VirtualKeyboard.qml

%description
Sugar Candy login theme for SDDM

%prep
%setup -n %sname
install -m 644  %SOURCE2 %_builddir/sddm-sugar-candy-theme/Components/

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
* Mon May 23 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.5-alt2
- export Virtual keyboard from theme 
- closes:
 (alt bug 42815)
 (alt bug 42814)

* Sun May 08 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.5-alt1
 Init Build for Sisyphus
