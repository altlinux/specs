Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat rpm-macros-ninja-build
BuildRequires: /usr/bin/clang-format /usr/bin/cppcheck /usr/bin/desktop-file-validate /usr/bin/doxygen /usr/bin/wx-config-3.0 libX11-devel libpcre-devel pkgconfig(glib-2.0) python3-devel rpm-build-python3 zlib-devel
# END SourceDeps(oneline)
# undefined symbol: L_*, LOG_*, parse32 in libFileSystem
# those are from static libUtil, in main binary
%set_verify_elf_method unresolved=relaxed
BuildRequires: boost-devel boost-filesystem-devel boost-signals-devel libpng-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 3

Name:           springlobby
Version:        0.273
Release:        alt2_3
Summary:        Free cross-platform lobby client for the Spring RTS project

# License clarification: http://springlobby.info/issues/show/810
License:        GPLv2
URL:            https://springlobby.springrts.com/
Source0:        https://springlobby.springrts.com/dl/stable/springlobby-%{version}.tar.bz2
ExclusiveArch:  %{ix86} x86_64

BuildRequires:  libalure-devel
BuildRequires:  boost-complete
BuildRequires:  ctest cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dumb-devel
BuildRequires:  gcc-c++ >= 8
BuildRequires:  gettext-tools
BuildRequires:  libappstream-glib 
BuildRequires:  libcurl-devel
BuildRequires:  libnotify-devel
BuildRequires:  libminizip-devel
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  libopenal-devel
BuildRequires:  libtorrent-rasterbar-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_sound-devel
BuildRequires:  libSDL-devel
BuildRequires:  libwxGTK3.0-devel

# https://github.com/springlobby/springlobby/issues/709
BuildRequires:  jsoncpp-devel

Requires:       icon-theme-hicolor
Requires:       libGLU

Requires:     libfluidsynth
#Requires:     springrts

# There are other "lobbies" for spring, make a virtual-provides
Provides:       spring-lobby = %{version}-%{release}
Source44: import.info
Patch33: springlobby-0.270-alt-linkage.patch

%description
SpringLobby is a free cross-platform lobby client for the Spring RTS project.


%prep
%setup -q


# Unbunle libs
rm -rf \
    src/downloader/lib/src/lib/minizip
%patch33 -p1


%build
%{fedora_v2_cmake} \
    -B $PWD/%{_vpath_builddir} \
    -G Ninja


%install
%ninja_install -C %{_vpath_builddir}
%find_lang %{name}
rm -rf %{buildroot}%{_docdir}/%{name}/COPYING


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc --no-dereference COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_docdir}/%{name}/
%{_metainfodir}/*.xml


%changelog
* Thu Nov 23 2023 Igor Vlasenko <viy@altlinux.org> 0.273-alt2_3
- removed recommends: on spring-rts

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 0.273-alt1_3
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.271-alt1_6
- update to new release by fcimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.271-alt1_1
- update to new release by fcimport

* Tue Sep 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.267-alt2_5
- NMU: rebuilt with boost-1.74.0.

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.267-alt1_5
- new version

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

