Name: libnetfilter_cthelper
Version: 1.0.0
Release: alt2

Summary: userspace library for helper infrastructure in kernel-space.
License: %gpl2plus
Group: System/Libraries
Url: http://netfilter.org/projects/libnetfilter_cttimeout/

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Sat Oct 30 2010
BuildRequires: libnfnetlink-devel rpm-build-licenses libmnl-devel

%description
libnetfilter_cthelper is the userspace library that provides the programming interface to the user-space helper 
infrastructure available since Linux kernel 3.6. With this library, you register, configure, enable and disable user-space helpers. 

%package devel
Summary: userspace library for helper infrastructure in kernel-space.
Group: Development/C
Requires: %name = %{?epoch:%epoch:}%version-%release

%description devel
libnetfilter_cthelper is the userspace library that provides the programming interface to the user-space helper 
infrastructure available since Linux kernel 3.6. With this library, you register, configure, enable and disable user-space helpers. 

%prep
%setup -q
%patch0 -p1

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
* Tue Feb 05 2019 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2
- rebuilt in new environment

* Mon Jun 24 2013 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- first build for Sisyphus
