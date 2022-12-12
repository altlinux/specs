Name: putty
Version: 0.78
Release: alt2

Summary: Free SSH, Telnet and Rlogin client
License: MIT
Group: Networking/Remote access

Url: http://www.chiark.greenend.org.uk/~sgtatham/putty/
Source0: %name-%version.tar.gz
Source1: %name-icons.tar.bz2
Source2: %name-%version.tar.gz.gpg
Source3: putty.desktop
Source4: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libgtk+3-devel rpm-macros-cmake cmake ImageMagick-tools

%description
This is the Unix port of the popular Windows ssh client, PuTTY. It
supports flexible terminal setup, mid-session reconfiguration using
Ctrl-rightclick, multiple X11 authentication protocols, and various
other interesting things not provided by ssh in an xterm.

%prep
%setup
%setup -T -D -a1 -n %name-%version
%ifarch %e2k
sed -i 's/mmintrin\.h/no_&/' crypto/CMakeLists.txt
%endif

%ifnarch %e2k
# that gtk update is not there yet
sed -i 's/G_APPLICATION_FLAGS_NONE/G_APPLICATION_DEFAULT_FLAGS/' \
	unix/main-gtk-application.c
%endif

%build
%add_optflags -Wall -Werror -Wstrict-aliasing -Wno-unused
%ifarch %e2k
# lcc 1.25.15: ftbfs workaround ('unreachable' macro ignored)
# reported upstream and as mcst#6021
%add_optflags -Wno-error=return-type -Wno-error=maybe-uninitialized
# glib2 deprecation warnings
%add_optflags -Wno-error=deprecated-declarations
%endif
export CFLAGS=" -DNOT_X_WINDOWS -Wno-error=unused-function"
mkdir %{_cmake__builddir}

cd %{_cmake__builddir}

cmake -DCMAKE_INSTALL_PREFIX=/usr ..

make

make -C ../icons putty-48.png

make -C doc

mkdir -p %buildroot{%_bindir,%_man1dir}
%makeinstall_std prefix=%prefix mandir=%_mandir

%install
	
%cmake_install
install -d html
install -pm 0644 doc/html/*.html html

# icon
install -pDm644 putty48.png %buildroot%_liconsdir/%name.png
install -pDm644 putty32.png %buildroot%_niconsdir/%name.png
install -pDm644 putty16.png %buildroot%_miconsdir/%name.png

install -pDm644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

%files
%doc LICENCE README
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png

%changelog
* Mon Dec 12 2022 Michael Shigorin <mike@altlinux.org> 0.78-alt2
- E2K: build fixes (clmul, gtk issues) by ilyakurdyukov@

* Wed Dec 07 2022 Artyom Bystrov <arbars@altlinux.org> 0.78-alt1
- new version 0.78

* Sun Jul 18 2021 Michael Shigorin <mike@altlinux.org> 0.76-alt1
- new version (watch file uupdate)

* Fri May 14 2021 Michael Shigorin <mike@altlinux.org> 0.75-alt2
- E2K: ftbfs wokaround (reported upstream; mcst#6021)

* Sat May 08 2021 Michael Shigorin <mike@altlinux.org> 0.75-alt1
- new version (watch file uupdate)
- explicit -lm

* Sat Jun 27 2020 Michael Shigorin <mike@altlinux.org> 0.74-alt1
- new version (watch file uupdate)

* Mon Sep 30 2019 Michael Shigorin <mike@altlinux.org> 0.73-alt1
- new version (watch file uupdate)

* Sun Jul 21 2019 Michael Shigorin <mike@altlinux.org> 0.72-alt1
- new version (watch file uupdate)

* Sat Mar 16 2019 Michael Shigorin <mike@altlinux.org> 0.71-alt1
- new version (watch file uupdate)

* Mon Jul 10 2017 Michael Shigorin <mike@altlinux.org> 0.70-alt1
- new version (watch file uupdate)
- dropped patch (fixed in upstream release)

* Mon May 22 2017 Michael Shigorin <mike@altlinux.org> 0.69-alt1
- new version (watch file uupdate)
- added upstream patch to fix FTBFS against gtk2 (via fedora)

* Thu Feb 23 2017 Michael Shigorin <mike@altlinux.org> 0.68-alt1
- new version (watch file uupdate)

* Sat Mar 05 2016 Michael Shigorin <mike@altlinux.org> 0.67-alt1
- new version (watch file uupdate)

* Tue Nov 10 2015 Michael Shigorin <mike@altlinux.org> 0.66-alt1
- new version (watch file uupdate)
- spec cleanup

* Mon Jul 27 2015 Michael Shigorin <mike@altlinux.org> 0.65-alt1
- new version (watch file uupdate)

* Tue Mar 03 2015 Michael Shigorin <mike@altlinux.org> 0.64-alt1
- security fixes:
  + failure to scrub private keys from memory after use, see
    http://www.chiark.greenend.org.uk/~sgtatham/putty/wishlist/private-key-not-wiped-2.html
  + missing range check in Diffie-Hellman key exchange, see
    http://www.chiark.greenend.org.uk/~sgtatham/putty/wishlist/diffie-hellman-range-check.html

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1.qa1
- NMU: fixed bugs in watch file

* Wed Aug 07 2013 Michael Shigorin <mike@altlinux.org> 0.63-alt1
- security fixes for vulnerabilities exploitable by custom sshd, see
  http://www.chiark.greenend.org.uk/~sgtatham/putty/changes.html

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.62-alt1.1
- Fixed build with new glib2

* Tue Dec 13 2011 Michael Shigorin <mike@altlinux.org> 0.62-alt1
- 0.62
  + 0.59, 0.60 and 0.61 stored the keyboard-interactive password
    for the whole session by accident so it could be retrieved
- several other bugfixes

* Thu Jul 14 2011 Terechkov Evgenii <evg@altlinux.org> 0.61-alt1
- 0.61 beta

* Sat Oct  2 2010 Terechkov Evgenii <evg@altlinux.org> 0.60-alt4
- 20101001 snapshot (ALT#23796)
- Build with libgtk+2
- Old patches dropped

* Wed May 27 2009 Michael Shigorin <mike@altlinux.org> 0.60-alt3
- adapted repocop patch (iconsdir)

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 0.60-alt2
- worked around FTBFS with gcc-4.4
  + proper maintainer should find a better fix
- dropped obsolete macros
- me as (improper) Packager: again

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.60-alt1
- new version
- add watch file

* Sat Jan 27 2007 Michael Shigorin <mike@altlinux.org> 0.59-alt1
- 0.59
- employed new and shiny configure
  + removed old makefile patch
  + fixed build with gcc-4.1 -Werror -Wall -Wl,-as-needed
- replaced Debian menu file with freedesktop 
  (borrowed from Dag Wieers' repo)
- added temporary patch to define (forgotten?) release
- changed Url: to homepage instead of download location
- added Packager:
- removed pscp(1), psftp(1) manpage stubs
  (proper ones arrived)

* Sat May 13 2006 Michael Shigorin <mike@altlinux.org> 0.58-alt3
- fixed #9559 (thanks Andrei Bulava for report/fix)

* Tue Mar 07 2006 Michael Shigorin <mike@altlinux.org> 0.58-alt2
- fixed build with --as-needed
- spec cleanup

* Thu Sep 22 2005 Michael Shigorin <mike@altlinux.org> 0.58-alt1
- built for ALT Linux
- adapted from Mandriva spec for 0.58-1mdk

* Wed Apr 06 2005 Götz Waschk <waschk@linux-mandrake.com> 0.58-1mdk
- New release 0.58

* Tue Feb 22 2005 Götz Waschk <waschk@linux-mandrake.com> 0.57-1mdk
- New release 0.57

* Wed Oct 27 2004 Götz Waschk <waschk@linux-mandrake.com> 0.56-1mdk
- don't bzip2 source for sig checks
- add signature
- New release 0.56

* Wed Aug 4 2004 Tibor Pittich <Tibor.Pittich@mandrake.org> 1:0.55-1mdk
- 0.55
- added support to build stable or snapshot versions

* Mon Feb 16 2004 David Walluck <walluck@linux-mandrake.com> 1:0.54-0.20040216.3mdk
- fix changelog entries

* Sun Feb 15 2004 David Walluck <walluck@linux-mandrake.com> 1:0.54-0.20040216.2mdk
- bump epoch to fix improper version tag in the 0.53b release

* Sun Feb 15 2004 David Walluck <walluck@linux-mandrake.com> 0:0.54-0.20040216.1mdk
- 0.54 (20040216)

* Thu Sep 18 2003 Laurent Culioli <laurent@pschit.net> 0.53b-0.cvs.20030917.2mdk
- fix menu
- drop requires

* Wed Sep 17 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.53b-0.cvs.20030917.1mdk
- initial cooker inport of this famous ssh/telnet client

