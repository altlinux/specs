Name: smbnetfs
Version: 0.5.3a
Release: alt1

Summary: SMB filesystem using FUSE - mount network neighbourhood
Group: System/Kernel and hardware
License: GPL
Url: http://sourceforge.net/projects/smbnetfs

Packager: Ivan A. Melnikov <iv@altlinux.org>

Source: %name-%version.tar
BuildRequires: libfuse-devel libsmbclient-devel

%description
SMBNetFS is a filesystem (using FUSE) that allows you to use
samba/microsoft network in the same manner as the network
neighborhood in Microsoft Windows.

%prep
%setup
touch NEWS

%build
%autoreconf
%configure --with-gnome-keyring=no
%make

%install
%makeinstall

%files
%doc %_datadir/doc/*
%_bindir/*

%changelog
* Sat Mar 12 2011 Ivan A. Melnikov <iv@altlinux.org> 0.5.3a-alt1
- New version.

* Tue Jul 20 2010 Ivan A. Melnikov <iv@altlinux.org> 0.5.2-alt1
- New version.
- Minor spec cleanup.

* Tue May 27 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.3.11a-alt1
- Upstream version bump

* Tue Feb 19 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.3.11-alt1
- Upstream version bump

* Wed Nov 21 2007 Maxim Ivanov <redbaron@altlinux.ru> 0.3.10-alt1
- Initial build for sisyphus

