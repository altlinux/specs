# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 1

Summary: Fast, high-quality sample rate conversion library
Name: zita-resampler
Version: 1.6.2
Release: alt2
License: GPLv3+
Group: Sound
Url: http://kokkinizita.linuxaudio.org/linuxaudio/zita-resampler/resampler.html
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-resampler-%version.tar.bz2
Patch: zita-resampler-1.6.2-destdir.patch
BuildRequires: gcc-c++ libsndfile-devel

Requires: lib%name%sover = %EVR

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

%package -n lib%name%sover
Summary: Convolution engine library
Group: System/Libraries
Conflicts: %name < 1.6.2

%description -n lib%name%sover
%name is a fast, partitioned convolution engine library.

%package devel
Summary: Development libraries and headers for %name
Group: Development/Other
Requires: lib%name%sover = %EVR

%description devel
This package contains the headers and development libraries for %name.

%prep
%setup
%patch0 -p1 -b .destdir
sed 's|ldconfig||' -i source/Makefile

%build
%ifarch %ix86 x86_64
export CXXFLAGS+='%optflags -mno-avx -fpic'
%endif
%make_build -C source

ln -sf libzita-resampler.so.%version source/libzita-resampler.so
export LDFLAGS="-L../source"
%make_build -C apps CXXFLAGS+=-I../source

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir -C source
%makeinstall_std MANDIR=%_man1dir PREFIX=%prefix LIBDIR=%_libdir -C apps

%files
%doc AUTHORS COPYING
%_bindir/zresample
%_bindir/zretune
%_man1dir/zresample.1.*
%_man1dir/zretune.1.*

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files devel
%doc docs/*
%_includedir/%name
%_libdir/lib%name.so

%changelog
* Sun Jan 20 2019 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt2
- compilation with avx breaks work of package with older or lower
Intel CPUs such as Atom. Recompilation with avx disabled
(Thanks Denis Medvedev <nbr@altlinux.org>)

* Sun Nov 25 2018 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt1
- new version 1.6.2

* Thu May 18 2017 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux Sisyphus.
