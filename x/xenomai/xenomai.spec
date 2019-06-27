%define _unpackaged_files_terminate_build 1

Summary: Real-Time Framework for Linux (Cobalt)
Name: xenomai
Version: 3.0.8
Release: alt2
Source0: %{name}-%{version}.tar
License: GPL
Group: Networking/Other
Url: http://www.xenomai.org
ExclusiveArch: x86_64

BuildRequires: libiniparser-devel
#BuildRequires: doxygen asciidoc asciidoc-a2x w3m

%description
Xenomai is a real-time development framework cooperating with the Linux kernel,
in order to provide a pervasive, interface-agnostic, hard real-time support to
user-space applications, seamlessly integrated into the GNU/Linux environment.

Xenomai is based on an abstract RTOS core, usable for building any kind of real-time
interfaces, over a nucleus which exports a set of generic RTOS services. Any number
of RTOS personalities called skins can then be built over the nucleus, providing
their own specific interface to the applications, by using the services of a single
generic core to implement it.

This version is for Cobalt core.

%package -n lib%name
Summary: Xenomai libraries (Cobalt)
Group: Networking/Other

%description -n lib%name
Library files for Xenomai (Cobalt)

%package -n lib%name-devel
Summary: Xenomai development header files
Group: Development/C

%description -n lib%name-devel
Header files for Xenomai Library files

%package -n lib%name-devel-static
Summary: Xenomai static libraries (Cobalt)
Group: Development/C

%description -n lib%name-devel-static
Static library files for Xenomai (Cobalt)

%package -n %name-kernel-source
Summary: Xenomai (Cobalt) patches for Linux kernel
Group: Development/C
BuildArch: noarch

%description -n %name-kernel-source
Linux kernel patches for Xenomai (Cobalt)

%prep
%setup -q

%build
%autoreconf
export CFLAGS=-fno-omit-frame-pointer
%configure --with-core=cobalt \
	--includedir=/usr/include/xenomai \
	--with-testdir=/usr/lib/xenomai \

%make_build

%install
%makeinstall_std SUDO=false
rm -rf %buildroot/usr/src/debug
rm -rf %buildroot/usr/lib/debug
rm -rf %buildroot/usr/demo
mkdir -p %buildroot/usr/src/xenomai-kernel-source/config
cp -Ra	scripts	\
	include	\
	kernel	%buildroot/usr/src/xenomai-kernel-source/
cp config/version-{code,label} \
		%buildroot/usr/src/xenomai-kernel-source/config/
mv %buildroot/usr/sbin/version %buildroot/usr/sbin/xeno-version

%files
%doc README
/etc/*.conf
%_bindir/*
%exclude %_bindir/xeno-config
%exclude %_bindir/wrap-link.sh
%_sbindir/*
%_libexecdir/%name/

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/xenomai
%_libdir/*.so
%_bindir/xeno-config
%_bindir/wrap-link.sh
%_libdir/*.wrappers
%_libdir/dynlist.ld
%_libdir/%name/*.o

%files -n lib%name-devel-static
%_libdir/lib*.a*

%files -n %name-kernel-source
%_usrsrc/xenomai-kernel-source

%changelog
* Thu Jun 27 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.8-alt2
- Make proper -devel package.

* Fri Jun 21 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.8-alt1
- Update to 3.0.8
- Add xenomai-kernel-source package

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.4.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jun 02 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Mon May 18 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.7-alt1
- intial build for ALT

