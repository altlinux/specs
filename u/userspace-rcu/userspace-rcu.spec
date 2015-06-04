Name:           userspace-rcu
Version:        0.8.1
Release:        alt1
Summary:        RCU (read-copy-update) implementation in user space

Group:          System/Libraries
License:        LGPLv2+
URL:            http://lttng.org/urcu/

Source: 	%name-%version.tar
# Source0:        http://lttng.org/files/urcu/%{name}-%{version}.tar.bz2
Patch0:         userspace-rcu-aarch64.patch
BuildRequires:  autoconf automake libtool
# Upstream do not yet support mips
ExcludeArch:    mips
#Source44: import.info

%description
This data synchronization library provides read-side access which scales
linearly with the number of cores. It does so by allowing multiples copies
of a given data structure to live at the same time, and by monitoring
the data structure accesses to detect grace periods after which memory
reclamation is possible.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1


%build
# Patch for AArch64 and PPC64LE needs it
autoreconf -vif
%configure --disable-static
#Remove Rpath from build system
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

V=1 make %{?_smp_mflags}


%install
mkdir -p %buildroot

%make_install DESTDIR=%buildroot install
rm -vf %buildroot/%{_libdir}/*.la

%check
#TODO greenscientist: make check currently fail in mockbuild
#make check

%files
#%doc LICENSE gpl-2.0.txt lgpl-relicensing.txt lgpl-2.1.txt
%{_docdir}/%{name}/README
%{_docdir}/%{name}/ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/liburcu*.pc
%{_docdir}/%{name}/README
%{_docdir}/%{name}/*.txt


%changelog
* Thu Jun 04 2015 Danil Mikhailov <danil@altlinux.org> 0.8.1-alt1
- initial build for ALT Linux Sisyphus

