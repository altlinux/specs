Name: trsec
Version: 1.0
Release: alt2

Summary: Translate between CISPO and Astra Linux security labels.
License: GPLv2
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Group: System/Kernel and hardware
Source0: %name-%version.tar

BuildPreReq: rpm-build-kernel
BuildRequires: libiptables-devel

%description
Translate between CISPO and Astra Linux security labels (userspace part).


%package -n kernel-source-trsec

Group: Development/Kernel
BuildArch: noarch
Summary: Translate between CISPO and Astra Linux security labels (source).
%description -n kernel-source-trsec
Translate between CISPO and Astra Linux security labels (source).

%prep
%setup -q
make libxt_TRSEC.so VERSION=%version

%install
make install-lib DESTDIR=%buildroot
cd ..
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%name-%version.tar.bz2 %name-%version

%files -n kernel-source-trsec
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar.bz2

%files
%doc README.md
/lib*/iptables/*

%changelog
* Tue Feb 20 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0-alt2
- build for sisyphus fixed
- pass VERSION to Makefile

* Tue Feb 20 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0-alt1
- first build


