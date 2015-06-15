Name: livecd-initrd-add-cifs
Version: 0.1
Release: alt1

Summary: Added CIFS support for initrd
License: Public domain
Group: System/Base

Url: http://altlinux.org/m-p
Packager: Denis Pynkin <dans@altlinux.org>

BuildArch: noarch

Source0: cifs.mk

%description
%summary
Rules for make-initrd

%prep

%build

%install
install -pDm644 %SOURCE0 %buildroot/%_sysconfdir/initrd.mk.d/cifs.mk

%files
%_sysconfdir/initrd.mk.d/cifs.mk

%changelog
* Wed Jun 10 2015 Denis Pynkin <dans@altlinux.org> 0.1-alt1
- Initial version
