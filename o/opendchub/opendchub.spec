Name: opendchub
Version: 0.8.2
Release: alt1.1

Summary: Direct Connect Hub

License: GPL
Group: System/Servers
Url: http://opendchub.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/opendchub/%name-%version.tar
Source1: %name.init
Patch0: %name-bufoverflow.patch
Patch1: %name-no_nsl.patch

# Automatically added by buildreq on Mon Oct 17 2011
BuildRequires: libcap-devel libssl-devel perl-devel

%description
Opendchub is a hub of direct connect file sharing network.

%prep
%setup
#patch0 -p1
#patch1 -p1

%build
%autoreconf
%configure --enable-switch_user

%make_build

%install
%makeinstall_std

#install -d %buildroot%_sysconfdir/opendchub
#install -D %SOURCE1 %buildroot%_initdir/%name

#%pre
#%groupadd -g 190 opendchub
#%useradd -u 190 -d %_sysconfdir/opendchub -s /bin/false -c "Open DC Hub" -g opendchub opendchub

%files
%doc AUTHORS ChangeLog NEWS README Documentation/* Samplescripts
%_bindir/*
#%_initdir/opendchub
#%dir %attr(750,opendchub,opendchub) %_sysconfdir/opendchub

%changelog
* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 0.8.2-alt1.1
- rebuilt for pelr-5.14

* Sun May 08 2011 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script) (ALT bug #24785)

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7.15-alt1.1
- rebuilt with perl 5.12

* Sat Aug 04 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.15-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
