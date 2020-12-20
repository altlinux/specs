%define srcname tpc

Name: TurionPowerControl
Version: 0.44
Release: alt1.rc2p

Summary: AMD K10/K11 P-State, frequency and voltage modification utility
License: The modified BSD license
Group: System/Configuration/Hardware
URL: http://turionpowercontrol.googlecode.com/
VCS: https://github.com/turionpowercontrol/tpc.git
Source: %name-%version.tar
Source1: TurionPowerControl.conf
Source2: %srcname.cfg
Source3: %srcname.service
Patch0: tpc-0.44-nbfid-cfg.patch
Patch1: tpc-0.44-remove-MSVC_Round.patch

BuildRequires: gcc-c++ libncurses-devel
ExclusiveArch: %ix86 x86_64

%description
TurionPowerControl is a command line tool that allows users to tweak AMD K10/K11 processors parameters.
TurionPowerControl, despite its name, allows to view and control many parameters of modern AMD processors.
It can manipulate power states, frequencies, DRAM timings, power settings and can report temperatures, monitor pstate changes and precise cpu usage.
It is available for Windows and Linux, for both 32 bit and 64 bit architectures and fully supports multiprocessor machines.
Currently supported processors are:
- Family 10h: All Phenom, Phenom II, Athlon II, Turion Mxxx and Pxxx processors
- Family 11h: Turion ZM/RM and Athlon QL processors
- Family 12h: Llano A-series processors (partial and experimental support), beginning from version 0.41
- Family 14h: Ontario C-series, Zacate E-series processors (partial and experimental support), beginning from version 0.41
- Family 15h: Bulldozer platform (FX Series, Interlagos and Valencia server platforms)

%prep
%setup -n %name-%version
%patch0 -p2
%patch1 -p2

%build
%make_build

%install
install -D -m755 %name %buildroot%_sbindir/%name
install -D -m644 %{S:1} %buildroot%_modulesloaddir/%name.conf
install -D -m644 %{S:2} .
install -D -m644 %{S:3} %buildroot%_unitdir/%srcname.service
ln -s %name %buildroot%_sbindir/%srcname

%post
modprobe cpuid ||:
modprobe msr ||:

%files
%doc doc
%doc %srcname.cfg
%_sbindir/%name
%_sbindir/tpc
%_modulesloaddir/%name.conf
%_unitdir/%srcname.service

%changelog
* Sun Dec 20 2020 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1.rc2p
- upstream tip (0.44 rc2+)

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1.rc2
- new version

* Wed Apr 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.43-alt0.1
- updated version

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.42.2-alt0.2
- bugfix release

* Mon Feb 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.42.2-alt0.1
- updated version
- TODO: config file
- TODO: support daemon mode with init and /etc/sysconfig/tpc

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.41-alt0.2
- first build for Sisyphus
- TODO: config file
- TODO: support daemon mode with init and /etc/sysconfig/tpc
