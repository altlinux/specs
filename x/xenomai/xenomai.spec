%define _unpackaged_files_terminate_build 1
%define name xenomai
%define version 2.4.8
%define release alt1
%define libname      lib%name

Summary: Real-Time Framework for Linux
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar
Packager: Michail Yakushin <silicium@altlinux.org>
License: GPL
Group: Networking/Other
Url: http://www.xenomai.org
Requires: %libname

BuildRequires: gcc-c++

%description
Xenomai is a real-time development framework cooperating with the Linux kernel, 
in order to provide a pervasive, interface-agnostic, hard real-time support to 
user-space applications, seamlessly integrated into the GNU/Linux environment.

Xenomai is based on an abstract RTOS core, usable for building any kind of real-time
interfaces, over a nucleus which exports a set of generic RTOS services. Any number 
of RTOS personalities called skins can then be built over the nucleus, providing
their own specific interface to the applications, by using the services of a single 
generic core to implement it. 


%package -n %{libname}
Summary: Xenomailibraries
Group: Networking/Other

%description -n %{libname}
Library files for xenomai

%package -n libxenomai-devel
Summary: xenomai libraries - header files
Group: Development/C

%package -n libxenomai-devel-static
Summary: xenomai static libraries
Group: Development/C

%description -n libxenomai-devel
header files for xenomail Library files

%description -n libxenomai-devel-static
Static xenomai Library files

%prep
%setup -n xenomai 

%build
autoreconf -fisv
./configure --prefix=/usr/ --includedir=/usr/include/xenomai --libdir=%{_libdir} 
make 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT SUDO=false
rm -f $RPM_BUILD_ROOT/%{_libdir}/posix.wrappers
rm -f $RPM_BUILD_ROOT/%{_bindir}/xeno-info

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_man1dir}/*.1*
%{_man5dir}/*.5*
%{_datadir}/xenomai
%doc %_docdir/xenomai

%files -n %{libname}
%{_libdir}/lib*.so*

%files -n libxenomai-devel
%{_includedir}/xenomai

%files -n libxenomai-devel-static
%{_libdir}/lib*.a*

%changelog
* Tue Jun 02 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.8-alt1
- 2.4.8 

* Mon May 18 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.7-alt1
- intial build for ALT 

