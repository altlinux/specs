Summary: CUPS printer drivers for SPL (Samsung Printer Language) printers

%define real_name splix
Name: printer-driver-%real_name
Version: 2.0.0
Release: alt2.svn306

Provides: %real_name = %version
Obsoletes: %real_name

# svn co https://splix.svn.sourceforge.net/svnroot/splix/splix splix
# revision 306

License:	GPL
Group:		Publishing

URL: http://splix.ap2c.org/
Source:	http://downloads.sourceforge.net/splix/%real_name-%version.tar
Patch: splix-2.0.0-mdv-gcc44.patch
Patch1: splix-2.0.0-mdv-tools-nojbig.patch
Patch2: splix-2.0.0-debian-arm-alighnment.patch
Patch3: splix-deviceID.patch

Requires: cups

# Automatically added by buildreq on Tue Nov 06 2007
BuildRequires: cups-ddk gcc-c++ libqt4-devel

%description
SpliX is a set of CUPS printer drivers for SPL (Samsung Printer Language)
printers. If you have a such printer, you need to download and use SpliX.
Moreover you will find documentation about this proprietary language.

%package tools
Summary: additional tools for splix
License: GPL
Group: Publishing
Requires: %name = %version-%release

%description tools
An additional tools for splix

%prep

%setup -q -n %real_name-%version
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make V=1 OPTIM_CXXFLAGS="%optflags" DISABLE_JBIG=1 THREADS=1

#additional tools
%make CXXFLAGS="%optflags `pkg-config QtCore --cflags`" LIBS="`pkg-config QtCore --libs`" -C tools

%install
%makeinstall_std

#additional tools
install -Dpm755 tools/decompress %buildroot%_bindir/%name-decompress

%files
%doc AUTHORS COPYING ChangeLog README THANKS TODO
%_prefix/lib/cups/filter/*
%_datadir/cups/model/*/*

%files tools
%_bindir/*

%changelog
* Tue Jun 05 2012 Fr. Br. George <george@altlinux.ru> 2.0.0-alt2.svn306
- Update to current svn
- Rawhide patch applied

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt2
- repair build (not tested!)
- ARM support patch from debian

* Mon Sep 14 2009 Stanislav Ievlev <inger@altlinux.org> 2.0.0-alt1
- 2.0.0

* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt1
- Initial build
