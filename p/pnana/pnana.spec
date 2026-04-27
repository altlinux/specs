%define _unpackaged_files_terminate_build 1

Name: pnana
Version: 0.0.6
Release: alt1

Summary: Modern Terminal Text Editor
License: MIT
Group: Editors
Url: https://github.com/Cyxuan0311/PNANA
VCS: https://github.com/Cyxuan0311/PNANA.git

# Source-url: https://github.com/Cyxuan0311/PNANA/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor.tar
Patch1: alt-prepare-offline-build.patch
Patch3: alt-fix-moving-file-by-btn.patch
Patch4: alt-fix-copying-cache-dir.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: golang
BuildRequires: libcurl-devel
BuildRequires: libftxui-devel
BuildRequires: libtree-sitter-devel
BuildRequires: lua-devel
BuildRequires: chafa-devel

# ffmpeg libs
BuildRequires: libavformat-devel
BuildRequires: libswscale-devel

%description
%name is a modern terminal text editor built with FTXUI, inspired by
Nano, Micro, and Sublime Text. It provides a friendly user interface,
intuitive keyboard shortcuts, and powerful editing features.

%prep
%setup -a1
%autopatch -p1
sed -i 's;\(DESTINATION\s\+\)\.config/\(%name.*\);\1%_datadir/\2;' CMakeLists.txt

%build
%cmake \
    -DPNANA_VERSION=%version \
    -DBUILD_IMAGE_PREVIEW=ON \
    -DBUILD_TREE_SITTER=ON \
    -DBUILD_LUA=ON \
    -DBUILD_GO=ON \
    -DBUILD_AI_CLIENT=ON \
    #
%cmake_build

%install
%cmake_install
rm -f %buildroot%_datadir/%name/install.sh

mkdir -p %buildroot%_libdir/%name
mv %buildroot%_bindir/%name %buildroot%_libdir/%name/%name-bin
cat > %buildroot%_bindir/%name <<EOF
#!/bin/sh

config_dir="\$HOME/.config/%name"
[[ -f \$config_dir/config.json ]] || \\
    install -Dpm 644 %_datadir/%name/config.json \$config_dir/config.json

%_libdir/%name/%name-bin "\$@"
EOF
chmod 755 %buildroot%_bindir/%name

%files
%doc README.md
%dir %_libdir/%name
%dir %_datadir/%name
%_bindir/%name
%_libdir/%name/%name-bin
%_datadir/%name/config.json

%changelog
* Mon Apr 27 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.0.6-alt1
- new version

* Thu Apr 16 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.0.5-alt4
- fix incorrect copying of cache to pnana config dir

* Wed Apr 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.0.5-alt3
- fix file moving failure to target directory on F6 key press (closes: 58744)

* Wed Apr 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.0.5-alt2
- set the correct latest version of the project (closes: 58736)

* Fri Apr 10 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.0.5-alt1
- initial build for ALT Linux
