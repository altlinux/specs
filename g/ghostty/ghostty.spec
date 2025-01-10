%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name ghostty
%define ver_major 1.0
%define beta %nil
%define xdg_name com.mitchellh.%_name

%def_disable bootstrap

Name: %_name
Version: %ver_major.1
Release: alt1%beta

Summary: Ghostty terminal emulator
License: MIT
Group: Terminals
Url: https://ghostty.org

Vcs: https://github.com/ghostty-org/ghostty.git

%if_disabled snapshot
Source: https://release.files.ghostty.org/%version/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-vendor.tar

# aarch64 build failed
#ExclusiveArch: %zig_arches
ExclusiveArch: x86_64

%define adwaita_ver 1.6

Provides: xvt
Provides: x-terminal-emulator

BuildRequires(pre): rpm-macros-zig rpm-macros-alternatives
BuildRequires: zig llvm-devel
BuildRequires: pandoc
BuildRequires: pkgconfig(oniguruma)
BuildRequires: pkgconfig(bzip2)
BuildRequires: /usr/bin/tic
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver

%description
Ghostty is a fast, feature-rich, and cross-platform terminal emulator
that uses platform-native UI and GPU acceleration.

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
export ZIG_GLOBAL_CACHE_DIR=zig-cache
./nix/build-support/fetch-zig-cache.sh
tar -cf %_sourcedir/%name-%version%beta-vendor.tar zig-cache}

cp -r ./vendor %_zig_cache_dir

%build
%define _zig_cache_dir ${PWD}/zig-cache

#ReleaseSafe -- too slow

zig build \
    --verbose --release=safe \
    -Dtarget=native -Dcpu=baseline \
    -Doptimize=ReleaseFast \
    --system %_zig_cache_dir/p \
    --cache-dir %_zig_cache_dir \
    --global-cache-dir %_zig_cache_dir
%nil

%install
export DESTDIR=%buildroot
zig build \
    --verbose --release=safe \
    -Dtarget=native -Dcpu=baseline \
    -Doptimize=ReleaseFast \
    --system %_zig_cache_dir/p \
    --cache-dir %_zig_cache_dir \
    --global-cache-dir %_zig_cache_dir \
    install \
    --prefix %_prefix \
    --prefix-lib-dir %_libdir \
    --prefix-exe-dir %_bindir \
    --prefix-include-dir %_includedir \

# alternatives (xterm -- 40, g-t -- 39, blackbox -- 38, terminology --30)
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt	%_bindir/%_name	29
%_bindir/x-terminal-emulator	%_bindir/%_name	29
EOF

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%_name
%_datadir/%_name/
%_desktopdir/%xdg_name.desktop
%_datadir/terminfo/%_name.*
%_datadir/terminfo/g/%_name
%_datadir/terminfo/x/xterm-%_name
%_datadir/bash-completion/completions/%_name.bash
%_datadir/fish/vendor_completions.d/%_name.fish
%_datadir/zsh/site-functions/_%{_name}
%_iconsdir/hicolor/*/apps/%{xdg_name}*.*
%_datadir/vim/vimfiles/*/*
%_datadir/nvim/site/*/*
#%_datadir/metainfo/%xdg_name.metainfo.xml
%_altdir/%name
%_man1dir/%_name.1*
%_man5dir/%_name.5*
%doc README*

%changelog
* Sat Jan 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus


