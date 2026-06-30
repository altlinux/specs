Group: Networking/WWW
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 3

%global forgeurl https://github.com/axel-download-accelerator/axel

Name:       axel
Version:    2.17.14
Release:    alt1_4
Summary:    Light command line download accelerator for Linux and Unix

# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/axel-download-accelerator/axel
%global forgesource https://github.com/axel-download-accelerator/axel/archive/2.17.14/axel-2.17.14.tar.gz
%global archivename axel-2.17.14
%global archiveext tar.gz
%global archiveurl https://github.com/axel-download-accelerator/axel/archive/2.17.14/axel-2.17.14.tar.gz
%global topdir axel-2.17.14
%global extractdir axel-2.17.14
%global repo axel
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 2.17.14
#global date %nil
#global distprefix %nil
# FedoraForgeMeta2ALT: end generated meta

# spdx
License:    GPL-2.0-or-later
URL:        %forgeurl
Source0:    %forgesource
BuildRequires: gettext-tools libasprintf-devel
BuildRequires: pkgconfig(libssl)
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: txt2man
BuildRequires: automake
BuildRequires: gcc
Source44: import.info

%description
Axel tries to accelerate HTTP/FTP downloading process by using
multiple connections for one file. It can use multiple mirrors for a
download. Axel has no dependencies and is lightweight, so it might
be useful as a wget clone on byte-critical systems.

%prep
%setup -q -n axel-2.17.14

%build
autopoint -f
%autoreconf -I m4 -I %_datadir/gettext/m4
%{configure}
%make_build


%install
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 -p -T doc/axelrc.example %{buildroot}%{_sysconfdir}/axelrc

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%doc ChangeLog README.md doc/API
%doc --no-dereference COPYING
%config(noreplace) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*


%changelog
* Tue Jun 30 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.17.14-alt1_4
- NMU: fix FTBFS with gettext 1.0

* Fri Aug 01 2025 Igor Vlasenko <viy@altlinux.org> 2.17.14-alt1_3
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 2.17.11-alt1_2
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 2.17.10-alt1_3
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 2.17.10-alt1_1
- update to new release by fcimport

* Thu Nov 22 2018 Grigory Ustinov <grenka@altlinux.org> 2.16.1-alt1
- Build new version.
- Cleanup spec.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.16-alt1_1.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.16-alt1_1
- update to new release by fcimport

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1_1
- new version

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.13.1-alt1_2
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_6
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_5
- initial release by fcimport

