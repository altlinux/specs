Name: cpuinfo
Version: 0.5.2
Release: alt3.qa1
Summary: Applet for CPU temperature and frequency
Summary(ru_RU.UTF8): Апплет для частоты и температуры CPU
Summary(uk_UA.UTF8): Аплет для частоти та температури CPU
Source: %name-%version.tar
Url: http://kde-apps.org/content/show.php?content=35035
Group: Monitoring
License: %gpl2plus
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ kdelibs-devel libXt-devel libdnet-devel
BuildRequires: libjpeg-devel libpng-devel xml-utils xorg-cf-files
BuildRequires: libtqt-devel

%description
This applet shows the current CPU temperature and frequency.
Make sure you have enabled the temperature ACPI kernel module
(thermal.ko).

%description -l ru_RU.UTF8
Этот апплет показывает текущую температуру и частоту CPU.
Убедитесь, что у вас работает температурный ACPI-модуль ядра
(thermal.ko).

%description -l uk_UA.UTF8
Цей аплет показує поточну температуру і частоту CPU.
Переконайтеся, що у вас працює температурний ACPI-модуль ядра
(thermal.ko).


%prep
%setup
%patch -p1


%build
make -f admin/Makefile.common
%K3configure \
	--disable-rpath \
	--without-arts \
	--with-gnu-ld
%make_build CXXFLAGS="-I%_includedir/tqtinterface"


%install
%K3install
%K3find_lang %name --with-kde


%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%_libdir/kde3/*.so
%_K3apps/kicker/applets/*


%changelog
* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt3.qa1
- Adapt to new KDE3 placement

* Sun Jan 23 2011 Michael Shigorin <mike@altlinux.org> 0.5.2-alt3
- fixed FTBFS with kde 3.5.12

* Mon Dec 20 2010 Michael Shigorin <mike@altlinux.org> 0.5.2-alt2
- rebuilt for Sisyphus

* Fri Dec 17 2010 Led <led@altlinux.ru> 0.5.2-tmc7
- add support 'atk0110' into Linux kernel hwmon subsystem for CPUs
- fix build with g++ 4.5

* Tue Nov 02 2010 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- rebuilt for Sisyphus

* Mon Nov 01 2010 Led <led@altlinux.ru> 0.5.2-tmc6
- removed space before degree symbol

* Mon Nov 01 2010 Led <led@altlinux.ru> 0.5.2-tmc5
- move SysFreqSrc::createInstances() upward

* Fri Oct 29 2010 Led <led@altlinux.ru> 0.5.2-tmc4
- fix: added creating SysHWMonSrc instances

* Fri Oct 29 2010 Led <led@altlinux.ru> 0.5.2-tmc3
- sources: add Linux kernel hwmon subsystem (k8temp, k10temp, coretemp) for CPUs

* Thu Oct 28 2010 Led <led@altlinux.ru> 0.5.2-tmc2
- cleaned up BuildRequires

* Thu Oct 28 2010 Led <led@altlinux.ru> 0.5.2-tmc1
- cpufreqd: cosmetic fixes

* Thu Oct 28 2010 Led <led@altlinux.ru> 0.5.2-tmc0
- 0.5.2

* Thu Oct 28 2010 Led <led@altlinux.ru> 0.5-tmc0
- 0.5

* Thu Oct 28 2010 Led <led@altlinux.ru> 0.4.3-tmc1
- 0.4.3

* Thu Oct 28 2010 Led <led@altlinux.ru> 0.4-tmc0
- 0.4

* Thu Oct 28 2010 Led <led@altlinux.ru> 0.3-tmc1
- cpuinfo.desktop: add ru and uk Comment, clean ups

* Wed Oct 27 2010 Led <led@altlinux.ru> 0.3-tmc0
- fixed License
- cleaned up spec
- cleaned up %%files
- added proper ChangeLog
- cleaned up description
- added uk description

* Mon Mar 22 2010 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1.5
- fix build with autoconf-2.64

* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1.4
- fixed russian locale for Summary

* Wed Oct 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1.3
- added russian description and summary (fixed #22071). Thanks to Phantom.

* Mon May 25 2009 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1.2
- fix for automake-1.11

* Tue Dec 25 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1.1
- fix for autotools-2.6 (thanks to wRAR for hints again)

* Tue Oct 23 2007 Motsyo Gennadi <drool@altlinux.ru> 0.3-alt1
- initial build for ALT Linux
