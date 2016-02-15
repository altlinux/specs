# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
Name:           alphabet-soup
Version:        1.1
Release:        alt2_16
Summary:        Guide your worm through the soup to spell words
Group:          Games/Other
License:        Crystal Stacker
URL:            http://www.t3-i.com/asoup.htm
Source0:        http://www.t3-i.com/ncdgames/as11src.zip
Source1:        alphabet-soup.desktop
Source2:        alphabet-soup.png
Patch0:         alphabet-soup-1.1-linux.patch
Patch1:         alphabet-soup-1.1-rhbz699425.patch
BuildRequires:  alfont-devel dumb-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Guide your worm through the soup to spell words and earn points. Play the way
you like with several game mode selections. Words are chosen from one of three
included dictionaries, or import your own.

%prep
%setup -q -c
%patch0 -p1 -z .unix
%patch1 -p1
sed -i 's/\r//' readme.txt

%build
make %{?_smp_mflags} -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations"

%install
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

%files
%doc readme.txt license-change.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_15
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_11
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_9
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_9
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_7
- initial release by fcimport

