Summary: The Wake On Lan client
Name: wol
Version: 0.7.1
Release: alt3
License: GPL
Group: Networking/Other
Url: http://ahh.sf.net/wol/
Packager: Mikhail Pokidko <pma@altlinux.ru>
Source: %name-%version.tar.gz

BuildRequires: perl-podlators

%description
wol is the Wake On Lan client. It wakes up magic packet compliant machines
such as boxes with wake-on-lan ethernet-cards. Some workstations provides
SecureON which extends wake-on-lan with a password. This feature is also
provided by wol.

%prep
%setup

%build
%configure
%make %?_smp_mflags

%install
%makeinstall
%find_lang %name

#post
#%%/sbin/install-info %_infodir/%name.info.gz %_infodir/dir

#preun
#%%/sbin/install-info --delete %_infodir/%name.info.gz %_infodir/dir

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_infodir/*.info*
%_man1dir/*
%_bindir/*

%changelog
* Tue Mar 01 2011 Timur Aitov <timonbl4@altlinux.org> 0.7.1-alt3
- Fixed build man page

* Tue Nov 24 2009 Mikhail Pokidko <pma@altlinux.org> 0.7.1-alt2
- Fixed info files.

* Tue Feb 06 2007 Mikhail Pokidko <pma@altlinux.ru> 0.7.1-alt1
- 1st build

