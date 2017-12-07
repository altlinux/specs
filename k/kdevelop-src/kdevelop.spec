Version: 4.7.3
Release: alt2.git
Serial: 3

%define _unpackaged_files_terminate_build 1
%define unstable 0
%define post_version 1
%define with_api_docs 0
%def_enable okteta
# from the Project's CMakeLists.txt
%define build_req_kde_ver_min 4.6.0
%define build_req_kdeplatform_min 1.7.0
%define req_kdev_php_min 1.7.0

%if %unstable
%define pkg_sfx -pre4.7
%define pkg_sfx_other %nil
%define if_unstable() %{expand:%*}
%define if_stable() %nil
%else
%define pkg_sfx %nil
%define pkg_sfx_other -pre4.7
%define if_unstable()  %nil
%define if_stable() %{expand:%*}
%endif

%define kdevplatform kdevplatform%{pkg_sfx}
%define kdevplatform_other kdevplatform%{pkg_sfx_other}
%define kdevelop kdevelop%{pkg_sfx}
%define kdevelop_other kdevelop%{pkg_sfx_other}

%add_python_req_skip gdb

%define desc_common \
KDevelop is a free, open source IDE (Integrated Development Environment)\
for MS Windows, Mac OS X, Linux, Solaris and FreeBSD.\
\
It is a feature-full, plugin extensible IDE for C/C++ and other \
programming languages.\
\
KDevelop provides a complete environment (development, debugging,\
profiling, testing) for C/C++ application development. It supports\
make- and CMake projects out of box, modules for other build systems\
are being developed.\
\
Also it has modules (packaged separately) for PHP, Python, Valgrind\
and other programming languages and development tools.

# this should be oneliner :/
%define req_normal %kdevelop-mini = %serial:%version-%release %kdevelop-for-debug = %serial:%version-%release %kdevplatform-subversion >= %build_req_kdeplatform_min %kdevplatform-git >= %build_req_kdeplatform_min %kdevelop-for-github = %serial:%version-%release %kdevelop-kde-integration = %serial:%version-%release
%define req_normal_features \
  * KDE Plasma integration \
  * debug module \
  * module for Subversion support \
  * module for Git support \
  * module for accessing GitHub

%define req_big %kdevelop = %serial:%version-%release %kdevelop-for-kde = %serial:%version-%release %kdevelop-for-qt = %serial:%version-%release %kdevelop-ninja = %serial:%version-%release
%define req_big_features %req_normal_features \
  * module for QT apps development \
  * module for KDE apps development \
  * module for Ninja build system support

%if_enabled okteta
%global req_big %req_big %kdevelop-okteta = %serial:%version-%release
%global req_big_features %req_big_features \
  * Okteta viewer module
%endif

# this one too :/
%define req_maxi %req_big %kdevplatform-cvs >= %build_req_kdeplatform_min %kdevplatform-bazaar >= %build_req_kdeplatform_min %kdevelop-for-php >= %req_kdev_php_min
%define req_maxi_features %req_big_features \
  * module for CVS support \
  * module for Bazaar support \
  * module for PHP programming language support

Name: %kdevelop-src
Summary: A KDE-centric IDE - source package
License: GPLv2
Group: Development/Tools
Url: http://www.kdevelop.org/

Source: kdevelop-%version.tar.gz
Source1: kdevelop-translations-%version.tar.gz
%if %post_version
Patch0: kdevelop-post-%version.patch
%endif
Patch1: kdevelop-%version-%release-alt-fixes.patch
Patch2: kdevelop-alt-translations.patch

# Automatically added by buildreq on Tue Mar 30 2010 (-bi)
#BuildRequires: cvs gcc-c++ git-core glib2-devel glibc-devel-static kde4base-workspace-devel kdevplatform-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libqt3-devel libxkbfile-devel mercurial openssh qt4-assistant qt4-designer rpm-build-ruby subversion valgrind-devel xorg-xf86vidmodeproto-devel
BuildRequires(pre): kde4libs-devel
BuildRequires: cvs gcc-c++ glib2-devel glibc-devel kde4base-workspace-devel valgrind-devel cppunit-devel libcheck-devel qjson-devel
BuildRequires: kde4libs-devel >= %build_req_kde_ver_min
BuildRequires: %kdevplatform-devel >= %build_req_kdeplatform_min

# For Kasten plugin
BuildRequires: kde4utils-devel
# For Okteta plugin
%if_enabled okteta
BuildRequires: kde4sdk-devel
%endif

%description
%desc_common

This is a KDevelop source package

%package -n %kdevelop
Summary: A KDE-centric IDE - normal installation
Group: Development/Tools
Requires: %req_normal
BuildArch: noarch

Conflicts: %kdevelop_other
%if_stable Obsoletes: %{kdevelop_other} < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable

%description -n %kdevelop
%desc_common

This package provides a "medium" variant of KDevelop installation.
Besides a minimal installation it includes the following modules:
%req_normal_features

%package -n %kdevelop-devel
Group: Development/KDE and QT
Summary: Development libraries for KDevelop
Requires: %kdevelop-libs = %serial:%version-%release
BuildArch: noarch

Conflicts: %{kdevelop_other}-devel
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-devel < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-devel

%description -n %kdevelop-devel
Development libraries for KDevelop.

# Drop previous -unstable
Conflicts: kdevelop-unstable-common

%package -n %kdevelop-mini
Group: Development/Tools
Summary:  A KDE-centric IDE - normal installation
Requires: %kdevplatform >= %build_req_kdeplatform_min
Requires: %kdevelop-libs = %serial:%version-%release
Requires: gcc gcc-c++

Provides: %kdevelop-base = %serial:%version-%release
Obsoletes: %kdevelop-base < %release:%version-%release
Conflicts: %{kdevelop_other}-mini
Conflicts: %{kdevelop_other}-base
# Only stable package replaces unstable counterpart
%if !%unstable
Obsoletes: %{kdevelop_other}-base < %serial:%version-%release
Obsoletes: %{kdevelop_other}-mini < %serial:%version-%release
%endif

# Drop previous -unstable
Conflicts: kdevelop-unstable-base

Requires: make cmake
%description -n %kdevelop-mini
%desc_common

This package contains minimal installation of KDevelop IDE.
It provides only basic set of features and extensions modules.

%package -n %kdevelop-libs
Group: Development/Other
Summary: Base libraries for KDevelop
Requires: kde-common >= 4
Requires: %kdevplatform-libs >= %build_req_kdeplatform_min
Conflicts: kdevelop <= 3.0.2-alt0.2

Conflicts: %{kdevelop_other}-libs
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-libs < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-libs

# Drop -common subpackage
Conflicts: %kdevelop-common
Obsoletes: %kdevelop-common <= %serial:%version-%release
Conflicts: %{kdevelop_other}-common
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-common <= %serial:%version-%release

%description -n %kdevelop-libs
This package contains base libraries for %name

%package -n %kdevelop-maxi
Group: Development/Tools
Summary: A KDE-centric IDE - maximal installation
Requires: %req_maxi
BuildArch: noarch

Conflicts: %{kdevelop_other}-maxi
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-maxi < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-maxi

%description -n %kdevelop-maxi
%desc_common

This meta-package provides a full KDevelop installation
by depending on other KDevelop-related packages.
Besides an usual KDevelop features it provides the following
list of modules: %req_maxi_features

%package -n %kdevelop-big
Group: Development/Tools
Summary: A KDE-centric IDE - extended installation
Requires: %req_big
BuildArch: noarch

Conflicts: %{kdevelop_other}-big
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-big < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-big

%description -n %kdevelop-big
%desc_common

This package provides an extended KDevelop installation
by depending on other KDevelop-related packages.
Besides an usual KDevelop features it provides the following
list of modules: %req_big_features

%package -n %kdevelop-kde-integration
Summary: A KDE-centric IDE - modules for Plasma
Group: Development/Tools
Conflicts: %{kdevelop_other}-kde-integration
%description -n %kdevelop-kde-integration
%desc_common

This package provides modules to integrate KDevelop
into KDE Plasma.

%package -n %kdevelop-for-github
Group: Development/Tools
Summary: KDevelop module for accessing projects on GitHub
Requires: %kdevelop-mini = %serial:%version-%release
Requires: %kdevplatform-git >= %build_req_kdeplatform_min

Conflicts: %{kdevelop_other}-for-github
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-for-github < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-for-github

%description -n %kdevelop-for-github
This KDevelop module allows to access projects on GitHub from within
KDevelop.

%package -n %kdevelop-for-debug
Group: Development/Debug
Summary: KDevelop module for debugging
Requires: %kdevelop-mini = %serial:%version-%release
Requires: valgrind gdb

Conflicts: %{kdevelop_other}-for-debug
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-for-debug < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-for-debug

%description -n %kdevelop-for-debug
This KDevelop module provides KDevelop with debugging capabilities
using GDB and Valgrind as backends.

%package -n %kdevelop-ninja
Group: Development/Tools
Summary: KDevelop module for Ninja build system support
Requires: %kdevelop-mini = %serial:%version-%release
Requires: ninja-build

Conflicts: %{kdevelop_other}-ninja
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-ninja < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-ninja

%description -n %kdevelop-ninja
This KDevelop module provides support for Ninja build system

%package -n %kdevelop-for-qt
Group: Development/KDE and QT
Summary: Templates for developing Qt applications with KDevelop
Requires: %kdevelop-mini = %serial:%version-%release
Requires: qt4-devel qt4-doc

Conflicts: %{kdevelop_other}-for-qt
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-for-qt < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-for-qt

%description -n %kdevelop-for-qt
Templates for developing Qt applications with KDevelop

%package -n %kdevelop-for-kde
Group: Development/KDE and QT
Summary: Templates for developing KDE applications with KDevelop
Requires: %kdevelop-mini = %serial:%version-%release
Requires: %kdevelop-for-qt = %serial:%version-%release
Requires: kde4sdk-kapptemplate
Requires: kde4libs-devel kde4pimlibs-devel kde4base-runtime-devel kde4base-workspace-devel kde4base-devel
Requires: kde4multimedia-devel kde4graphics-devel kde4network-devel
BuildArch: noarch

Conflicts: %{kdevelop_other}-for-kde
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-for-kde < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-for-kde

%description -n %kdevelop-for-kde
Templates for developing KDE applications with KDevelop

%package -n %kdevelop-okteta
Group: Development/Other
Summary: Okteta KDevelop plugin
Requires: %kdevelop-mini = %serial:%version-%release

Conflicts: %{kdevelop_other}-okteta
# Only stable package replaces unstable counterpart
%if_stable Obsoletes: %{kdevelop_other}-okteta < %serial:%version-%release

# Drop previous -unstable
Conflicts: kdevelop-unstable-okteta

%description -n %kdevelop-okteta
Okteta KDevelop plugin provides simple Hex Editing

%package -n %kdevelop-php-templates
Group: Development/Other
Summary: PHP-specific file templates for KDevelop
BuildArch: noarch
Requires: %kdevelop-for-php
Requires: %kdevelop = %serial:%version-%release

%description -n %kdevelop-php-templates
File templates for PHP development using KDevelop

%package -n %kdevelop-python-templates
Group: Development/Other
Summary: Python-specific file templates for KDevelop
BuildArch: noarch
Requires: %kdevelop-for-python
Requires: %kdevelop = %serial:%version-%release

%description -n %kdevelop-python-templates
File templates for Python development using KDevelop

%prep
%setup -q -a 1 -n kdevelop-%version
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

%if_disabled okteta
find po -name 'kdevokteta.po' -exec rm {} \;
%endif

%build
%K4cmake
%K4make

%if %with_api_docs
%make_build apidox
%endif

%install
%K4install
%if %with_api_docs
%make_build DESTDIR=%buildroot install-apidox
%endif

# Fix permissions of desktop files
chmod -x %buildroot%_K4xdg_apps/*

# remove all desktop_extragear-* translations, zerg@ told they aren't needed at all
find %buildroot -name 'desktop_extragear*.mo' -exec rm {} \;

%K4find_lang --output=%name-mini.lang --with-kde          kdevelop
for m in \
kdevcmakebuilder kdevcmake kdevcpp kdevcustommake kdevformatters \
 kdevmakebuilder kdevelopsessions kdevmanpage \
 kdevcustombuildsystem
do
    %K4find_lang --output=%name-mini.lang --with-kde --append $m
done

%K4find_lang --output=%{name}-kde-integration.lang --with-kde  kdevexecuteplasmoid \
	plasma_applet_kdevelopsessions plasma_runner_kdevelopsessions

%if_enabled okteta
%K4find_lang --output=kdevokteta.lang --with-kde kdevokteta
%endif

%K4find_lang --output=kdevqthelp.lang --with-kde kdevqthelp

%K4find_lang --output=kdevgdb.lang --with-kde kdevgdb

%K4find_lang --output=kdevlibs.lang --with-kde kdevkdeprovider

%K4find_lang --output=kdevninja.lang --with-kde kdevninja

%K4find_lang --output=kdevghprovider.lang --with-kde kdevghprovider

%files -n %kdevelop
%files -n %kdevelop-maxi
%files -n %kdevelop-big

%files -n %kdevelop-kde-integration -f %name-kde-integration.lang
%_K4apps/plasma
%_K4lib/kdevexecuteplasmoid.so
%_K4srv/kdevexecuteplasmoid.desktop
%_K4lib/krunner_kdevelopsessions.so
%_K4lib/plasma_engine_kdevelopsessions.so
%_K4srv/plasma-*.desktop

%files -n %kdevelop-for-github -f kdevghprovider.lang
%_K4lib/kdevghprovider.so
%_K4srv/kdevghprovider.desktop

%files -n %kdevelop-for-debug -f kdevgdb.lang
%_K4lib/kdevgdb.so
%_K4apps/kdevgdb
%_K4srv/kdevgdb.desktop

%files -n %kdevelop-for-kde

%files -n %kdevelop-ninja -f kdevninja.lang
%_K4lib/kcm_kdev_ninjabuilder.so
%_K4lib/kdevninja.so

%files -n %kdevelop-for-qt -f kdevqthelp.lang
%_K4lib/kdevqthelp.so
%_K4lib/kdevqthelp_config.so
%_K4srv/kdevqthelp*.desktop
%_K4apps/kdevappwizard/templates/*make_qt4*.tar.bz2
%_K4apps/kdevfiletemplates/templates/qt*.tar.bz2
%_K4apps/kdevfiletemplates/templates/qobject*.tar.bz2
%_K4apps/kdevfiletemplates/templates/cpp_qtestlib.tar.bz2
%_K4apps/kdevfiletemplates/templates/cpp_qtestlib_kde.tar.bz2
%_K4apps/kdevfiletemplates/templates/cpp_qtestlib_kdevelop.tar.bz2
%_K4conf/kdevelop-qthelp.knsrc

%files -n %kdevelop-mini -f %name-mini.lang
%doc AUTHORS README HACKING
%_K4bindir/kdevelop
%_K4bindir/kdevelop!
%_K4lib/kcm_kdevcmake_settings.so
%_K4lib/kcm_kdev_cmakebuilder.so
%_K4lib/kdevcmakebuilder.so
%_K4lib/kdevcmakemanager.so
%_K4lib/kdevcmakedocumentation.so

%_K4apps/kdevcustommakemanager
%_K4lib/kcm_kdevcustombuildsystem.so
%_K4lib/kdevcustombuildsystem.so
%_K4lib/kdevcustommakemanager.so

%_K4lib/kcm_kdev_makebuilder.so
%_K4lib/kdevmakebuilder.so

%_K4lib/kdevdefinesandincludesmanager.so
%_K4lib/kcm_kdevcustomdefinesandincludes.so

%_K4apps/kdevcppsupport
%_K4lib/kdevcpplanguagesupport.so

%_K4lib/kdevastyle.so
%_K4lib/kdevcustomscript.so

%_K4lib/kdevmanpage.so
%_K4apps/kdevmanpage/manpagedocumentation.css

%_K4srv/*.desktop
%exclude %_K4srv/kdevqthelp*.desktop
%exclude %_K4srv/kdevghprovider.desktop
%if_enabled okteta
%exclude %_K4srv/kdevokteta*.desktop
%endif
%exclude %_K4srv/kdevgdb.desktop
%exclude %_K4srv/kdevexecuteplasmoid.desktop
%exclude %_K4srv/plasma-*.desktop

%_K4apps/kdevelop
%dir %_K4apps/kdevappwizard
%dir %_K4apps/kdevappwizard/templates
%_K4apps/kdevappwizard/templates/cmake_plaincpp.tar.bz2
%dir %_K4apps/kdevcodegen
%dir %_K4apps/kdevcodegen/templates
%_K4apps/kdevcodegen/templates/*.txt
%_K4apps/kdevcodegen/templates/cpp_*.cpp
%_K4apps/kdevcodegen/templates/cpp_*.h
%dir %_K4apps/kdevfiletemplates
%dir %_K4apps/kdevfiletemplates/templates
%_K4apps/kdevfiletemplates/templates/c_gobject*.tar.bz2
%_K4apps/kdevfiletemplates/templates/cmake_module*.tar.bz2
%_K4apps/kdevfiletemplates/templates/cpp_basic*.tar.bz2
%_K4apps/kdevfiletemplates/templates/private_pointer.tar.bz2
%_K4xdg_apps/kdevelop.desktop
%_K4xdg_apps/kdevelop_ps.desktop
%_K4conf/kdeveloprc
%_K4iconsdir/hicolor/*/*/*.*
%_K4xdg_mime/kdevelop.xml

%files -n %kdevelop-libs -f kdevlibs.lang
%_K4lib/kdevkdeprovider.so

%_K4libdir/libkdev4cmakecommon.so

%_K4libdir/libkdev4cppduchain.so
%_K4libdir/libkdev4cppparser.so
%_K4libdir/libkdev4cpprpp.so
%_K4libdir/libkdevcompilerprovider.so

%if_enabled okteta
%files -n %kdevelop-okteta -f kdevokteta.lang
%_K4lib/kdevokteta.so
%_K4apps/kdevokteta
%_K4srv/kdevokteta*.desktop
%endif

%files -n %kdevelop-devel
%_K4apps/cmake/modules/*.cmake
%_K4includedir/kdevelop
#%doc %_K4doc/en/kdevelop-apidocs/

%files -n %kdevelop-php-templates
%_K4apps/kdevfiletemplates/templates/php_phpunit.tar.bz2

%files -n %kdevelop-python-templates
%_K4apps/kdevfiletemplates/templates/python_*.tar.bz2

%changelog
* Thu Dec 07 2017 Oleg Solovyov <mcpain@altlinux.org> 3:4.7.3-alt2.git
- fix autocompletion crash

* Wed Nov 22 2017 Oleg Solovyov <mcpain@altlinux.org> 3:4.7.3-alt1.git
- post v4.7.2 release build (rev.934f5f6923034c685fa48d8e17a67bba1a77a8c5)

* Fri Nov 13 2015 Alexey Morozov <morozov@altlinux.org> 3:4.7.2-alt1.git
- post v4.7.2 release build (rev.ac55d7a858d9648fceaa96037a2bb74078998806)

* Mon Jan 12 2015 Alexey Morozov <morozov@altlinux.org> 3:4.7.0-alt1
- v4.7.0 release
- translations are taken from the upstream release, w/o local fixes
  or enhancements

* Fri Nov 15 2013 Alexey Morozov <morozov@altlinux.org> 3:4.5.2-alt1.git
- v4.5.2 release plus 39618b4daa45b9feed88a54789c301ae75f7bb63 commit
- Translations merged and siglhtly modified
- Spec is cleared from excessive versioned dependencies as Repocop suggests
- Plasma-specific modules are packaged separately (in %kdevelop-kde-integration)

* Fri Jun  7 2013 Alexey Morozov <morozov@altlinux.org> 3:4.5.1-alt1
- v4.5.1 release

* Tue Apr 30 2013 Alexey Morozov <morozov@altlinux.org> 3:4.5.0-alt1.git
- a post 4.5.0 snapshot (ff1b813e716271de6bfab7f7be75a3e808650754,

  one minor commit after v4.5.0)
* Tue Apr 30 2013 Alexey Morozov <morozov@altlinux.org> 3:4.5.0-alt1.git
- a post 4.5.0 snapshot (ff1b813e716271de6bfab7f7be75a3e808650754,
  one minor commit after v4.5.0)

* Mon Apr  8 2013 Alexey Morozov <morozov@altlinux.org> 3:4.4.1-alt2.git
- a post-4.4.1 snapshot (0f2c97bf42c60484ba1ad73021f904c4dc34d3eb)
- explicitly remove desktop_extragear*.mo files from the build
- translations are synchronized with upstream

* Fri Nov 30 2012 Alexey Morozov <morozov@altlinux.org> 3:4.4.1-alt1.git
- a post-4.4.1 snapshot (88f0a7496a5989a2d071b0ec5671697aa365723b)
- updated translations

* Tue Oct 30 2012 Alexey Morozov <morozov@altlinux.org> 3:4.4.0-alt3.git
- a new post-4.4.0 snapshot (87ae4b8ce8af46a4dc56f940e1f40831f2589ed7)
  Splash screen now says it's actually KDevelop-4.4 :-)
- translations are synchronized with upstream.

* Thu Oct 18 2012 Alexey Morozov <morozov@altlinux.org> 3:4.4.0-alt2.git
- fixed obsoletes

* Thu Oct 18 2012 Alexey Morozov <morozov@altlinux.org> 3:4.4.0-alt1.git
- one commit after release (git 0e2bb7c215b856b5add1fc42a5656260afbb41f0)
- translations are synchronized with upstream
- re-enabled Okteta module

* Tue Oct 16 2012 Alexey Morozov <morozov@altlinux.org> 3:4.3.1-alt3.git
- Updated to the latest post-4.3.1 git snapshot
  (1f6674f778240741fab2ad1254e326057960ede3)
- Synchronized translations with the latest upstream revisions suitable
  for 4.3
- Okteta module disabled, because it depends on obsoleted (pre-4.9.x)
  KDE SDK libraries. Use kdevelop-pre4.4 if you need this module.

* Fri Apr 20 2012 Alexey Morozov <morozov@altlinux.org> 3:4.3.1-alt2.git
- Drop -common subpackage, renamed -base to -mini, carefully set packages
  architecture (noarch or arch-dependent)

* Thu Apr 19 2012 Alexey Morozov <morozov@altlinux.org> 3:4.3.1-alt1.git
- a post-v4.3.1 git snapshot (6b95b832d72696df0278ac7b9d290c96b798ef07)
- Russian translations updated and merged with upstream

* Sat Apr 07 2012 Alexey Morozov <morozov@altlinux.org> 3:4.3.0-alt1.1
- Added explicit dependency on kdevelop-libs for kdevelop-base as
  a workaround for apt inability to install built package
- Deps-only packages are now noarch

* Wed Apr 04 2012 Alexey Morozov <morozov@altlinux.org> 3:4.3.0-alt1
- v4.3.0 (logs of intermediate unstable builds are in the -unstable package)
- major spec overhaul and cleanup
- restored okteta module

* Sun Jan 29 2012 Sergey V Turchin <zerg@altlinux.org> 3:4.2.3-alt4.git
- rebuilt with kde-4.8
- temporary disable okteta module

* Tue Dec 13 2011 Alexey Morozov <morozov@altlinux.org> 2:4.2.3-alt3.git
- post-4.2.3 git snapshot (ac7753c16170e82bbfc579822184f22b6fefd1a6)
- a lot of small spec changes (group names, proper file permissions,
  package kdevelop-for-misc is renamed to kdevelop-for-subversion)
- moved kdevokteta.desktop to the corresponding package to fix KDevelop
  bootup warning
- actually move gdb-specific parts to -for-debug subpackage
- updated Russian translation

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2:4.2.3-alt2.git.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Alexey Morozov <morozov@altlinux.org> 2:4.2.3-alt2.git
- post-4.2.3 git snapshot (c3f6cea2916bc158b45de534d2cb738a556e7ee7)
- translations merged with upstream and slightly improved
- RPM build requirements are set according to source reqs

* Thu Jun 30 2011 Alexey Morozov <morozov@altlinux.org> 2:4.2.3-alt1
- new version (4.2.3)
- translations merged with upstream

* Thu Jun 16 2011 Alexey Morozov <morozov@altlinux.org> 2:4.2.2-alt2.git
- new version (post-4.2.2, git b389cfb2e620abe089d4a86f2315503d6d95196f)
- translations merged with upstream and slightly updated

* Mon Apr 25 2011 Alexey Morozov <morozov@altlinux.org> 2:4.2.2-alt1
- new version (post-4.2.2 with updated translations)

* Tue Mar 15 2011 Alexey Morozov <morozov@altlinux.org> 2:4.2.0-alt0.1
- new version (post-4.2.0 with updated translations)
- qthelp plugin is moved to kdevelop-for-qt subpackage

* Thu Jan 20 2011 Alexey Morozov <morozov@altlinux.org> 2:4.1.2-alt0.4
- (Russian) translations merged with upstream and slightly fixed/updated

* Mon Jan 17 2011 Alexey Morozov <morozov@altlinux.org> 2:4.1.2-alt0.3
- re-included Qt/CMake application templates

* Mon Jan 17 2011 Alexey Morozov <morozov@altlinux.org> 2:4.1.2-alt0.2
- translations updated

* Sat Jan 15 2011 Alexey Morozov <morozov@altlinux.org> 2:4.1.2-alt0.1
- new version (4.1.2, not yet announced)

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 2:4.1.1-alt1
- new version

* Wed Nov 10 2010 Alexey Morozov <morozov@altlinux.org> 2:4.1.0-alt1.1
- merge with zerg@'s changes
- translations fetched from upstream SVN and slightly revised
- patch #1 is re-fetched from 4:4.1.0-0ubuntu1
- updated build and runtime dependency on kdevplatform
  (from project's CMakeLists.txt)

* Tue Oct 26 2010 Sergey V Turchin <zerg@altlinux.org> 2:4.1.0-alt1
- new version

* Thu Oct 14 2010 Alexey Morozov <morozov@altlinux.org> 2:4.0.90-alt0.1
- new version (4.1rc1)
- dropped outdated/missing stuff, build existing plugins as separate
  packages
- added okteta subpackage
- added kdevelop-4.0.90-appmenu_fix.diff (#1) based on
  kubuntu_01_appmenu_fix.diff from 4:4.0.2-0ubuntu2

* Tue Aug 24 2010 Sergey V Turchin <zerg@altlinux.org> 2:4.0.1-alt1
- new version
- add kdevelop-pg-qt

* Thu Apr 29 2010 Sergey V Turchin <zerg@altlinux.org> 2:4.0.0-alt1
- 4.0.0 release

* Mon Apr 19 2010 Sergey V Turchin <zerg@altlinux.org> 2:3.10.2-alt1
- RC3

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 2:3.9.99-alt1
- 3.9.99

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 2:3.9.98-alt1
- 3.9.98

* Thu Aug 27 2009 Sergey V Turchin <zerg@altlinux.org> 2:3.9.95-alt1
- new version

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.3-alt1
- new version

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.1-alt1
- new version

* Fri Oct 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.0-alt2
- fix loop in filegroup plugin

* Thu Oct 18 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.5.0-alt1
- new version

* Thu Jul 19 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt3
- split kio-chm to separate package
- reorganize subpackages like kde* empty *-common

* Tue May 22 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt2
- update tarball from ftp.kde.org

* Mon May 21 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.1-alt1
- new version

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 2:3.4.0-alt1
- new version

* Wed Oct 18 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.5-alt1
- new version

* Thu Sep 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.4-alt2
- fix build requires

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.3-alt1
- new version

* Wed Apr 05 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.1-alt1
- new version

* Wed Jan 11 2006 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.0-alt2
- fix BuildRequires to support cvs

* Tue Dec 13 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.3.0-alt1
- new version

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt3
- fix linking libkdevinterfaces

* Mon Jun 20 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt2
- fix KChmPart linking

* Thu Jun 09 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.1-alt1
- new version

* Mon Apr 04 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.2.0-alt1
- new version

* Wed Jan 12 2005 Sergey V Turchin <zerg at altlinux dot org> 2:3.1.2-alt1
- new version

* Wed Nov 03 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.1.1-alt1
- new version

* Thu Jun 10 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.4-alt1
- new version

* Wed Apr 21 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.3-alt1
- new version

* Wed Mar 31 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.2-alt1
- split, add requires

* Thu Mar 11 2004 Sergey V Turchin <zerg at altlinux dot org> 2:3.0.2-alt0.1
- new version

* Mon Jan 12 2004 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.12
- CVS update
- link libpthread to kdevelop executable (no .la => no .so dep recursion)

* Mon Dec 29 2003 Sergey V Turchin <zerg at altlinux dot org> 2:3.0-alt0.11.1
- remove %%_libdir/*.la; fix finding kdelibs in project apps

* Sun Nov 23 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.11
- update to CVS
- qmake in $PATH patch

* Sat Nov 8 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.10
- gettext-tools dependency
- non-KDE menus bugfix
- update to CVS HEAD

* Fri Oct 17 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0-alt0.07
- exec filename changes from gideon to kdevelop
- version numbering change

* Wed Oct 15 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a7-alt1
- updated to alpha7+

* Wed Sep 24 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt3
- libpcre-devel python22-devel dependencies (for hasher builds)

* Mon Sep 22 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt2
- add_findprov_lib_path spec fix
- removed kiconedit depencency; not to depend on Big KDE

* Fri Sep 12 2003 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:3.0a6-alt1
- new Sisyphus requirements
- updated to the current cvs version (~alpha 6)

* Thu Sep  4 2003 Sergey A. Sukiyazov <corwin@micom.net.ru> 2:3.0-ssa0.a4a
- add graphviz build requirements
- add and disable patch to set default codec via locale.
- add patch to qstring convert via locale.

* Fri Dec 20 2002 Viktor S. Grishchenko <gritzko@altlinux.ru> 3.0-a2-cvs
- total spec clean-up
- CVS update

* Fri Oct 04 2002 Gor <vg@altlinux.ru> 2:2.1.2-alt3
- spec fixes for new kde deps
- sources updated from CVS

* Fri Oct 04 2002 Gor <vg@altlinux.ru> 2:2.1.2-alt2
- rebuild with gcc-3.2 & new kdelibs

* Wed Jul 31 2002 Viktor S. Grishchenko <gritzko@altlinux.ru> 2:2.1.2-alt1
- update from cvs (KDE_2_2_BRANCH, 2.1.2+fixes)
- removed MDK patches (obsolete)
- removed automake hack patch
- removed  kdevelop-2.1beta1-kde3.patch
- detect_alt_autoconf.patch to choose appropriate autoconf alternative

* Fri Jun 14 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt3
- update from cvs (KDEVELOP_2_0_BRANCH)

* Fri May 31 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt2
- fix missing C reference files

* Fri May 31 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1.1-alt1
- new version

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.1-alt1
- new version

* Tue Mar 19 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt5
- add any PreReq

* Fri Feb 15 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt4
- sync with cooker (add patches 3-6)

* Tue Jan 22 2002 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt3
- rebuild without fam
- sync with cooker (update cvs)

* Mon Dec 10 2001 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt2
- fix Patch10 (QString.patch)

* Fri Dec 07 2001 Sergey V Turchin <zerg@altlinux.ru> 2:2.0.2-alt1
- new version

* Wed Nov 21 2001 Sergey V Turchin <zerg@altlinux.ru> 1:2.2-alt8
- add Patch10 from Sergey A. Sukiyazov <corwin@micom.don.ru>

* Fri Oct 12 2001 AEN <aen@logic.ru> 2.2-alt7
- rebuild with new libpng

* Fri Oct 12 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt6
- rebuild with new libpng

* Tue Aug 28 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt5
- fix broken dependences

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.2-alt4
- Fixed .la bug

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.2-alt3
- Some spec cleanup
- Added -devel package
- Fixed filelists
- Added c_cpp_reference documentation

* Mon Aug 20 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt2
- fixed %%serial

* Fri Aug 17 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt1
- build for ALT

* Tue Aug 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0-2mdk
- Fix generated menu

* Wed Aug 06 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0-1mdk
- kdevelop 2.0 for kde 2.2

* Wed Aug 01 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.pre1.1mdk
- kde 2.2 pre1

* Fri Jun 29 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.beta1.1mdk
- KDE 2.2.beta1

* Fri Jun 08 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.alpha2.3mdk
- Clean ./configure
- Enable debug and don't strip when we are not in final release

* Tue May 24 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.alpha2.2mdk
- Re-enable debug (low level)

* Wed May 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.alpha2.1mdk
- kdevelop 2.2 alpha2

* Tue May 02 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.alpha1.1mdk
- kdevelop 2.2 alpha1

* Wed Apr 11 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4.1-3mdk
- Add requires

* Tue Apr 10 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4.1-2mdk
- Move KDE menu entries in %%_datadir/applnk
- Rebuild against latest GCC

* Wed Mar 21 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4.1-1mdk
- Kdevelop 1.4.1
- Disable PATH for kdelibsdoc-dir (looks in kdelibs buildroot!???)

* Sun Mar 11 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-6mdk
- Rebuild for Linux-Mandrake 8.0 Beta 2
- Rebuild against Qt 2.3.0
- Re-enable default PATH for kdelibsdoc-dir
- Clean BuildRequires

* Thu Mar  8 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 1.4-5mdk
- removed BuildRequires for libreadline4

* Thu Mar 01 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-4mdk
- Requires: libjpeg-devel

* Wed Feb 28 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-3mdk
- Add BuildRequires

* Sun Feb 25 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-2mdk
- Repackage (update in KDE 2.1 sources)

* Fri Feb 23 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-1mdk
- Kdevelop 1.4

* Tue Feb 20 2001 David BAUDENS <baudens@mandrakesoft.com> 1.4-0.20010220.1mdk
- Enable --disable-debug
- Rewrite file list to fix updates
- Remove non needed %%find_lang

* Tue Feb 13 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010213.1mdk
- Update code
- rebuild for kde > beta 2

* Thu Jan 17 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.4mdk
- Fix requires

* Thu Jan 17 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.3mdk
- Fix requires

* Thu Jan 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.2mdk
- Fix requires

* Thu Jan 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.4-0.20010116.1mdk
- initial packaging
