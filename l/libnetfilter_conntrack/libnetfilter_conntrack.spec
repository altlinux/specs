Name: libnetfilter_conntrack
Version: 0.9.0
Release: alt1
Serial: 1

Summary: API to the in-kernel connection tracking state table.
License: %gpl2plus
Group: System/Libraries
Url: http://netfilter.org/projects/libnetfilter_conntrack/
Packager: Avramenko Andrew <liks@altlinux.ru>

Source: %name-%version.tar

Requires: libnfnetlink
# Automatically added by buildreq on Sat Oct 30 2010
BuildRequires: libnfnetlink-devel rpm-build-licenses

%description
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table

%package devel
Summary: Netfilter conntrack userspace library
Group: Development/C
Requires: %name = %version-%release

%description devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table

%prep
%setup -q

%build
%autoreconf -fisv
%configure --disable-static
%make_build

%install
%makeinstall
rm -f %buildroot%_libdir/%name/*.la

%files
%doc COPYING
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/%name
%_libdir/pkgconfig/*.pc


%changelog
* Sat Oct 30 2010 Anton Farygin <rider@altlinux.ru> 1:0.9.0-alt1
- New version
- updated build requires

* Sun Mar 01 2009 Avramenko Andrew <liks@altlinux.ru> 1:0.0.99-alt1
- New version
- Fix repocop warnings

* Sat Apr 19 2008 Avramenko Andrew <liks@altlinux.ru> 1:0.0.89-alt1
- New version 

* Wed Nov 28 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.82-alt1
- New version

* Mon Jul 30 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.81-alt1
- New version (bug fixes)

* Fri Jul 06 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.80-alt1
- New version

* Wed May 30 2007 Avramenko Andrew <liks@altlinux.ru> 1:0.0.75-alt1
- New version

* Mon May 07 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt3
- BuildRequires changed from libnfnetlink to libnfnetlink-devel 

* Thu Apr 13 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt2
- Add post/postun section
- Split devel package
- Disable static

* Wed Apr 11 2007 Avramenko Andrew <liks@altlinux.ru> 20070410-alt1
- New version build (fix #11443)

* Fri Mar 23 2007 Avramenko Andrew <liks@altlinux.ru> 0.0.31-alt1
- Initial build for Sisyphus
