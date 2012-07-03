Version: 0.600.1
Release: alt1
%setup_python_module virtinst
Name: python-module-virtinst
Packager: Anton Protopopov <aspsk@altlinux.ru>

Summary: Python modules and utilities for installing virtual machines
License: GPLv2+
Group: Development/Python
Url: http://virt-manager.org/
BuildArch: noarch

# http://virt-manager.org/download/sources/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: python-devel

%description
virtinst is a module that helps build and install libvirt based virtual
machines. Currently supports KVM, QEmu and Xen virtual machines. Package
includes several command line utilities, including virt-install (build
and install new VMs) and virt-clone (clone an existing virtual machine).

%prep
%setup
%patch -p1

%build
%python_build

%install
%python_install
%find_lang %modulename

%files -f %modulename.lang
%_bindir/*
%python_sitelibdir/%modulename
%python_sitelibdir/virtconv
%python_sitelibdir/*.egg-*

%_man1dir/*
%_man5dir/*

%changelog
* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.600.1-alt1
- 0.600.1

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.600.0-alt2.git.6669f4
- git snapshot
- add ALT Linux detect OS

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.600.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.600.0-alt1
- 0.600.0

* Tue Mar 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.500.6-alt1
- 0.500.6

* Tue Jan 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.500.5-alt1
- 0.500.5

* Tue Jan 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.500.4-alt1.hg20110108
- snapshot 20110108

* Thu Dec 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.500.4-alt1.hg20101217
- snapshot 20101217

* Tue Dec 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.500.1-alt2
- Merge with gears/

* Wed Dec 09 2009 Anton Protopopov <aspsk@altlinux.org> 0.500.1-alt1
- Updated to 0.500.1.

* Thu Oct 08 2009 Anton Protopopov <aspsk@altlinux.org> 0.500.0-alt1
- Updated to 0.500.0.

* Thu Jul 02 2009 Dmitry V. Levin <ldv@altlinux.org> 0.400.3-alt1
- Updated to 0.400.3.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.400.0-alt1
- new version

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.300.3-alt1
- Initial ALT build
