%define _unpackaged_files_terminate_build 1
Name:    pocketsphinx
Version: 5.1.0
Release: alt1

Summary: A small speech recognizer
License: BSD-2-Clause and BSD-3-Clause and MIT
Group:   Other
Url:     https://github.com/cmusphinx/pocketsphinx

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: libpulseaudio-devel
BuildRequires: libportaudio2-devel

%description
This is PocketSphinx, one of Carnegie Mellon University's open source large
vocabulary, speaker-independent continuous speech recognition engines.

%prep
%setup

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C

%description -n lib%name-devel
%summary

%build
%cmake -GNinja -Wno-dev -DBUILD_SHARED_LIBS=ON
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files
%doc AUTHORS README.md
%_bindir/*
%_datadir/%name
%_man1dir/*.1*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name
%_includedir/%name.h
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc

%changelog
* Thu May 07 2026 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Sun Oct 19 2025 Andrey Cherepanov <cas@altlinux.org> 5.0.4-alt1
- Initial build for Sisyphus.
