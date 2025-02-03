%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name ghostty
%define ver_major 1.1
%define beta %nil
%define xdg_name com.mitchellh.%_name

%def_enable check
%def_disable bootstrap

Name: %_name
Version: %ver_major.0
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

ExclusiveArch: %zig_arches
#ExclusiveArch: x86_64

%define adwaita_ver 1.6

Provides: xvt
Provides: x-terminal-emulator

BuildRequires(pre): rpm-macros-zig rpm-macros-alternatives rpm-build-python3 rpm-build-gir
BuildRequires: zig
BuildRequires: pandoc
BuildRequires: pkgconfig(oniguruma)
BuildRequires: pkgconfig(bzip2)
BuildRequires: /usr/bin/tic
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_check:BuildRequires: /dev/pts fonts-ttf-gnu-freefont-mono}

%description
Ghostty is a fast, feature-rich, and cross-platform terminal emulator
that uses platform-native UI and GPU acceleration.

%package nautilus
Summary: Nautilus extension for the Ghostty
Group: Graphical desktop/GNOME
Requires: %name = %EVR
Requires: nautilus-python
%add_python3_path %_datadir/nautilus-python/extensions

%description nautilus
This package provides integration with the Ghostty for the Nautilus file
manager.

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
export ZIG_GLOBAL_CACHE_DIR=zig-cache
./nix/build-support/fetch-zig-cache.sh
tar -cf %_sourcedir/%name-%version%beta-vendor.tar zig-cache}

cp -r ./vendor %_zig_cache_dir

%build
%define _zig_cache_dir ${PWD}/zig-cache
%define _zig_system_integration --system %_zig_cache_dir/p
%define _zig_optimize_mode ReleaseFast
%zig_build
%nil

%install
DESTDIR=%buildroot \
%__zig build install %{?_zig_build_options} %{?_zig_install_options}

# alternatives (xterm -- 40, g-t -- 39, blackbox -- 38, terminology --30)
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt	%_bindir/%_name	29
%_bindir/x-terminal-emulator	%_bindir/%_name	29
EOF

%find_lang --with-gnome %name

%check
%__zig build test %{?_zig_build_options}


%files -f %name.lang
%_bindir/%_name
%_datadir/%_name/
%_desktopdir/%xdg_name.desktop
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

%files nautilus
%_datadir/nautilus-python/extensions/%xdg_name.py
%_datadir/nautilus-python/extensions/__pycache__/*

%changelog
* Fri Jan 31 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat Jan 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus


