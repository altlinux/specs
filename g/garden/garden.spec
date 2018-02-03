# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           garden
Version:        1.0.9
Release:        alt1_5
Summary:        An innovative old-school 2D vertical shoot-em-up

Group:          Games/Other
License:        GPLv3+
URL:            http://garden.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
#Patch0:         garden-dso.patch
#Patch1:         garden-printf-format.patch
Patch2:         garden-1.0.8-inline.patch

BuildRequires:  liballegro-devel
BuildRequires:  desktop-file-utils
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
Requires:       liballegro4.4
Source44: import.info

%description
Garden of colored lights is an old school 2D vertical shoot-em-up with some
innovative elements. Innovative graphics, soundtrack and game concept. The
game itself is very challenging and as you progress, you will understand that
you are dealing with a true piece of art...

%prep
%setup -q

# patch for DSO-linking
# https://sourceforge.net/tracker/?func=detail&aid=2982590&group_id=242667&atid=1121672
#%%patch0 -p1 -b .dso
#%%patch1 -p0 -b .format
%patch2 -p1

%build
autoreconf -if
%configure 
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Tim Waugh <twaugh@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/garden/feature-requests/4/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">garden.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Choose your equipment and fly your ship past the enemies</summary>
  <description>
    <p>
      In garden of coloured lights you must fly as far as you can while enemies
      attack.
      You choose how to equip the ship, depending on your strategy.
    </p>
    <p>
      The futuristic landscape scrolls upwards while strange plant-like enemies
      engage your ship in various ways.
      There are boss enemies to kill in each stage.
    </p>
  </description>
  <url type="homepage">http://garden.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://garden.sourceforge.net/drupal/sites/default/files/images/stage1_1.png</screenshot>
    <screenshot>http://garden.sourceforge.net/drupal/sites/default/files/images/stage1_2.png</screenshot>
    <screenshot>http://garden.sourceforge.net/drupal/sites/default/files/images/stage0_0.png</screenshot>
  </screenshots>
</application>
EOF

desktop-file-validate \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README NEWS AUTHORS ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_5
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_2
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_15
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_11
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_6
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_5
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_5
- update to new release by fcimport

* Mon Oct 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_4
- update to new release by fcimport

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_3
- initial release by fcimport

