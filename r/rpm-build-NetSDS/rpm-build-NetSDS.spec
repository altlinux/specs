%define netsds_name	NetSDS
%define netsds_version	0.0.2
%define netsds_release	alt3

Name:	 	rpm-build-%netsds_name
Version:	%netsds_version
Release:	%netsds_release
Summary: 	RPM helper macros to rebuild NetSDS packages
Url: http://www.netstyle.com.ua/

Group:		Development/Other
License:	GPL
BuildArch:	noarch
Source0:	rpm.macros.NetSDS

Packager:	Michael Bochkaryov <misha@altlinux.ru>

PreReq: rpm-macros-webserver-common

%description
These helper macros provide possibility to rebuild
NetSDS packages by some Alt Linux Team Policy compatible way.

%install
%__mkdir_p %buildroot/%_rpmmacrosdir
%__cp %SOURCE0 %buildroot/%_rpmmacrosdir/%netsds_name

%__subst 's,@netsds_name@,%netsds_name,'       %buildroot/%_rpmmacrosdir/%netsds_name
%__subst 's,@netsds_version@,%netsds_version,' %buildroot/%_rpmmacrosdir/%netsds_name
%__subst 's,@netsds_release@,%netsds_release,' %buildroot/%_rpmmacrosdir/%netsds_name

%files
%_rpmmacrosdir/%netsds_name

%changelog
* Mon Jul 06 2009 Michael Bochkaryov <misha@altlinux.ru> 0.0.2-alt3
- netsds user and group fixed
- Url tag added

* Sun Jul 05 2009 Michael Bochkaryov <misha@altlinux.ru> 0.0.2-alt2
- netsds_spooldir macros added

* Mon May 11 2009 Michael Bochkaryov <misha@altlinux.ru> 0.0.2-alt1
- Macros file corrected
- Added compatibility to web policy

* Tue Oct 21 2008 Grigory Milev <week@altlinux.ru> 0.0.1-alt1
- Initial build
