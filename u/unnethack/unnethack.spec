Name: unnethack
Version: 5.2.0
Release: alt2
Summary: An enhancement to the dungeon exploration game NetHack
Source: %version.tar.gz
Group: Games/Adventure
Url: https://unnethack.wordpress.com
License: NethackGPL

# Automatically added by buildreq on Sat Nov 26 2011
# optimized out: libtinfo-devel
BuildRequires: flex groff-base libgsl-devel libncurses-devel

%description
UnNetHack is a variant of NetHack.

It features more randomness, more levels, more challenges and more fun
than vanilla NetHack.

%prep
%setup
sed -i 's/[$](LFLAGS) \(.*\)[$](LIBS)/\1 $(LFLAGS) $(LIBS)/' sys/autoconf/Makefile.src

%build
LIBS=-lgsl %configure --enable-curses-graphics
make include/autoconf_paths.h
make -C util recover
%make_build

%install
make install DESTDIR=%buildroot CHOWN=echo CHGRP=echo CHMOD=echo
mv %buildroot%_datadir/unnethack/recover %buildroot%_bindir/recover.bin && ln -s %_bindir/recover.bin %buildroot%_datadir/unnethack/recover
mv %buildroot%_datadir/unnethack/unnethack %buildroot%_bindir/unnethack.bin && ln -s %_bindir/unnethack.bin %buildroot%_datadir/unnethack/unnethack

%files
%doc doc README
%attr(2711,root,games) %_bindir/*.bin
%_bindir/*[^n]
%_datadir/%name
%_defaultdocdir/%name
%dir %attr(775,root,games) %_localstatedir/%name
%attr(775,root,games) %_localstatedir/%name/[sbl]*
%attr(664,root,games) %_localstatedir/%name/[^sbl]*

%changelog
* Thu Dec 19 2019 Fr. Br. George <george@altlinux.ru> 5.2.0-alt2
- Fix parallel build

* Wed Oct 16 2019 Fr. Br. George <george@altlinux.ru> 5.2.0-alt1
- Autobuild version bump to 5.2.0

* Thu Feb 27 2014 Fr. Br. George <george@altlinux.ru> 5.1.0-alt1
- Autobuild version bump to 5.1.0
- Fix build

* Thu Apr 19 2012 Fr. Br. George <george@altlinux.ru> 4.0.0-alt1
- Autobuild version bump to 4.0.0

* Thu Mar 01 2012 Fr. Br. George <george@altlinux.ru> 3.6.1-alt1
- Autobuild version bump to 3.6.1

* Sun Nov 27 2011 Fr. Br. George <george@altlinux.ru> 3.6.0-alt1
- Autobuild version bump to 3.6.0
- Snapshot version corrected manually
- Patchset fix

* Sun Nov 27 2011 Fr. Br. George <george@altlinux.ru> 3.5.3-alt20101010.1
- Initial build from scratch

