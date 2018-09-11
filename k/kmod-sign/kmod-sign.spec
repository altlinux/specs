Name: kmod-sign
Version: 4.18
Release: alt1

Summary: kernel modules signing tools
License: LGPL
Group: System/Kernel and hardware
BuildRequires: kernel-source-%version
BuildRequires: openssl-devel

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

%files
%_bindir/*

%changelog
* Tue Sep 11 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 4.18-alt1
- initial build


