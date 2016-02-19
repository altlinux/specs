Name: bitstream-headers
Version: 1.1
Release: alt2
Summary: biTStream is a set of C headers allowing a simpler access to binary structures such as specified by MPEG, DVB, IETF, etc.
Group: Development/C

Packager: Alexei Takaseev <taf@altlinux.ru>

License: MIT
Url: http://www.videolan.org/developers/bitstream.html
Source0: %name-%version.tar
#Patch0: %%name-%%version-%%release.patch
BuildArch: noarch

%description
biTStream is a set of C headers allowing a simpler access to binary
structures such as specified by MPEG, DVB, IETF, etc.

biTStream is lower level, and more efficient: fewer memory allocations,
fewer memory copies. It also features a better separation between layers
and specifications.

%prep
%setup
#%%patch0 -p1

%install
make PREFIX=%buildroot/usr install

%files
%doc AUTHORS COPYING INSTALL NEWS README TODO
%_includedir/bitstream

%changelog
* Fri Feb 19 2016 Alexei Takaseev <taf@altlinux.org> 1.1-alt2
- aac: add enumerations
- mp2v: add high progressive profile
- fix bad printing of vbi & telx descriptors
- fix A/52 bitrate table
- dvb strings: fix character set for chinese streams

* Tue Oct 06 2015 Alexei Takaseev <taf@altlinux.org> 1.1-alt1
- 1.1

* Wed Apr 08 2015 Alexei Takaseev <taf@altlinux.org> 1.0-alt8
- fixes for proper cpp inclusion
- mp2v: add colorspace fields

* Sat Jan 31 2015 Alexei Takaseev <taf@altlinux.org> 1.0-alt7
- fix a52e_set_frmsiz
- fix PTS signaling in PES
- Add encoder/decoder for DVB Simulcrypt EMMG interface

* Thu Oct 30 2014 Alexei Takaseev <taf@altlinux.org> 1.0-alt6
- Add support for SMPTE 2022-1 Forward Error Correction
- add rtp_clear_marker

* Sun Jun 29 2014 Alexei Takaseev <taf@altlinux.org> 1.0-alt5
- update to git:047c02753ca8b6b3e8d69b9b9a4790559d6aa8b7

* Tue Oct 02 2012 Alexei Takaseev <taf@altlinux.org> 1.0-alt4
- dvb/pes: Fix for PES payload offset

* Sat Aug 11 2012 Alexei Takaseev <taf@altlinux.org> 1.0-alt3
- Enforce consistency naming between tables (git: 6a24504cc5b5c4c4bd11dffc89209f2e2474b814)

* Tue Jun 26 2012 Alexei Takaseev <taf@altlinux.org> 1.0-alt2
- Issue with bit 33 in PCR

* Sat May 19 2012 Alexei Takaseev <taf@altlinux.org> 1.0-alt1
- Initial RPM release
