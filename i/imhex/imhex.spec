Name: imhex
Version: 1.30.1
Release: alt1.1

Summary: A hex editor for reverse engineers and programmers

License: GPL-2.0-only AND Zlib AND MIT AND Apache-2.0
Group: Development/Other
Url: https://imhex.werwolv.net/

# Source-url: https://github.com/WerWolv/ImHex/releases/download/v%version/Full.Sources.tar.gz
Source: %name-%version.tar

# https://github.com/WerWolv/ImHex/commit/fc93f8bd664b5394f8ba8bcb3c18fcc424d6bdbd
Patch: %name-fmt10.patch

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
%patch0 -p1
rm -rv lib/external/{capstone,fmt,curl,nativefiledialog,yara,nlohmann_json}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo      \
    -DIMHEX_STRIP_RELEASE=OFF              \
    -DIMHEX_OFFLINE_BUILD=ON               \
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
cp -av lib/external/microtar/LICENSE microtar-LICENSE
cp -av lib/external/xdgpp/LICENSE xdgpp-LICENSE
rm -rv %buildroot%_datadir/licenses/imhex/

%files
%doc README.md *LICENSE
%_bindir/imhex
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%_libdir/libimhex.so*
%_libdir/%name/
%_datadir/metainfo/
%_datadir/metainfo/net.werwolv.imhex.appdata.xml

%check
# build binaries required for tests
%cmake_build --target unit_tests
%ctest --exclude-regex '(Helpers/StoreAPI|Helpers/TipsAPI|Helpers/ContentAPI)'

%_bindir/desktop-file-validate %buildroot/%_desktopdir/%name.desktop
%_bindir/appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/net.werwolv.%name.metainfo.xml

%changelog
* Wed Oct 18 2023 Nazarov Denis <nenderus@altlinux.org> 1.30.1-alt1.1
- NMU: Fix build with fmt 10

* Tue Jul 24 2023 Mikhail Tergoev <fidel@altlinux.org> 1.30.1-alt1
- Initial build for ALT Sisyphus
