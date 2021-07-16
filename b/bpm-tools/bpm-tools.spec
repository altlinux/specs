Name: bpm-tools
Version: 0.3
Release: alt2
Summary: Automatic calculating and tagging the tempo of music files
License: GPL-2.0+
Group: Sound
Url: http://www.pogo.org.uk/~mark/bpm-tools/

Source: http://www.pogo.org.uk/~mark/bpm-tools/releases/%name-%version.tar.gz
Patch: bpm-tools-0.3-alt-makefile.patch

Requires: sox

%description
Automatic calculating and tagging the tempo (in beats-per-minute) of music files.

%prep
%setup
%patch -p2

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix
chmod -x %buildroot%_man1dir/*

%files
%doc COPYING README
%_bindir/*
%_man1dir/*

%changelog
* Fri Jul 16 2021 Leontiy Volodin <lvol@altlinux.org> 0.3-alt2
- Fixed bpm-graph.

* Sun May 30 2021 Leontiy Volodin <lvol@altlinux.org> 0.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built for mixxx.
