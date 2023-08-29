Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-gettextize pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           gweled
Version:        0.9.1
Release:        alt2_32.20130730git819bed

Summary:        Swapping gem game

License:        GPL-2.0-or-later
URL:            http://launchpad.net/gweled
#Source0:        http://launchpad.net/gweled/trunk/0.9/+download/gweled-%%{version}.tar.gz
#Fork using sdl_mixer rather than libcanberra or mikmod
#https://github.com/Marisa-Chan/gweled-sdl_mixer.git
Source0:	gweled-sdl_mixer-819bed.tar.gz
Patch0:		gweled-fix-librsvg-segfault-v2.patch
Patch1: gweled-c99.patch

BuildRequires:  libgnomeui-devel >= 2.0.0
BuildRequires:  librsvg-devel librsvg-gir-devel
BuildRequires:  desktop-file-utils
BuildRequires:	intltool libtool
BuildRequires:	libSDL_mixer-devel
Requires:	icon-theme-hicolor
Source44: import.info

%description
Gweled is a Gnome version of a popular PalmOS/Windows/Java game called
"Bejeweled" or "Diamond Mine". The aim of the game is to make alignment of 3 or
more gems, both vertically or horizontally by swapping adjacent gems. The game
ends when there are no possible moves left.


%prep
%setup -qn gweled-sdl_mixer-819bed
%patch0 -p0
%patch1 -p1

%build

export LDFLAGS="${LDFLAGS} -lm -Wl,--export-dynamic "
./autogen.sh
%configure --localstatedir=/var/lib
#echo "Encoding=UTF-8" >> data/gweled.desktop
#mv gweled.desktop gweled.desktop.old
#iconv --from-code=ISO-8859-1 --to-code=UTF-8 <gweled.desktop.old > gweled.desktop
%make_build



%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --delete-original \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --add-category LogicGame                    \
  --remove-category Application                        \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

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
<!-- Copyright 2014 William Moreno <williamjmorenor@fedoraproject.org> -->
<!--
BugReportURL: https://bugs.launchpad.net/gweled/+bug/1322917
SentUpstream: 2014-06-12
-->
<application>
  <id type="desktop">gweled.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Align three identical gems to remove them from board</summary>
  <description>
    <p>
      Gweled is a version for GNU / Linux of the popular mobile game called
      Bejeweled or Diamond Mine.
      The game consist in to move adjacent gems to align three or more vertically
      or horizontally to remove them from the board.
    </p>
  </description>
  <url type="homepage">http://launchpad.net/gweled</url>
  <screenshots>
    <screenshot type="default">http://gweled.org/images/screen1.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name}



%files -f %{name}.lang
%doc --no-dereference COPYING
%doc AUTHORS NEWS
%attr(2711,root,games) %{_bindir}/%{name}
%config(noreplace) %attr(0664,games,games) %{_localstatedir}/lib/games/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/sounds/%{name}/

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.9.1-alt2_32.20130730git819bed
- update to new release by fcimport

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 0.9.1-alt2_30.20130730git819bed
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_19.20130730git819bed
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_17.20130730git819bed
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_15.20130730git819bed
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_14.20130730git819bed
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_13.20130730git819bed
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_12.20130730git819bed
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_11.20130730git819bed
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_10.20130730git819bed
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_9.20130730git819bed
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_8.20130730git819bed
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_7.20130725bzr91
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_5
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_4
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_4
- update to new release by fcimport

* Wed Nov 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_3
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_2
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_3
- converted from Fedora by srpmconvert script

