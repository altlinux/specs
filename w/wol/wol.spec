Summary: The Wake On Lan client
Name: wol
Version: 0.7.1
Release: alt4
License: GPL-2.0
Group: Networking/Other
Url: http://ahh.sf.net/wol/
Packager: Mikhail Pokidko <pma@altlinux.ru>
Source: %name-%version.tar
Patch0: 0001-Throw-out-obsolete-AC_HEADER_STDC.patch
Patch1: 0002-Fix-config.h-test-consumption.patch
Patch2: 0003-Fix-malloc-detection.patch
Patch3: 0004-Fix-xmalloc.patch

BuildRequires: perl-podlators
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
wol is the Wake On Lan client. It wakes up magic packet compliant machines
such as boxes with wake-on-lan ethernet-cards. Some workstations provides
SecureON which extends wake-on-lan with a password. This feature is also
provided by wol.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure \ --with-gnu-ld
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
* Wed Jan 22 2025 Ulysses Apokin <ulysses@altlinux.org> 0.7.1-alt4
- Fix FTBFS.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt3.1
- NMU: added BR: texinfo

* Tue Mar 01 2011 Timur Aitov <timonbl4@altlinux.org> 0.7.1-alt3
- Fixed build man page

* Tue Nov 24 2009 Mikhail Pokidko <pma@altlinux.org> 0.7.1-alt2
- Fixed info files.

* Tue Feb 06 2007 Mikhail Pokidko <pma@altlinux.ru> 0.7.1-alt1
- 1st build
