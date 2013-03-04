%def_disable static

Name: libpfring
Version: 1.0.0
Release: alt5

Summary: User space library used to manpulate PF_RING
License: GPLv2
Group: System/Libraries
Url: http://www.ntop.org/PF_RING.html

Source: %name-%version.tar

Patch1: libpfring-1.0.0-alt-crap-path.patch
Patch2: libpfring-1.0.0-alt-crap-configure.patch

BuildRequires: glibc-pthread
BuildRequires: kernel-headers-pf_ring
%{?_enable_static:BuildRequires: glibc-devel-static}

%define vers_maj 1.0
%define libname libpfring%vers_maj
%define soname libpfring.so.%vers_maj

%description
PF_RING is a high speed packet capture library that turns a commodity PC into an efficient and cheap
network measurement box suitable for both packet and active traffic analysis and manipulation.
Moreover, PF_RING opens totally new markets as it enables the creation of efficient application such as
traffic balancers or packet filters in a matter of lines of codes.

User space library used to manpulate PF_RING

%package -n %libname
Summary: User space library used to manpulate PF_RING
Group: System/Libraries
Provides: %name = %version-%release
Obsoletes: %name

%description -n %libname
PF_RING is a high speed packet capture library that turns a commodity PC into an efficient and cheap
network measurement box suitable for both packet and active traffic analysis and manipulation.
Moreover, PF_RING opens totally new markets as it enables the creation of efficient application such as
traffic balancers or packet filters in a matter of lines of codes.

User space library used to manpulate PF_RING

%package devel
Summary: Development environment for %name
Group: Development/C
Requires: %libname = %version-%release
Requires: kernel-headers-pf_ring

%description devel
Development environment for %name

%package devel-static
Summary: Static library %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static library %name

%prep
%setup -q

%patch1 -p3
%patch2 -p3

%build
# remove static libs
rm -rf libs
%autoreconf
%configure --disable-bpf
%make_build

#%if_enabled static
## then static.
#make clean
#%make_build CFLAGS="%optflags"
#%endif #static

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
install -pm644 libpfring.so %buildroot%_libdir/libpfring.so.%version
ln -s libpfring.so.%version %buildroot%_libdir/%soname
ln -s libpfring.so.%version %buildroot%_libdir/libpfring.so
%if_enabled static
install -pm644 libpfring.a %buildroot%_libdir/
%endif #static
install -pm644 pfring.h %buildroot%_includedir/

%files -n %libname
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so

%if_enabled static
%files devel-static
%_libdir/*.a
%endif #static

%changelog
* Mon Mar 04 2013 Timur Aitov <timonbl4@altlinux.org> 1.0.0-alt5
- add SONAME

* Tue Feb 26 2013 Timur Aitov <timonbl4@altlinux.org> 1.0.0-alt4
- kernel module v5.5.2 (r5908)

* Wed Oct 20 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt3
- add pfring_e1000e_dna.h to includedir
- don't build static subpackage

* Thu Oct 14 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2
- update for kernel module v4.4.1

* Thu Feb 25 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- initial build
