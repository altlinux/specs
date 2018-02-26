%def_disable static

Name: libpfring
Version: 1.0.0
Release: alt3

Summary: User space library used to manpulate PF_RING
License: GPLv3+
Group: System/Libraries
Url: http://www.ntop.org/PF_RING.html

Source: %name-%version.tar

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

%build
# First build shared,
%make_build CFLAGS="%optflags %optflags_shared"
mkdir -p shared
gcc -shared -o shared/libpfring.so.%version \
	-Wl,-soname,%soname \
	-Wl,-whole-archive,libpfring.a,-no-whole-archive \
	-lpthread

#%if_enabled static
## then static.
#make clean
#%make_build CFLAGS="%optflags"
#%endif #static

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
install -pm644 shared/libpfring.so.%version %buildroot%_libdir/
ln -s libpfring.so.%version %buildroot%_libdir/%soname
ln -s libpfring.so.%version %buildroot%_libdir/libpfring.so
%if_enabled static
install -pm644 libpfring.a %buildroot%_libdir/
%endif #static
install -pm644 pfring.h %buildroot%_includedir/
install -pm644 pfring_e1000e_dna.h %buildroot%_includedir/

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
* Wed Oct 20 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt3
- add pfring_e1000e_dna.h to includedir
- don't build static subpackage

* Thu Oct 14 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2
- update for kernel module v4.4.1

* Thu Feb 25 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- initial build
