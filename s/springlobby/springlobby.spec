# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ libSDL_sound-devel libgcrypt-devel libgnutls-devel libgpg-error-devel libidn-devel libogg-devel libuuid-devel libvorbis-devel pkgconfig(ogg) pkgconfig(vorbis) pkgconfig(vorbisfile) zlib-devel
# END SourceDeps(oneline)
Name:			springlobby
Version:		0.144
Release:		alt1_1
Summary:		A lobby client for the spring RTS game engine

Group:			Games/Other
# License clarification: http://springlobby.info/issues/show/810
License:		GPLv2
URL:			http://springlobby.info
Source0:		http://www.springlobby.info/tarballs/springlobby-%{version}.tar.bz2
Patch0:			springlobby-gtkfix.patch


BuildRequires:	ctest cmake
BuildRequires:	wxGTK-devel libtorrent-rasterbar-devel
BuildRequires:	libSDL-devel SDL_sound-devel libSDL_mixer-devel
BuildRequires:	desktop-file-utils gettext
BuildRequires:	libopenal-devel libcurl-devel

# There are other "lobbies" for spring, make a virtual-provides
Provides:		spring-lobby = %{version}-%{release}

Requires:		icon-theme-hicolor
# Springlobby is completely useless without the spring package
Requires:		springrts
# Spring does not build on PPC, exclude it here too
ExcludeArch:	ppc ppc64
Source44: import.info


%description
SpringLobby is a free cross-platform lobby client for the Spring RTS project.


%prep
%setup -q
%patch0 -p0 -b .springlobby-gtkfix
sed -i 's,#include <curl/types.h>,,' src/utils/curlhelper.h src/utils/downloader.cpp


%build
# Use boost filesystem 2 explicitly (bug 654807)
export CFLAGS="$CFLAGS -DBOOST_FILESYSTEM_VERSION=2"
export CXXFLAGS="$CXXFLAGS -DBOOST_FILESYSTEM_VERSION=2"
%{fedora_cmake}
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Handled in %%doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/
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

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING THANKS
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%changelog
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

