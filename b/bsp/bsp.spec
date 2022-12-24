Group: Games/Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           bsp
Version:        5.2
Release:        alt2_31
Summary:        The most popular node builder for Doom

License:        GPLv2+
URL:            http://games.moria.org.uk/doom/bsp/
Source0:        http://games.moria.org.uk/doom/bsp/download/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
Patch0:         bsp-configure-c99.patch
Source44: import.info

%description
Before you can play a level that you have created, you must use a node
builder to create the data that Doom will use to render the level.
Doom uses a rendering algorithm based on a binary space partition,
otherwise known as a BSP tree. This is stored in a data lump called
NODES in the WAD file. This data structure must be pre-calculated and
stored in the WAD file before the level can be played; the tool that
does this is called a node builder.

BSP is one of several node builders that can do this. There are
others: idbsp is the original node builder that id Software used on
the original Doom levels, for instance. BSP was the best known and
most widely used node builder throughout the height of the Doom
editing craze in the mid 1990s.


%prep
%setup -q
iconv -f ISO_8859-2 -t UTF8 bsp.6 > bsp.6.tmp
mv bsp.6.tmp bsp.6
%patch0 -p1

%build
%configure
%make_build CFLAGS='%{optflags}' LIBS="-lm"


%install
install -D -p -m 755 bsp $RPM_BUILD_ROOT/%{_bindir}/bsp
install -D -p -m 644 bsp.6 $RPM_BUILD_ROOT/%{_mandir}/man6/bsp.6


%files
%doc AUTHORS ChangeLog INSTALL NEWS README visplane.txt test-wads/
%doc --no-dereference COPYING
%{_bindir}/bsp
%{_mandir}/man6/bsp.6*


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 5.2-alt2_31
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_26
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_21
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_7
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt2_6
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_6
- update to new release by fcimport

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 5.2-alt1_5
- converted from Fedora by srpmconvert script

