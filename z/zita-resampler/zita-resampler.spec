Summary: Fast, high-quality sample rate conversion library
Name: zita-resampler
Version: 1.3.0
Release: alt1
License: GPLv3+
Group: System/Libraries
Url: http://kokkinizita.linuxaudio.org/linuxaudio/zita-resampler/resampler.html
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-resampler-%version.tar.bz2
BuildRequires: gcc-c++ libsndfile-devel

%description
zita-resampler is a C++ library for resampling audio signals. It is
designed to be used within a real-time processing context, to be fast,
and to provide high-quality sample rate conversion.

The library operates on signals represented in single-precision
floating point format. For multichannel operation both the input and
output signals are assumed to be stored as interleaved samples.

The API allows a trade-off between quality and CPU load. For the
latter a range of approximately 1:6 is available. Even at the highest
quality setting zita-resampler will be faster than most similar
libraries, e.g. libsamplerate.

%package devel
Summary: Development libraries and headers for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package contains the headers and development libraries for %name.

%prep
%setup
sed 's|ldconfig||' -i libs/Makefile

%build
%make_build -C libs
ln -sf libzita-resampler.so.%version libs/libzita-resampler.so
export LDFLAGS="-L../libs"
%make_build -C apps CXXFLAGS+=-I../libs

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_lib -C libs
%makeinstall_std MANDIR=%_man1dir PREFIX=%prefix LIBDIR=%_lib -C apps

%files
%doc AUTHORS COPYING
%_libdir/lib%name.so.*
%_bindir/zresample
%_bindir/zretune
%_man1dir/zresample.1.*
%_man1dir/zretune.1.*

%files devel
%doc docs/*
%_includedir/%name
%_libdir/lib%name.so

%changelog
* Thu May 18 2017 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux Sisyphus.
