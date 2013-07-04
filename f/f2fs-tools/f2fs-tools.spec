%define fsname f2fs
Name: %fsname-tools
Version: 1.1.0
Release: alt2
Summary: Tools for Flash-Friendly File System (F2FS)
License: GPLv2
Group: System/Kernel and hardware
URL: http://sourceforge.net/projects/%name
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Provides: mkfs.%fsname = %version-%release

BuildRequires: libuuid-devel

%description
Tools for Flash-Friendly File System (F2FS).
Currently, the tools include mkfs.f2fs only.


%prep
%setup -q
%patch -p1


%build
%autoreconf
%configure --disable-shared --enable-static
%make_build


%install
%makeinstall_std


%files
%doc AUTHORS
%_sbindir/*
%_man8dir/*
%exclude %_libdir


%changelog
* Thu Jul 04 2013 Led <led@altlinux.ru> 1.1.0-alt2
- upstream updates

* Sun Feb 10 2013 Led <led@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri Oct 12 2012 Led <led@altlinux.ru> 1.0.0-alt1
- initial build
