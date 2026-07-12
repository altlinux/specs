Name: rehex
Version: 0.64.0
Release: alt1

Summary: Reverse Engineers' Hex Editor

License: GPL-2.0
Group: Editors
URL: https://rehex.solemnwarning.net

# Source-url: https://github.com/solemnwarning/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libbotan-devel
BuildRequires: libcapstone-devel
BuildRequires: libgtk+3-devel
BuildRequires: libjansson-devel
BuildRequires: libunistring-devel
BuildRequires: libwxBase3.2-devel
BuildRequires: lua-devel
BuildRequires: lua5.4-module-busted
BuildRequires: perl-Template
BuildRequires: dos2unix
BuildRequires: zip

# remove inner dependencies
%filter_from_requires /^lua5.4(class)/d
%filter_from_requires /^lua5.4(compat)/d
%filter_from_requires /^lua5.4(document_stream)/d
%filter_from_requires /^lua5.4(enum)/d
%filter_from_requires /^lua5.4(executor/d
%filter_from_requires /^lua5.4(ffi)/d
%filter_from_requires /^lua5.4(kaitaistruct)/d
%filter_from_requires /^lua5.4(lulpeg.lulpeg)/d
%filter_from_requires /^lua5.4(microsoft_pe)/d
%filter_from_requires /^lua5.4(parser)/d
%filter_from_requires /^lua5.4(preprocessor)/d
%filter_from_requires /^lua5.4(stable_sort)/d
%filter_from_requires /^lua5.4(string_/d
%filter_from_requires /^lua5.4(util/d

%description
A cross-platform hex editor for reverse engineering, and everything else.

Features:

* Large (1TB+) file support
* Decoding of integer/floating point value types
* Inline disassembly of machine code
* Highlighting and annotation of ranges of bytes
* Side by side comparison of whole files or selections
* Lua scripting support
* Virtual address mapping support
* Support for common text encodings (ASCII, Unicode, ISO-8859-X, etc)
* Import and export of Intel HEX files
* Bitmap data visualisation
* Binary Templates for automatically annotating data (similar to 010 Editor)
* Bit editing/manipulation
* Checksumming of files/selections

%prep
%setup

# convert CR+LF to LF
dos2unix *.txt README.md

# fix README.md
sed -i "s|(res/|(|;s|(doc/|(|" README.md

# fix plugins.tt
sed -i "s|/usr/lib/rehex/</code></li>|%_libdir/rehex/</code>)</li>|" help/pages/plugins.tt

%build
%make_build prefix=%_prefix libdir=%_libdir

%install
%makeinstall

%files
%doc *.md *.txt doc/*.gif res/icon64.png
%_bindir/%name
%_libdir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sun Jul 12 2026 Alexander Kovalev <alexvk@altlinux.org> 0.64.0-alt1
- Initial build for ALT.
