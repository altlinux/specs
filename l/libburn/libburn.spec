Name: libburn
Version: 1.4.9
Release: alt0.1

Summary: CD/DVD-R/RW disc reading/writing library
License: %gpl2plus
Group: System/Libraries
#Url: http://libburnia-project.org
Url: https://dev.lovelyhq.com/libburnia/web/wikis/home

#VCS: https://dev.lovelyhq.com/libburnia/libburn.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

Packager: Anton V. Boyrahinov <boyarsh@altlinux.org>

BuildRequires(pre): rpm-build-licenses

%description
libburnia.pykix.org is an open-source software project for reading, mastering
and writing optical discs. For now this means only CD-R, CD-RW, DVD-RAM,
DVD+RW, DVD-RW.

The project comprises of several more or less interdependent parts which
together strive to be a usable foundation for application development.
These are libraries, language bindings, and middleware binaries which emulate
classical (and valuable) Linux tools.

Our scope is currently Linux 2.4 and 2.6 only. For ports to other systems
we would need : login on a development machine resp. a live OS on CD or DVD,
advise from a system person about the equivalent of Linux sg or FreeBSD CAM,
volunteers for testing of realistic use cases.

We have a workable code base for burning CDs and overwriteable DVDs, though.
The burn API is quite comprehensively documented and can be used to build a
presentable application.
We have a functional binary which emulates parts of cdrecord in order to
prove that usability, and in order to allow you to explore libburnia's scope
by help of existing cdrecord frontends.

%package devel
Summary: Development files for libburn
Group: Development/C
Requires: %name = %version-%release

%description devel
libburnia.pykix.org is an open-source software project for reading, mastering
and writing optical discs. For now this means only CD-R, CD-RW, DVD-RAM,
DVD+RW, DVD-RW.

The project comprises of several more or less interdependent parts which
together strive to be a usable foundation for application development.
These are libraries, language bindings, and middleware binaries which emulate
classical (and valuable) Linux tools.

Our scope is currently Linux 2.4 and 2.6 only. For ports to other systems
we would need : login on a development machine resp. a live OS on CD or DVD,
advise from a system person about the equivalent of Linux sg or FreeBSD CAM,
volunteers for testing of realistic use cases.

We have a workable code base for burning CDs and overwriteable DVDs, though.
The burn API is quite comprehensively documented and can be used to build a
presentable application.
We have a functional binary which emulates parts of cdrecord in order to
prove that usability, and in order to allow you to explore libburnia's scope
by help of existing cdrecord frontends.

%package -n cdrskin
Summary: minimal cdrecord implementation based on libburn
Group: Archiving/Cd burning
Requires: %name = %version

%description -n cdrskin
cdrskin  is a limited cdrecord compatibility wrapper for libburn.
Cdrecord is a powerful GPL'ed burn program included in Joerg
Schilling's cdrtools. cdrskin strives to be a second source for
the services traditionally provided by cdrecord.
cdrskin does not contain any bytes copied from cdrecord's sources.
Many bytes have been copied from the message output of cdrecord
runs, though.

%prep
%setup
#%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*

%files devel
%dir %_includedir/%name
%_includedir/%name/%name.h
%_libdir/%name.so
%_pkgconfigdir/*.pc

%files -n cdrskin
%_bindir/cdrskin
%_man1dir/*

%changelog
* Thu Feb 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.9-alt0.1
- updated to 1.4.8-9-gc84889b

* Fri Dec 20 2013 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- 1.3.4
- updated Url:

* Sun Feb 24 2013 Michael Shigorin <mike@altlinux.org> 1.2.6-alt1
- 1.2.6
- minor spec cleanup according to policy recommendations

* Wed Nov 07 2012 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

* Tue Mar 20 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Mon Oct 31 2011 Mikhail Efremov <sem@altlinux.org> 1.1.6-alt1
- 1.1.6.

* Wed Jun 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.6.pl00-alt1
- 1.0.6.pk00

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.0.pl00-alt1
- 0.9.0.pl00

* Sun Nov 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.8.pl00-alt1
- 0.8.8.pl00
- -devel dependances fixed (closes #12907)

* Thu Sep 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.6.pl00-alt1
- 0.8.6.pl00

* Thu May 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.0.pl00-alt1
- 0.8.0.pl00

* Tue Dec 08 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.4.pl00-alt1
- 0.7.4.pl00

* Mon Nov 09 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.2.pl00-alt1
- 0.7.2.pl00

* Tue Apr 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.4.pl00-alt1
- 0.6.4.pl00

* Thu Mar 06 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.2-alt1
- new version

* Sun Jan  6 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version

* Wed Sep 26 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.8-alt2
- cdrskin linking fix from led@
- spec fix fom led@

* Wed Sep 19 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3.8-alt1
- new version
- added requires to subpackages

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.4-alt1
- new version

* Thu Feb 08 2007 Eugene Ostapets <eostapets@altlinux.org> 0.3.0.1-alt0.1
- Initial build

