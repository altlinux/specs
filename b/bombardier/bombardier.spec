Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: bombardier
Version: 0.8.3
Release: alt1_22
Summary: The GNU Bombing utility

License: GPL-2.0-or-later        
URL: http://packages.debian.org/stable/source/bombardier
Source0: http://http.debian.net/debian/pool/main/b/bombardier/bombardier_0.8.3+nmu3.tar.xz
Source1: bombardier.desktop
Source2: bombardier-logo.png
Patch0: bombardier-height.patch
Patch1: bombardier-0.8.2-string-format.patch
Patch2: format.patch
BuildRequires: libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel, desktop-file-utils, gcc
Requires: icon-theme-hicolor
Source44: import.info


%description
Fly an ncurses plane over an ncurses city, and try to level the buildings.

%prep


%setup -qn bombardier-0.8.3+nmu3

%patch0 -p0
%patch1 -p0
%patch2 -p0

# link with --as-needed
sed -i -e 's,$(LDFLAGS) -o $@ $(OBJS),-o $@ $(OBJS) $(LDFLAGS),' Makefile

%build
make CFLAGS="$RPM_OPT_FLAGS"


%install
install -pD -m 755 bombardier %{buildroot}%{_bindir}/bombardier
install -pD -m 644 bombardier.6 %{buildroot}%{_mandir}/man6/bombardier.6

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install            \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps


%files
%{_bindir}/bombardier
%doc --no-dereference COPYING
%doc README DEDICATION VERSION
%{_datadir}/applications/bombardier.desktop
%{_datadir}/icons/hicolor/32x32/apps/bombardier-logo.png
%{_mandir}/man6/bombardier.6*


%changelog
* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 0.8.3-alt1_22
- update to new release by fcimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_16
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_13
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_9
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_19
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_18
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_17
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_15
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_13
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt1_12
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt1_11
- initial release by fcimport

