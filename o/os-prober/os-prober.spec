%filter_from_requires s,python-module-zope\.app\.appsetup,,

Name: os-prober
Version: 1.52
Release: alt1

Summary: Operating systems detector
License: GPLv2+
Group: System/Configuration/Boot and Init
Url: http://packages.debian.org/sid/os-prober

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Source0: %name-%version.tar

Patch1: %name-1.41-evms-hackaround-alt.patch
Patch2: %name-1.42-UUID-rootdev-alt.patch

%description
This is a small package that may be depended on by any bootloader
installer package to detect other filesystems with operating systems on
them, and work out how to boot other linux installs.

%prep
%setup
%patch1 -p2
%patch2 -p1

%build
%make_build

%install
mkdir -p %buildroot/%_bindir/
cp -a os-prober %buildroot/%_bindir/
cp -a linux-boot-prober %buildroot/%_bindir/
mkdir -p %buildroot/usr/lib/
mkdir -p %buildroot/usr/lib/%name
cp -a newns %buildroot/usr/lib/%name

mkdir -p %buildroot/usr/lib/os-probes/init
cp -a os-probes/init/common/* %buildroot/usr/lib/os-probes/init
mkdir -p %buildroot/usr/lib/os-probes/mounted
cp -a os-probes/mounted/x86/* %buildroot/usr/lib/os-probes/mounted/
cp -a os-probes/mounted/common/* %buildroot/usr/lib/os-probes/mounted/
cp -a os-probes/common/* %buildroot/usr/lib/os-probes/

mkdir -p %buildroot/usr/lib/linux-boot-probes/mounted
cp -a linux-boot-probes/common/* %buildroot/usr/lib/linux-boot-probes
cp -a linux-boot-probes/mounted/x86/* %buildroot/usr/lib/linux-boot-probes/mounted/
cp -a linux-boot-probes/mounted/common/* %buildroot/usr/lib/linux-boot-probes/mounted/

mkdir -p %buildroot%_datadir/%name
cp -a common.sh %buildroot%_datadir/%name/
mkdir -p %buildroot%_localstatedir/%name

%files
%doc README
%_bindir/*
/usr/lib/linux-boot-probes
/usr/lib/os-probes
/usr/lib/%name
%_datadir/%name/
%_localstatedir/%name

%changelog
* Fri May 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.52-alt1
- 1.52

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.48-alt1
- 1.48

* Mon Jul 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.47-alt1
- 1.47

* Mon Apr 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.44-alt1
- 1.44

* Tue Mar 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.42-alt2
- add suport for UUID= root devices in lilo.conf (ALT #25168)

* Tue Feb 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.42-alt1
- 1.42

* Fri Nov 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.41-alt1
- 1.41

* Mon Oct 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.39-alt2
- hackaround evms

* Sun Jul 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.39-alt1
- 1.39

* Mon Jun 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.38-alt1
- 1.38

* Mon Apr 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.36-alt1
- initial
