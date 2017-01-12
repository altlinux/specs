Name: cccc
Version: 0.1
Release: alt1

Summary: C and C++ Code Counter, a software metrics tool

Url: https://github.com/AlertProject/CCCC
License: GPLv2+
Group: Development/Tools

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires: gcc-c++ pccts-devel

# Source-git: https://github.com/AlertProject/CCCC
Source: %name-%version.tar

%description
C and C++ Code Counter, a software metrics tool.

%prep
%setup

%build
#cd cccc

# We have to duplicate a little from the upstream build system.  See
# cccc/posixgcc.mak.
CFLAGS="%optflags"
CFLAGS="$CFLAGS -c -I/usr/include/pccts -Wno-deprecated -Wall -x c++"

make -C cccc -f posixgcc.mak CFLAGS="$CFLAGS" \
	PCCTS_H=/usr/include/pccts PCCTS_BIN=/usr/bin \
	ANTLR=/usr/bin/pccts-antlr DLG=/usr/bin/pccts-dlg

%check
cd test
make -f posix.mak
cd ..

%install
install -D -m644 debian/%name.1 %buildroot%_man1dir/%name.1
install -D cccc/cccc %buildroot%_bindir/%name

%files
%doc changes.txt README.md cccc/*.html
%_bindir/%name
%_man1dir/*

%changelog
* Thu Jan 12 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
