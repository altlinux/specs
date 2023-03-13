Name: simutrans-pak128
Version: 2.8.2
Release: alt1
Summary: Transport and Economic Simulation Game Assets
License: Artistic-2.0
Group: Games/Strategy
Url: http://github.com/simutrans/pak128
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: simupak128-2.8.2-for123.zip
BuildRequires: unzip
Requires: simutrans >= 123.0

BuildArch: noarch

%description
During development people wanted larger graphics. From this the 128 tile set was born.
Also it first featured a complex economy and has a really very wide variety of vehicles,
buildings or industries. It contains roughly 7 time more graphics data than pak64 and thus
requires by far the largest amounth of RAM and processing power of all Simutrans sets.
You need to upgrade Simutrans to 123.0 or later to run this release of pak128 !

%prep
%setup -c -n simutrans

%build
%install
mkdir -p %buildroot%_datadir/simutrans
cp -a * %buildroot%_datadir/

%files
%_datadir/simutrans

%changelog
* Mon Mar 13 2023 Artyom Bystrov <arbars@altlinux.org> 2.8.2-alt1
- initial build for ALT Sisyphus

* Mon Jan 31 2022 Michiel van der Wulp <michiel.vanderwulp@gmail.com> - 2.8.2
- updated to 2.8.2, see https://github.com/simutrans/pak128/commit/0adb1d2a6cd9cb1254bede2f52081916cbb93921
- The offcial sources are now located at http://github.com/simutrans/pak128
* Fri Oct  5 2018 Michiel van der Wulp <michiel.vanderwulp@gmail.com>
- new version 2.8.1 priority signals + bug fix
- for simutrans 120.4.1 and higher
- detailed changes see https://forum.simutrans.com/index.php/topic,18539.0/topicseen.html
* Thu Sep 20 2018 Michiel van der Wulp <michiel.vanderwulp@gmail.com>
- new version 2.8
- for Simutrans 120.4 and higher
- detailed changes see https://forum.simutrans.com/index.php/topic,18507.0.html
* Sun Oct 29 2017 michiel.vanderwulp@gmail.com
- new version 2.7
- for Simutrans 120.2.2 and higher
- detailed changes see http://forum.simutrans.com/index.php?topic=17501.0
* Fri Feb  5 2016 michiel.vanderwulp@gmail.com
- new version 2.6
- for Simutrans 120 and higher
- detailed changes see http://forum.simutrans.com/index.php?topic=15213.0
* Mon Sep 14 2015 michiel.vanderwulp@gmail.com
- new version 2.5.3
- for simutrans 120 and up
- detailed changes see http://forum.simutrans.com/index.php?topic=13975.0
* Wed May 20 2015 michiel.vanderwulp@gmail.com
- new version build on pak128 2.5.2+ nightly r1560, bugfixes
- for simutrans 120 and up
- the zip file does not contain a top dir simutrans any more like previous versions
* Tue Mar 17 2015 michiel.vanderwulp@gmail.com
- new version build on pak128 2.5.2 for simutrans 120 and up
* Sat Feb 15 2014 michiel.vanderwulp@gmail.com
- new version build on pak128 2.3.0 for simutrans 112.2 and up
* Thu Dec 27 2012 mailaender@opensuse.org
- initial package release (version 2.2.0)
