%def_enable snapshot
%define _name p11-kit
%define _libexecdir %_prefix/libexec

%def_enable trust_module
# the hash implementation -- freebl or internal
%define hash_impl freebl
%define trust_paths %_datadir/ca-certificates/ca-bundle.crt
#%%define trust_paths %_sysconfdir/pki/ca-trust/source:%_datadir/pki/ca-trust-source
%def_disable systemd

Name: lib%_name
Version: 0.23.9
Release: alt1

Summary: Library for loading and sharing PKCS#11 modules
Group: System/Libraries
License: BSD
Url: http://p11-glue.freedesktop.org/p11-kit.html

%if_enabled snapshot
# VCS: https://github.com/p11-glue/p11-kit.git
Source: %_name-%version.tar
%else
#Source: http://p11-glue.freedesktop.org/releases/%_name-%version.tar.gz
Source: https://github.com/p11-glue/%_name/releases/download/%version/%_name-%version.tar.gz
%endif

Source1: p11-kit-extract-trust
Patch: %name-0.23.8-alt-lfs.patch
Patch1: %name-0.23.8-proxy-refresh-slots.patch

Requires: ca-certificates
Requires: pkcs11-trust-module = %version-%release

BuildRequires: libtasn1-devel libffi-devel
%if %hash_impl == freebl
BuildRequires: libnss-devel
%endif
%{?_enable_systemd:BuildRequires: systemd-devel}
%{?_enable_doc:BuildRequires: gtk-doc}

%description
%_name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

%package        trust
Summary: System trust module from %name package
Group: System/Libraries
Requires: %name = %version-%release
Provides: pkcs11-trust-module = %version-%release
#Conflicts: libnss < 3.14.3

%description    trust
The %name-trust package contains a system trust PKCS#11 module which
contains certificate anchors and black lists.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
%_name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

The %name-devel package provides libraries and headers for developing
applications that use %_name library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/C
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%_name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they\'re discoverable.

This package contains development documentation for %_name library.

%prep
%setup -n %_name-%version
%patch1 -p1
%{?_enable_snapshot:NOCONFIGURE=1 ./autogen.sh}
%patch

%build
%autoreconf
%configure --disable-static \
	--enable-debug=no \
	%{subst_enable trust_module} \
%if_enabled trust_module
	--with-libtasn1 \
	--with-trust-paths=%trust_paths \
%endif
	--with-hash-impl=%hash_impl \
	%{subst_enable doc}
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/pkcs11/modules
install -p -m755 %SOURCE1 %buildroot/%_libexecdir/%_name/

# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_libdir/libnssckbi.so	%_libdir/pkcs11/p11-kit-trust.so 30
EOF

%check
#%make check

%files
%_bindir/%_name
%_bindir/trust
%_libdir/lib%_name.so.*
%_libdir/%_name-proxy.so
%dir %_libexecdir/%_name
%_libexecdir/%_name/p11-kit-remote
%dir %_datadir/%_name
%dir %_datadir/%_name/modules
%dir %_sysconfdir/pkcs11
%dir %_sysconfdir/pkcs11/modules

%if_enabled systemd
%_prefix/lib/systemd/user/%_name-remote.socket
%_prefix/lib/systemd/user/%_name-remote@.service
%_prefix/lib/systemd/user/sockets.target.wants/%_name-remote.socket
%endif

%_libdir/pkcs11/%_name-client.so
%_libexecdir/%_name/%_name-server
%doc %_name/pkcs11.conf.example
%doc AUTHORS COPYING NEWS README

%exclude %_sysconfdir/pkcs11/pkcs11.conf.example
%exclude %_libdir/pkcs11/*.la

%if_enabled trust_module
%files trust
%_libdir/pkcs11/%_name-trust.so
%_datadir/%_name/modules/%_name-trust.module
%_libexecdir/%_name/%_name-extract-trust
%_libexecdir/%_name/trust-extract-compat
%exclude %_altdir/%name
%endif

%files devel
%_includedir/%_name-1
%_libdir/lib%_name.so
%_pkgconfigdir/%_name-1.pc

%if_enabled doc
%files devel-doc
%_datadir/gtk-doc/html/%_name
%endif

%changelog
* Mon Oct 16 2017 Paul Wolneykien <manowar@altlinux.org> 0.23.9-alt1
- Exclude the alteranatives file for libnssckbi.so.
- Patch the sources just after unpacking them.
- Release 0.23.9 (thx Daiki Ueno).

* Wed Sep 06 2017 Paul Wolneykien <manowar@altlinux.org> 0.23.8-alt2
- Refresh the slot list each time C_GetSlotList() is called (patch).

* Thu Aug 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23.8-alt1
- 0.23.8 (0.23.7-24-g26312a8)

* Sun Jun 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23.7-alt1
- 0.23.7

* Mon Mar 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23.5-alt1
- 0.23.5

* Sat Feb 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23.4-alt1
- 0.23.4

* Fri Dec 23 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.3-alt1
- 0.23.3

* Sun Jan 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.2-alt1
- 0.23.2

* Wed Dec 02 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.1-alt1
- 0.23.1 (ALT #31583)

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.22.1-alt1
- 0.22.1

* Tue Oct 07 2014 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Wed Sep 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21.2-alt1
- 0.21.3

* Mon Jul 07 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- 0.20.3

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Wed Oct 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Wed Sep 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Wed Aug 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.5-alt1
- 0.18.5

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt1
- 0.18.3

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Fri Apr 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Wed Apr 10 2013 Dmitry V. Levin <ldv@altlinux.org> 0.18.0-alt1
- Updated to 0.18.0 (stable).

* Sat Mar 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.17.5-alt1
- 0.17.5

* Sat Mar 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.17.4-alt1
- 0.17.4 (unstable)

* Wed Mar 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.4-alt1
- 0.16.4
- used %_datadir/pki/ca-trust-source and %_sysconfdir/pki/ca-trust/source
  as system CA anchors paths
- new -trust subpackage with system trust PKCS#11 module that provides
  an alternative to libnss module

* Sun Mar 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt1
- 0.16.3

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.15.2-alt1
- 0.15.2

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt1
- 0.14

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12
- %%check section

* Thu Nov 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Sun Sep 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Wed Aug 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- first build for Sisyphus

