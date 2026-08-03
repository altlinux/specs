%define _unpackaged_files_terminate_build 1

Name:     open-vmdk
Version:  0.3.13
Release:  alt1

Summary:        Tools to create OVA files from raw disk images
License:        Apache-2.0
Group:          System/Configuration/Other
Url:            https://github.com/vmware/open-vmdk
Vcs:            https://github.com/vmware/open-vmdk.git

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: zlib-devel

%description
Open VMDK is an assistant tool for creating Open Virtual Appliance (OVA).
An OVA is a tar archive file with Open Virtualization Format (OVF) files
inside, which is composed of an OVF descriptor with extension .ovf,
one or more virtual machine disk image files with extension .vmdk,
and a manifest file with extension .mf.

%package -n ovfenv

Summary:       Tools to get or set OVF environment variables
Group:         System/Configuration/Other
Requires:      open-vm-tools
BuildArch:     noarch

%description -n ovfenv
Show the value of an OVF property, whether the properties
were presented to this VM in guestinfo or on a cdrom.
Optionally, allows a property value to be modified.

%prep
%setup

%build
%make_build

%install
%makeinstall_std DESTDIR=%buildroot PREFIX=/usr install

%python3_fix_shebang %buildroot%_bindir/ovfenv
	
install -m0644 templates/*.ovf %buildroot%_datadir/%name
install -d -m 755 %buildroot%_sharedstatedir/ovfenv

%files
%_bindir/mkova.sh
%_bindir/ova-compose
%_bindir/vmdk-convert
%_datadir/%name/
%config(noreplace) %_sysconfdir/open-vmdk.conf

%files -n ovfenv
%_bindir/ovfenv
%dir %_sharedstatedir/ovfenv

%changelog
* Fri Jul 31 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.3.13-alt1
- Initial build.

