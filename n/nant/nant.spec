Name: nant
Version: 0.91
Release: alt1

Summary: A cross platform build tool for the .Net platform
License: GPLv2+
Group: Development/Other

# git://github.com/nant/nant.git
Url: http://nant.sourceforge.net

# for build boo with bootstraped nant
Provides: mono(NAnt.Core)
Provides: mono(NAnt.DotNetTasks)

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Tue Dec 25 2007
BuildRequires: mono-winforms mono-web libgcc mono-devel mono-mcs
BuildRequires: mono-nunit-devel

%description
NAnt is a .NET based build tool. In theory it is kind of like make without
make's wrinkles. In practice it's a lot like Ant.

If you are not familiar with Jakarta Ant you can get more information at the
Ant project web site (http://ant.apache.org/).

If you are not familiar with NAnt you can get more information at the NAnt
project web site (http://NAnt.sourceforge.net).

%package doc
Summary: Documentation and examples for nant
Group: Documentation
BuildArch: noarch

%description doc
Documentation for nant

%package devel
Summary: Develepment file for nant
Group: Development/Other
Requires: %name = %version-%release

%description devel
Develepment file for nant

%prep
%setup
%patch -p1

# install to libdir instead of datadir
sed -i -e "/property name=\"install\.share\"/ s/'share'/'lib'/" NAnt.build
sed -i -e "s,/share/,/lib/," etc/nant.pc.in

# Remove NDoc support
rm src/NAnt.DotNet/Tasks/NDocTask.cs
find lib -name 'NDoc*.dll' | xargs rm

# Remove NUnit1 support and fix build with system NUnit.
# Based on Debian's 004-nant-nunit_2.4.dpatch
find lib -iname 'nunit*' | xargs rm

# Remove SharpCvsLib support
find lib -name "*SharpCvsLib*.dll" | xargs rm
find lib -name "scvs.exe" | xargs rm

# Use system SharpZipLib which is older than the one bundled with nant
# https://bugzilla.novell.com/show_bug.cgi?id=426065
find lib -name "*SharpZipLib*.dll" | xargs rm


find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
sed -i 's/\r//' doc/license.html
sed -i 's/\r//' COPYING.txt
sed -i 's/\r//' README.txt
sed -i 's/\r//' doc/releasenotes.html

%build
%make

%install
%make install prefix=%_prefix DESTDIR=%buildroot

find examples -name \*.dll -o -name \*.exe|xargs rm -f
rm -rf %buildroot%_datadir/NAnt/doc

mkdir -p %buildroot/%_libdir/pkgconfig
test "%_libdir" = "%_prefix/lib" || mv %buildroot/%_prefix/lib/pkgconfig/* %buildroot/%_libdir/pkgconfig

## Fix script
#cat <<EOF > %buildroot%_bindir/nant
##!/bin/sh
#mono /usr/lib/NAnt/NAnt.exe "\$@"
#EOF
#chmod 755 %buildroot%_bindir/nant

%files
%_bindir/nant
#%_monogacdir/*
#%_libexecdir/NAnt
%_prefix/lib/NAnt

%files doc
%doc doc web examples

%files devel
%_pkgconfigdir/*.pc

%changelog
* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 0.91-alt1
- 0.91

* Fri May 22 2009 Alexey Shabalin <shaba@altlinux.ru> 0.86-alt6.cvs.20080818
- bootstrap, build with local dlls, as 0.86-alt4.cvs.20080818

* Fri Nov 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.86-alt5.cvs.20080818
- build with system libraries(patch1,patch2)
- install all libraries over gacutil (for sign use patch3)
- package doc as noarch

* Wed Sep 10 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.86-alt4.cvs.20080818
- cvs snapshot 20080818

* Tue Jan 15 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.86-alt3.cvs.20071228
- Removed BuildArch: noarch

* Fri Jan 11 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.86-alt2.cvs.20071228
- Updated to 0.86 post-beta1

* Fri May 18 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 0.86-alt2.cvs.20070514
- Do not try to detect path to mono with pkg-config in executable

* Mon May 14 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 0.86-alt1.cvs.20070514
- Initial build for Sisyphus
