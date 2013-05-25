%define mname nvidia
Name: kernel-src-%mname
Version: 319.23
Release: alt1
Summary: Linux nvidia module sources
License: NVIDIA
Group: Development/Kernel
URL: http://www.%mname.com
%define _ver %(echo "%version" | tr -d .)
%define sname kernel-source-%mname-%_ver
ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64

BuildRequires: rpm-build-kernel
BuildRequires: %sname

%description
%mname module sources for Linux kernel.


%prep
%setup -q -T -c
tar -xf %kernel_src/%sname.tar*


%build
ln -sf Makefile.kbuild %sname/Makefile


%install
install -d -m 0755 %buildroot%kernel_src
tar --transform='s,^%sname,%mname-%version,' -cJf %buildroot%kernel_src/%mname-%version.tar.xz %sname


%files
%_usrsrc/*


%changelog
* Sat May 25 2013 Led <led@altlinux.ru> 319.23-alt1
- 319.23
- rename package: kernel-source-* -> kernel-src-*

* Fri May 17 2013 Led <led@altlinux.ru> 319.17-alt1
- 319.17

* Wed Apr 24 2013 Led <led@altlinux.ru> 310.44-alt1
- 310.44
