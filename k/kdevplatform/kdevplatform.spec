
%def_disable apidox
%define unstable 0
%define post_version 1
%define _unpackaged_files_terminate_build 1

%if %unstable
%define pkg_sfx -unstable
%define pkg_sfx_other %nil
%define if_unstable() %{expand:%*}
%define if_stable() %nil
%else
%define pkg_sfx %nil
%define pkg_sfx_other -unstable
%define if_unstable()  %nil
%define if_stable() %{expand:%*}
%endif

%define kdevplatform kdevplatform%{pkg_sfx}
%define kdevplatform_other kdevplatform%{pkg_sfx_other}
%define kdevelop kdevelop%{pkg_sfx}
%define kdevelop_other kdevelop%{pkg_sfx_other}

Name: %kdevplatform
Version: 1.3.1
Release: alt1.git
Serial: 1

Group: Development/Tools
Summary: A foundation for KDE-based Integrated Development Environments
Url: http://www.kde.org
License: GPL

Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdevplatform-%version.tar.gz
Source1: kdevplatform-translations-%version.tar.gz
%if %post_version
Patch0: kdevplatform-post-%version.patch
%endif
Patch1: kdevplatform-%version-%release-alt-fixes.patch
Patch2: kdevplatform-alt-translations.patch

BuildRequires(pre): kde4libs-devel >= 4.6.0
BuildRequires: attica-devel boost-devel cvs gcc-c++ glib2-devel glibc-devel
BuildRequires: libsubversion-devel libssh2-devel qjson-devel
Conflicts: kde4libs < 4.6.0

Conflicts: %{kdevplatform_other}
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevplatform_other} < %serial:%version-%release

Requires: %kdevplatform-libs = %serial:%version-%release

%description
%name provides a foundation for KDE-based Integrated Development Environments
like KDevelop or Quanta

%package libs
Summary: Commonly used KDevelop Platform libraries
Group: Development/Tools
Requires: kde4libs >= %{get_version kde4libs}

Conflicts: %{kdevplatform_other}-libs
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevplatform_other}-libs < %serial:%version-%release

# Drop over-splitted packages
Obsoletes: libkdevplatforminterfaces4%pkg_sfx < %serial:%version-%release
Obsoletes: libkdevplatformlanguage4%pkg_sfx < %serial:%version-%release
Obsoletes: libkdevplatformoutputview4%pkg_sfx < %serial:%version-%release
Obsoletes: libkdevplatformproject4%pkg_sfx < %serial:%version-%release
Obsoletes: libkdevplatformshell4%pkg_sfx < %serial:%version-%release
Obsoletes: libkdevplatformutil4%pkg_sfx < %serial:%version-%release
Obsoletes: libkdevplatformvcs4%pkg_sfx < %serial:%version-%release
Obsoletes: libkdevplatformdebugger4%pkg_sfx < %serial:%version-%release
Obsoletes: libsublime4%pkg_sfx < %serial:%version-%release
Obsoletes: libkdevplatformdocumentation4%pkg_sfx < %serial:%version-%release

# Get rid of useless -common subpackage
Obsoletes: %kdevplatform-common < %serial:%version-%release
%if_stable Obsoletes: kdevplatform-unstable-common < %serial:%version-%release

%description libs
This package contains commonly used KDevelop Platform libraries:
 * libkdevplatforminterfaces4
 * libkdevplatformlanguage4
 * libkdevplatformoutputview4
 * libkdevplatformproject4
 * libkdevplatformshell4
 * libkdevplatformutil4
 * libkdevplatformvcs4
 * libkdevplatformdebugger4
 * libsublime4
 * libkdevplatformdocumentation4

%package subversion
Summary: KDevelop Platform module for Subversion support
Group: Development/Tools
Requires: kde4libs >= %{get_version kde4libs}
Requires: %name-libs = %serial:%version-%release
Requires: subversion

Conflicts: %{kdevplatform_other}-subversion
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevplatform_other}-subversion < %serial:%version-%release

# Backward compatibility
Obsoletes: %{kdevelop}-for-subversion

%description subversion
This package contains KDevelop Platform module for subversion support

%package git
Summary: KDevelop Platform module for Git support
Group: Development/Tools
Requires: kde4libs >= %{get_version kde4libs}
Requires: %name-libs = %serial:%version-%release
Requires: /usr/bin/git

Conflicts: %{kdevplatform_other}-git
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevplatform_other}-git < %serial:%version-%release

%description git
This package contains KDevelop platform module for git support

%package cvs
Summary: KDevelop Platform module for CVS support
Group: Development/Tools
Requires: kde4libs >= %{get_version kde4libs}
Requires: %name-libs = %serial:%version-%release
Requires: /usr/bin/cvs

Conflicts: %{kdevplatform_other}-cvs
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevplatform_other}-cvs < %serial:%version-%release

%description cvs
This package contains KDevelop platform module for CVS support

%package -n libkdevplatformtests4%pkg_sfx
Summary: KDevelop Platform tests framework
Group: Development/Tools
Requires: %name-libs = %serial:%version-%release
Requires: kde4libs >= %{get_version kde4libs}

Conflicts: libkdevplatformtests4%{pkg_sfx_other}
%if_stable Obsoletes: libkdevplatformtests4%{pkg_sfx_other} < %serial:%version-%release

%description -n libkdevplatformtests4%pkg_sfx
KDevPlatform tests framework.

%package devel
Summary: Development files for kdevplatform
Group: Development/C++

Conflicts: %{kdevplatform_other}-devel
%if_stable Obsoletes: %{kdevplatform_other}-devel < %serial:%version-%release

Requires: %{kdevplatform}-libs = %serial:%version-%release
Requires: libkdevplatformtests4%pkg_sfx = %serial:%version-%release
%description devel
Development files for kdevplatform.

%prep
%setup -q -a 1 -n kdevplatform-%version
%if %post_version
%patch0 -p1
%endif
%patch1 -p1
cd po
%patch2 -p1
cd ..

cat >>CMakeLists.txt <<EOF

include(MacroOptionalAddSubdirectory)
macro_optional_add_subdirectory( po )
EOF

%build
%K4cmake
%K4make

%if_enabled apidox
make apidox
%endif


%install
%K4install
%K4find_lang --output=%name.lang --with-kde          kdevappwizard

for m in \
kdevclassbrowser kdevcontextbrowser kdevdocumentswitcher kdevdocumentview \
kdevexecute kdevfilemanager kdevgenericprojectmanager kdevgrepview kdevkonsole \
kdevpatchreview kdevplatform kdevproblemreporter kdevprojectmanagerview \
kdevquickopen kdevsnippet kdevstandardoutputview kdevexternalscript \
kdevcodeutils kdevopenwith kdevpastebin kdevreviewboard
do
    %K4find_lang --output=%name.lang --with-kde --append $m
done

%K4find_lang --output=%name-subversion.lang --with-kde kdevsubversion
%K4find_lang --output=%name-git.lang --with-kde kdevgit
%K4find_lang --output=%name-cvs.lang --with-kde kdevcvs

%files -f %name.lang
%_K4bindir/*
%_K4lib/*.so
%exclude %_K4lib/kdevsubversion.so
%exclude %_K4lib/kdevgit.so
%exclude %_K4lib/kdevcvs.so
%_K4apps/kdevcodeutils
%_K4apps/kdevexternalscript
%_K4apps/kdevprojectmanagerview
%_K4apps/kdevstandardoutputview
%_K4apps/kdevfilemanager
%_K4apps/kdevquickopen
%_K4apps/kdevproblemreporter
%_K4apps/kdevcontextbrowser
%_K4apps/kdevsourceformatter
%_K4apps/kdevappwizard
%_K4apps/kdevclassbrowser
%_K4apps/kdevdebugger
%_K4apps/kdevdocumentswitcher
%_K4apps/kdevcodegen
%_K4apps/kdevpatchreview
%_K4apps/kdevdocumentview
%_K4apps/kdevgrepview
%_K4apps/kdevsession
%_K4apps/kdevsnippet
%_K4srv/kdevquickopen.desktop
%_K4srv/kcm_kdev_uisettings.desktop
%_K4srv/kdevfilemanager.desktop
%_K4srv/kdevgenericmanager.desktop
%_K4srv/kdevkonsoleview.desktop
%_K4srv/kdevprojectmanagerview.desktop
%_K4srv/kdevsnippet.desktop
%_K4srv/kdevstandardoutputview.desktop
%_K4srv/kcm_kdev_envsettings.desktop
%_K4srv/kcm_kdev_bgsettings.desktop
%_K4srv/kcm_kdev_ccsettings.desktop
%_K4srv/kcm_kdev_projectsettings.desktop
%_K4srv/kdevproblemreporter.desktop
%_K4srv/kdevexecute.desktop
%_K4srv/kcm_kdev_genericprojectmanagersettings.desktop
%_K4srv/kcm_kdevsourceformattersettings.desktop
%_K4srv/kdevcontextbrowser.desktop
%_K4srv/kcm_kdev_pluginsettings.desktop
%_K4srv/kdevappwizard.desktop
%_K4srv/kdevclassbrowser.desktop
%_K4srv/kdevdocumentswitcher.desktop
%_K4srv/kdevopenwith.desktop
%_K4srv/kdevpatchreview.desktop
%_K4srv/kdevdocumentview.desktop
%_K4srv/kdevgrepview.desktop
%_K4srv/kdevcodeutils.desktop
%_K4srv/kdevexternalscript.desktop
%_K4srv/kdevpastebin.desktop
%_K4srv/kdevreviewboard.desktop
%_K4srv/kdev-dash-projectfileelement.desktop
%_K4srv/kdevexecutescript.desktop
%_K4srv/kdevprojectdashboard.desktop
%_K4srv/kdevvcschangesview.desktop
%_K4srvtyp/kdevelopplugin.desktop
%_K4iconsdir/hicolor/*/actions/run-clean.*
%_K4iconsdir/hicolor/*/actions/run-install.*
%_K4iconsdir/hicolor/*/apps/reviewboard.*

%files libs
%_K4libdir/libkdevplatforminterfaces.so.*
%_K4libdir/libkdevplatformlanguage.so.*
%_K4libdir/libkdevplatformoutputview.so.*
%_K4libdir/libkdevplatformproject.so.*
%_K4libdir/libkdevplatformshell.so.*
%_K4libdir/libkdevplatformutil.so.*
%_K4libdir/libkdevplatformvcs.so.*
%_K4libdir/libsublime.so.*
%_K4libdir/libkdevplatformdebugger.so.*
%_K4libdir/libkdevplatformdocumentation.so.*

%files -n libkdevplatformtests4%pkg_sfx
%_K4libdir/libkdevplatformtests.so.*

%files subversion -f %name-subversion.lang
%_K4srv/kdevsubversion.desktop
%_K4lib/kdevsubversion.so
%_K4iconsdir/hicolor/*/apps/subversion.*

%files git -f %name-git.lang
%_K4srv/kdevgit.desktop
%_K4lib/kdevgit.so
%_K4iconsdir/hicolor/*/apps/git.*

%files cvs -f %name-cvs.lang
%_K4srv/kdevcvs.desktop
%_K4lib/kdevcvs.so
%_K4apps/kdevcvs

%files devel
#%_K4apps/cmake/modules/FindKDevPlatform.cmake
%_K4libdir/cmake/kdevplatform/
%_K4includedir/kdevplatform
%_K4link/lib*.so

%changelog
* Wed Apr 18 2012 Alexey Morozov <morozov@altlinux.org> 1:1.3.1-alt1.git
- a post v1.3.1 git snapshot (02b62ccfa7c0f3df6b523e55dbd99bbb89b8c694)

* Wed Apr 04 2012 Alexey Morozov <morozov@altlinux.org> 1:1.3.0-alt1
- v1.3.0 (logs of intermediate unstable builds are in -unstable package)
- re-organized -subpackages: dropped empty -common, moved most of platform
  libraries into -libs, extracted -subversion, -git, -cvs and fixed their
  dependencies.

* Mon Feb 06 2012 Alexey Morozov <morozov@altlinux.org> 1:1.2.3-alt6.git
- Updated (Russian) translations

* Wed Feb 01 2012 Sergey V Turchin <zerg@altlinux.org> 1:1.2.3-alt5.git
- add serial

* Tue Dec 13 2011 Alexey Morozov <morozov@altlinux.org> 1.2.3-alt4.git
- updated to the current stable git (post-1.2.3, 1302c471d33fedf5954b42c753f29e0a67d186a9)
- translations updated from upstream (up to rev.1266520)
- translations slightly updated and fixed

* Wed Nov 09 2011 Alexey Morozov <morozov@altlinux.org> 1.2.3-alt3.git
- minor improvements in Russian translations

* Sun Oct 23 2011 Alexey Morozov <morozov@altlinux.org> 1.2.3-alt2.git
- updated to the current stable git (post-1.2.3, 98173f88e8477eab39636ef50e37461a3fd94db5)
- translations updated from upstream and slightly improved

* Thu Jun 30 2011 Alexey Morozov <morozov@altlinux.org> 1.2.3-alt1
- new version (1.2.3)
- translations updated from upstream

* Thu Jun 16 2011 Alexey Morozov <morozov@altlinux.org> 1.2.2-alt2.git
- updated to the current stable git (post-1.2.2, 4ac566124a98cd500f7037fa24ceb014b009d660)
- translations updated from upstream and slightly polished

* Mon Apr 25 2011 Alexey Morozov <morozov@altlinux.org> 1.2.2-alt1
- updated to the current stable git (post-1.2.2)
- translations updated from upstream and slightly polished

* Tue Mar 15 2011 Alexey Morozov <morozov@altlinux.org> 1.2.0-alt0.2
- updated to the current stable git
- translations updated from upstream and slightly polished

* Fri Mar 11 2011 Alexey Morozov <morozov@altlinux.org> 1.2.0-alt0.1
- new version (kdevplatform.po is taken from upstream)

* Wed Jan 26 2011 Alexey Morozov <morozov@altlinux.org> 1.1.2-alt1
- merged with upstream translations.

* Thu Jan 20 2011 Alexey Morozov <morozov@altlinux.org> 1.1.2-alt0.4
- (Russian) translations merged with the upstream and slightly updated

* Mon Jan 17 2011 Alexey Morozov <morozov@altlinux.org> 1.1.2-alt0.3
- translations merged with the upstream.
- Russian translations updated

* Mon Jan 17 2011 Alexey Morozov <morozov@altlinux.org> 1.1.2-alt0.2
- few translations updated

* Fri Jan 14 2011 Alexey Morozov <morozov@altlinux.org> 1.1.2-alt0.1
- new version (1.1.2, not announced yet)

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- new version

* Mon Nov  1 2010 Alexey Morozov <morozov@altlinux.org> 1.1.0-alt1.1
- merged with zerg@'s package
- included updated translations (particularly for Russian)

* Tue Oct 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Thu Oct 14 2010 Alexey Morozov <morozov@altlinux.org> 1.0.90-alt0.1
- new version (1.1rc1)
  * cleaned up obsoleted stuff
  * included few new plugins (git, externalscript, pastebin etc)
    and platform libraries

* Tue Aug 24 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- new version

* Thu Apr 29 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- 1.0.0 release

* Mon Apr 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.10.2-alt1
- RC3

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.99-alt1
- 0.9.99

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.98-alt1
- 0.9.98

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.95-alt1
- initial specfile
