Name: woff2
Version: 0.0
Release: alt1

Summary: WOFF2 compress/decompress tools

Url: https://github.com/google/woff2
License: Apache 2.0
Group: File tools

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/google/woff2.git
Source: %name-%version.tar

BuildRequires: gcc-c++

BuildRequires: libbrotli-devel >= 0.6.0

%description
WOFF2 compress/decompress tools.

%prep
%setup

%build
%make_build || make

%install
mkdir -p %buildroot%_bindir/
cp -a woff2_compress woff2_decompress %buildroot%_bindir/

%files
%doc README.md
%_bindir/woff2_compress
%_bindir/woff2_decompress

%changelog
* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0-alt1
- initial build for ALT Linux Sisyphus
