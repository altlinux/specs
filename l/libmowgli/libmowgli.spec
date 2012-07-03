Name: libmowgli
Version: 0.9.50
Release: alt1

Summary: mowgli is a development framework for C (like GLib)

License: see COPYING
Group: System/Libraries
#Url: http://sacredspiral.co.uk/~nenolod/mowgli/
#Url: http://www.atheme-project.org/projects/mowgli.shtml
#Url: https://launchpad.net/ubuntu/+source/libmowgli

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://distfiles.atheme.org/%name-%version.tar

%description
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries, hashes),
or replace some of the slow GLib list manipulation functions), or stand
alone. It also provides a powerful hook system and convenient logging
for your code, as well as a high performance block allocator.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_includedir/*

%changelog
* Mon Apr 18 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.50-alt1
- new version 0.9.50 (with rpmrb script)

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt2
- cleanup spec, remove broken Url

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Sat Oct 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)
- fix URL, Source URL

* Sun Aug 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version 0.3.1 (with rpmrb script)

* Sun Aug 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- initial build for ALT Linux Sisyphus

