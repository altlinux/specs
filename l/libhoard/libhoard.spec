Name: libhoard
Summary: The Hoard Multiprocessor Memory Allocator
Version: 3.8.0
Release: alt2
License: GPL
Group: System/Servers
BuildRequires: gcc-c++
Url: http://prisms.cs.umass.edu/emery/index.php?page=hoard
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar

%package devel
Summary: %summary
Group: Development/C
Requires: libhoard = %version-%release

%description devel
%summary

%description
The Hoard Multiprocessor Memory Allocator


%prep
%setup

%build
pushd src
find -type f -name '.depend' -print0 \
	| xargs -0r rm -f
%ifarch x86_64
%make_build linux-gcc-x86-64
%else
%make_build linux-gcc-x86
%endif

%install
pushd src
mkdir -p %buildroot%_includedir/hoard
find -type f -print0 | xargs -0r chmod -x
cp -a heaplayers %buildroot%_includedir/hoard/
cp *.h %buildroot%_includedir/hoard
install -m644 -D libhoard.so %buildroot%_libdir/libhoard.so

%files
%_libdir/libhoard.so

%files devel
%doc doc
%_includedir/hoard

%changelog
* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 3.8.0-alt2
- auto rebuild

* Sat Apr 17 2010 Denis Smirnov <mithraen@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Mon Sep 21 2009 Denis Smirnov <mithraen@altlinux.ru> 3.7.1-alt2
- build with -fPIC

* Sun Sep 20 2009 Denis Smirnov <mithraen@altlinux.ru> 3.7.1-alt1
- first buidl for Sisyphus

