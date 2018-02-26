%define origname imms

Name: xmms-imms
Version: 3.0.2
Release: alt6
Epoch: 20110327

Summary: Intelligent Multimedia Management System
License: GPL
Group: Sound

Url: http://www.luminal.org/phpwiki/index.php/IMMS
Source: http://imms.googlecode.com/files/%origname-%version.tar.bz2
Patch0: imms-3.0.2-alt-configure.patch
Patch1: imms-3.0.2-alt-gcc43.patch
Packager: Michael Shigorin <mike@altlinux.org>

Obsoletes: imms

Summary(ru_RU.KOI8-R): "Умный" менеджер плейлиста
Summary(uk_UA.KOI8-U): "Розумний" менеджер плейл╕сту

# Automatically added by buildreq on Sun Oct 05 2008
BuildRequires: gcc-c++ id3lib-devel libXScrnSaver-devel libglade-devel libpcre-devel libsqlite3-devel libvorbis-devel libxmms-devel sqlite
BuildRequires: libX11-devel
BuildRequires: libfftw3-devel

# need new macros
BuildRequires(pre): libxmms-devel >= 1.2.8-alt2

%description
IMMS is an adaptive playlist plug-in for XMMS designed to simplify
management and prioritization of large collections of music.

Some of the key features include:
* Rating and playlist adjustment is done completely transparently
  to the user.  IMMS is super easy to use!
* Files are indentified by paths and checksums. Even if you move them
  they still keep their ratings.
* Though mostly "good" songs will be played, ocasionally less popular
  songs will sneak in to give them a chance to earn user's favour.
* IMMS does a better job of shuffling than XMMS. It is able to recognise
  different versions of the same song and not play them
  in quick succession.

It is also available for Audacious and Quod Libet players.

%description -l ru_RU.KOI8-R
IMMS - адаптивный модуль списка воспроизведения XMMS, созданный
для упрощения управления и приоретизации больших коллекций музыки.

%description -l uk_UA.KOI8-U
IMMS - адаптивный модуль списку в╕дтворення XMMS, створений
для спрощення керування та приоретизац╕╖ великих колекц╕й музики.

%prep
%setup -n %origname-%version
%patch0 -p1
%patch1 -p1

%build
%configure
#%make_build LIBS="-lglib" 
make LIBS="-lglib"

%install
install -pDm644 build/libxmmsimms2.so %buildroot%xmms_generaldir/libxmmsimms2.so
install -pDm755 build/immstool %buildroot%_bindir/immstool
install -pDm755 build/immsd %buildroot%_bindir/immsd

%files
%doc README 
%xmms_generaldir/*
%_bindir/*

# TODO: 
# - build libtorch (www.torch.ch) and enable analyzer
# - build 3.1.0rc (for audacious/quodlibet as well?)

%changelog
* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 20110327:3.0.2-alt6
- re-added lost BR:

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 20081105:3.0.2-alt5
- fixed build with gcc 4.3

* Sun Oct 05 2008 Michael Shigorin <mike@altlinux.org> 20081005:3.0.2-alt4
- fixed build (BR: gnome-libs-devel was unneeded)

* Sat Mar 22 2008 Michael Shigorin <mike@altlinux.org> 20080322:3.0.2-alt3
- rebuild (thanks icesik@)
- spec macro abuse cleanup

* Fri Mar 21 2008 Igor Zubkov <icesik@altlinux.org> 20051228:3.0.2-alt2
- fix rebuild
- buildreq

* Wed Dec 28 2005 Michael Shigorin <mike@altlinux.org> 20051228:3.0.2-alt1
- 3.0.2 (minor bugfixes)
- This release fixes a bug that caused correlations to stop working
  and song selection to possibly become biased when "dead" files were
  present in the playlist.

* Tue Dec 06 2005 Michael Shigorin <mike@altlinux.org> 20051206:3.0.1-alt1
- 3.0.1 (major bugfixes)
- This release fixes an important bug affecting the ratings of new
  songs. All users of 2.99.x and 3.0 are encouraged to upgrade.

* Mon Nov 28 2005 Michael Shigorin <mike@altlinux.org> 20051128:3.0-alt1
- 3.0

* Wed Dec 15 2004 Michael Shigorin <mike@altlinux.ru> 20041215:2.0.1-alt1
- 2.0.1
- updated buildrequires

* Wed Aug 18 2004 Michael Shigorin <mike@altlinux.ru> 20040818:1.2a-alt1
- 1.2a (major bugfixes)

* Tue Aug 17 2004 Michael Shigorin <mike@altlinux.ru> 20040817:1.2-alt1
- 1.2

* Fri Apr 16 2004 Michael Shigorin <mike@altlinux.ru> 20040416:1.1-alt1
- 1.1

* Thu Feb 26 2004 Michael Shigorin <mike@altlinux.ru> 20040226:1.0.1-alt1
- 1.0.1

* Tue Jan 27 2004 Michael Shigorin <mike@altlinux.ru> 20040127:1.0-alt1
- 1.0!

* Fri Dec 05 2003 Michael Shigorin <mike@altlinux.ru> 20031205:0.9.9-alt1
- 0.9.9 (major bugfixes)

* Wed Nov 12 2003 Michael Shigorin <mike@altlinux.ru> 20031112:0.9.8-alt1
- 0.9.8 (minor bigfixes; lives better with crossfade)

* Sat Oct 25 2003 Michael Shigorin <mike@altlinux.ru> 20031025:0.9.4-alt1
- updated for new plugin policy 
- renamed to %name

* Thu Oct 09 2003 Michael Shigorin <mike@altlinux.ru> 0.9.4-alt1
- 0.9.4 (minor feature enhancements)

* Tue Oct 07 2003 Michael Shigorin <mike@altlinux.ru> 0.9.3-alt1
- 0.9.3 (major bugfixes in 0.9.2)
- updated BuildRequires (libpcre-devel)

* Thu Jul 31 2003 Michael Shigorin <mike@altlinux.ru> 0.9-alt1
- built for ALT Linux

