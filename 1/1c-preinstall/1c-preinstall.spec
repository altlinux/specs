Name:    1c-preinstall
Version: 8.3
Release: alt2

Summary: Set correct environment for 1C:Enterprise client
License: GPL
Group:   System/Libraries
URL:     http://1c.ru/
Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: libwebkitgtk2
Requires: xorg-server
Requires: cups
Requires: libImageMagick

BuildArch: noarch

%description
This metapackage is intend to deploy correct environment for
1C:Enterprise client installation.

Tested with 1C:Enterprise client version 8.3.3.641

%post
ln -sf "$(basename %_libdir/libMagickWand*.so.*)" %_libdir/libWand.so.1
/sbin/ldconfig

%preun
rm -f %_libdir/libWand.so.1
/sbin/ldconfig

%files

%changelog
* Fri Jun 21 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt2
- Force create symbolic link

* Wed Jun 19 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt1
- Initial build in Sisyphus
