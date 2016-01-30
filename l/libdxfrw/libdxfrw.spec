Name: libdxfrw
Version: 0.6.3
Release: alt1

Summary: Library to read/write DXF files

License: GPLv2+
Group: System/Libraries
Url: http://sourceforge.net/p/libdxfrw/home/Home/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sourceforge.net/project/libdxfrw/%name-%version.tar

# Automatically added by buildreq on Sat Oct 17 2015
# optimized out: libstdc++-devel python3-base
BuildRequires: gcc-c++

%description
libdxfrw is a free C++ library to read and write DXF files in both formats,
ASCII and binary form.

%package devel
Summary: Development files for libdxfrw
Requires: %name = %version-%release
Group: Development/Other

%description devel
Development files for libdxfrw.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
#rm -rf %buildroot%_libdir/*.la

%files
%doc AUTHORS ChangeLog COPYING README
%_bindir/dwg2dxf
%_libdir/*.so.*

%files devel
%_includedir/libdxfrw0/
%_libdir/*.so
%_pkgconfigdir/libdxfrw0.pc

%changelog
* Sat Jan 30 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- initial build for ALT Linux Sisyphus

* Fri Sep 11 2015 Tom Callaway <spot@fedoraproject.org> - 0.6.1-1
- update to 0.6.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.11-4
- Rebuilt for GCC 5 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Tom Callaway <spot@fedoraproject.org> - 0.5.11-1
- update to 0.5.11
- resync with librecad changes

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-3
- apply fixes from librecad 2.0.0beta5

* Wed Apr 24 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-2
- drop empty NEWS and TODO files
- force INSTALL to use -p to preseve timestamps

* Sun Feb 24 2013 Tom Callaway <spot@fedoraproject.org> - 0.5.7-1
- initial package
