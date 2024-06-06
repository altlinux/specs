%add_findreq_skiplist %_libdir/imhex/plugins/*

Name: imhex
Version: 1.34.0
Release: alt1

Summary: A hex editor for reverse engineers and programmers

License: GPL-2.0-only AND Zlib AND MIT AND Apache-2.0
Group: Development/Other
Url: https://imhex.werwolv.net/

# Source-url: https://github.com/WerWolv/ImHex/releases/download/v%version/Full.Sources.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cli11-devel libcapstone-devel libcurl-devel libfmt-devel libglfw3-devel libmagic-devel libmbedtls-devel libnativefiledialog-extended-devel libyara-devel nlohmann-json-devel libfreetype-devel
BuildRequires: cmake gcc-c++
BuildRequires: ctest

# For desktop file & AppData
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

ExcludeArch: %ix86 armh

%description
ImHex is a Hex Editor, a tool to display, decode and analyze binary data to
reverse engineer their format, extract informations or patch values in them.

What makes ImHex special is that it has many advanced features that can often
only be found in paid applications. Such features are a completely custom binary
template and pattern language to decode and highlight structures in the data, a
graphical node-based data processor to pre-process values before they're
displayed, a disassembler, diffing support, bookmarks and much much more. At the
same time ImHex is completely free and open source under the GPLv2 language.

%prep
%setup
rm -rv lib/third_party/{capstone,fmt,nativefiledialog,yara,nlohmann_json}
sed -i '/generateSDKDirectory()/d' CMakeLists.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo      \
    -DIMHEX_STRIP_RELEASE=OFF              \
    -DIMHEX_OFFLINE_BUILD=ON               \
    -DIMHEX_ENABLE_UNIT_TESTS=ON           \
    -DUSE_SYSTEM_NLOHMANN_JSON=ON          \
    -DUSE_SYSTEM_FMT=ON                    \
    -DUSE_SYSTEM_CURL=ON                   \
    -DUSE_SYSTEM_CAPSTONE=ON               \
    -DUSE_SYSTEM_YARA=ON                   \
    -DUSE_SYSTEM_NFD=ON                    \
    -DUSE_SYSTEM_LLVM=OFF

%cmake_build

%install
%cmake_install

# install licenses
cp -av lib/third_party/microtar/LICENSE microtar-LICENSE
cp -av lib/third_party/xdgpp/LICENSE xdgpp-LICENSE
rm -rv %buildroot%_datadir/licenses

# this is a symlink for the old appdata name that we don't need
rm -fv %buildroot%_datadir/metainfo/net.werwolv.%name.appdata.xml

# drop updater binary
rm -fv %buildroot%_bindir/imhex-updater

%check
# build binaries required for tests
%cmake_build --target unit_tests
%ctest --exclude-regex '(Helpers/StoreAPI|Helpers/TipsAPI|Helpers/ContentAPI)'

%_bindir/desktop-file-validate %buildroot/%_desktopdir/%name.desktop
%_bindir/appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/net.werwolv.%name.metainfo.xml

%files
%doc README.md *LICENSE
%_bindir/imhex
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%_libdir/libimhex.so*
%_libdir/%name/
%_datadir/metainfo/*

%changelog
* Thu Jun 06 2024 Mikhail Tergoev <fidel@altlinux.org> 1.34.0-alt1
- updated to upstream 1.34.0

* Mon Apr 01 2024 Mikhail Tergoev <fidel@altlinux.org> 1.33.2-alt1
- updated to upstream 1.33.2

* Tue Mar 05 2024 Mikhail Tergoev <fidel@altlinux.org> 1.33.1-alt1
- updated to upstream 1.33.1

* Tue Jan 09 2024 Mikhail Tergoev <fidel@altlinux.org> 1.32.2-alt1
- update to upstream 1.32.2

* Wed Oct 18 2023 Mikhail Tergoev <fidel@altlinux.org> 1.31.0-alt1
- update to upstream 1.31.0

* Wed Oct 18 2023 Nazarov Denis <nenderus@altlinux.org> 1.30.1-alt1.1
- NMU: Fix build with fmt 10

* Tue Jul 24 2023 Mikhail Tergoev <fidel@altlinux.org> 1.30.1-alt1
- Initial build for ALT Sisyphus
