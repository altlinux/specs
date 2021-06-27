# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 1

Summary: Fast, high-quality sample rate conversion library
Name: zita-resampler
Version: 1.8.0
Release: alt1
License: GPLv3+
Group: Sound
Url: http://kokkinizita.linuxaudio.org/linuxaudio/zita-resampler/resampler.html
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# Source-url: http://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-resampler-%version.tar.bz2
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
%autopatch -p1

# To make sure to have the correct ALT specific flags:
sed -i -e 's|-O[23]||' -e 's|ldconfig||' -e 's|-march=native||' -e '/^CPPFLAGS += -DENABLE_SSE2/d' source/Makefile
sed -i -e 's|-O[23]||' -e 's|-march=native||' apps/Makefile

%build
# Disable avx
%ifarch %ix86 x86_64
export CXXFLAGS+=' -mno-avx'
%endif
# Enable SSE2 on x86_64
%ifarch x86_64
CXXFLAGS+=" -DENABLE_SSE2"
export CXXFLAGS
%endif

%make_build -C source

ln -sf libzita-resampler.so.%version source/libzita-resampler.so
export CXXFLAGS+=" -I../source"
export LDFLAGS+=" -L../source"
%make_build -C apps

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
* Sun Jun 27 2021 Anton Midyukov <antohami@altlinux.org> 1.8.0-alt1
- new version (1.8.0) with rpmgs script

* Mon May 13 2019 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt3
- Fix optflags

* Sun Jan 20 2019 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt2
- compilation with avx breaks work of package with older or lower
Intel CPUs such as Atom. Recompilation with avx disabled
(Thanks Denis Medvedev <nbr@altlinux.org>)

* Sun Nov 25 2018 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt1
- new version 1.6.2

* Thu May 18 2017 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux Sisyphus.
