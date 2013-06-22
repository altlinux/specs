%define mname kvm
Name: kernel-src-%mname
Version: 3.9
Release: alt1
Summary: KVM Linux kernel module sources
Group: Development/Kernel
BuildArch: noarch
License: GPLv2+
URL: http://www.linux-kvm.org
Source: %mname-kmod-%version.tar
Patch: %mname-kmod-%version-alt.patch
Provides: kernel-source-kvm = %version-%release

BuildRequires: rpm-build-kernel

%description
This package contains sources for the KVM Linux kernel modules.


%prep
%setup -q -n %mname-kmod-%version
%patch -p1


%install
install -d -m 0755 %buildroot%kernel_src
D="$(basename "$PWD")"
tar -C .. --transform "s/^$D/%mname-%version/" -cJf %buildroot%kernel_src/%mname-%version.tar.xz "$D"


%files
%_usrsrc/*


%changelog
* Sat Jun 22 2013 Led <led@altlinux.ru> 3.9-alt1
- 3.9

* Sat Jun 22 2013 Led <led@altlinux.ru> 3.8-alt1
- 3.8

* Thu Jun 20 2013 Led <led@altlinux.ru> 3.7.6-alt1
- 3.7.6

* Mon Nov 05 2012 Led <led@altlinux.ru> 3.6-alt1
- 3.6

* Thu Oct 25 2012 Led <led@altlinux.ru> 3.5.4-alt1
- 3.5.4

* Thu Aug 02 2012 Led <led@massivesolutions.co.uk> 3.5-cx0
- 3.5

* Thu May 24 2012 Led <led@massivesolutions.co.uk> 3.4-cx0
- 3.4

* Sat May 12 2012 Led <led@massivesolutions.co.uk> 3.3-cx0
- 3.3

* Fri Jan 20 2012 Led <led@massivesolutions.co.uk> 3.2-cx0
- 3.2

* Sun Nov 20 2011 Led <led@massivesolutions.co.uk> 3.1-cx0
- 3.1

* Fri Aug 19 2011 Led <led@massivesolutions.co.uk> 3.0b-cx0
- initial build
