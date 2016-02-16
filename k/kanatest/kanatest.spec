# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xml2-config
# END SourceDeps(oneline)
Name:           kanatest
Version:        0.4.8
Release:        alt2_17
Summary:        Hiragana and Katakana drill tool

Group:          Games/Other
License:        GPLv2+
URL:            http://clayo.org/kanatest/
Source0:        http://clayo.org/kanatest/%{name}-%{version}.tar.gz

# Already fixed upstream, backported until new release is published
Patch1:         kanatest-0.4.8-gtkfixes.patch
# Format security patch
Patch2:		kanatest-0.4.8-format-security.patch


BuildRequires:  desktop-file-utils >= 0.9
BuildRequires:  gtk2-devel >= 2.0
BuildRequires:  libxml2-devel
BuildRequires:  gettext
Requires:       fontlang(ja)
Requires:       icon-theme-hicolor
Source44: import.info

%description
Kanatest is a simple, GTK 2-based kana drill tool. It offers three drill modes:
hiragana, katakana, and mixed mode. The tester shows random kana characters
and waits until you enter the romaji equivalent in an entry field. At the end,
statistics are provided

%prep
%setup -q
%patch1 -p1 -b gtkfixes
%patch2 -p1 -b .format

sed -i src/Makefile.in \
	-e 's|DISABLE_DEPRECATED|ENABLE_DEPRECATED|g'

%build
export PLATFORM_CFLAGS="$RPM_OPT_FLAGS -Werror-implicit-function-declaration"
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}


%files -f %{name}.lang
%doc README COPYING ChangeLog
%{_bindir}/kanatest
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/kanatest.png
%{_datadir}/icons/hicolor/16x16/apps/*
%{_datadir}/icons/hicolor/22x22/apps/*
%{_datadir}/icons/hicolor/24x24/apps/*
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/scalable/apps/*


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_15
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_8
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_7
- update to new release by fcimport

* Tue Aug 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_6
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_5
- initial release by fcimport

