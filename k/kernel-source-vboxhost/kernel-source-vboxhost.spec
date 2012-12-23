%define module_name vboxhost

%{!?x86_64:%define x86_64 x86_64}

Name: kernel-source-%module_name
Version: 4.1.24
Release: alt1
Summary: Linux VirtualBox host modules sources
License: GPLv2
Group: Development/Kernel
URL: http://www.virtualbox.org
BuildArch: noarch
Source: %module_name-%version.tar
Patch: %module_name-%version-%release.patch
ExclusiveArch: %ix86 %x86_64

BuildRequires: rpm-build-kernel

%description
VirtualBox host modules sources for Linux kernel.


%prep
%setup -n %module_name-%version
%patch -p1


%install
install -d -m 0755 %buildroot%_usrsrc/kernel/sources
tar --transform='s,^\.,/%module_name-%version,' -cJf %kernel_srcdir/%module_name-%version.tar.xz .


%files
%_usrsrc/kernel


%changelog
* Sun Dec 23 2012 Led <led@altlinux.ru> 4.1.24-alt1
- 4.1.24

* Wed Nov 14 2012 Led <led@altlinux.ru> 4.1.22-alt1
- 4.1.22

* Tue Aug 21 2012 Led <led@massivesolutions.co.uk> 4.1.20-cx1
- 4.1.20

* Tue Jun 26 2012 Led <led@massivesolutions.co.uk> 4.1.18-cx1
- 4.1.18

* Thu May 24 2012 Led <led@massivesolutions.co.uk> 4.1.16-cx1
- 4.1.16

* Sat May 12 2012 Led <led@massivesolutions.co.uk> 4.1.14-cx1
- 4.1.14

* Fri Jan 20 2012 Led <led@massivesolutions.co.uk> 4.0.16-cx1
- 4.0.16

* Mon Oct 31 2011 Led <led@massivesolutions.co.uk> 4.0.14-cx1
- 4.0.14

* Tue Jul 19 2011 Led <led@massivesolutions.co.uk> 4.0.12-cx1
- 4.0.12

* Fri Jul 01 2011 Led <led@massivesolutions.co.uk> 4.0.10-cx1
- 4.0.10

* Sat May 28 2011 Led <led@massivesolutions.co.uk> 4.0.8-cx1
- cleaned up spec

* Sat May 28 2011 Led <led@massivesolutions.co.uk> 4.0.8-cx0
- initial build
