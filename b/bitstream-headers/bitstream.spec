Name: bitstream-headers
Version: 1.0
Release: alt2
Summary: biTStream is a set of C headers allowing a simpler access to binary structures such as specified by MPEG, DVB, IETF, etc.
Group: Development/C

Packager: Alexei Takaseev <taf@altlinux.ru>

License: MIT
Url: http://www.videolan.org/developers/bitstream.html
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

%description
biTStream is a set of C headers allowing a simpler access to binary
structures such as specified by MPEG, DVB, IETF, etc.

biTStream is lower level, and more efficient: fewer memory allocations,
fewer memory copies. It also features a better separation between layers
and specifications.

%prep
%setup
%patch0 -p1

%install
make PREFIX=%buildroot/usr install

%files
%doc AUTHORS COPYING INSTALL NEWS README TODO
%_includedir/bitstream
%_includedir/bitstream/*

%changelog
* Tue Jun 26 2012 Alexei Takaseev <taf@altlinux.org> 1.0-alt2
- Issue with bit 33 in PCR

* Sat May 19 2012 Alexei Takaseev <taf@altlinux.org> 1.0-alt1
- Initial RPM release
