# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# git clone https://github.com/emeryberger/Heap-Layers.git
# cd Heap-Layers
# DATE=$(git log -1 --format="%cd" --date=short | sed "s|-||g")
# git archive --format=tar --prefix=Heap-Layers-${DATE}/ master | xz > ../Heap-Layers-${DATE}.tar.xz
#

%define hdate 20180514

#
# git clone https://github.com/emeryberger/Hoard.git
# cd Hoard
# DATE=$(git log -1 --format="%cd" --date=short | sed "s|-||g")
# git archive --format=tar --prefix=Hoard-${DATE}/ master | xz > ../Hoard-${DATE}.tar.xz
#
%define gdate 20180524
%define rel 4

%define major 0
%define libname libhoard%{major}
%define develname libhoard-devel

Summary:	The Hoard Memory Allocator
Name:		libhoard
Version:	3.12
Release:	alt1_1.git20180524.4
Group:		System/Libraries
License:	GPL
URL:		http://www.hoard.org/
#Source0:	https://github.com/emeryberger/Hoard/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	Hoard-%{gdate}.tar.xz
Source1:	Heap-Layers-%{hdate}.tar.xz
Patch1:		libhoard-3.12-mga-build.patch
Source44: import.info

%description
The Hoard memory allocator is a fast, scalable, and memory-efficient memory
allocator for Linux, Solaris, Mac OS X, and Windows. Hoard is a drop-in
replacement for malloc that can dramatically improve application performance,
especially for multithreaded programs running on multiprocessors and multicore
CPUs.

%package -n	%{libname}
Summary:	A fast, scalable, and memory-efficient memory allocator
Group:		System/Libraries

%description -n	%{libname}
The Hoard memory allocator is a fast, scalable, and memory-efficient memory
allocator for Linux, Solaris, Mac OS X, and Windows. Hoard is a drop-in
replacement for malloc that can dramatically improve application performance,
especially for multithreaded programs running on multiprocessors and multicore
CPUs.

%package -n	%{develname}
Summary:	Development files for libhoard
Group:		Development/C++
Requires:	%{libname} >= %{version}
Provides:	hoard-devel = %{version}

%description -n	%{develname}
This package contains development files for libhoard.

%prep
%setup -q -n Hoard-%{gdate} -a1
%patch1 -p1

pushd src
ln -s ../Heap-Layers-* Heap-Layers
popd

%build
%add_optflags %optflags_shared
export MGAFLAGS="%{optflags}"
%ifarch armv7hl x86_64 aarch64
export MGAFLAGS="$MGAFLAGS -fPIC"
%endif
export LDFLAGS=""
%make_build -C src generic-gcc CXX=g++

%install
install -d %{buildroot}%{_libdir}
install -m0755 src/libhoard.so.%{major} %{buildroot}%{_libdir}
ln -s libhoard.so.%{major} %{buildroot}%{_libdir}/libhoard.so

%files -n %{libname}
%doc doc NEWS README.md THANKS
%{_libdir}/libhoard.so.%{major}*

%files -n %{develname}
%{_libdir}/libhoard.so



%changelog
* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 3.12-alt1_1.git20180524.4
- update by mgaimport

* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 3.9.0-alt1_7
- new version

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 3.8.0-alt2
- auto rebuild

* Sat Apr 17 2010 Denis Smirnov <mithraen@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Mon Sep 21 2009 Denis Smirnov <mithraen@altlinux.ru> 3.7.1-alt2
- build with -fPIC

* Sun Sep 20 2009 Denis Smirnov <mithraen@altlinux.ru> 3.7.1-alt1
- first buidl for Sisyphus

