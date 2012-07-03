%define srcname tpc

Name: TurionPowerControl
Version: 0.42.2
Release: alt0.1

Summary: Utility to tweak AMD processors parameters
License: BSD like
Group: System/Configuration/Hardware
URL: http://code.google.com/p/turionpowercontrol/downloads/list
#Url: http://http://amdath800.dyndns.org/amd/

Source: http://amdath800.dyndns.org/amd/tpc/tpc-0.422.tar.gz
Source1: tpc.init

BuildRequires: gcc-c++

%description
TurionPowerControl is a nice command line tool 
that allows users to tweak AMD processors parameters.

%prep
%setup -c

%build
cd src
%make_build

%install
install -D -m644 src/%name %buildroot%_sbindir/%name
install -D -m755 %{S:1} %buildroot%_initdir/tpc

%post
modprobe cpuid ||:
modprobe msr ||:
%post_service tpc

%preun
%preun_service tpc

%files
%doc doc
%doc bin/Ubuntu-x86_64/example.cfg
%_sbindir/%name
%_initdir/tpc

%changelog
* Mon Feb 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.42.2-alt0.1
- updated version
- TODO: config file
- TODO: support daemon mode with init and /etc/sysconfig/tpc

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.41-alt0.2
- first build for Sisyphus
- TODO: config file
- TODO: support daemon mode with init and /etc/sysconfig/tpc
