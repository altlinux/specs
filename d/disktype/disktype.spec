Name: disktype
Version: 9
Release: alt2

Summary: A disk and disk image format analyzer
Group: File tools
License: MIT/X

URL: http://disktype.sourceforge.net/
Source0: http://download.sourceforge.net/disktype/disktype-%version.tar.gz

BuildRequires: glibc-kernheaders

%description
The purpose of disktype is to detect the content format of a disk or
disk image. It knows about common file systems, partition tables, and
boot codes.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
install -pDm 755 disktype %buildroot%_bindir/disktype
install -pDm 644 disktype.1 %buildroot%_man1dir/disktype.1

%files
%doc HISTORY README TODO
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 12 2007 Victor Forsyuk <force@altlinux.org> 9-alt2
- Build with glibc-kernheaders instead of linux-libc-headers.

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 9-alt1.0
- Automated rebuild.

* Tue Jun 06 2006 Victor Forsyuk <force@altlinux.ru> 9-alt1
- Initial build.
