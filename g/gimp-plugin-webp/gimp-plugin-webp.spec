%define gimpver 2.0

Name: gimp-plugin-webp
# Author does not assign version to his software, so we construct 'virtual'
# version that is quite low-numbered to ensure easy updates in future
# and contains code last modification date
Version: 0.0.20110721
Release: alt2

Summary: Gimp plugin for WebP image format import/export
License: GPLv3
Group: Graphics

URL: http://registry.gimp.org/node/25874
#Source0: http://registry.gimp.org/files/file-webp-source.tar.gz
Source0: gimp-plugin-webp.tar

Requires: gimp2 >= 2.2

# Automatically added by buildreq on Sat Jul 16 2011
BuildRequires: libgimp-devel libwebp-devel

%description
Gimp plugin for WebP image format import/export.

%prep
%setup -c

%build
export CFLAGS="%optflags"
export LIBS=-lwebp
gimptool-2.0 --build file-webp.c

%install
export DESTDIR=%buildroot
gimptool-2.0 --install-admin-bin file-webp

%files
%_libdir/gimp/%gimpver/plug-ins/*

%changelog
* Mon Jan 09 2012 Victor Forsiuk <force@altlinux.org> 0.0.20110721-alt2
- Rebuild against libwebp.so.2.

* Sat Jul 16 2011 Victor Forsiuk <force@altlinux.org> 0.0.20110721-alt1
- Initial build.
