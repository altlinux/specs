Name: xorg-glamor
Version: 0.5.1
Release: alt2
Summary: X.Org glamor library
License: MIT
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: XORG_ABI_EXTENSION = %get_xorg_abi_extension
Obsoletes: xorg-drv-glamor < %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): xorg-sdk
BuildRequires: libEGL-devel libGL-devel libdrm-devel libgbm-devel libpixman-devel xorg-resourceproto-devel xorg-scrnsaverproto-devel

%description
Open-source X.org graphics common driver based on GL library

%package devel
Summary: X.Org glamor development package
Group: Development/C
Obsoletes: libglamor-devel < %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%set_verify_elf_method unresolved=relaxed

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--enable-glx-tls \
	--enable-xv \
	--with-xorg-module-dir=%_xorgmoduledir

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%_xorgmoduledir/*.so
%_xorgsysconfigdir/*.conf

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc


%changelog
* Wed Oct 16 2013 Valery Inozemtsev <shrek@altlinux.ru> 0.5.1-alt2
- disable GLES (closes: #28857)

* Tue Oct 15 2013 Valery Inozemtsev <shrek@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sat Oct 20 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt1
- 0.5

* Fri Feb 24 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt1
- initial release

