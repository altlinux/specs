# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           overgod
Version:        1.0
Release:        alt2_28
Summary:        Another arcade-style shoot-em-up
Group:          Games/Other
License:        GPLv2+
URL:            http://www.allegro.cc/depot/Overgod
Source0:        http://downloads.sourceforge.net/overgod/overgod.tar.gz
Source1:        overgod.desktop
Source2:        overgod.png
Source3:        overgod.appdata.xml
Patch0:         overgod-1.0.patch
Patch1:         overgod-1.0-format-string.patch
Patch2:         overgod-1.0-shield_bmp_array_overrun.patch
Patch3:         overgod-1.0-inline-use-fix.patch
BuildRequires:  liballegro-devel desktop-file-utils libappstream-glib
Requires:       icon-theme-hicolor
Source44: import.info

%description
For too long has humanity been ruled by cruel and disputatious gods!
Fly through the various layers of the Celestial Oversphere to unseat
those who control the universe.

In Overgod you control a little vehicle in the middle of the screen and fly
around and shoot things - a bit like asteroids, but the asteroids move
independently and shoot back. You can also upgrade your vehicle in various
ways.


%prep
%setup -q
%patch0 -p1 -z .unix
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's/\r//' readme.txt licence.txt

# as-needed
sed -i -e 's,$(CC) $(LDFLAGS) -o $@ $^,$(CC) -o $@ $^ $(LDFLAGS),' Makefile


%build
%make_build \
  CFLAGS="$RPM_OPT_FLAGS -Wno-unused-but-set-variable" PREFIX=%{_prefix}


%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc readme.txt licence.txt
%{_bindir}/overgod
%{_datadir}/overgod
%{_datadir}/appdata/overgod.appdata.xml
%{_datadir}/applications/overgod.desktop
%{_datadir}/icons/hicolor/48x48/apps/overgod.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_28
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_27
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_25
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_24
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_23
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_21
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_18
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_17
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_16
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_15
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_14
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_14
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_13
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_12
- initial release by fcimport

