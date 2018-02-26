%define realname gtk-sharp-beans

Name: lib%{realname}
Version: 2.14.1
Release: alt1
Summary: C# bindings for GTK+ API not included in GTK#

Group: Development/Other
License: LGPLv2
Url: http://github.com/mono/%name
# Releases are tarballs downloaded from a tag at github.
# They are releases, but the file is generated on the fly.
# The actual URL is: http://github.com/mono/$name/tarball/$tagname

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libgio-sharp-devel libgtk-sharp2-devel libgtk-sharp2-gapi
BuildRequires: mono-devel mono-mcs glib2-devel
BuildRequires: rpm-build-mono
BuildRequires: /proc

%description
C# bindings for GTK+ API not included in GTK#

%package devel
Summary: Development files for gtk-sharp-beans
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for gtk-sharp-beans

%prep
%setup -q
%patch -p1

%build

NOCONFIGURE=true ./autogen.sh
%configure --disable-static
%make

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_monodir/%realname/%realname.*
gacutil -i %realname.dll -root %buildroot/usr/lib
dll=$(find %buildroot/usr/lib -type f -iname %realname.dll | sed -e "s,%buildroot,,g")
ln -sf $dll %buildroot%_monodir/%realname/%realname.dll

%files
%doc AUTHORS COPYING NEWS README
%_monodir/%realname
%_monogacdir/*

%files devel
%_libdir/pkgconfig/*pc
%_datadir/gapi-2.0/*.xml

%changelog
* Fri Mar 11 2011 Alexey Shabalin <shaba@altlinux.ru> 2.14.1-alt1
- initial build
