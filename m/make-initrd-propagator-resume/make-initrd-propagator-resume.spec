%add_findreq_skiplist /usr/share/make-initrd/features/*

Name: make-initrd-propagator-resume
Version: 0.2
Release: alt1

Summary: Put propagator resume from disk hooks into make-initrd generated image
License: GPL
Group: System/Base

Source0: %name-%version.tar 

# For new put-file utility
Requires: make-initrd >= 0.7.6-alt1

BuildArch: noarch

%description
Make-initrd feature, able to add resume from disk support to
hybrid propagator/make-initrd initrd

%prep
%setup

%install
mkdir -p %buildroot/usr/share/make-initrd/features/
cp -a propagator-resume %buildroot/usr/share/make-initrd/features/

%files 
%_datadir/make-initrd/features/propagator-resume

%changelog
* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- NMU: updated for current make-initrd (see make-initrd-propagator)

* Wed Apr 27 2011 Mykola Grechukh <gns@altlinux.ru> 0.1-alt1
- resume from disk works
- blacklisting modules

* Tue Apr 19 2011 Mykola Grechukh <gns@altlinux.ru> 0.0-alt3
- debugging

* Tue Apr 19 2011 Mykola Grechukh <gns@altlinux.ru> 0.0-alt2
- half-implemented, taken code from initramfs

* Sat Apr 16 2011 Mykola Grechukh <gns@altlinux.ru> 0.0-alt1
- initial work. No real functionality yet
