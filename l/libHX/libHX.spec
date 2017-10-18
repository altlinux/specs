Name: libHX
Version: 3.22
Release: alt1
Summary: General-purpose library for typical low-level operations

Group: System/Libraries
License: LGPLv2 or LGPLv3
URL: http://jengelh.hopto.org/files/libHX/

Source: libHX-%version.tar
Patch: %name-%version-%release.patch

%description
A library for:
- rbtree with key-value pair extension
- deques (double-ended queues) (Stacks (LIFO) / Queues (FIFOs))
- platform independent opendir-style directory access
- platform independent dlopen-style shared library access
- auto-storage strings with direct access
- command line option (argv) parser
- shconfig-style config file parser
- platform independent random number generator with transparent
  /dev/urandom support
- various string, memory and zvec ops

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/%name.so; do
        t=$(readlink "$f")
        ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/%name.so.* %buildroot/%_lib/

%files
/%_lib/%name.so.*

%files devel
%doc doc/api.txt README.txt
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/libHX.pc

%changelog
* Wed Oct 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 3.22-alt1
- 3.22

* Thu Oct 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.11-alt1
- v3.11

* Mon Jul 27 2009 Andriy Stepanov <stanv@altlinux.ru> 2.9-alt1
- Bump to  v2.9

* Tue Apr 21 2009 Andriy Stepanov <stanv@altlinux.ru> 2.7-alt1
- New version.

* Sat Jan 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.3-alt1
- buld for Sisyphus, based on Fedora package 

* Tue Jan 20 2009 Till Maas <opensource@till.name> - 2.3-1
- Update to new release

* Mon Dec 29 2008 Till Maas <opensource@till.name> - 2.1-1
- Update to new release

* Sat Dec 20 2008 Till Maas <opensource@till.name> - 1.25-3
- Fix .so symlink

* Thu Nov 27 2008 Till Maas <opensource@till.name> - 1.25-2
- Move libHX.so.* to /%%{_lib} because of /sbin/mount.crypt from pam_mount

* Thu Sep 11 2008 Till Maas <opensource@till.name> - 1.25-1
- Update to latest version

* Fri Sep 05 2008 Till Maas <opensource@till.name> - 1.23-1
- Update to latest version

* Wed Jun 11 2008 Till Maas <opensource till name> - 1.18-2
- Set variable V for make: displays full compiler commandline

* Wed Jun 11 2008 Till Maas <opensource till name> - 1.18-1
- Update to latest version

* Tue May 27 2008 Till Maas <opensource till name> - 1.17-1
- Update to latest version

* Mon May 05 2008 Till Maas <opensource till name> - 1.15-1
- Update to latest version
- Update description

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.10.2-2
- Autorebuild for GCC 4.3

* Wed Dec 26 2007 Till Maas <opensource till name> - 1.10.2-1
- update to latest version
- fixed bug: https://sourceforge.net/tracker/?func=detail&atid=430593&aid=1845721&group_id=41452

* Thu Sep 27 2007 Till Maas <opensource till name> - 1.10.1-2
- add tests as examples to devel documentation

* Wed Sep 26 2007 Till Maas <opensource till name> - 1.10.1-1
- initial spec for Fedora
