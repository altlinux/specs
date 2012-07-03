Summary:	Binary firmware for the Poulsbo (psb) 3D X11 driver
Name:		firmware-psb
Version:	0.30
Release:	alt1
License:	Redistributable, no modification permitted
Group:		System/Kernel and hardware
URL:		http://ppa.launchpad.net/ubuntu-mobile/ubuntu/pool/main/p/psb-firmware/
Source0:	%{name}-%{version}.tar
BuildArch:	noarch


%description
This package contains the binary firmware for the Poulsbo (psb) 3D X11
driver.

%prep
%setup -q 

%install
mkdir -p %{buildroot}/lib/firmware
install -m 0644 msvdx_fw.bin %{buildroot}/lib/firmware


%files
%doc COPYING
/lib/firmware/msvdx_fw.bin

%changelog
* Fri Jun 04 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.30-alt1
- build for Sisyphus

* Thu Aug 20 2009 Adam Williamson <awilliam@redhat.com> - 0.30-3
- switch to noarch

* Wed Aug 19 2009 Adam Williamson <awilliam@redhat.com> - 0.30-2
- correct license for RPMFusion conventions

* Mon Aug 10 2009 Adam Williamson <awilliam@redhat.com> - 0.30-1
- begin changelog tracking

