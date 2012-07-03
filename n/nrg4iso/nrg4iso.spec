Name: nrg4iso
Version: 1.0.1
Release: alt1

Summary: A tool to convert Nero (.nrg) CD images to ISO 9660 images
License: BSD
Group: File tools

Url: http://nrg4iso.googlecode.com
Source: %url/files/nrg4iso-%version.tgz

%description
nrg4iso is a command line utility that enables you to convert a Nero CD image
file (.nrg) into an ISO 9660 CD image file. The utility handles all DAO and
TAO data images.

%prep
%setup -n nrg4iso

%build
%__subst 's@machine/endian.h@endian.h@' endian.h
%__subst 's/O_RDONLY,/O_RDONLY | O_LARGEFILE,/' nrg.c
%make_build CC="gcc -D_LARGEFILE64_SOURCE"

%install
install -pD -m755 nrg4iso %buildroot%_bindir/nrg4iso

%files
%_bindir/*

%changelog
* Wed Oct 24 2007 Victor Forsyuk <force@altlinux.org> 1.0.1-alt1
- 1.0.1
- Fixed to work with large files.

* Thu Sep 13 2007 Victor Forsyuk <force@altlinux.org> 1.0-alt1
- Initial build.
