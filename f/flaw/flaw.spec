# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate /usr/bin/glib-gettextize gcc-c++ libICE-devel libSM-devel
# END SourceDeps(oneline)
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name flaw
%define version 1.3.2a
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		flaw
Version:	1.3.2a
Release:	alt2_13
Summary:	Free top-down wizard battle game
Group:		Games/Other
License:	GPLv3+
URL:		http://flaw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		flaw-aarch64.patch

BuildRequires:	libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libSDL-devel fonts-ttf-gnu-freefont-serif 
BuildRequires:	libSDL_gfx-devel desktop-file-utils fonts-ttf-gnu-freefont-sans gettext intltool
Requires:	fonts-ttf-gnu-freefont-sans fonts-ttf-gnu-freefont-serif
Source44: import.info

%description
FLAW is a free top-down wizard battle game.
It can be played by up to 5 players simultaneously. The goal of the game is to
survive as long as possible while more and more fireballs appear in the arena.
Game play is simple and self-explanatory. It's all about evading the fireballs
and knocking your opponents down. In addition there are collectible magic gems
that provide special abilities.

%prep
%setup -q
#patch to build on aarch64, upstream notified to use autoconf 2.69
%patch0 -p 1

# Fix spurious executable permissions
chmod 644 src/*.cc
chmod 644 src/*.h

# Remove deprecated tag Enconding from flaw.desktop
sed -i -e '2d' data/flaw.desktop

%build
%configure --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

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
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/flaw/feature-requests/3/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">flaw.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Casual Wizards Battle Game</summary>
  <description>
    <p>
      Flaw is a game where you control a wizard and your goal is to survive as
      much as you can.
    </p>
    <p>
      In addition to the fireballs that arise increasingly in larger quantities,
      there are other wizards trying to kill you.
    </p>
    <p>
      The game has some items that give you special abilities to defend yourself or attack your enemies.
    </p>
    <p>
      Flaw can be played on single-player mode or with your friends.
    </p>
  </description>
  <url type="homepage">http://flaw.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://flaw.sourceforge.net/images/ingame1.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/ingame3.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/ingame2.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/menu.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%{_bindir}/flaw
%{_datadir}/flaw
%{_datadir}/pixmaps/flaw.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/flaw.desktop
%exclude %{_docdir}/%{name}/INSTALL
%doc %{_docdir}/%{name}

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt2_12
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt2_10
- update to new release by fcimport

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt2_9
- rebuild with new SDL

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_8
- update to new release by fcimport

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_6
- update to new release by fcimport

* Tue Nov 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_4
- update to new release by fcimport

* Mon Jul 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_2
- update to new release by fcimport

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt3_5
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt3_4
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_4
- update to new release by fcimport

* Fri Oct 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_3
- bugfix release, close 33627 from ALTLinux Testers Team

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_3
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_2
- converted from Fedora by srpmconvert script

