Name: simple-mtpfs
Version: 0.1
Release: alt2
Summary: Fuse-based MTP driver
Group: System/Kernel and hardware
License: GPLv2+
Url: https://github.com/phatina/simple-mtpfs
Source0: https://github.com/downloads/phatina/simple-mtpfs/%name-%version.tar

BuildRequires: libfuse-devel >= 2.8
BuildRequires: libmtp-devel gcc-c++
Requires: fuse
Provides: fuse-%name

%description
SIMPLE-MTPFS (Simple Media Transfer Protocol FileSystem) is a file system for
Linux (and other operating systems with a FUSE implementation, such as Mac OS X
or FreeBSD) capable of operating on files on MTP devices attached via USB to
local machine. On the local computer where the SIMPLE-MTPFS is mounted, the
implementation makes use of the FUSE (Filesystem in Userspace) kernel module.
The practical effect of this is that the end user can seamlessly interact with
MTP device files.

%prep
%setup

%build
./autogen.sh
%configure
%make %{?_smp_mflags}

%install
%makeinstall_std 

%files
%_bindir/%name
%_man1dir/%{name}.1.*
%doc COPYING README

%changelog
* Sun Jun 23 2013 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- Update from git

* Tue May 21 2013 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus (based on Fedora spec)
