Name: mate
Version: 1.26.0
Release: alt1

Summary: MATE Desktop installers
License: %gpl2plus
Group: Graphical desktop/MATE

BuildArch: noarch

BuildPreReq: rpm-build-licenses

%description
A set of virtual packages for MATE Desktop installation.

%package minimal
Summary: MATE Desktop minimal installer
Group: Graphical desktop/MATE

Requires: mate-desktop mate-session mate-panel mate-menus mate-window-manager mate-settings-daemon
Requires: mate-polkit mate-control-center mate-media mate-screensaver mate-power-manager mate-notification-daemon
Requires: mate-system-monitor mate-file-manager mate-file-archiver mate-terminal mate-text-editor
Requires: mate-themes mate-icon-theme mate-backgrounds mate-user-guide

%description minimal
This virtual package installs MATE Desktop with minimum components.

%package default
Summary: MATE Desktop installer for optimal user's requirements
Group: Graphical desktop/MATE

Requires: mate-minimal
Requires: mate-calc mate-dictionary mate-disk-usage-analyzer
Requires: mate-document-viewer mate-document-viewer-caja mate-document-viewer-thumbnailer
Requires: mate-file-manager-extensions mate-file-manager-archiver
Requires: mate-image-viewer mate-menu-editor mate-screenshot mate-search-tool mate-sensors-applet

%description default
This virtual package installs MATE Desktop for an average user's
requirements.

%package maxi
Summary: MATE Desktop full installer
Group: Graphical desktop/MATE

Requires: mate-default
Requires: mate-disk-image-mounter
Requires: mate-document-viewer-djvu mate-document-viewer-dvi mate-document-viewer-pixbuf mate-document-viewer-xps
Requires: mate-file-manager-beesu mate-file-manager-image-converter mate-file-manager-open-terminal
Requires: mate-file-manager-sendto mate-file-manager-share mate-file-manager-wallpaper mate-system-log
Requires: python3-module-caja

%description maxi
This virtual package installs full MATE Desktop.

%files minimal
%files default
%files maxi

%changelog
* Tue Feb 22 2022 Valery Inozemtsev <shrek@altlinux.ru> 1.26.0-alt1
- updated to mate 1.26

* Mon Mar 11 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt2
- mate-maxi: removed dependency to caja-gnome-mplayer-properties-page cause
  package deletion

* Thu Mar 22 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.20.0-alt1
- updated to mate 1.20

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.18.0-alt1
- gst -> gst 1.0
- bumped version

* Wed Feb 14 2018 Anton Midyukov <antohami@altlinux.org> 1.15.0-alt3
- Remove requires webclient (requires rekonq, it is not clear why)

* Sun Feb 11 2018 Anton Midyukov <antohami@altlinux.org> 1.15.0-alt2
- Replace requires firefox to webclient (Closes: 34510)
- Replace requires mate-file-archiver to mate-file-manager-archiver

* Mon Oct 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.15.0-alt1
- updated to mate 1.16

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1
- mate-netspeed is merged with mate-applets

* Wed Nov 18 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1
- exale is not the best choice for a music player

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2
- added exaile as audioplayer
- added gnome-mplayer-caja

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1
- preparations to add gnome-mplayer-caja

* Thu Oct 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt0.1
- preparations for 1.10 mate release
- added blueman (replaces mate-bluetooth)
- added zenity (replaces mate-dialogs)
- added mate-user-guide
- not yet added galculator (will replace mate-calc)

* Thu Mar 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt2
- dropped mate-character-map in favor of gucharmap

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1
- preparations for 1.8

* Sun Aug 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt4
- mate-document-viewer-impress dropped upstream

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt3
- added new subpackages of mate-utils: mate-system-log mate-screenshot
  mate-dictionary mate-search-tool mate-disk-usage-analyzer

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt2
- gst-plugins-good added to mate-default

* Thu Apr 11 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6.0-alt1
- mate-file-manager-dropbox removed from mate-maxi

* Fri Mar 22 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.0-alt5
- added Requires: gvfs-utils into mate-default (closes #28677)

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt4
- added Requires: mate-mplayer
  Requires: mate-file-manager-actions
  Requires: mate-file-manager-terminal

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3
- added missing dependencies.

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2
- dropped dependencies on obsolete mate 1.4 packages

* Tue Feb 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1
- dropped mate-icon-theme-faenza
- bumped to 1.5

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3
- dropped caja-sound-converter

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2
- dropped mate-display-manager

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1.1
- Build for Sisyphus

* Sun Oct 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- first version, based on gnome3 spec

