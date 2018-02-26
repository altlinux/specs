Name:		kmod
Version:	8
Release:	alt2
Summary:	Linux kernel module management utilities

Group:		System/Kernel and hardware
License:	GPLv2+
URL:		http://modules.wiki.kernel.org/
ExclusiveOS:	Linux
Requires:	lib%name = %version-%release

Source0:	%name-%version.tar
Patch0:		%name-manpage.patch

BuildRequires:	docbook-dtds docbook-style-xsl glibc-devel-static liblzma-devel xsltproc zlib-devel

#Provides:	module-init-tools = 3.17-alt1
#Obsoletes:	module-init-tools < 3.17-alt1

%description
The kmod package provides various programs needed for automatic
loading and unloading of modules under 2.6, 3.x, and later kernels, as well
as other module management programs. Device drivers and filesystems are two
examples of loaded and unloaded modules.

%package -n lib%name
Summary:	Libraries to handle kernel module loading and unloading
License:	LGPLv2+
Group:		System/Kernel and hardware
Provides:	%name-libs = %version-%release

%description -n lib%name
The kmod-libs package provides runtime libraries for any application that
wishes to load or unload Linux kernel modules from the running system.

%package -n lib%name-devel
Summary:	Header files for kmod development
Group:		Development/C
Requires:	lib%name = %version-%release
Provides:	%name-devel = %version-%release

%description -n lib%name-devel
The libkmod-devel package provides header files used for development of
applications that wish to load or unload Linux kernel modules.

%prep
%setup -q
%patch0 -p1

%build
touch libkmod/docs/gtk-doc.make
%autoreconf

%configure \
	--prefix=/ \
	--disable-static \
	--bindir=/bin \
	--with-rootlibdir=/%_lib \
	--with-zlib \
	--with-xz
%make_build

%install
%make_install DESTDIR=%buildroot install
rm -rf %buildroot/%_libdir/*.la

# New configuration files we ship (if any) should go into /lib/modprobe.d
# in order to allow the local sysadmin to customize /etc/modprobe.d
mkdir -p %buildroot/{%_sysconfdir,/lib}/modprobe.d
mkdir -p %buildroot/{%_sysconfdir,/lib}/depmod.d

# Add blacklists from module-init-tools
find rpm/modprobe.d -maxdepth 1 -type f -name '*.conf' -print0 |
	xargs -r0 install -m644 -p -t %buildroot/lib/modprobe.d/ --

%ifarch %ix86 x86_64
install -m644 -p rpm/modprobe.d/arch/i386.conf %buildroot/lib/modprobe.d/arch.conf
%endif

# Make compatibility symlinks
mkdir -p %buildroot/sbin
for n in modprobe modinfo insmod rmmod depmod lsmod; do
	t=$(relative /bin/kmod /sbin/$n)
	ln -s "$t" "%buildroot/sbin/$n"
done

# lsmod was in /bin before
ln -s kmod %buildroot/bin/lsmod


%files
/bin/kmod
%doc NEWS README TODO COPYING

%files -n lib%name
/%_lib/libkmod.so*

%files -n lib%name-devel
%_includedir/libkmod.h
%_libdir/pkgconfig/libkmod.pc
%_libdir/libkmod.so

%changelog
* Thu May 10 2012 Alexey Gladkov <legion@altlinux.ru> 8-alt2
- Fix rename kmod-devel to libkmod-devel.
- Fix libkmod-devel requires.

* Wed Apr 25 2012 Alexey Gladkov <legion@altlinux.ru> 8-alt1
- Version (8).

* Thu Feb 16 2012 Alexey Gladkov <legion@altlinux.ru> 5-alt2
- Remove compatibility symlinks for now.

* Fri Feb 10 2012 Alexey Gladkov <legion@altlinux.ru> 5-alt1
- Version (5).
- Replace the module-init-tools package.
- Add blacklists.
- Add compatibility symlinks.

* Wed Feb 01 2012 Alexey Gladkov <legion@altlinux.ru> 4-alt1
- Version (4).
- Fix provides.

* Fri Jan 13 2012 Alexey Gladkov <legion@altlinux.ru> 3-alt1
- Version (3).
- Build for ALTLinux.

* Thu Jan 05 2012 Jon Masters <jcm@jonmasters.org> - 3-1
- Update to latest upstream (adds new depmod replacement utility)
- For the moment, use the "kmod" utility to test the various functions

* Fri Dec 23 2011 Jon Masters <jcm@jonmasters.org> - 2-6
- Update kmod-2-with-rootlibdir patch with rebuild automake files

* Fri Dec 23 2011 Jon Masters <jcm@jonmasters.org> - 2-5
- Initial build for Fedora following package import

* Thu Dec 22 2011 Jon Masters <jcm@jonmasters.org> - 2-4
- There is no generic macro for non-multilib "/lib", hardcode like others

* Thu Dec 22 2011 Jon Masters <jcm@jonmasters.org> - 2-3
- Update package incorporating fixes from initial review feedback
- Cleaups to SPEC, rpath, documentation, library and binary locations

* Thu Dec 22 2011 Jon Masters <jcm@jonmasters.org> - 2-2
- Update package for posting to wider test audience (initial review submitted)

* Thu Dec 22 2011 Jon Masters <jcm@jonmasters.org> - 2-1
- Initial Fedora package for module-init-tools replacement (kmod) library
