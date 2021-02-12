%define _unpackaged_files_terminate_build 1

Name: mono-addins
Version: 1.3.3
Release: alt1
License: MIT
URL: http://www.go-mono.com
Group: Development/Other
Summary: Mono Addins

# https://github.com/mono/mono-addins.git
Source: %name-%version.tar

Patch1: mono-addins-alt-build-1.patch
Patch2: mono-addins-alt-build-2.patch
Patch3: mono-addins-opensuse-fix-delay-sign.patch

BuildRequires(pre): rpm-build-mono
BuildRequires: libgcc libgtk-sharp2-devel mono-devel
BuildRequires: /proc

%description
Mono Addin Support

%package devel
Summary: Development files for Mono Addin
Group: Development/Other
Requires: %name = %EVR

%description devel
Development files for Mono Addin

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
./autogen.sh
%configure --enable-gui
%make

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/mautil
%_monodir/%name
%_monogacdir/*
%_man1dir/*.1*

%files devel
%_pkgconfigdir/*.pc

%changelog
* Fri Feb 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.3-alt1
- Updated to upstream version 1.3.3 (Closes: #39460).

* Sat Apr 30 2016 Denis Medvedev <nbr@altlinux.org> 0.6.2-alt3
- fix manpages packing

* Fri Aug 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt2
- fix build with automake >= 1.11.3

* Thu Feb 09 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt3
- update buildreq

* Fri Jun 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt2
- fix path to mautil for x86_64
- split *.pc files to devel package

* Fri Jan 16 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4-alt1
- 0.4

* Mon Feb 25 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Jan 09 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt2
- to apply a mono-policy for pkgconfig files (patch1)

* Mon Dec 31 2007 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- initial package for ALTLinux
