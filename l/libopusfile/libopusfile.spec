%define		srcname opusfile

Name:		lib%srcname
Version:	0.6
Release:	alt1
Summary:	A high-level API for decoding and seeking within .opus files
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Group:		System/Libraries
License:	BSD
Url:		http://www.opus-codec.org/
Source0:	http://downloads.xiph.org/releases/opus/%srcname-%version.tar.gz

# Automatically added by buildreq on Sat Mar 16 2013 (-bi)
# optimized out: elfutils libcom_err-devel libkrb5-devel pkg-config
BuildRequires: libogg-devel libopus-devel libssl-devel

%description
libopusfile provides a high-level API for decoding and seeking
within .opus files. It includes:
* Support for all files with at least one Opus stream (including
multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API (allowing chained files to be
decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S)
(including seeking).
* Support for both random access and streaming data sources.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with %name.

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
%name-devel-static contains the static libraries needed to
develop programs which make use of %name.

%prep
%setup -n %srcname-%version

%build
%configure
%make_build V=1

%install
make DESTDIR=%buildroot install

%files
%doc COPYING AUTHORS README.txt
%_libdir/libopusfile.so.*

%files devel
%_includedir/opus/opusfile*
%_pkgconfigdir/opusfile.pc
%_libdir/libopusfile.so

%files devel-static
%_libdir/libopusfile.a

%changelog
* Tue Oct 27 2015 Motsyo Gennadi <drool@altlinux.ru> 0.6-alt1
- 0.6

* Sat Mar 09 2013 Motsyo Gennadi <drool@altlinux.ru> 0.2-alt1
- initial build for ALT Linux
