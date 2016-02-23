Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/cppcheck /usr/bin/desktop-file-install /usr/bin/doxygen /usr/bin/msgfmt /usr/bin/msgmerge /usr/bin/pkg-config /usr/bin/xgettext /usr/bin/xsltproc gcc-c++ libX11-devel libminizip-devel perl(FileHandle.pm) perl(Text/Wrap.pm) pkgconfig(glib-2.0) pkgconfig(libnotify) zlib-devel
# END SourceDeps(oneline)
# undefined symbol: L_*, LOG_*, parse32 in libFileSystem
# those are from static libUtil, in main binary
%set_verify_elf_method unresolved=relaxed
BuildRequires: boost-devel boost-filesystem-devel boost-signals-devel libpng-devel
Name:			springlobby
Version:		0.195
Release:		alt1_9
Summary:		A lobby client for the spring RTS game engine

# License clarification: http://springlobby.info/issues/show/810
License:		GPLv2
URL:			http://springlobby.info
Source0:		http://www.springlobby.info/tarballs/springlobby-%{version}.tar.bz2

BuildRequires: ctest cmake
BuildRequires:	wxGTK-devel, libtorrent-rasterbar-devel
BuildRequires:	libSDL-devel, SDL_sound-devel, libSDL_mixer-devel
BuildRequires:, desktop-file-utils, gettext
BuildRequires:	libopenal-devel, libcurl-devel
BuildRequires:	libalure-devel
BuildRequires:	dumb-devel
BuildRequires: boost-devel boost-devel-headers boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel

# There are other "lobbies" for spring, make a virtual-provides
Provides:		spring-lobby = %{version}-%{release}

Requires:		icon-theme-hicolor
Requires:		springrts
ExclusiveArch:	%{ix86} x86_64
Source44: import.info
Patch33: springlobby-0.195-alt-as-needed.patch

%description
SpringLobby is a free cross-platform lobby client for the Spring RTS project.

%prep
%setup -q
%patch33 -p1

%build
%{fedora_cmake}
make %{?_smp_mflags}

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

