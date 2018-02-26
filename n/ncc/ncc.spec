Name: ncc
Version: 2.6
Release: alt0.1

Summary: ncc - The new generation C compiler

License: Artistic
Group: Development/Other
Url: http://students.ceid.upatras.gr/~sxanth/ncc/index.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://students.ceid.upatras.gr/~sxanth/ncc/%name-%version.tar.bz2

# Automatically added by buildreq on Mon Jan 30 2006
BuildRequires: gcc-c++ libncurses-devel libstdc++-devel libtinfo-devel

%description
ncc is a compiler that produces program analysis information. ncc is a
decent replacement of cflow and cscope able to analyse any program using
the gcc compiler. The program also includes a graphical call-graph
navigator and source browser which is extremely practical for hacking
and comprehending large projects.

%prep
%setup -q
sed -i "5i#include <alloca.h>" dbstree.h
#%__subst "s|/usr|\$(DESTDIR)/usr|g" Makefile

%build
%make

%install
mkdir -p %buildroot{%_bindir,%_includedir,%_man1dir}

#%make_install install DESTDIR=%buildroot
# from broken Makefile install
cp objdir/ncc %buildroot%_bindir/ncc
ln -sf ncc %buildroot%_bindir/nccar
ln -sf ncc %buildroot%_bindir/nccld
ln -sf ncc %buildroot%_bindir/nccc++
ln -sf ncc %buildroot%_bindir/nccg++
cp nccnav/nccnav %buildroot%_bindir/nccnav
ln -fs nccnav %buildroot%_bindir/nccnavi
cp ncc.1 %buildroot%_man1dir/
cp doc/nognu %buildroot%_includedir/


%files
%doc README.* doc/ABAN* doc/CHANGES doc/KEYS.txt
%doc doc/NCC doc/TROUBLES doc/hacking*
%_bindir/*
%_man1dir/*
%_includedir/*

%changelog
* Tue Feb 06 2007 Vitaly Lipatov <lav@altlinux.ru> 2.6-alt0.1
- new version 2.6 (with rpmrb script)

* Fri Oct 27 2006 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt0.1
- new version 2.5 (with rpmrb script)

* Mon Jan 30 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt0.1
- initial build for ALT Linux Sisyphus
