Name: emacs-ghostel
Version: 0.59.0
Release: alt1

Summary: Terminal emulator for Emacs
License: GPL-3.0-or-later
Group: Terminals
URL: https://dakra.github.io/ghostel
VCS: https://github.com/dakra/ghostel

ExclusiveArch: aarch64 x86_64

Source0: %name-%version.tar
Source1: deps-%version.tar

BuildRequires: /proc
BuildRequires: zig rpm-macros-zig
BuildRequires: blueprint-compiler
BuildRequires: fontconfig-devel
BuildRequires: glslang
BuildRequires: highway-devel
BuildRequires: libfreetype-devel
BuildRequires: libsimdutf-devel
BuildRequires: libspirv-cross-devel
BuildRequires: libxml2-devel
BuildRequires: termutils-devel
BuildRequires: zlib-devel
BuildRequires: /usr/bin/emacs

%description
Ghostel is an Emacs terminal emulator powered by libghostty-vt - the same
VT engine that drives the Ghostty terminal. A native dynamic module written
in Zig handles terminal state, rendering, and local PTY I/O; Elisp manages
keymaps, buffers, commands, and remote process integration.

%define _zig_system_integration %nil
%define _zig_optimize_mode ReleaseFast
%define modulepath %_libdir/emacs/site-lisp

%prep
%setup -a1

%build
export EMACS_BIN_DIR=%_bindir
%zig_build \
	-fsys=fontconfig \
	-fsys=freetype \
	-fsys=glslang \
	-fsys=gtk4-layer-shell \
	-fsys=harfbuzz \
	-fsys=highway \
	-fsys=libpng \
	-fsys=oniguruma \
	-fsys=simdutf \
	-fsys=spirv-cross \
	-fsys=zlib \
    --prefix .

%install
install -pm0644 -D ghostel-module.so \
    %buildroot%modulepath/ghostel/ghostel-module.so
emacs -Q --batch -L lisp -f batch-byte-compile lisp/*.el
emacs -Q --batch --eval \
'(progn
    (setq generated-autoload-file
        (expand-file-name "ghostel-autoloads.el" "lisp"))
	(setq backup-inhibited t)
	(update-directory-autoloads "lisp"))'
cp -av etc lisp %buildroot%modulepath/ghostel

%ifdef bootstrap
tar cf %SOURCE1 --exclude '*/rules' zig-pkg
%endif

%files
%_libdir/emacs/site-lisp/ghostel

%changelog
* Tue Oct 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.59.0-alt1
- 0.59.0 released

* Mon Oct 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.57.0-alt1
- 0.57.0 released

* Mon Sep 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.56.0-alt1
- 0.56.0 released

* Wed Sep 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.53.0-alt1
- 0.53.0 released
