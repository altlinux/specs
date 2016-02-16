# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libSDL-devel perl(FileHandle.pm) perl(SDL/Rect.pm) perl(SDL/Surface.pm)
# END SourceDeps(oneline)
Name:           nazghul
Version:        0.7.1
Release:        alt2_16.20120228gitb0a402a
Summary:        A computer role-playing game (CRPG) engine

License:        GPLv2+
URL:            http://sourceforge.net/projects/nazghul/
Group:          Games/Other

# Occasionally upstream names things with an underscore.
%global         version_us %(echo %{version} | sed -e 's/\\./_/g')

#Source0:        nazghul-20120228gitb0a402a.txz

# Construct cvs checkout tarball with:
#  ./nazghul-make-snapshot %%{cvsdate}
Source0:        nazghul-20120228gitb0a402a.txz
Source1:        haxima-music-license
Patch0:         nazghul-desktop.patch
Patch1:         nazghul-format-security.patch
Patch2:         nazghul-armbuild.patch

# For building from a CVS snapshot
BuildRequires:  automake, autoconf
BuildRequires:  libSDL_image-devel, libSDL_mixer-devel, desktop-file-utils
BuildRequires:  libpng-devel, xcftools
Source44: import.info

%description
Nazghul is an old-school RPG engine modeled after those made in the
heyday of top-down, 2d tile-based graphics. It is specifically modeled
after Ultima V.


%package -n haxima
Summary:        A full-featured role-playing game for the Nazghul engine
# The music files installed in /usr/share/nazghul/haxima/music have been
# relicensed as CC-BY-SA (specifically version 2).   See the
# haxima-music-license file for details. The rest of the package is GPLv2+.
License:        GPLv2+ and CC-BY-SA
Group:          Games/Other
Requires:       nazghul = %{version}
Provides:       nazghul-haxima = %{version}-%{release}
Obsoletes:      nazghul-haxima < 0.6.0-8

%description -n haxima
A complete, playable and full-featured role playing game which runs
under the Nazghul CRPG engine.

You must install Nazghul in order to play Haxima.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# clean up CVS directories left in the source tarball
find . -depth -type d -name CVS -exec rm -rf {} \;

# Fix line endings
sed -i -e 's/\r//' doc/engine_extension_and_design/my_TODO.2004.05.05.txt

mv doc/* .

cp %SOURCE1 .


%build
./autogen.sh
%configure
make %{?_smp_mflags}

# Want a 256x256 icon, so generate one from the existing .xcf file
pushd icons
xcf2png haxima.xcf > haxima.png


%install
make install DESTDIR=%{buildroot}

mv %{buildroot}/%{_bindir}/haxima.sh %{buildroot}/%{_bindir}/haxima

desktop-file-install \
    --dir %{buildroot}/%{_datadir}/applications \
    haxima.desktop

install -D -m 644 icons/haxima.png %{buildroot}/%{_datadir}/pixmaps/haxima.png

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/haxima.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/nazghul/support-requests/5/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">haxima.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Top view 2D role playing game</summary>
  <description>
    <p>
      Haxima is a 2D role playing game (RPG) that runs on the Nazghul engine.
      You start out as a defenseless wanderer, you have to equip yourself,
      learn spells, and travel the land completing quests.
    </p>
  </description>
  <url type="homepage">http://myweb.cableone.net/gmcnutt/nazghul.html</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/haxima/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/haxima/b.png</screenshot>
  </screenshots>
</application>
EOF

%files
%{_bindir}/nazghul
%dir %{_datadir}/nazghul
%doc AUTHORS ChangeLog COPYING NEWS GAME_RULES GHULSCRIPT
%doc MAP_HACKERS_GUIDE engine_extension_and_design world_building


%files -n haxima
%{_bindir}/haxima
%{_datadir}/nazghul/haxima
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*haxima.desktop
%{_datadir}/pixmaps/haxima.png
%doc USERS_GUIDE haxima-music-license


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_16.20120228gitb0a402a
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_14.20120228gitb0a402a
- update to new release by fcimport

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_5.20120228gitb0a402a
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_4.20120228gitb0a402a
- update to new release by fcimport

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt2_3.20120228gitb0a402a.1
- Rebuilt with libpng15

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_3.20120228gitb0a402a
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_2.20120228gitb0a402a
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_1.20120104cvs
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_1.20120104cvs
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_4.20120104cvs
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_3.20100413cvs
- update to new release by fcimport

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_2.20100413cvs
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_2.20100413cvs
- converted from Fedora by srpmconvert script

