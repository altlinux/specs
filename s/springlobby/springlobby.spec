Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/cppcheck /usr/bin/desktop-file-install /usr/bin/doxygen /usr/bin/xsltproc libX11-devel libminizip-devel perl(FileHandle.pm) perl(Text/Wrap.pm) pkgconfig(glib-2.0) pkgconfig(libnotify) zlib-devel
# END SourceDeps(oneline)
# undefined symbol: L_*, LOG_*, parse32 in libFileSystem
# those are from static libUtil, in main binary
%set_verify_elf_method unresolved=relaxed
BuildRequires: boost-devel boost-filesystem-devel boost-signals-devel libpng-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:			springlobby
Version:		0.195
Release:		alt2_17
Summary:		A lobby client for the spring RTS game engine

# License clarification: http://springlobby.info/issues/show/810
License:		GPLv2
URL:			http://springlobby.info
Source0:		http://www.springlobby.info/tarballs/springlobby-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:	ctest cmake
BuildRequires:	libwxGTK3.0-devel, libtorrent-rasterbar-devel
BuildRequires:	libSDL-devel, libSDL_sound-devel, libSDL_mixer-devel
BuildRequires:	desktop-file-utils gettext gettext-tools
BuildRequires:	libopenal-devel, libcurl-devel
BuildRequires:	libalure-devel
BuildRequires:	dumb-devel
BuildRequires:  boost-complete

# There are other "lobbies" for spring, make a virtual-provides
Provides:		spring-lobby = %{version}-%{release}

Requires:		icon-theme-hicolor
Requires:		springrts
ExclusiveArch:	%{ix86} x86_64
Source44: import.info
Patch33: springlobby-0.195-alt-linkage.patch

%description
SpringLobby is a free cross-platform lobby client for the Spring RTS project.

%prep
%setup -q
%patch33 -p1

%build
%{fedora_cmake} .
%make_build

%install
%makeinstall_std

# Useless file
rm -f $RPM_BUILD_ROOT%{_prefix}/config.h

# Fix Icon entry
sed -i -e 's/^Icon=\(.*\).svg/Icon=\1/g' \
		$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-install	\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--remove-category Application \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

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
<!-- Copyright 2014 Eduardo Mayorga <e@mayorgalinux.com> -->
<!--
BugReportURL: https://github.com/springlobby/springlobby/issues/241
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">springlobby.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Find games using Spring-RTS engine</summary>
  <description>
    <p>
      SpringLobby configures the Spring-RTS engine so that you can connect to
      the server using the right maps and mods.
      This helps you to discover the game you want.
      It also allows you to communicate to other players before the game's start.
    </p>
  </description>
  <url type="homepage">http://springlobby.info</url>
  <screenshots>
    <screenshot type="default">http://springlobby.info/landing/screenshots/10_sp.png</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name}

%files -f %{name}.lang
%{_docdir}/%{name}
%{_bindir}/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg

%changelog
* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.195-alt2_17
- update to new release by fcimport

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.195-alt2_15
- use boost-complete

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.195-alt1_15.1
- NMU: rebuilt with boost-1.67.0

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.195-alt1_15
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.195-alt1_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.195-alt1_11
- update to new release by fcimport

* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.195-alt1_9
- fixed build

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.169-alt1_11.1
- rebuild with boost 1.57.0

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_10
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_9
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_8
- update to new release by fcimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_4
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_3
- update to new release by fcimport

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1_2
- fc update

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.147-alt1_4
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.147-alt1_3
- update to new release by fcimport

* Wed Feb 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.147-alt1_2
- update to new release by fcimport

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.147-alt1_1.2
- Rebuilt with updated libtorrent-rasterbar

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.147-alt1_1.1
- Rebuilt with Boost 1.52.0

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.147-alt1_1
- new version

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.144-alt1_1
- update to new release by fcimport

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.139-alt2_2.1
- Rebuilt with Boost 1.49.0

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.139-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.139-alt1_2
- update to new release by fcimport

* Mon Nov 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.139-alt1_1
- update to new release by fcimport

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.136-alt1_1
- update to new release by fcimport

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.131-alt2_1.1
- Rebuilt with Boost 1.47.0

* Thu Jul 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.131-alt2_1
- initial release by fcimport

* Thu Jul 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.131-alt1_1
- initial release by fcimport

