Name: stegdetect
Version: 0.6
Release: alt3

Summary: Detect and extract steganography messages inside JPEG
License: BSD
Group: File tools

URL: http://www.outguess.org/detection.php
Source: http://www.outguess.org/stegdetect-%version.tar.gz

# Automatically added by buildreq on Wed Sep 30 2009
BuildRequires: gcc-c++ gtk+-devel

%description
Stegdetect is an automated tool for detecting steganographic content in
images. It is capable of detecting several different steganographic
methods to embed hidden information in JPEG images. Currently, the
detectable schemes are jsteg, jphide, invisible secrets, outguess 01.3b,
F5, appendX, and camouflage. Using linear discriminant analysis, it also
supports detection of new stego systems. Stegbreak is used to launch
dictionary attacks against JSteg-Shell, JPHide, and OutGuess 0.13b.

%prep
%setup

%build
# Rename conflicting variable, fixes gcc4 FTBFS.
%__subst 's/debug/stegdebug/g' stegdetect.c

libtoolize -i
# --without-libevent turned off build of xsteg
# (xsteg is gtk+ 1.x based app so we don't want it)
%configure --without-libevent
%make_build

%install
# by default 'make install' try to install unneeded thingies...
%makeinstall_std SUBDIRS=""

%files
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 30 2009 Victor Forsyuk <force@altlinux.org> 0.6-alt3
- Fix FTBFS due to missing libtoolize call in current configure macro.

* Tue May 16 2006 Victor Forsyuk <force@altlinux.ru> 0.6-alt2
- Fix FTBFS with gcc4.

* Tue Jun 21 2005 Victor Forsyuk <force@altlinux.ru> 0.6-alt1
- Initial build.
