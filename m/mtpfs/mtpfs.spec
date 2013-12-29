Summary: FUSE filesystem that supports MTP devices
Name: mtpfs
Version: 2.0
Release: alt1
License: GPLv3+
Group: System/Kernel and hardware
Url: https://github.com/Feandil/%name
Source: %name-%version.tar
#Patch: mtpfs-1.0-libmad.patch
Requires: fuse
Provides: fuse-%name

BuildRequires: libmtp-devel libfuse-devel
BuildRequires: glib2-devel libgio-devel
BuildRequires: libmad-devel libid3tag-devel

%description
MTPfs is a FUSE filesystem that supports reading and writing from any MTP device
supported by libmtp.


%prep
%setup -q
#patch -p1


%build
%autoreconf
%configure
%make_build


%install
%makeinstall_std


%files
%doc AUTHORS NEWS README
%_bindir/*


%changelog
* Sun Dec 29 2013 Led <led@altlinux.ru> 2.0-alt1
- 2.0

* Mon Mar 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- 1.1

* Wed Feb 01 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
