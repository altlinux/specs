%define mjversion 3.7
Name: povray
Version: %mjversion.0.10
Release: alt2

Summary: Persistence of Vision Ray Tracer (POV-Ray)
License: AGPL-3.0 and CC-BY-NC-SA-2.5 and CC-BY-SA-3.0
Group: Graphics

Url: http://www.povray.org
# VCS: https://github.com/POV-Ray/povray
Source: %name-%version.tar
Patch: %name-%version-alt.patch

Requires: %name-common

BuildRequires: gcc-c++ imake libjpeg-devel libpng-devel libtiff-devel libXpm-devel libXt-devel
BuildRequires: boost-devel boost-flyweight-devel

Summary(ru_RU.UTF-8): Трассировщик лучей POV-Ray

%description
POV-Ray is a free, full-featured ray tracer, written and
maintained by a team of volunteers on the Internet.
POV-Ray has the right balance of power and versatility
to satisfy extremely experienced and competent users, while
at the same time not being so intimidating as to completely
scare new users off.

%description -l ru_RU.UTF-8
POV-Ray - это свободный полнофункциональный трассировщик
лучей, написанный и поддерживаемый командой добровольцев
через Интернет. POV-Ray сохраняет баланс между мощностью
и гибкостью, отвечая желаниям самых опытных пользователей,
в то же время не отпугивая совсем новичков.

%package common
Group: Graphics
Summary: POV-Ray common files
Summary(ru_RU.UTF-8): Общие файлы для POV-Ray

%description common
Common files for POV-Ray: docs, textures, color maps,
scenes, scripts etc.

%description common -l ru_RU.UTF-8
Общие файлы для разных версий POV-Ray: документация,
текстуры, цветовые карты, сцены, скрипты и т.д.

%prep
%setup 
%patch -p1
%ifarch %e2k riscv64
sed -i 's,aarch64,&|riscv64|e2k,' unix/config/ax_boost_base.m4
%endif

%build
pushd unix
./prebuild.sh
popd
%configure COMPILED_BY='ALT Linux Team (http://www.altlinux.org, mailto:community@lists.altlinux.org)' --with-x --without-svga
%make_build CFLAGS=-Wno-multichar CXXFLAGS=-Wno-multichar
# Adjust bogus paths
sed -i \
  -e '/DEFAULT_DIR=/d' \
  -e 's,SYSCONFDIR=\$DEFAULT_DIR/etc,SYSCONFDIR=%{_sysconfdir},' \
  scripts/{allanim,allscene,portfolio}.sh

%install
%makeinstall_std
# remove carriage return symbols
find %buildroot%_datadir/povray-%mjversion/scripts/ -type f -print0 |\
	xargs -r0 sed -i -e 's,\r$,,g'

%check
make check

%files
%_bindir/povray

%files common
%config(noreplace) %_sysconfdir/%name/%mjversion/*
%dir %_datadir/%name-%mjversion
%_datadir/%name-%mjversion/*
%docdir %_defaultdocdir/%name-%mjversion
%dir %_defaultdocdir/%name-%mjversion
%_defaultdocdir/%name-%mjversion/*
%doc %_man1dir/*

%changelog
* Tue Oct 31 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.7.0.10-alt2
- NMU: fixed FTBFS on LoongArch.

* Fri Aug 20 2021 Anton Farygin <rider@altlinux.ru> 3.7.0.10-alt1
- 3.7.0.10

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7.0.8-alt5
- Rebuilt with boost-1.77.0.

* Fri Jul 10 2020 Michael Shigorin <mike@altlinux.org> 3.7.0.8-alt4
- fixed build on %%e2k (and riscv64, hopefully)
- License: clarification (3.7+)
- minor spec cleanup

* Wed Oct 02 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.7.0.8-alt3
- Fixed build on ppc64le.

* Fri Mar 01 2019 Anton Farygin <rider@altlinux.ru> 3.7.0.8-alt2
- rebuilt with libpng16

* Tue Jun 19 2018 Anton Farygin <rider@altlinux.ru> 3.7.0.8-alt1
- 3.7.0.8

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7.0.4-alt1.1
- NMU: rebuilt with boost-1.67.0

* Thu Oct 05 2017 Anton Farygin <rider@altlinux.ru> 3.7.0.4-alt1
- new version

* Tue Jun 06 2017 Anton Farygin <rider@altlinux.ru> 3.7.0.2-alt1
- 3.0.7.2 from git

* Wed Apr 03 2013 Fr. Br. George <george@altlinux.ru> 3.6-alt4
- Build with legacy libpng12

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
