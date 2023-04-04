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
%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtwebengine
%ifarch %ix86
%set_verify_elf_method relaxed
%endif
%def_enable always_reducing_debuginfo

%define is_ffmpeg %([ -n "`rpmquery --qf '%%{SOURCERPM}' libavformat-devel 2>/dev/null | grep -e '^libav'`" ] && echo 0 || echo 1)
%if %is_ffmpeg
%define qt_ffmpeg_type system-ffmpeg
%else
%define qt_ffmpeg_type %nil
%endif

Name: qt6-webengine
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtWebEngine components
Url: http://qt.io/
License: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
ExclusiveArch: %qt6_qtwebengine_arches

Source: %qt_module-everywhere-src-%version.tar
Source100: jquery.min.js
Source101: jquery.tablesorter.min.js
Patch1: alt-ftbfs.patch
# Debian
Patch200: remove_catapult_3rdparty.patch
Patch201: remove_catapult_core.patch

BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires(pre): libavformat-devel
BuildRequires: cmake libstdc++-devel-static
BuildRequires: libxkbcommon-devel libxkbfile-devel
%if %is_ffmpeg
BuildRequires: libavcodec-devel libavutil-devel libavformat-devel libswresample-devel libopus-devel
%endif
BuildRequires: libvpx-devel
BuildRequires: /proc
BuildRequires: flex libicu-devel libEGL-devel libdrm-devel
BuildRequires: libgio-devel libkrb5-devel
BuildRequires: git-core gperf libalsa-devel libcap-devel libdbus-devel libevent-devel libexpat-devel libjpeg-devel libminizip-devel libnss-devel
BuildRequires: libharfbuzz-devel fontconfig-devel
BuildRequires: libXcomposite-devel libXcursor-devel libXrandr-devel libXi-devel libxshmfence-devel libXtst-devel
BuildRequires: libXdamage-devel
BuildRequires: libcups-devel
BuildRequires: gyp libudev-devel libxml2-devel jsoncpp-devel liblcms2-devel
BuildRequires: libopus-devel libpci-devel libpng-devel libprotobuf-devel libpulseaudio-devel libre2-devel libsnappy-devel libsrtp2-devel
BuildRequires: libwebp-devel libxslt-devel ninja-build protobuf-compiler libva-devel libvdpau-devel
BuildRequires: libopenjpeg2.0-devel
BuildRequires: node-yargs node-terser
BuildRequires: python3(json) python3(html5lib)
BuildRequires: qt6-multimedia-devel qt6-svg-devel qt6-tools-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-websockets-devel qt6-webchannel-devel qt6-positioning-devel
#BuildRequires: qt6-phonon-devel

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: qt6-base-devel
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

%package -n libqt6-webengine
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
#Requires: qt6-quickcontrols2
%description -n libqt6-webengine
%summary

%package -n libqt6-webenginecore
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
#Requires: qt6-quickcontrols2
%description -n libqt6-webenginecore
%summary

%package -n libqt6-webenginewidgets
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
#Requires: qt6-quickcontrols2
%description -n libqt6-webenginewidgets
%summary

%package -n libqt6-pdf
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-pdf
%summary

%package -n libqt6-pdfwidgets
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-pdfwidgets
%summary

%package -n libqt6-pdfquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-pdfquick
%summary

%package -n libqt6-webenginequickdelegatesqml
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-webenginequickdelegatesqml
%summary

%package -n libqt6-webenginequick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-webenginequick
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
%patch200 -p1
%patch201 -p1
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
pushd src/3rdparty/chromium/third_party/jstemplate
    cat util.js jsevalcontext.js jstemplate.js exports.js >jstemplate_compiled.js
popd
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

#syncqt.pl-qt6  -version %version

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
%global __qt6_build_tool ninja
%Q6cmake \
    --log-level=STATUS \
    -DCMAKE_TOOLCHAIN_FILE:STRING="%_libdir/cmake/Qt6/qt.toolchain.cmake" \
%if %is_ffmpeg
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
    -DFEATURE_webengine_webrtc_pipewire:BOOL=OFF \
    -DFEATURE_webengine_spellchecker:BOOL=OFF \
    -DFEATURE_webengine_native_spellchecker:BOOL=OFF \
    #
#    -DFEATURE_webengine_spellchecker:BOOL=ON \
#    -DFEATURE_webengine_native_spellchecker:BOOL=OFF \
#make -Onone
%Q6make
%if %qdoc_found
cmake --build BUILD --target docs ||:
%endif

%install
%Q6install_qt
%if %qdoc_found
cmake --install BUILD --target docs ||:
%endif

%if_disabled system_icu
install -m 0644 \
    src/3rdparty/chromium/third_party/icu/common/icudtl.dat \
    %buildroot/%_qt6_datadir/resources/
%endif

# fix cmake dependencies
%IF_ver_not_eq %_qt6_version %version
sed -i -e \
  "s|%version[[:space:]][[:space:]]*\${_Qt6WebEngine\(.*_FIND_VERSION_EXACT\)|%_qt6_version \${_Qt6WebEngine\1|" \
  %buildroot/%_libdir/cmake/Qt6WebEngine*/Qt6WebEngine*Config.cmake
%endif

# find translations
echo "%%defattr(644,root,root,755)" >translations_list.lang
find %buildroot/%_qt6_translationdir/qtwebengine_locales -type f -name \*.pak | \
while read t
do
    lang_file=`basename $t`
    lang_name=`echo "$lang_file" | sed -e 's|\.pak$||' -e 's|-|_|'`
    if echo $lang_name | grep -q ^en
    then
	echo "%%_qt6_translationdir/qtwebengine_locales/$lang_file" >>translations_list.lang
    else
	echo "%%lang($lang_name) %%_qt6_translationdir/qtwebengine_locales/$lang_file" >>translations_list.lang
    fi
done

%files common -f translations_list.lang
%doc LICENSES/*
%dir %_qt6_translationdir/qtwebengine_locales/
%dir %_qt6_datadir/resources/
%_qt6_datadir/resources/qtwebengine*.pak
%if_disabled system_icu
%_qt6_datadir/resources/*icu*
%endif

%files -n libqt6-webenginequick
%_qt6_libdir/libQt?WebEngineQuick.so.*
%files -n libqt6-webenginequickdelegatesqml
%_qt6_libdir/libQt?WebEngineQuickDelegatesQml.so.*
%_qt6_qmldir/QtWebEngine/
%files -n libqt6-webenginecore
%_qt6_libdir/libQt?WebEngineCore.so.*
%_qt6_libexecdir/QtWebEngineProcess
%files -n libqt6-webenginewidgets
%_qt6_libdir/libQt?WebEngineWidgets.so.*
%files -n libqt6-pdf
%_qt6_libdir/libQt?Pdf.so.*
%_qt6_plugindir/imageformats/libqpdf.so
%files -n libqt6-pdfquick
%_qt6_libdir/libQt?PdfQuick.so.*
%_qt6_qmldir/QtQuick/Pdf/
%files -n libqt6-pdfwidgets
%_qt6_libdir/libQt?PdfWidgets.so.*

%files doc
%if %qdoc_found
#%_qt6_docdir/*
%endif
#%_qt6_examplesdir/*

%files devel
#%_bindir/qwebengine_convert_dict*
#%_qt6_bindir/qwebengine_convert_dict*
#
%_qt6_libexecdir/gn
#
%_qt6_plugindir/designer/libqwebengineview.so
%_qt6_headerdir/QtWebEngine*/
%_qt6_headerdir/QtPdf*/
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/qt_*.pri
%_qt6_libdir/metatypes/qt6*.json
%_qt6_datadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Mon Jun 06 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- workaround agains build system open descriptors limit

* Thu Jun 02 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
