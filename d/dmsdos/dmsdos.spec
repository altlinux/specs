Name:		dmsdos
Version:	0.9.2.3
Release:	alt2
Summary:	Reads compressed dos filesystems (CVF-FAT)
Group:		File tools
Source:		%name-%version-pre2.tgz
Patch1:		patch-aa
Patch2:		patch-ab
Patch3:		dmsdos-0.9.2.3-pre2-make.patch
License:	GPL
URL:		http://cmp.felk.cvut.cz/~pisa/dmsdos/sources

%description
DMSDOS gives read access to compressed partitions (files like
dblspace.xxx, drvspace.xxx and stacvol.xxx). The following
configurations are supported:
   - DoubleSpace / DriveSpace (msdos 6.x)
   - DoubleSpace / DriveSpace (older win95 releases)
   - DriveSpace 3 (win95 with Plus! pack or newer win95)
   - Stacker 3
   - Stacker 4

%package -n lib%name-devel
Group:	Development/C
Summary: Development environment for %name
%description -n lib%name-devel
Read and write access to compressed DOS partitions.

%prep
%setup -n %name-%version-pre2
chmod -R +rwX .
%patch1
%patch2
%patch3 -p1

%build
cd src
cp dmsdos-config.h.default dmsdos-config.h
%make_build without_kernel

%install
mkdir -p %buildroot{%_man1dir,%_man8dir,%_bindir,%_sbindir,%_libdir,%_includedir/%name}
cd src
install cvflist cvftest mcdmsdos dcread %buildroot%_bindir
install dmsdosfsck %buildroot%_sbindir
install lib*.so* %buildroot%_libdir
install *.h %buildroot%_includedir/%name

cd ../man
install dmsdosfsck.8  %buildroot%_man8dir
install cvflist.1  cvftest.1  dmsdosfsck.8  mcdmsdos.1 %buildroot%_man1dir

%files
%doc README
%_sbindir/*
%_bindir/*
%_man1dir/*
%_man8dir/*
%_libdir/*.so.*

%files -n lib%name-devel
%doc doc src/dcread.c
%_libdir/*.so
%_includedir/%name

%changelog
* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 0.9.2.3-alt2
- Fix gcc4.6 build

* Sun Mar 25 2012 Fr. Br. George <george@altlinux.ru> 0.9.2.3-alt1
- Initial build

