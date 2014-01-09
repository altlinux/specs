Name: libxshmfence
Version: 1.1
Release: alt1
Summary: X Shared Memory Fence library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xorg-xproto-devel xorg-util-macros

%description
X Shared Memory Fence library - shared memory "SyncFence" synchronization primitive

%package devel
Summary: The xshmfence Library and Header Files
Group: Development/C
Requires: %name = %version-%release

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
%_libdir/*.so.*

%files devel
%_includedir/X11/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Jan 09 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- initial release

