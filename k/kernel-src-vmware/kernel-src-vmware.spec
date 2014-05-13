%define mname vmware

%{!?x86_64:%define x86_64 x86_64}

Name: kernel-src-%mname
Version: 6.0.2
Release: alt2
Summary: Linux VMWare host modules sources
License: GPLv2
Group: Development/Kernel
URL: http://www.vmware.com
BuildArch: noarch
Source: %mname-%version.tar
Patch: %mname-%version-%release.patch
ExclusiveArch: %ix86 %x86_64

BuildRequires: rpm-build-kernel

%description
VMWare host modules sources for Linux kernel.


%prep
%setup -n %mname-%version
%patch -p1


%install
install -d -m 0755 %buildroot%_usrsrc/kernel/sources
tar -C .. -cJf %kernel_srcdir/%mname-%version.tar.xz %mname-%version


%files
%_usrsrc/kernel


%changelog
* Tue May 13 2014 Led <led@altlinux.ru> 6.0.2-alt2
- fixed typos

* Fri May 09 2014 Led <led@altlinux.ru> 6.0.2-alt1
- initial build
