Name: jpegquality
# No version designated by upstream, so we set version to arbitrary low digit string...
Version: 0.0
Release: alt1

Summary: Estimate the quality of the JPEG based on the quantization tables
License: Freely distributable
Group: Graphics

Url: http://www.hackerfactor.com
Source: http://www.hackerfactor.com/src/jpegquality.c

%description
Estimate the quality of the JPEG based on the quantization tables.

%prep
%setup -c -T
cp %SOURCE0 .

%build
gcc %optflags jpegquality.c -o jpegquality

%install
install -Dpm755 jpegquality %buildroot%_bindir/jpegquality

%files
%_bindir/*

%changelog
* Sat Mar 17 2012 Victor Forsiuk <force@altlinux.org> 0.0-alt1
- Initial build.
