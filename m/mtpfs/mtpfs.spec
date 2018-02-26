
Summary: FUSE filesystem that supports MTP devices
Name: mtpfs
Version: 1.1
Release: alt1
License: GPLv3+
Group: System/Kernel and hardware
Url: http://www.adebenham.com/mtpfs/
Source: http://www.adebenham.com/mtpfs/%name-%version.tar.gz
Patch: mtpfs-1.0-libmad.patch

BuildRequires: libmtp-devel
BuildRequires: libfuse-devel
BuildRequires: glib2-devel libgio-devel
BuildRequires: libmad-devel libid3tag-devel
Requires: fuse
Provides: fuse-%name

%description
MTPfs is a FUSE filesystem that supports reading and writing from any
MTP device supported by libmtp.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS NEWS README
%_bindir/%name

%changelog
* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- 1.1

* Wed Feb 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
