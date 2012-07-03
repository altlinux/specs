%define Name ALTSP
%define bname ltsp

%def_with icewm
%def_without kde

Name: %bname-server-packages
Version: 5.0
Release: alt0.16

Summary: %Name virtual packages
License: Public domain
Group: Networking/Remote access

Url: http://www.altlinux.org/LTSP
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
Virtual packages for %Name.

%package -n %bname-server-basic
Summary: %Name base packages
Group: Networking/Remote access
Obsoletes: %{bname}5-server-base
Provides: %{bname}5-server-base = %version-%release
Obsoletes: %{bname}5-server-basic
Provides: %{bname}5-server-basic = %version-%release
Requires: ltsp-server
Requires: ltspswapd
Requires: fuse
Requires: ltspfs
Requires: lbussd
Requires: ltsp-utils
Requires: dhcp-server
Requires: tftp-server
Requires: rpcbind
Requires: nfs-server
#Requires: unfs3
# common
Requires: unzip
Requires: glibc-locales
Requires: glibc-timezones
Requires: openssh-clients
Requires: xauth
Requires: xmessage
Requires: setxkbmap
# fonts
Requires: fonts-bitmap-100dpi
Requires: fonts-bitmap-75dpi
Requires: fonts-bitmap-cyrillic
Requires: fonts-bitmap-misc
Requires: fonts-ttf-dejavu
Requires: fonts-ttf-xorg
Requires: freefont-fonts-ttf
# dm
Requires: xdm
# wm
#Requires: twm
# term
Requires: xterm

%description -n %bname-server-basic
Base virtual package for %Name.

%package -n %bname-server-enhanced
Summary: %Name enhanced package
Group: Networking/Remote access
Obsoletes: %{bname}5-server-enhanced
Provides: %{bname}5-server-enhanced = %version-%release
Requires: %bname-server-basic = %version-%release
# common
Requires: alsa-plugins
Requires: alsa-plugins-pulse
#Requires: alsa-plugin-xaudio
Requires: syslinux
Requires: mkisofs
#Requires: libao-nas
#Requires: libao-esd
Requires: libao-pulse
Requires: nfs-clients
Requires: samba-client
Requires: samba-client-cups
Requires: vim-enhanced
Requires: browser-plugins-npapi
Requires: cups
Requires: cups-pdf
Requires: cups-ppd
Requires: ghostscript-cups
Requires: foomatic
Requires: hd2u
Requires: mc
Requires: unrar
Requires: zip
Requires: bc
Requires: p7zip
Requires: screen
#Requires: bash-completion
Requires: apt-utils
Requires: aspell-en
Requires: aspell-ru
Requires: aspell-uk
Requires: info
Requires: catdoc
Requires: mpg321
Requires: vorbis-tools
Requires: flac123
Requires: mtools
Requires: lftp
Requires: links
#Requires: psi
Requires: synaptic
# fonts
Requires: fonts-bitmap-terminus
Requires: fonts-bitmap-univga
#Requires: fonts-ttf-ms
Requires: fonts-type1-urw
Requires: fonts-type1-xorg
# xkb
Requires: xkeyboard-config

%description -n %bname-server-enhanced
Enhanced virtual package for %Name.

%if_with kde
%package -n %bname-server-kde
Summary: %Name KDE variant package
Group: Networking/Remote access
Obsoletes: %{bname}5-server-kde
Provides: %{bname}5-server-kde = %version-%release
Requires: %bname-server-enhanced = %version-%release
# dm
Requires: kdebase-kdm
# base KDE soft
Requires: iceauth
Requires: kdebase-wm
Requires: kdebase-kcontrol
Requires: kdebase-kio
Requires: kkbswitch
Requires: kdebase-konqueror
Requires: kdepim-kmail
Requires: kdeutils-ark
Requires: kdeaddons-kicker
Requires: kdebase-kdeprint
Requires: kdenetwork-kget
Requires: kdenetwork-kopete
Requires: kdenetwork-krdc
Requires: kdenetwork-lisa
# additional KDE soft
#   viewers
Requires: kdegraphics-kview
Requires: kdegraphics-kpdf
Requires: kdegraphics-kghostview
Requires: kchmviewer
Requires: kdegraphics-kviewshell
Requires: kdegraphics-ksvg
Requires: kdegraphics-kuickshow
#   multimedia
#Requires: kdeaddons-noatun
Requires: amarok-engine-xine
Requires: kdemultimedia-kmix
Requires: kaffeine
#   graphics
Requires: kdegraphics-kolourpaint
#   other
Requires: kdepim-korganizer
Requires: kdeutils-kcalc
Requires: kdeutils-kcharselect
Requires: kdeutils-kdessh
Requires: kleansweep
# locales
Requires: kde-i18n-ru
Requires: kde-i18n-uk

%description -n %bname-server-kde
KDE-based virtual package for %Name.
%endif

%if_with icewm
%package -n %bname-server-icewm
Summary: %Name light-variant package
Group: Networking/Remote access
Provides: %bname-server-light = %version-%release
Obsoletes: %bname-server-light
Requires: %bname-server-enhanced = %version-%release
# dm
#Requires: kdebase-kdm
# wm
Requires: icewm-startup-xxkb
Requires: icewm-startup-idesk
Requires: firefox-ru
#Requires: sylpheed
Requires: xarchiver
Requires: grdesktop
# viewers
Requires: xpdf
Requires: djvu-viewer
Requires: gqview
Requires: qiv
Requires: xchm
#Requires: evince
#  multimedia
Requires: aumix
Requires: audacious-plugins
Requires: gxine
#  graphics
#Requires: xpaint
#  other
Requires: xcalc

%description -n %bname-server-icewm
IceWM-based virtual package for %Name.
%endif

%package -n %bname-server-addons
Summary: %Name additional packages
Group: Networking/Remote access
Obsoletes: %{bname}5-server-addons
Provides: %{bname}5-server-addons = %version-%release
Requires: %bname-server-basic = %version-%release
Requires: ltsp-usermode

%description -n %bname-server-addons
Additional packages for %Name.

%files -n %bname-server-basic
%files -n %bname-server-enhanced
%if_with kde
%files -n %bname-server-kde
%endif
%if_with icewm
%files -n %bname-server-icewm
%endif
%files -n %bname-server-addons

# TODO:
# - cut pkglists to the required minimum,
#   distro formation is better done otherwise

%changelog
* Fri Jan 20 2012 Michael Shigorin <mike@altlinux.org> 5.0-alt0.16
- fixed build
- updated for t6/branch
- renamed -light subpackage back into -icewm and made it conditional
- made -kde subpackage conditional and disabled it by default

* Sun Dec 27 2009 Michael Shigorin <mike@altlinux.org> 5.0-alt0.15.6
- added alsa-plugins-pulse to ltsp-server-enhanced

* Tue Dec 08 2009 Michael Shigorin <mike@altlinux.org> 5.0-alt0.15.5
- temporarily dropped twm from ltsp-server-basic deps
  (its session scores higher than current kde3, see #22480)

* Mon Jul 13 2009 Michael Shigorin <mike@altlinux.org> 5.0-alt0.15.4
- dropped xpaint (orphaned?)

* Sun Jun 14 2009 Michael Shigorin <mike@altlinux.org> 5.0-alt0.15.3
- dropped sylpheed either

* Sat Jun 13 2009 Michael Shigorin <mike@altlinux.org> 5.0-alt0.15.2
- restored the package by dropping dependencies which have vanished
  and weren't used at least by defaut anyways
- metadata: s/LTSP5/A&/
- me as a Packager:

* Thu Mar 05 2009 Michael Shigorin <mike@altlinux.org> 5.0-alt0.15.1
- NMU: replaced unfs3 with nfs-server for better performance
  (we didn't get around to VE template, and that would be
  a separate affair anyways)

* Mon May 12 2008 Led <led@altlinux.ru> 5.0-alt0.15
- added to ltsp-server-basic requires:
  + xmessage
- added to ltsp-server-enhanced requires:
  + alsa-plugin-xaudio
  + libao-pulse
- removed from ltsp-server-basic requires:
  + xorg-x11-xfs
- removed from ltsp-server-kde requires:
  + kdeutils-kdessh
  + kleansweep

* Mon Mar 31 2008 Led <led@altlinux.ru> 5.0-alt0.14
- renamed ltsp5-server* -> ltsp-server*
- removed man-pages-ru requires in ltsp-server-enhanced

* Mon Oct 08 2007 Led <led@altlinux.ru> 5.0-alt0.13
- cleaned up Requires

* Wed Aug 01 2007 Led <led@altlinux.ru> 5.0-alt0.12
- fixed Requires in ltsp5-server-basic

* Thu Jul 26 2007 Led <led@altlinux.ru> 5.0-alt0.11
- removed noatun from ltsp5-server-kde requires
- renamed ltsp5-server-base to ltsp5-server-basic
- moved ltsp-usermode requires from ltsp5-server-basic to
  new virtual package ltsp5-server-addons

* Thu Jul 12 2007 Led <led@altlinux.ru> 5.0-alt0.10
- added to ltsp5-server-enhanced requires:
  + alsa-plugins

* Tue Jul 10 2007 Led <led@altlinux.ru> 5.0-alt0.9
- fixed bname-server-enhanced requires

* Mon Jul 09 2007 Led <led@altlinux.ru> 5.0-alt0.8
- added to ltsp5-server-enhanced requires:
  + syslinux
  + mkisofs

* Thu Jul 05 2007 Led <led@altlinux.ru> 5.0-alt0.7
- added portmap to ltsp5-server-base requires

* Thu Jul 05 2007 Led <led@altlinux.ru> 5.0-alt0.6
- replaced nfs-server with unfs3 in ltsp5-server-base requires
- added to ltsp5-server-enhanced requires:
  + libao-nas

* Wed Jun 27 2007 Led <led@altlinux.ru> 5.0-alt0.5
- added ltsp-usermode to ltsp5-server-base Requires

* Wed May 23 2007 Led <led@altlinux.ru> 5.0-alt0.4
- fixed Requires

* Thu May 17 2007 Led <led@altlinux.ru> 5.0-alt0.3
- updated require list in enhanced package

* Wed May 16 2007 Led <led@altlinux.ru> 5.0-alt0.2
- fixed Requires

* Tue May 15 2007 Led <led@altlinux.ru> 5.0-alt0.1
- initial build
