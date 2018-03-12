Name: libXpresent
Version: 1.0.0
Release: alt1
Summary: X Present Extension
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-util-macros libXext-devel libXfixes-devel libXrandr-devel xorg-presentproto-devel

%description
X Present Extension

%package devel
Summary: Xpresent Libraries and Header Files
Group: Development/C

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING README
%_libdir/*.so.*

%files devel
%_includedir/X11/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Mon Mar 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- initial build

