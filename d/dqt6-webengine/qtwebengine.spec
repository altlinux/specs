%define IF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define IF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define IF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"
%define IF_ver_eq() %if "%(rpmvercmp '%1' '%2')" == "0"
%define IF_ver_not_gt() %if "%(rpmvercmp '%1' '%2')" <= "0"
%define IF_ver_not_gteq() %if "%(rpmvercmp '%1' '%2')" < "0"
%define IF_ver_not_lt() %if "%(rpmvercmp '%2' '%1')" <= "0"
%define IF_ver_not_lteq() %if "%(rpmvercmp '%2' '%1')" < "0"
%define IF_ver_not_eq() %if "%(rpmvercmp '%1' '%2')" != "0"
%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module dqtwebengine
%ifarch %ix86
%set_verify_elf_method relaxed
%endif
%def_enable always_reducing_debuginfo

%define ffmpeg_ver %{get_version libavformat-devel}
#define is_ffmpeg %([ -n "`rpmquery --qf '%%{SOURCERPM}' libavformat-devel 2>/dev/null | grep -e '^libav'`" ] && echo 0 || echo 1)
%IF_ver_gteq %ffmpeg_ver 5
%def_disable system_ffmpeg
%else
%def_enable system_ffmpeg
%endif

Name: dqt6-webengine
Version: 6.10.3
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - QtWebEngine components
Url: http://qt.io/
License: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
ExclusiveArch: %dqt6_qtwebengine_arches

Source: %qt_module-everywhere-src-%version.tar.gz
Source100: jquery.min.js
Source101: jquery.tablesorter.min.js
Patch1: alt-ftbfs.patch
# FC
Patch10: qtwebengine-link-pipewire.patch
Patch11: qtwebengine-aarch64-new-stat.patch
Patch12: qtwebengine-fix-arm-build.patch
Patch13: qtwebengine-use-openh264.patch
Patch14: qtwebengine-SIOCGSTAMP.patch
Patch15: qtwebengine-add-missing-pipewire-headers.patch
Patch16: qtwebengine-chromium-141-glibc-2.42-SYS_SECCOMP.patch
# Debian
Patch200: remove_catapult_3rdparty.patch
Patch201: remove_catapult_core.patch
Patch202: compressing_files.patch
# LoongArch
Patch3500: qt6-webengine-6.7.1-loongarch64.patch

BuildRequires(pre): rpm-macros-dqt6-webengine
BuildRequires(pre): rpm-macros-dqt6 dqt6-tools
BuildRequires(pre): libavformat-devel
BuildRequires: /proc
BuildRequires: clang-devel
BuildRequires: cmake libstdc++-devel-static
BuildRequires: libxkbcommon-devel libxkbfile-devel
%if_enabled system_ffmpeg
BuildRequires: libavcodec-devel libavutil-devel libavformat-devel libswresample-devel
%endif
BuildRequires: libvpx-devel libopenh264-devel
BuildRequires: /proc
BuildRequires: flex libicu-devel libEGL-devel libdrm-devel libgbm-devel libepoxy-devel
BuildRequires: libgio-devel libkrb5-devel
BuildRequires: git-core gperf libalsa-devel libcap-devel libdbus-devel libevent-devel libexpat-devel libminizip-devel libnss-devel
BuildRequires: libharfbuzz-devel fontconfig-devel
BuildRequires: libXcomposite-devel libXcursor-devel libXrandr-devel libXi-devel libxshmfence-devel libXtst-devel
BuildRequires: libXdamage-devel
BuildRequires: libcups-devel
BuildRequires: gyp libudev-devel libxml2-devel jsoncpp-devel liblcms2-devel
BuildRequires: libopus-devel libpulseaudio-devel pipewire-libs-devel
BuildRequires: libpci-devel libprotobuf-devel protobuf-compiler libre2-devel libsnappy-devel libsrtp2-devel
BuildRequires: libpng-devel libjpeg-devel libtiff-devel libwebp-devel
BuildRequires: libxslt-devel libva-devel libvdpau-devel
BuildRequires: libhunspell-devel
BuildRequires: ninja-build gn
BuildRequires: libopenjpeg2.0-devel
BuildRequires: node-yargs node-terser
BuildRequires: python3(json) python3(html5lib)
BuildRequires: dqt6-multimedia-devel dqt6-svg-devel dqt6-tools-devel
BuildRequires: dqt6-declarative-devel
BuildRequires: dqt6-websockets-devel dqt6-webchannel-devel dqt6-positioning-devel
BuildRequires: libdqt6-quicktemplates2 libdqt6-quickcontrols2 libdqt6-quickwidgets libdqt6-quicktest libdqt6-designer libdqt6-qmlcompiler libdqt6-printsupport vulkan-headers libdqt6-help
#BuildRequires: dqt6-phonon-devel

# find librares
%add_findprov_lib_path %_dqt6_libdir

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: dqt6-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libdqt6-webengine
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
#Requires: dqt6-quickcontrols2
%description -n libdqt6-webengine
%summary

%package -n libdqt6-webenginecore
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
#Requires: dqt6-quickcontrols2
%description -n libdqt6-webenginecore
%summary

%package -n libdqt6-webenginewidgets
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
#Requires: dqt6-quickcontrols2
%description -n libdqt6-webenginewidgets
%summary

%package -n libdqt6-pdf
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-pdf
%summary

%package -n libdqt6-pdfwidgets
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-pdfwidgets
%summary

%package -n libdqt6-pdfquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-pdfquick
%summary

%package -n libdqt6-webenginequickdelegatesqml
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-webenginequickdelegatesqml
%summary

%package -n libdqt6-webenginequick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
Provides: %name = %EVR
Obsoletes: %name < %EVR
%description -n libdqt6-webenginequick
%summary

%prep
%define icu_ver %{get_version libicu-devel}
%IF_ver_gteq %icu_ver 5.9
%def_enable system_icu
%else
%def_disable system_icu
%endif
%setup -n %qt_module-everywhere-src-%version
#
%patch1 -p1
#
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
#
#%patch200 -p1
#%patch201 -p1
%patch202 -p1
%ifarch loongarch64
%patch3500 -p2
%endif
#
#ln -s /usr/include/nspr src/3rdparty/chromium/nspr4

# delete all "toolprefix = " lines from build/toolchain/linux/BUILD.gn, as we
# never cross-compile in native Fedora RPMs, fixes ARM and aarch64 FTBFS
sed -i -e '/toolprefix = /d' -e 's/\${toolprefix}//g' \
  src/3rdparty/chromium/build/toolchain/linux/BUILD.gn
# http://bugzilla.redhat.com/1337585
# can't just delete, but we'll overwrite with system headers to be on the safe side
cp -bv /usr/include/re2/*.h src/3rdparty/chromium/third_party/re2/src/re2/
# add compile flags
sed -i 's|"-fPIC"|"-DPIC","-fPIC"|' src/3rdparty/chromium/build/config/compiler/BUILD.gn
sed -i 's|"-fPIC"|"-DPIC","-fPIC"|' src/3rdparty/chromium/third_party/*/BUILD.gn

%if_enabled always_reducing_debuginfo
sed -i -e 's/symbol_level=2/symbol_level=1/g' cmake/Functions.cmake
%endif
%ifnarch x86_64
# most arches run out of memory with full debuginfo, so use -g1 on non-x86_64
sed -i -e 's/symbol_level=2/symbol_level=1/g' cmake/Functions.cmake
%endif
sed -i -e 's/symbol_level=[[:digit:]]/symbol_level=0/g' cmake/Functions.cmake


# redefine _FORTIFY_SOURCE
for f in \
    src/3rdparty/chromium/build/config/compiler/BUILD.gn \
    src/3rdparty/chromium/third_party/minigbm/src/common.mk
do
    sed -i 's|_FORTIFY_SOURCE=[[:digit:]]|_FORTIFY_SOURCE=1|g' $f
done

# install missing files
for f in \
    src/3rdparty/chromium/third_party/devtools-frontend/src/front_end/third_party/lighthouse/lighthouse-dt-bundle.js \
    src/3rdparty/chromium/third_party/devtools-frontend/src/front_end/third_party/lighthouse/report-assets/report-generator.js \
    src/3rdparty/chromium/third_party/devtools-frontend/src/front_end/diff/diff_match_patch.js
do mkdir -p `dirname $f`; touch $f; done
# jQuery 
cp %SOURCE100 examples/webenginewidgets/contentmanipulation/
cp %SOURCE100 src/3rdparty/chromium/third_party/pycoverage/coverage/htmlfiles/
cp %SOURCE101 src/3rdparty/chromium/third_party/pycoverage/coverage/htmlfiles/

# copy the Chromium license so it is installed with the appropriate name
cp -p src/3rdparty/chromium/LICENSE LICENSES/LICENSE.Chromium

# fix find system ninja
mkdir -p bin
ln -s %_bindir/ninja-build bin/ninja
# fix find system python
ln -s %__python3 bin/python

#syncqt.pl-dqt6  -version %version

%build
ulimit -n $(ulimit -Hn) ||:
%add_optflags %optflags_shared -Wno-error=return-type
export PATH=$PWD/bin:$PATH
NUM_PROCS="%__nprocs"
cat /proc/meminfo | grep ^Mem
cat /sys/fs/cgroup/user.slice/user-${UID}.slice/memory.max ||:
cat /sys/fs/cgroup/user.slice/user-${UID}.slice/memory.high ||:
ulimit -a | grep mem
MEM_PER_PROC=10000000
MAX_MEM=`grep ^MemTotal: /proc/meminfo | sed -e 's|^\(.*\)[[:space:]].*|\1|' -e 's|.*[[:space:]]||'`
#NUM_PROCS="$(($MAX_MEM / $MEM_PER_PROC))"
[ "$NUM_PROCS" -ge 2  ] || NUM_PROCS=2
[ "$NUM_PROCS" -le 16  ] || NUM_PROCS=16

export NPROCS=$NUM_PROCS
export STRIP=strip
export NINJAFLAGS="-v -j $NUM_PROCS"
export NINJAJOBS="-j $NUM_PROCS"
export NINJA_PATH=%_bindir/ninja-build
OPTFLAGS="%optflags"
%if_enabled always_reducing_debuginfo
export OPTFLAGS=`echo "$OPTFLAGS" | sed -e 's/ -g / -g1 /g'`
%endif
%ifnarch x86_64
# most arches run out of memory with full debuginfo, so use -g1 on non-x86_64
export OPTFLAGS=`echo "$OPTFLAGS" | sed -e 's/ -g / -g1 /g'`
%endif
export RPM_OPT_FLAGS="$OPTFLAGS"
export CFLAGS="$OPTFLAGS" CXXFLAGS="$OPTFLAGS"
%if "%_lib" == "lib"
export LDFLAGS+="-Wl,--no-keep-memory -Wl,--hash-size=31 -Wl,--reduce-memory-overheads"
%endif
%global _dqt6_build_tool ninja
%DQ6cmake \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    --log-level=STATUS \
    -DCMAKE_TOOLCHAIN_FILE:STRING="%_dqt6_libdir/cmake/Qt6/qt.toolchain.cmake" \
%if_enabled system_ffmpeg
    -DFEATURE_webengine_system_ffmpeg:BOOL=ON \
%endif
%if_enabled system_icu
    -DFEATURE_webengine_system_icu:BOOL=ON \
%endif
    -DFEATURE_webengine_system_libevent:BOOL=ON \
    -DFEATURE_webengine_system_libopenjpeg2:BOOL=ON \
    -DFEATURE_qtpdf_build:BOOL=ON \
    -DFEATURE_qtpdf_widgets_build:BOOL=ON \
    -DFEATURE_qtpdf_quick_build:BOOL=ON \
    -DFEATURE_webengine_proprietary_codecs:BOOL=ON \
    -DFEATURE_webengine_kerberos:BOOL=ON \
    -DFEATURE_webengine_developer_build:BOOL=OFF \
    -DFEATURE_webengine_embedded_build:BOOL=OFF \
    -DFEATURE_webengine_extensions:BOOL=ON \
    -DFEATURE_webengine_webrtc:BOOL=ON \
    -DFEATURE_webengine_webrtc_pipewire:BOOL=ON \
    -DFEATURE_webengine_spellchecker:BOOL=ON \
    -DFEATURE_webengine_native_spellchecker:BOOL=OFF \
    #
%DQ6make
%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
#cmake --install BUILD --target docs ||:
mkdir -p %buildroot/%_docdir/dqt6/
cp -ar BUILD/share/doc/dqt6/* %buildroot/%_docdir/dqt6/
%endif

%if_disabled system_icu
install -m 0644 \
    src/3rdparty/chromium/third_party/icu/common/icudtl.dat \
    %buildroot/%_dqt6_datadir/resources/
%endif

# fix cmake dependencies
%IF_ver_not_eq %_dqt6_version %version
sed -i -e \
  "s|%version[[:space:]][[:space:]]*\${_Qt6WebEngine\(.*_FIND_VERSION_EXACT\)|%_dqt6_version \${_Qt6WebEngine\1|" \
  %buildroot/%_dqt6_libdir/cmake/Qt6WebEngine*/Qt6WebEngine*Config.cmake
%endif
# relax depends on plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?*/{*,}/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

# find translations
echo "%%defattr(644,root,root,755)" >translations_list.lang
find %buildroot/%_dqt6_translationdir/qtwebengine_locales -type f -name \*.pak | \
while read t
do
    lang_file=`basename $t`
    lang_name=`echo "$lang_file" | sed -e 's|\.pak$||' -e 's|-|_|'`
    if echo $lang_name | grep -q ^en
    then
	echo "%%_dqt6_translationdir/qtwebengine_locales/$lang_file" >>translations_list.lang
    else
	echo "%%lang($lang_name) %%_dqt6_translationdir/qtwebengine_locales/$lang_file" >>translations_list.lang
    fi
done

%files common -f translations_list.lang
%doc LICENSES/*
%dir %_dqt6_translationdir/qtwebengine_locales/
%dir %_dqt6_datadir/resources/
%_dqt6_datadir/resources/*

%files -n libdqt6-webenginequick
%_dqt6_libdir/libQt?WebEngineQuick.so.*
%_dqt6_qmldir/QtWebEngine/
%files -n libdqt6-webenginequickdelegatesqml
%_dqt6_libdir/libQt?WebEngineQuickDelegatesQml.so.*
%files -n libdqt6-webenginecore
%_dqt6_libdir/libQt?WebEngineCore.so.*
%_dqt6_libexecdir/webenginedriver
%_dqt6_libexecdir/QtWebEngineProcess
%files -n libdqt6-webenginewidgets
%_dqt6_libdir/libQt?WebEngineWidgets.so.*
%files -n libdqt6-pdf
%_dqt6_libdir/libQt?Pdf.so.*
%_dqt6_plugindir/imageformats/libqpdf.so
%files -n libdqt6-pdfquick
%_dqt6_libdir/libQt?PdfQuick.so.*
%_dqt6_qmldir/QtQuick/Pdf/
%files -n libdqt6-pdfwidgets
%_dqt6_libdir/libQt?PdfWidgets.so.*

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif
%_dqt6_examplesdir/*

%files devel
#%_bindir/qwebengine_convert_dict*
#%_dqt6_bindir/qwebengine_convert_dict*
#
%_dqt6_libexecdir/gn
%_dqt6_libexecdir/qwebengine_convert_dict
#
%_dqt6_plugindir/designer/libqwebengineview.so
%_dqt6_headerdir/QtWebEngine*/
%_dqt6_headerdir/QtPdf*/
%_dqt6_libdatadir/libQt*.so
%_dqt6_libdir/libQt*.so
%_dqt6_libdir/libQt*.prl
%_dqt6_libdatadir/libQt*.prl
%_dqt6_libdir/cmake/Qt*/
%_dqt6_archdatadir/mkspecs/modules/qt_*.pri
%_dqt6_archdatadir/metatypes/qt6*.json
%_dqt6_archdatadir/modules/*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc

%changelog
* Wed Jun 10 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.3-alt0.dde.1
- merge with new version

* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Wed Feb 25 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.2-alt0.dde.1
- merge with new version

* Thu Feb 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- new version

* Tue Jan 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.1-alt1
- new version

* Fri Nov 21 2025 Leontiy Volodin <lvol@altlinux.org> 6.9.3-alt0.dde.1
- merge with new version

* Thu Nov 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt1
- new version

* Tue Sep 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt3
- add fix against rendering issue (closes: 55903)

* Mon Sep 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt2
- add some fixes from Fedora

* Tue Aug 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt1
- new version

* Thu Aug 07 2025 Leontiy Volodin <lvol@altlinux.org> 6.9.1-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Jun 03 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.1-alt1
- new version

* Wed Mar 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt3
- enable spellchecker

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt2
- fix compile on arm

* Thu Feb 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt1
- new version

* Tue Aug 27 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt3
- build to repo

* Mon Aug 26 2024 Ivan A. Melnikov <iv@altlinux.org> 6.7.2-alt2
- Update loongarch64 patches
  + import updated cumulative patch from
     https://github.com/AOSC-Dev/chromium-loongarch64
  + drop loongarch-don-t-break-other-arches.patch, not needed
    after 6.6.2-alt3

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Wed Apr 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt3
- apply LoongArch patches only for loongarch64 build

* Fri Feb 23 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 6.6.2-alt2
- Added LoongArch support patch from
  https://github.com/AOSC-Dev/chromium-loongarch64
  commit 651c6a0455330c97
- Fixup LoongArch patch to not break break other arches

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Thu Nov 23 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt2
- fix to build with icu-74

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Mon Oct 02 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt3
- split modules to separate package

* Mon Sep 04 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt2
- update debian patches

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Mon Jun 06 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- workaround agains build system open descriptors limit

* Thu Jun 02 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
