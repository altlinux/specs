Name: sfnt2woff-zopfli
Version: 1.1.0
Release: alt1

Summary: WOFF utilities with Zopfli compression

License: ASL 2.0 MPL 1.1/GPL 2.0/LGPL 2.1
Group: File tools
Url: https://github.com/bramstein/sfnt2woff-zopfli

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/bramstein/sfnt2woff-zopfli/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: zlib-devel

%description
This is a modified version of the sfnt2woff utility that uses Zopfli
as a compression algorithm instead of zlib.
This results in compression gains of - on average - 5-8%% compared to regular WOFF files.
Zopfli generates compressed output that is compatible
with regular zlib compression so the resulting WOFF files can be used everywhere.

%prep
%setup

%build
CFLAGS="%optflags" CXXFLAGS="%optflags" %make_build

%install
mkdir -p %buildroot%_bindir
install -m 0755 sfnt2woff-zopfli woff2sfnt-zopfli %buildroot%_bindir/

%files
%doc LICENSE
%doc README.md
%_bindir/sfnt2woff-zopfli
%_bindir/woff2sfnt-zopfli

%changelog
* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version (1.1.0) with rpmgs script

