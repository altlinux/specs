Group: Games/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ninvaders
Version:        0.1.1
Release:        alt3_20
Summary:        Space Invaders clone written in ncurses for cli gaming
License:        GPLv2+
URL:            http://ninvaders.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         ninvaders-0.1.1-fedora.patch
BuildRequires:  gcc
BuildRequires:  libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
Source44: import.info

%description
Ever wanted to place space invaders when you can't find a GUI? Now you can!
ninvaders is a ncurses based space invaders clone to play from the command
line.

%prep
%setup -q
%patch0 -p0
iconv -f iso-8859-1 -t utf8 ChangeLog > ChangeLog.new && \
touch -r ChangeLog ChangeLog.new && mv ChangeLog.new ChangeLog
sed -i 's|-lncurses|-lncurses -Wl,--allow-multiple-definition|' Makefile

%build
%make_build

%install
install -Dp -m0755 nInvaders %{buildroot}%{_bindir}/nInvaders

%files
%doc ChangeLog README gpl.txt
%{_bindir}/nInvaders

%changelog
* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.1.1-alt3_20
- update to new release by fcimport

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt3_16
- fixed build with gcc10

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_16
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_14
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_6
- update to new release by fcimport

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_5
- converted from Fedora by srpmconvert script

