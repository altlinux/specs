%define fsname f2fs
Name: %fsname-tool
Version: 1.0.0
Release: alt1
Summary: Tools for Flash-Friendly File System (F2FS)
License: GPLv2
Group: System/Kernel and hardware
URL: http://sourceforge.net/projects/%name
Source: %name-%version.tar
Provides: mkfs.%fsname = %version-%release

%description
Tools for Flash-Friendly File System (F2FS).
Now only mkfs.%fsname


%prep
%setup


%build
%autoreconf
%configure --bindir=%_sbindir
%make_build


%install
%makeinstall_std


%files
%doc AUTHORS ChangeLog
%_sbindir/*
%_man8dir/*


%changelog
* Mon Oct 08 2012 Led <led@altlinux.ru> 1.0.0-alt1
- initial build
