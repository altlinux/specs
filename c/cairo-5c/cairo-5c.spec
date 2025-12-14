Name:           cairo-5c
Version:        1.23
Release:        alt1.1
Source:         %name-%version.tar
Group:          Development/Other
License:        LGPL-2.1
URL:            https://cgit.freedesktop.org/cairo-5c
VCS:            https://anongit.freedesktop.org/git/cairo-5c
Summary:        Nickle language binding for the cairo graphics library

Requires:       nickle
# Automatically added by buildreq on Sat Dec 13 2025
# optimized out: fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libX11-devel libXext-devel libcairo-devel libcairo-gobject libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libpng-devel nickle perl pkg-config python3 python3-base sh5 xorg-proto-devel
BuildRequires: fonts-ttf-vera librsvg-devel nickle-devel perl-parent

%description
Cairo-5c provides a simple binding for the cairo graphics library within the
nickle programming environment.

%package examples
Group:  Development/Other
Summary:        Nickle language binding for the cairo examples

%description examples
%summary

%prep
%setup

%build
%set_verify_elf_method relaxed
%autoreconf
%configure --disable-static
%make_build

%make check

%install
%makeinstall_std

%files
%_libdir/lib*.so*
%_datadir/nickle/*.5c
%_man3dir/*

%files examples
%_defaultdocdir/%name/examples

%changelog
* Sun Dec 14 2025 Fr. Br. George <george@altlinux.org> 1.23-alt1.1
- Add nickle dependency

* Sat Dec 13 2025 Fr. Br. George <george@altlinux.org> 1.23-alt1
- Version up

* Sat Dec 13 2025 Fr. Br. George <george@altlinux.org> 1.22-alt1
- Initial build for ALT
