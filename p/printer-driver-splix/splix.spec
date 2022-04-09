Summary: CUPS printer drivers for SPL (Samsung Printer Language) printers

%define real_name splix
Name: printer-driver-%real_name
Version: 2.0.1
Release: alt2.svn315.1

Provides: %real_name = %version
Obsoletes: %real_name

# svn co https://splix.svn.sourceforge.net/svnroot/splix/splix splix
# revision 306

License: GPL
Group: Publishing

URL: http://splix.ap2c.org/
Source:	http://downloads.sourceforge.net/splix/%real_name-%version.tar
Patch: splix-2.0.0-mdv-gcc44.patch
Patch1: splix-2.0.0-mdv-tools-nojbig.patch
Patch2: splix-2.0.0-debian-arm-alighnment.patch
Patch3: splix-deviceID.patch
Patch4: splix-2.0.1-gcc8-fix.patch

Requires: cups

BuildRequires: cups-ddk gcc-c++

%description
SpliX is a set of CUPS printer drivers for SPL (Samsung Printer Language)
printers. If you have a such printer, you need to download and use SpliX.
Moreover you will find documentation about this proprietary language.

%prep

%setup -q -n %real_name-%version
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2

%build
%make_build V=1 OPTIM_CXXFLAGS="%optflags" DISABLE_JBIG=1 THREADS=1

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog README THANKS TODO
%_prefix/lib/cups/filter/*
%_datadir/cups/model/*/*

%changelog
* Tue Apr 05 2022 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt2.svn315.1
- build without qt4
- don't build additional tools

* Tue Feb 12 2019 Ivan Razzhivin <underwit@altlinux.org> 2.0.1-alt1.svn315.1
- GCC8 fix

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 2.0.1-alt1.svn315
- Update to current svn
- Move Samsung drivers back to /pps dir

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
