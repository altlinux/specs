%define srcname tpc

Name: TurionPowerControl
Version: 0.44
Release: alt1.rc2

Summary: Utility to tweak AMD processors parameters
License: BSD like
Group: System/Configuration/Hardware
URL: http://code.google.com/p/turionpowercontrol/downloads/list

Source: http://turionpowercontrol.googlecode.com/files/tpc-0.44-rc2.tar.gz
Source1: TurionPowerControl.conf

BuildRequires: gcc-c++ libncurses-devel

%description
TurionPowerControl is a nice command line tool 
that allows users to tweak AMD processors parameters.

%prep
%setup -n %srcname-%version-rc2

%build
cd src
%make_build

%install
cd src
install -D -m755 %name %buildroot%_sbindir/%name
install -D -m755 %{S:1} %buildroot%_modulesloaddir/%name.conf

%post
modprobe cpuid ||:
modprobe msr ||:

%files
%doc doc
%doc bin/Ubuntu-amd64/example.cfg
%_sbindir/%name
%_modulesloaddir/%name.conf

%changelog
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
