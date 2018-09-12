Name: kmod-sign
Version: 4.18
Release: alt2

Summary: kernel modules signing tools
License: LGPL
Group: System/Kernel and hardware
BuildRequires: kernel-source-%version
BuildRequires: openssl-devel
Source0: kmod-gen-cert

%description
Set of tools for linux kernel modules signing

%prep
%setup -cT -n %name-%version
tar -xf /usr/src/kernel/sources/kernel-source-%version.tar
cp */scripts/{sign-file.c,extract-cert.c} ./

%build
gcc -o sign-file  sign-file.c -lcrypto
gcc -o extract-cert  extract-cert.c -lcrypto

%install
mkdir -p %buildroot%_bindir
install sign-file extract-cert %buildroot%_bindir
install %SOURCE0 %buildroot%_bindir

%files
%_bindir/*

%changelog
* Wed Sep 12 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 4.18-alt2
- script for key generation added

* Tue Sep 11 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 4.18-alt1
- initial build


