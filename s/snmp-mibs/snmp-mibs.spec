%define mibsdir %_datadir/mibs
%define pibsdir %_datadir/pibs

Name: snmp-mibs
Version: 0.3
Release: alt3

Summary: MIB files
License: BSD-style
Group: Networking/Other
BuildArch: noarch
URL: http://git.altlinux.org/people/shaba/packages/snmp-mibs.git

Packager: Alexey Shabalin <shaba@altlinux.ru>

Source0: ietf-mibs.tar
Source1: iana-mibs.tar
Source2: irtf-mibs.tar
Source3: tubs-mibs.tar
Source4: ietf-pibs.tar
Source5: tubs-pibs.tar
Source6: cisco-mibs.tar
Source7: doc-mibrfcs.tar
Source8: net-snmp-mibs.tar
Source9: raritan-mibs.tar

%package std
Summary: Standard MIB files 
Group: Networking/Other
BuildArch: noarch
Provides: snmp-mibs net-snmp-mibs
Obsoletes: net-snmp-mibs

%package ext
Summary: Extended MIB and PIB files
Group: Networking/Other
BuildArch: noarch

%package doc-mibrfcs
Summary: RFC doc of MIB files 
Group: Networking/Other
BuildArch: noarch

%package cisco
Summary: Cisco MIB files
Group: Networking/Other
BuildArch: noarch

%package raritan
Summary: Raritan MIB files
Group: Networking/Other
BuildArch: noarch

%description
MIB files. May be used with other packages (libsmi,net-snmp, for example)

%description std
This package contains standard MIB files:
 o IETF - standard MIBS for SNMP, SNMPv2, interfaces, IP,.
 o IANA - standard identifiers for protocols, ifType, etc.

%description ext
This package contains Extended MIB files:
 o IRTF - SMIng oids, extensions, types.
 o TUBS - MIBS for the Technical University of Braunschweig

%description doc-mibrfcs
RFC doc of MIB files.

%description cisco
This package contains Cisco MIB files

%description raritan
This package contains Raritan MIB files

%prep
%setup -q -c -b0 -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8 -b9

%build

%install
mkdir -p %buildroot%mibsdir
mkdir -p %buildroot%mibsdir/site
mkdir -p %buildroot%pibsdir
mkdir -p %buildroot%pibsdir/site

cp -pr ietf-mibs/ietf %buildroot%mibsdir/
cp -pr iana-mibs/iana %buildroot%mibsdir/
cp -pr irtf-mibs/irtf %buildroot%mibsdir/
cp -pr tubs-mibs/tubs %buildroot%mibsdir/
cp -pr net-snmp-mibs/net-snmp %buildroot%mibsdir/
cp -pr cisco-mibs/cisco %buildroot%mibsdir/
cp -pr raritan-mibs/raritan %buildroot%mibsdir/

cp -pr ietf-pibs/ietf %buildroot%pibsdir/
cp -pr tubs-pibs/tubs %buildroot%pibsdir/
gzip doc-mibrfcs/mibrfcs/*

%files std
%dir %mibsdir
%dir %mibsdir/iana
%dir %mibsdir/ietf
%dir %mibsdir/net-snmp
%dir %mibsdir/site
%mibsdir/iana/*
%mibsdir/ietf/*
%mibsdir/net-snmp/*

%files ext
%dir %mibsdir/irtf
%dir %mibsdir/tubs
%mibsdir/irtf/*
%mibsdir/tubs/*
%dir %pibsdir
%dir %pibsdir/ietf
%dir %pibsdir/site
%dir %pibsdir/tubs
%pibsdir/ietf/*
%pibsdir/tubs/*

%files doc-mibrfcs
%doc doc-mibrfcs/mibrfcs/*

%files cisco
%dir %mibsdir/cisco
%mibsdir/cisco/*

%files raritan
%dir %mibsdir/raritan
%mibsdir/raritan/*

%changelog
* Wed Dec 21 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3-alt3
- Update net-snmp-mibs from new net-snmp

* Thu Sep 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.3-alt2
- Update net-snmp-mibs from new net-snmp

* Mon Mar 29 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- add MIBs from Raritan

* Thu Mar 18 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt2
- Add Obsoletes and Provides for net-snmp-mibs in std subpackage

* Wed Mar 10 2010 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- add MIBs from Net-SNMP project to std package (ALT #23076)

* Fri Feb 26 2010 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- Initial build for Sisyphus.
