Name: qpress
Summary: File archiver designed for speed
License: GPLv2
Group: Archiving/Compression
Version: 1.1
Release: alt1
Url: http://www.quicklz.com/
Source: %name.tar
Patch0: qpress-1.1-isatty-include.patch

BuildRequires: unzip gcc-c++

%description
qpress is a portable file archiver using QuickLZ and designed to utilize
fast storage systems to their max. It's often faster than file copy
because the destination is smaller than the source. A few features:

* multiple cores, reaching upto 1.1 Gbyte/s in-memory compression on a
  quad core i7
* 64-bit file sizes and tested with terabyte sized archives containing
  millions of files and directories
* pipes and redirection and *nix-like behaviour for scripting and
  flexibility
* Adler32 checksums to ensure that decompressed data has not been corrupted
* data recovery of damaged archives with 64 Kbyte grannularity

%prep
%setup -c -n %name-%version
%patch0 -p1

%build
%make_build

%install
install -d -m 755 %buildroot%_bindir
install -m 755 %name %buildroot%_bindir/

%files
%_bindir/%name

%changelog
* Tue Dec 15 2015 Terechkov Evgenii <evg@altlinux.org> 1.1-alt1
- Initial build for ALT Linux Sisyphus
