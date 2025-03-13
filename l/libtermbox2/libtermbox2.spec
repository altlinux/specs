%define oname termbox2

Name: libtermbox2
Version: 2.5.0
Release: alt1

Summary: termbox2 is a terminal rendering library for creating TUIs
License: MIT
Group: System/Libraries
Url: https://github.com/termbox/termbox2
Vcs: https://github.com/termbox/termbox2

Source: %name-%version.tar
Patch: fix-alt-makefile.patch

%description
termbox2 is a terminal rendering library for creating TUIs. It is a suckless
alternative to the ubiquitous ncurses library. It ships with built-in support
for popular terminals and can also fallback to terminfo if present. Compared to
the original termbox, it retains a simple API and no dependencies beyond libc,
and adds stricter error checking, more efficient escape sequence parsing,
opt-in support for 32-bit color, extended grapheme clusters, code gen for
built-in escape sequences, a test suite, and more.

termbox2 is organized as a single file header library, though it is possible to
compile it as a stand-alone shared or static library.

%package devel
Summary: Development files for %oname
Group: Development/C
Requires: %name = %EVR

%description devel
Contains header files for developing applications that use termbox2.

%prep
%setup
%patch -p1

%build
%make_build lib

%install
%make install_lib DESTDIR=%buildroot \
	prefix=%_prefix \
	libdir=%_libdir \
	includedir=%_includedir

%files
%_libdir/%name.so.*

%files devel
%_libdir/%name.so
%_includedir/%oname.h

%changelog
* Wed Mar 05 2025 Ulysses Apokin <ulysses@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus.
