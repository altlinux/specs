# -*- mode: rpm-spec; coding: utf-8 -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: simutrans
Version: 0.111.2.1
Release: %branch_release alt1

Summary: Transport and Economic Simulation Game
License: Artistic
Group: Games/Strategy

Url: http://www.simutrans.com/
Source: %name-%version.tar.bz2
Source1: config.default
Source2: simutrans.run
Source3: simutrans.desktop
Source4: simutrans.png
Source5: simutrans_langtabs-99-17.tar.bz2
Patch10: simutrans-alt-ru.patch
Patch20: simutrans-no-x86-specifics.patch

Requires: simutrans-pak >= 0.111.2

BuildRequires(pre): rpm-macros-branch
BuildPreReq: bzlib-devel

# Automatically added by buildreq on Mon Jun 13 2011
BuildRequires: bzlib-devel gcc-c++ libSDL-devel libSDL_mixer-devel zlib-devel

Summary(ru_RU.UTF-8): Транспортно-экономическая игра-симулятор

%description
Simutrans is a freeware transportation simulator that runs under
Windows, Linux, and a few other operating systems (Apple Macintosh
with Intel processors, BEOS). It's similar to Transport Tycoon,
Transport Tycoon Deluxe and Transport Giant.

You take on the role of operating a transportation company, and your
goal is to get goods of various kinds, as well as passengers and mail,
from one place to the next.

Don't be fooled by the tile-based graphics - this is a very complex
game, and it is constantly evolving, with new features being added. It
is a living game, and consistently being made better and better.

%description -l ru_RU.UTF-8
Simutrans - это свободный (freeware) транспортный симулятор, работающий
под Windows, Linux и несколькими другими операционными системами
(Apple Macintosh на процессорах Intel, BeOS). Simutrans похож на
Transport Tycoon, Transport Tycoon Deluxe и Transport Giant.

В ходе игры Вы выступаете в роли управляющего транспортной компании, и Вашей
задачей является доставка различных грузов, пассажиров и почты из
одного места в другое.

Не придавайте слишком большое значение тому, что графика в игре сравнительно
проста - сама игра очень сложна и постоянно развивается, в неё добавляются
новые возможности. Это живой, развивающийся проект, который становится со
временем лучше и лучше.

%prep
%setup -a 5
%patch10 -p1
%ifnarch %ix86
%patch20 -p1
%endif
cp -pr %SOURCE1 .

%build
make

%install
mkdir -p %buildroot{%_libexecdir/simutrans,%_bindir,%_iconsdir,%_desktopdir}

install -m 0755 build/default/sim %buildroot%_libexecdir/simutrans/simutrans.bin
cp -pr simutrans/{config,font,music,text} %buildroot%_libexecdir/simutrans/

sed -e 's,@LIBEXECDIR@,%_libexecdir,g' %SOURCE2 > %buildroot%_bindir/simutrans
chmod 0755 %buildroot%_bindir/simutrans
install -m 0644 %SOURCE3 %buildroot%_desktopdir/
install -m 0644 %SOURCE4 %buildroot%_iconsdir/

%files
%doc simutrans/*.txt
%_bindir/*
%_libexecdir/simutrans
%_iconsdir/*
%_desktopdir/*

%changelog
* Thu Mar 22 2012 Aleksey Avdeev <solo@altlinux.ru> 0.111.2.1-alt1
- new version

* Sat Jun 25 2011 Aleksey Avdeev <solo@altlinux.ru> 0.110.0.1-alt2
- buffer overflow fix

* Sun Jun 19 2011 Aleksey Avdeev <solo@altlinux.ru> 0.110.0.1-alt1
- new version

* Thu Feb 26 2009 Michael Shigorin <mike@altlinux.org> 0.99.17.1-alt2.r1533
- applied PPC patch by sbolshakov@ (only on non-x86 arches)
- spec cleanup
- buildreq
- NB: this package would benefit from proper maintainer. :)

* Tue Jan 08 2008 Michael Shigorin <mike@altlinux.org> 0.99.17.1-alt1.r1533
- rebuilt for Sisyphus

* Sat Jan  5 2008 Alexey Morozov <morozov@altlinux.org> 0.99.17.1-alt1.r1533
- Initial build for ALTLinux (SuSE binary-only spec was taken as
  starting point).
