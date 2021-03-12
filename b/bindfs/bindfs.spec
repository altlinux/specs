Name: bindfs
Version: 1.15.1
Release: alt1
License: GPLv2

Summary: %name is a FUSE filesystem for mounting a directory to another location, similarly to mount --bind
Group: System/Base
URL: http://bindfs.org/
Source: %name-%version.tar.gz

BuildRequires: libfuse-devel

%description
bindfs is a FUSE filesystem for mounting a directory to another
location, similarly to mount --bind.
The permissions inside the mountpoint can be altered using various
rules.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-static=no
%make

%install
%makeinstall_std

%files
%doc COPYING ChangeLog README.md TODO
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 12 2021 Slava Aseev <ptrnine@altlinux.org> 1.15.1-alt1
- Updated to upstream version 1.15.1

* Mon Sep 03 2018 Pavel Moseev <mars@altlinux.org> 1.13.9-alt1
- Updated to upstream version 1.13.9

* Thu Sep 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.6-alt1
- Version 1.12.6

* Sat May 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.12.1-alt1
- New version

* Sat Nov 17 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.11-alt1
- New version

* Tue Nov 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.9-alt1
- Build for ALT
