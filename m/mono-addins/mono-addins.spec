Name: mono-addins
Version: 0.6.2
Release: alt1
License: LGPL
URL: http://www.go-mono.com
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Summary: Mono Addins
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libgcc libgtk-sharp2-devel mono-devel mono-mcs

BuildRequires: /proc
BuildPreReq: rpm-build-mono

%description
Mono Addin Support

%package devel
Summary: Development files for Mono Addin
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for Mono Addin

%prep
%setup -q
%patch -p1

%build
./autogen.sh
%configure --enable-gui
%make

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/mautil
%_monodir/%name
%_monodir/xbuild/*
%_monogacdir/*
%_man1dir/*.gz

%files devel
%_pkgconfigdir/*.pc

%changelog
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
