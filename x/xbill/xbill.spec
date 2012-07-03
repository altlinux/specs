Summary: Stop Bill from loading his OS into all the computers
Summary(ru_RU.KOI8-R): Помешайте Биллу поставить свою ОС на все компьютеры
Name: xbill
Version: 2.1
Release: alt4.qa2

Packager: Grigory Batalov <bga@altlinux.ru>

License: GPL
Group: Games/Arcade
Source: ftp://ftp.xbill.org/pub/xbill/%name-%version.tar.gz
Url: http://www.xbill.org/

# Automatically added by buildreq on Tue Sep 09 2008
BuildRequires: flex gcc-c++ imake libXaw-devel

%description
The xbill game tests your reflexes as you seek out and destroy all
forms of Bill, establish a new operating system throughout the
universe, and boldly go where no geek has gone before.  Xbill has
become an increasingly attractive option as the Linux Age progresses,
and it is very popular at Red Hat.

%description -l ru_RU.KOI8-R
Игра xBill развивает рефлексы. Найдите и уничтожьте всех маленьких
человечков, пытающихся заразить ваши компьютеры вирусом Windows [TM].

%prep
%setup -q

%build
%configure --bindir=%_bindir --localstatedir=%_localstatedir/games --disable-motif --disable-gtk
%make_build

%install
%make_install DESTDIR=%buildroot install

# Menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=xBill
Comment=%{summary}
Icon=%{name}
#Exec=%_gamesbindir/%name
Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%attr(2711,root,games) %_x11bindir/xbill
%dir %_localstatedir/games/%name
%attr(664,root,games) %_localstatedir/games/%name/scores
%config(noreplace) %_localstatedir/games/%name/scores
%_datadir/%name
%_desktopdir/%{name}.desktop

%changelog
* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 2.1-alt4.qa2
- NMU: converted debian menu to freedesktop

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.1-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for xbill
  * postclean-05-filetriggers for spec file

* Tue Sep 09 2008 Grigory Batalov <bga@altlinux.ru> 2.1-alt4
- Build requirements were updated.

* Tue Mar 07 2006 Grigory Batalov <bga@altlinux.ru> 2.1-alt3
- Provide %_localstatedir/games/%name directory (#9123)

* Wed Feb 08 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.1-alt2.1
- Rebuild with libXaw3d.so.8 .

* Fri Jan 24 2003 Grigory Batalov <bga@altlinux.ru> 2.1-alt2
- Rebuilt with gcc-3.2

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 2.1-alt1.1
- Fixed suid/sgid file permissions

* Wed May 22 2002 Grigory Batalov <bga@altlinux.ru> 2.1-alt1
- Built for ALT Linux

* Sun Oct 28 2001 Brian Wellington <bwelling@xbill.org>
- Updated to 2.1

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Apr 27 2001 Bill Nottingham <notting@redhat.com>
- rebuild for C++ exception handling on ia64

* Wed Oct 18 2000 Than Ngo <than@redhat.com>
- rebuilt against gcc-2.96-60

* Tue Jul 18 2000 Than Ngo <than@redhat.de>
- rebuilt with gcc-2.96-4.0

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul  2 2000 Jakub Jelinek <jakub@redhat.com>
- Rebuild with new C++

* Sun Jun 18 2000 Than Ngo <than@redhat.de>
- rebuilt in the new build environment
- use RPM maccros

* Mon May 08 2000 Preston Brown <pbrown@redhat.com>
- fix for gcc 2.95 from t-matsuu@protein.osaka-u.ac.jp.

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- rebuild with config(noreplace) score file, new description
- replace wmconfig with desktop file

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built pacakge for 6.0

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc
