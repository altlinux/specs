Name: ecm
Version: 1.03
Release: alt2

Summary: Converts CD image files into a lossless format optimized for compression tools
License: GPL
Group: Archiving/Compression

Url: http://www.neillcorlett.com/ecm
# Upstream gone, use ftp://ftp.netbsd.org/pub/pkgsrc/distfiles/cmdpack-1.03-src.tar.gz
Source: cmdpack-%version-src.tar.gz

%description
%summary

%prep
%setup -n cmdpack-%version-src

%build
cd src
gcc %optflags -Wall -Wextra -Werror -fomit-frame-pointer "ecm.c" -s -o "../ecm"

%install
install -D ecm %buildroot%_bindir/ecm
ln %buildroot%_bindir/ecm %buildroot%_bindir/unecm

%files
%doc doc/cmdpack.txt
%_bindir/*

%changelog
* Mon Apr 20 2020 Michael Shigorin <mike@altlinux.org> 1.03-alt2
- E2K: fix superfluous optimization level

* Wed Apr 30 2014 Fr. Br. George <george@altlinux.ru> 1.03-alt1
- Initial build from Arch

