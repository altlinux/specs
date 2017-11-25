# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gittag v2.15
%global gitowner axel-download-accelerator

Name: axel
Version: 2.15
Release: alt1_1
Summary: Light command line download accelerator for Linux and Unix

Group: Networking/WWW
License: GPLv2+
URL: https://github.com/%{gitowner}/%{name}
Source0: https://github.com/%{gitowner}/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
BuildRequires: gettext-tools libasprintf-devel
BuildRequires: pkgconfig(libssl)
BuildRequires: autoconf
BuildRequires: automake
Source44: import.info

%description
Axel tries to accelerate HTTP/FTP downloading process by using
multiple connections for one file. It can use multiple mirrors for a
download. Axel has no dependencies and is lightweight, so it might
be useful as a wget clone on byte-critical systems.

%prep
%setup -q -n %{name}-%{version}


%build
./autogen.sh
%{configure}
%make_build


%install
make install \
DESTDIR=%{buildroot}

install -m 755 -p src/%{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 -p -T doc/axelrc.example %{buildroot}%{_sysconfdir}/axelrc

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%doc ChangeLog CREDITS AUTHORS README.md doc/API
%doc COPYING
%config(noreplace) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*


%changelog
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

