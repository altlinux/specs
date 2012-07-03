Name: s3backer
Version: 1.3.1
Release: alt7

Summary: FUSE-based single file backing store via Amazon S3
Group: System/Kernel and hardware
License: GPL
Url: http://code.google.com/p/s3backer/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version.patch

Requires: fuse

# Automatically added by buildreq on Mon Mar 21 2011 (-bb)
BuildRequires: libcurl-devel libexpat-devel libfuse-devel libssl-devel zlib-devel

%description
%summary

%prep
%setup
#setup -q -n %%distname-%%version
%patch0 -p1

%build
touch NEWS AUTHORS ChangeLog
autoreconf -fisv
%configure
%make

%install
%makeinstall

%files
%_bindir/s3backer
%_docdir/packages/s3backer/CHANGES
%_docdir/packages/s3backer/COPYING
%_docdir/packages/s3backer/INSTALL
%_docdir/packages/s3backer/README
%_docdir/packages/s3backer/TODO
%_man1dir/s3backer.1.bz2

%changelog
* Tue May 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt7
- fix build

* Mon Mar 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt6
- fix build

* Thu Feb 03 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt5
- fix requires to fuse

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt4
- auto rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt3
- rebuild with new openssl

* Fri Feb 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt2
- fix buildrequires

* Fri Feb 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt1
- first build for Sisyphus
