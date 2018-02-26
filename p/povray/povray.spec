Name: povray
Version: 3.6
Release: alt3
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Persistence of Vision Ray Tracer (POV-Ray)
Summary(ru_RU.UTF-8): Трассировщик лучей POV-Ray
# Licensed like freeware. See POVLEGAL.DOC.
License: povray
Group: Graphics
Url: http://www.povray.org

Source: ftp://ftp.povray.org/pub/povray/Official/Unux/%name-%version.tar.bz2

Requires: %name-common
#Obsoletes: megapovplus

# Automatically added by buildreq on Mon Nov 10 2008
BuildRequires: gcc-c++ imake libXpm-devel libXt-devel libjpeg-devel libpng-devel libtiff-devel

#BuildRequires: XFree86-devel xpm-devel

%description
POV-Ray is a free, full-featured ray tracer, written and
maintained  by  a  team of volunteers on the Internet.
POV-Ray has the right balance of power and versatility
to satisfy extremely experienced and competent users, while
at the same time not being so intimidating as to completely
scare new users off.

%description -l ru_RU.UTF-8
POV-Ray - это свободный, полнофункциональный трассировщик
лучей, написанный и поддерживаемый командой добровольцев
через Интернет. POV-Ray сохраняет баланс между мощностью
и гибкостью, отвечая желаниям самых опытных пользователей,
в то же время, не отпугивая новичков.

#---------------------------------------------------------
%package common
Group: Graphics
Summary: POV-Ray common files
Summary(ru_RU.UTF-8): Общие файлы для POV-Ray
#Obsoletes: megapovplus-common

%description common
Common files for POV-Ray: docs, textures, color maps,
scenes, scripts etc.

%description common -l ru_RU.UTF-8
Общие файлы для разных версий POV-Ray: документация,
текстуры, цветовые карты, сцены, скрипты и т.д.

#---------------------------------------------------------
#%package mpi
#Group: Graphics
#Summary: An unofficial MPI-version of POV-Ray
#Requires: %name-common
#Url: http://www.verrall.demon.co.uk/mpipov/
#
#%description mpi
#A parrallel version of POV-Ray using MPI (mpich).
#POV-Ray is a free, full-featured ray tracer,  written  and
#maintained  by  a  team of volunteers on the Internet.  On
#the Unix platform POV-Ray can be compiled with support for
#preview  capabilities  using  the  X Window System.  Under
#Linux, POV-Ray can optionally use the SVGA library to pre-
#view renderings.
#
#---------------------------------------------------------
%prep
%setup -q -n %name-3.6.1

%build
%configure COMPILED_BY='ALT Linux Team (http://www.altlinux.ru, mailto:community@lists.altlinux.org)' --with-x --without-svga
%make_build CFLAGS=-Wno-multichar CXXFLAGS=-Wno-multichar
#LDFLAGS=-L%_libdir

%install
%make_install install DESTDIR=%buildroot
# \
# docdir=%_defaultdocdir/%name-%version \
# htmldir=%_defaultdocdir/%name-%version/html \
# imagesdir=%_defaultdocdir/%name-%version/html/images \
# vfaqdir=%_defaultdocdir/%name-%version/html/images/vfaq

# remove carriage return symbols
find %buildroot%_datadir/povray-3.6/scripts/ -type f -print0 |\
	xargs -r0 sed -i -e 's,\r$,,g'

#%__mkdir_p %buildroot/%_sysconfdir
#%__mv %buildroot/%_datadir/%name-%version/povray.ini %buildroot/%_sysconfdir/povray.ini
#cat <<EOF > %buildroot/%_sysconfdir/povray.conf
#[File I/O Security]
#none
#EOF

%files
%_bindir/povray

#%files mpi
#%_bindir/povray

%files common
%config(noreplace) %_sysconfdir/%name/%version/*
%dir %_datadir/%name-%version
%_datadir/%name-%version/*
%docdir %_defaultdocdir/%name-%version
%dir %_defaultdocdir/%name-%version
%_defaultdocdir/%name-%version/*
%doc %_man1dir/*

%changelog
* Mon Nov 10 2008 Grigory Batalov <bga@altlinux.ru> 3.6-alt3
- Carriage return symbols were removed from scripts.
- Russian package description converted to UTF-8.
- Link to the ALT Linux community mailing list was updated.

* Sat Feb 24 2007 Grigory Batalov <bga@altlinux.ru> 3.6-alt2
- Update build requirements.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.6-alt1.1
- Rebuilt with libstdc++.so.6.

* Wed Oct 13 2004 Grigory Batalov <bga@altlinux.ru> 3.6-alt1
- 3.6.1

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3.5-alt2.1.1
- Rebuilt with libtiff.so.4.

* Fri Feb 27 2004 Grigory Batalov <bga@altlinux.ru> 3.5-alt2.1
- libintl-devel requirement removed

* Fri Sep 26 2003 Grigory Batalov <bga@altlinux.ru> 3.5-alt2
- build requirements fixed

* Tue Dec 24 2002 Grigory Batalov <bga@altlinux.ru> 3.5-alt1.2
- more building fixes

* Wed Oct 16 2002 Stanislav Ievlev <inger@altlinux.ru> 3.5-alt1.1
- made buildable (under gcc3)
- use subst instead sed
- added packager tag
- fix buildreq

* Wed Oct 16 2002 Grigory Batalov <bga@altlinux.ru> 3.5-alt1
- Initial build
