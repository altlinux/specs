Summary: unzip like for .adf files (Amiga devices dumps)
Name: unadf
Version: 0.10.7
Release: alt1
Url: https://adflib.github.io/
Source: ADFlib-%version.tar.gz
Patch: %name-doublecomm-alt.patch
License: GPLv2
Group: Archiving/Other

# Automatically added by buildreq on Thu Nov 04 2010
BuildRequires: gcc-c++

%description
unzip like for .adf files (Amiga devices dumps)
powered by ADFLib

%package -n libadf
Summary: unzip like for .adf files (Amiga devices dumps) -- the library
Group: Development/C

%description -n libadf
The ADFlib is a portable C library designed to manage Amiga formatted
devices like harddisks and ZIP disks, or dump files of this kind of
media via the .ADF format.

%package -n libadf-devel
Summary: unzip like for .adf files (Amiga devices dumps) -- development suite
Group: Development/C

%description -n libadf-devel
Development suite for ADFLib

%prep
%setup -n ADFlib-%version
#patch -p1

%build
%autoreconf
%configure --includedir=%_includedir/adflib
%make_build

%install
%makeinstall
rm -fv %buildroot%_libdir/*.a

%files
%doc README *.md
%_bindir/*
%_man1dir/*

%files -n libadf
%_libdir/libadf.so.*

%files -n libadf-devel
%doc %_datadir/doc/adflib
%dir %_includedir/adf
%_includedir/adf/*
%_libdir/lib*
%_pkgconfigdir/*
%exclude %_libdir/libadf.so.*

%check
make check

%changelog
* Fri Jun 26 2026 Fr. Br. George <george@altlinux.org> 0.10.7-alt1
- Autobuild version bump to 0.10.7

* Fri Jun 26 2026 Fr. Br. George <george@altlinux.org> 0.10.6-alt1
- Change upsteam and full update

* Mon Oct 18 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.12-alt1.qa3
- Fixed FTBFS.

* Thu Apr 15 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.12-alt1.qa2
- Fixed FTBFS.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.12-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Nov 04 2010 Fr. Br. George <george@altlinux.ru> 0.7.12-alt1
- Version up

* Tue Oct 13 2009 Fr. Br. George <george@altlinux.ru> 0.7.11-alt2
- Test rebuild failure fix

* Wed May 28 2008 Fr. Br. George <george@altlinux.ru> 0.7.11-alt1
- Initial build from scratch

* Sat Jan 20 2007 Laurent Clevy <lclevy@club-internet.fr> 1.0:
  - stable version of unadf

