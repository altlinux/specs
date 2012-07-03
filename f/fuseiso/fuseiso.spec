Name: fuseiso
Version: 20070708
Release: alt2

Summary: Mount ISO filesystem images as a non-root user
Group: File tools
URL: http://sourceforge.net/projects/fuseiso/
License: GPL

Source0: %name-%version.tar.bz2

Patch0: fuseiso-20070708-alt-build.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sun Nov 16 2008
BuildRequires: gcc-c++ glib2-devel libfuse-devel zlib-devel

%description
Mount ISO filesystem images as a non-root user. Currently supports
plain ISO9660 Level 1 and 2, Rock Ridge, Joliet, zisofs..
Supported image types: ISO, BIN (single track only), NRG, MDF, IMG (CCD).

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/%name

%changelog
* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 20070708-alt2
- update Url

* Sun Jun 29 2008 Igor Zubkov <icesik@altlinux.org> 20070708-alt1
- build for Sisyphus

