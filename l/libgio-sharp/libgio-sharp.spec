%define realname gio-sharp

Summary: Gio# - .NET language binding for libgio
Name: lib%{realname}
Version: 2.22.3
Release: alt1
License: LGPL2+
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Url: http://www.mono-project.com/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libgcc libgtk-sharp2-devel libgtk-sharp2-gapi mono-devel mono-mcs glib2-devel
BuildRequires: rpm-build-mono
BuildRequires: /proc

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%description
Gio# is an unstable .NET language binding for libgio distributed as part
of the glib package.

%prep
%setup -q
%patch -p1

%build
NOCONFIGURE=true ./autogen-2.22.sh
%configure --disable-static
%make

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_monodir/%realname/%realname.*
gacutil -i gio/%realname.dll -root %buildroot/usr/lib
dll=$(find %buildroot/usr/lib -type f -iname %realname.dll | sed -e "s,%buildroot,,g")
ln -sf $dll %buildroot%_monodir/%realname/%realname.dll

%files
%doc README AUTHORS COPYING NEWS
%_monodir/%realname
%_monogacdir/*

%files devel
%_pkgconfigdir/*.pc
%_datadir/gapi-2.0/gio-api.xml

%changelog
* Mon May 16 2011 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3

* Fri Mar 11 2011 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 2.15.0-alt2.svn20081217
- svn version r137563
- move pkgconfig files from main to devel package

* Wed Oct 22 2008 Alexey Shabalin <shaba@altlinux.ru> 2.15.0-alt1.svn20080514
- Inital release for ALTLinux

