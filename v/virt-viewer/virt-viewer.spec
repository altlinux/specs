
Name: virt-viewer
Version: 11.0
Release: alt2

Summary: Virtual Machine Viewer
Group: System/Configuration/Other
License: GPL-2.0+
Url: https://gitlab.com/virt-viewer/virt-viewer
# Vcs https://gitlab.com/virt-viewer/virt-viewer
Source: %name-%version.tar
Patch0001: 0001-data-remove-bogus-param-for-meson-i18nmerge_file.patch

Obsoletes: spice-client < 0.12.5-alt3

Requires: libvirt-client

BuildRequires(pre): meson >= 0.54.0
BuildRequires: pkgconfig(glib-2.0) >= 2.48
BuildRequires: pkgconfig(gtk+-3.0) >= 3.18
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.0
BuildRequires: pkgconfig(libvirt) >= 1.2.8
BuildRequires: pkgconfig(libvirt-glib-1.0) >= 0.1.8
BuildRequires: pkgconfig(gtk-vnc-2.0) >= 0.4.0
BuildRequires: pkgconfig(spice-client-gtk-3.0) >= 0.35
BuildRequires: pkgconfig(spice-protocol) >= 0.12.7
BuildRequires: pkgconfig(vte-2.91) >= 0.46.0
BuildRequires: /usr/bin/pod2man
BuildRequires: gettext
BuildRequires: pkgconfig(govirt-1.0) >= 0.3.7
BuildRequires: pkgconfig(rest-0.7) >= 0.8
BuildRequires: bash-completion

%description
Virt Viewer provides a graphical viewer for the guest OS
display. At this time is supports guest OS using the VNC
or SPICE protocols. Further protocols may be supported in
the future as user demand dicatates. The viewer can connect
directly to both local and remotely hosted guest OS, optionally
using SSL/TLS encryption.

%prep
%setup
%patch0001 -p1

%build
%meson -Dbuild-id=%release -Dos-id=ALT
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md COPYING NEWS
%_bindir/*
%_man1dir/*
%_datadir/mime/packages/*.xml
%_desktopdir/*.desktop
%_datadir/metainfo/remote-viewer.appdata.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/bash-completion/completions/virt-viewer

%changelog
* Thu May 12 2022 Alexey Shabalin <shaba@altlinux.org> 11.0-alt2
- data: remove bogus param for meson i18n.merge_file

* Thu Dec 02 2021 Alexey Shabalin <shaba@altlinux.org> 11.0-alt1
- new version 11.0

* Fri Jun 11 2021 Alexey Shabalin <shaba@altlinux.org> 10.0-alt2
- backport fixes from upstream master branch (ALT#40198)

* Tue May 18 2021 Alexey Shabalin <shaba@altlinux.org> 10.0-alt1
- new version 10.0

* Sat May 09 2020 Alexey Shabalin <shaba@altlinux.org> 9.0-alt1
- new version 9.0

* Tue Apr 23 2019 Pavel Moseev <mars@altlinux.org> 8.0-alt3
- update translation

* Mon Mar 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 8.0-alt2
- Allow toggling clipboard sharing between host and guest.

* Sun Mar 10 2019 Alexey Shabalin <shaba@altlinux.org> 8.0-alt1
- 8.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 7.0-alt2
- app: Remove VirtViewerApp::has-focus
- app: Always add guest name comment

* Fri Jul 27 2018 Alexey Shabalin <shaba@altlinux.org> 7.0-alt1
- 7.0 release

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0-alt0.1
- upstream/master snapshot
- build without spice-controller

* Tue Mar 06 2018 Alexey Shabalin <shaba@altlinux.ru> 6.0-alt1
- 6.0

* Mon Nov 28 2016 Alexey Shabalin <shaba@altlinux.ru> 5.0-alt1
- 5.0

* Mon Jul 04 2016 Alexey Shabalin <shaba@altlinux.ru> 4.0-alt1
- 4.0

* Mon Jun 27 2016 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt2
- rebuild with spice-gtk-0.32-alt1

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.1-alt1
- 3.1

* Tue Dec 08 2015 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt1
- 3.0

* Tue Jan 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.7-alt1.1
- rebuild with new libgovirt

* Wed Aug 07 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.6-alt1
- 0.5.6
- build with oVirt support

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Thu Apr 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Tue Nov 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1
- build with gtk+3

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt2
- rebuild with new libspice-gtk-devel

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Thu Feb 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20110211
- snapshot 20110211

* Tue Jan 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20110112
- snapshot 20110112

* Thu Dec 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1.hg20101221
- snapshot 20101221
- build with spice support

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 31 2009 Ilya Mashkin <oddity@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.3-alt1
- Initial build for ALTLinux
