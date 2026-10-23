Name: fuse-zip
Version: 0.7.2
Release: alt1

Summary: Filesystem to navigate, extract, create and modify ZIP archives
Group: System/Kernel and hardware
License: GPL-3.0-or-later

Url: https://bitbucket.org/agalanin/fuse-zip/

# Source-url: https://bitbucket.org/agalanin/fuse-zip/downloads/%name-%version.tar.gz
Source: %name-%version.tar

Requires: fuse

BuildRequires: gcc-c++
BuildRequires: libzip-devel
BuildRequires: libfuse-devel

%description
With fuse-zip you really can work with ZIP archives as real directories.

Unlike KIO or Gnome VFS, it can be used in any application without
modifications.

Unlike other FUSE filesystems, only fuse-zip provides write support
to ZIP archives. Also, fuse-zip is faster that all known implementations
on large archives with many files.

%prep
%setup
sed -i '/CXXFLAGS=.*/d' lib/Makefile
sed -i '/CXXFLAGS=.*/d' Makefile

%build
%make_build
gzip fuse-zip.1

%install
install -d "%buildroot/usr/"{bin,share/man/man1}
install -D %name %buildroot%_bindir/%name
install -Dm 644 %name.1.gz %buildroot%_mandir/man1/%name.1.gz

%files
%doc README.md changelog LICENSE
%_bindir/%name
%_mandir/man1/%name.*

%changelog
* Fri Oct 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.2-alt1
- Initial build for ALT Linux.

