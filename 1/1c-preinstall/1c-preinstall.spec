Name:    1c-preinstall
Version: 8.3
Release: alt4

Summary: Set correct environment for 1C:Enterprise client
License: GPL
Group:   System/Libraries
URL:     http://1c.ru/
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: libImageMagick

Requires: libwebkitgtk2
Requires: xorg-server
Requires: cups
Requires: libImageMagick

#BuildArch: noarch

%description
This metapackage is intend to deploy correct environment for
1C:Enterprise client installation.

Tested with 1C:Enterprise client version 8.3.3.641

%install
mkdir -p %buildroot%_libdir
cp -a %_libdir/libMagickWand-*.so.1.* %buildroot%_libdir/
ln -rs %buildroot%_libdir/libMagickWand-*.so.1.* \
       %buildroot%_libdir/libWand.so.1

%files
%_libdir/libWand.so.1
%exclude %_libdir/libMagickWand*

%changelog
* Wed Jul 10 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt4
- Pack symlink libWand.so.1 as file, disable triggers

* Tue Jul 09 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt3
- Correct detect library path on x86_64 (ALT #29161)

* Fri Jun 21 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt2
- Force create symbolic link

* Wed Jun 19 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt1
- Initial build in Sisyphus
