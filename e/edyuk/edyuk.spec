# %set_verify_elf_method unresolved=relaxed
%define svn svn973
Summary: Edyuk is a Free crossplatform Qt4 IDE
Name: edyuk
Version: 1.1.0
Release: alt2.%svn.1
License: GPL
Group: Development/KDE and QT
Packager: Boris Savelev <boris@altlinux.org>
Url: http://www.edyuk.org
Source: %name-%version.tar.bz2
Patch: edyuk-1.1.0.desktop.patch
Patch2: edyuk-1.1.0.qt4.5.patch
Patch3: edyuk-1.1.0.version.patch

BuildRequires(pre): desktop-file-utils
# Automatically added by buildreq on Sat Oct 11 2008
BuildRequires: gcc-c++ libqt4-devel

%description
Edyuk is an Integrated Developement Environment built with Qt4 and meant to
provide a light, fast and stable environment for rapid application development
in C++/Qt4. Thanks to plugins (see III) its scope can hopefully be extended to
any possible programming related task (e.g version control, issue tracking,
management of other project formats, support for other languages/toolkits...)

%package -n lib%name
Summary: Edyuk shared library
Group: System/Libraries

%description -n lib%name
This package contains %name shared library.

%package -n lib%name-devel
Summary: Edyuk development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains %name development files.

%prep
%setup -q
%patch -p0
%patch2 -p0
%patch3 -p0

sed -i "s|/usr/local/edyuk|%_libdir/%name|g" install.pri
sed -i "s|/usr/lib|%_libdir|g" install.pri

%build
qmake-qt4
# parallel build is broken
%make

%install
rm -f %name
ln -s ../..%_libdir/%name/%name.bin %name
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/%name
#mkdir -p %buildroot%_datadir/mime/packages
cp -a %name %buildroot%_bindir
cp -a %name.bin %buildroot%_libdir/%name
cp -a plugins %buildroot%_libdir/%name
cp -a lib%name.* %buildroot%_libdir
#install %name.xml %buildroot%_datadir/mime/packages
INSTALL_ROOT=%buildroot %make install
mv %buildroot%_iconsdir/default.kde %buildroot%_iconsdir/hicolor

%files
%_bindir/%name
%_libdir/%name
%_datadir/%name
%_niconsdir/%name.*
%_miconsdir/%name.*
%_liconsdir/%name.*
%_desktopdir/%name.*
#_datadir/mime/packages/%name.xml

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/qt4/Edyuk

%changelog
* Wed Apr 07 2010 Boris Savelev <boris@altlinux.org> 1.1.0-alt2.svn973.1
- drop mime xml

* Mon Apr 13 2009 Boris Savelev <boris@altlinux.org> 1.1.0-alt2.svn973
- fix build
- add patches from Mandriva
- remove pre/post

* Fri Nov 07 2008 Boris Savelev <boris@altlinux.org> 1.1.0-alt1
- new version

* Sat Oct 11 2008 Boris Savelev <boris@altlinux.org> 1.0.1-alt1
- initial build for Sisyphus

