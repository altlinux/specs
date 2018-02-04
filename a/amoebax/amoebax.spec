# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           amoebax
Version:        0.2.1
Release:        alt1_13
Summary:        Action-Puzzle Game
Group:          Games/Other
License:        GPLv2+ and Free Art
URL:            http://www.emma-soft.com/games/amoebax/
Source0:        http://www.emma-soft.com/games/amoebax/download/amoebax-%{version}.tar.bz2
Patch0:         amoebax-0.2.0-gcc43.patch
BuildRequires:  libSDL_mixer-devel libSDL_image-devel zlib-devel libpng-devel
BuildRequires:  libvorbis-devel doxygen desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Amoebax is a cute and addictive action-puzzle game. Due an awful mutation,
some amoeba's species have started to multiply until they take the world if
you can't stop them. Fortunately the mutation made then too unstable and
lining up four or more will make them disappear.

Follow Kim or Tom through 6 levels in their quest to prevent the cute
multiplying amoebas to take the world and become the new Amoeba Master. Watch
out for the cute but amoeba's controlled creatures that will try to put and
end to your quest.

Amoebax is designed with levels for everyone, from children to adults. With
the training mode everybody will quickly become a master and the tournament
mode will let you have a good time with your friends. There is also catchy
music, funny sound effects, and beautiful screens that sure appeal to everyone
in the family.


%prep
%setup -q
%patch0 -p1


%build
%configure
%make_build


%install
%makeinstall_std

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
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress:  jordi@emma-soft.com
SentUpstream:  2014-09-17
-->
<application>
  <id type="desktop">amoebax.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A match-4 action puzzle game</summary>
  <description>
    <p>
      Amoebax is a cute action puzzle game where pairs of amoeba fall down,
      and when you match 4 colored amoeba in a row or column they disappear.
      There are 6 levels of difficulty, and also a split-screen mode to battle
      the amoeba-matching fun with a friend.
    </p>
  </description>
  <url type="homepage">http://www.emma-soft.com/games/amoebax/</url>
  <screenshots>
    <screenshot type="default">http://www.emma-soft.com/games/amoebax/screenshots/training.png</screenshot>
    <screenshot>http://www.emma-soft.com/games/amoebax/screenshots/normal.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

rm $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/manual.pdf

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
%if 0%{?fedora} && 0%{?fedora} < 19
   --delete-original \
%endif
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps


%files
%doc AUTHORS COPYING* NEWS README* THANKS TODO doc/manual.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_10
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_8
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_3
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_2
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_1
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_10
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt5_8
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt4_7
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3_7
- rebuild with new rpm desktop cleaner

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_7
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_7
- converted from Fedora by srpmconvert script

