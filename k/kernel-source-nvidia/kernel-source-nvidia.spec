%define mname nvidia
Name: kernel-source-%mname
Version: 310.44
Release: alt1
Summary: Linux nvidia module sources
License: NVIDIA
Group: Development/Kernel
URL: http://www.%mname.com
%define _ver %(echo "%version" | tr -d .)
ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64

BuildRequires: rpm-build-kernel
BuildRequires: %name-%_ver

%description
%mname module sources for Linux kernel.


%prep
%setup -q -T -c
tar -xf %kernel_src/%name-%_ver.tar*


%build


%install
install -d -m 0755 %buildroot%kernel_src
tar --transform='s,^%name-%_ver,%mname-%version,' -cJf %buildroot%kernel_src/%mname-%version.tar.xz %name-%_ver


%files
%_usrsrc/*


%changelog
* Wed Apr 24 2013 Led <led@altlinux.ru> 310.44-alt1
- 310.44
