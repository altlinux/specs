%def_enable iconv

Name: mpc
Version: 0.19
Release: alt1
Summary: Command line tool to interface MPD
License: %gpl2plus
Group: Sound
Url: http://mpd.wikia.com/?page=%name
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Alexey Rusakov <ktirf@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libmpdclient-devel

%description
Music Player Command (%name) is a client for MPD, the Music Player
Daemon. %name connects to a MPD running on a machine via a network.


%prep
%setup
%patch -p1


%build
%autoreconf
%configure \
    --docdir=%_docdir/%name-%version \
    %{subst_enable iconv}
%make_build


%install
%make_install DESTDIR=%buildroot docdir=%_docdir/%name-%version install
#install -m 0644 ChangeLog %buildroot%_docdir/%name-%version/


%files
%_bindir/*
%_man1dir/*
%doc AUTHORS COPYING README


%changelog
* Sun Oct 24 2010 Alexey Morsov <swi@altlinux.ru> 0.19-alt1
- new release version

* Mon Sep 14 2009 Alexey Rusakov <ktirf@altlinux.org> 0.17-alt2
- revert "disable character set conversion to/from pipe" (ALT #21080).

* Sun Aug 16 2009 Alexey Rusakov <ktirf@altlinux.org> 0.17-alt1
- 0.17

* Sun Aug 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.16-alt1
- 0.16
- thanks to led@ for his repository
- take upstream sources from the upstream git instead of tarballs

* Sun Dec 21 2008 Led <led@altlinux.ru> 0.14-alt1
- 0.14

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.12.1-alt0.3
- fixed Url

* Sun Aug 03 2008 Led <led@altlinux.ru> 0.12.1-alt0.2
- fixed Url (#9095)

* Sun Sep 09 2007 Led <led@altlinux.ru> 0.12.1-alt0.1
- 0.12.1
- cleaned up and fixed spec
- fixed License
- added %name-0.12.1-alt.patch

* Mon Sep 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.12.0-alt1
-  0.12.0.

* Wed Jan 18 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.11.2-alt1
-  0.11.2.

* Thu Feb 10 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.11.1-alt1
-  initial build.
