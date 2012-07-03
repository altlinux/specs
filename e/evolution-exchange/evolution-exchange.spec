%define ver_major 3.4
%define eds_ver_base 1.2

%def_disable debug
%def_disable static
%def_with sysdb4
%def_with openldap
%def_with krb5
%def_disable static_ldap
%def_disable gtk_doc

Name: evolution-exchange
Version: %ver_major.3
Release: alt1

Summary: Microsoft Exchange connector for Evolution
License: GPLv2+
Group: Networking/Mail
URL: http://www.gnome.org/projects/evolution/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define ver_base 3.4
%define evo_ver_base 3.4

# from configure.in.
%define evolution_ver 3.4.1
%define glib_ver 2.30.0
%define gtk_ver 3.2.0
%define eds_ver 3.3.5
%define libsoup_ver 2.33.92

Requires: evolution >= %evolution_ver
Requires: evolution-data-server >= %eds_ver

BuildRequires: gnome-common gtk-doc GConf
BuildPreReq: intltool >= 0.35
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: evolution-data-server-devel >= %eds_ver
BuildPreReq: evolution-devel >= %evolution_ver
BuildPreReq: libGConf-devel
BuildPreReq: libxml2-devel
BuildPreReq: libsoup-devel >= %libsoup_ver

%if_with sysdb4
BuildRequires: libdb4-devel
%endif

%if_with openldap
BuildRequires: libldap-devel
%if_enabled static_ldap
BuildRequires: libldap-devel-static libssl-devel libsasl2-devel
%endif
%endif

%if_with krb5
BuildRequires: libkrb5-devel
%endif

%add_findprov_lib_path %_libdir/evolution/%ver_base

%description
This is the Ximian Connector for Microsoft Exchange, which adds
support for Microsoft Exchange 2000 and 2003 to Evolution.

%package doc
Summary: Documentation for Ximian Connector for Microsoft Exchange
Group: Networking/Mail
BuildArch: noarch
Conflicts: %name < %version

%description doc
This package contains documentation for Ximian Connector for Microsoft
Exchange

%prep
%setup -q

%build
%if_with openldap
%if_enabled static_ldap
%define ldap_flags --with-openldap=yes --with-static-ldap
# Set LIBS so that configure will be able to link with static LDAP libraries,
# which depend on Cyrus SASL and OpenSSL.  XXX Is the "else" clause necessary?
if pkg-config openssl ; then
	export LIBS="-lsasl2 `pkg-config --libs openssl`"
else
	export LIBS="-lsasl2 -lssl -lcrypto"
fi
%else
%define ldap_flags --with-openldap=yes
%endif
%else
%define ldap_flags --without-openldap
%endif

export CFLAGS="$RPM_OPT_FLAGS -DLDAP_DEPRECATED"

%configure \
    --disable-schemas-install \
    %{subst_enable static} \
    %{?_enable_debug:--with-e2k-debug} \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    %ldap_flags \
    %{?_with_sysdb4:--with-libdb=%_prefix} \
%if_with krb5
    --with-krb5=%_prefix \
    --with-krb5-libs=%_libdir \
    --with-krb5-includes=%_includedir/krb5 \
%endif

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name-%ver_base

%post
%gconf2_install apps_exchange_addressbook-%ver_base

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall apps_exchange_addressbook-%ver_base
fi

%files -f %name-%ver_base.lang
%_bindir/exchange-connector-setup-%ver_base
%_libdir/evolution/%evo_ver_base/plugins/*
%_libdir/%name/%ver_base/*.so*
%_libdir/evolution-data-server/camel-providers/*
%_libdir/evolution-data-server/addressbook-backends/*.so
%_libdir/evolution-data-server/calendar-backends/*.so
%_datadir/evolution/%evo_ver_base/errors/org-gnome-exchange-operations.error
%_datadir/%name
%config %_sysconfdir/gconf/schemas/*
%doc AUTHORS NEWS README

%exclude %_libdir/evolution/%evo_ver_base/plugins/*.la
%exclude %_libdir/evolution-data-server/addressbook-backends/*.la
%exclude %_libdir/evolution-data-server/calendar-backends/*.la
%exclude %_libdir/%name/%ver_base/*.la

%files doc
%_datadir/gtk-doc/html/*

%changelog
* Mon Jun 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Jan 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sun Sep 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Fri Sep 02 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Sat Mar 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt2
- fixed build against newer gtk

* Mon Feb 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Thu Aug 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Wed Apr 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt2
- rebuild against new evoluition release

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Feb 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Wed Aug 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Sat Feb 28 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.5-alt1
- 2.24.5

* Mon Feb 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.4-alt1
- 2.24.4

* Mon Jan 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- don't rebuild documentation
- new -doc noarch subpackage
- updated buildreqs

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1.1-alt1
- 2.24.1.1

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- removed 2.24.0-compiler-warnings.patch (fixed upsream)

* Thu Oct 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Sat May 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.1-alt1
- 2.22.1.1

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Thu Mar 13 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.12.3-alt1
- 2.12.3
- Add patch for RedHat bug #402131 (Filters don't work for exchange)
- Remove libgnomeprint requirement.
- Remove obsolete patches.

* Thu Nov 29 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Wed Nov 21 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.1-alt2
- remove LDFLAGS --no-as-needed (fixed in e-d-s)

* Thu Oct 25 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.1-alt1
- 2.12.1
- Removed evolution-exchange-2.11.92-compilation-breakage.patch (fixed upstream).
- Removed evolution-exchange-2.12.0-warnings.patch (fixed upstream).

* Sat Oct 13 2007 Alexey Shabalin <shaba@altlinux.ru> 2.12.0-alt1
- Release 2.12.0
- Add support build with static ldap (default disable-> %%def_disable ldap_static)
- Remove patch for GNOME bug #405916 (fixed upstream).
- Add patches:
  + evolution-exchange-2.11.92-compilation-breakage.patch
  + evolution-exchange-2.12.0-warnings.patch

* Fri Aug 17 2007 Alexey Shabalin <shaba@altlinux.ru> 2.10.3-alt1
- Update to 2.10.3
- change packager
- add/remove patches from fc7
- mini fix spec
- add gconf schema install


* Sun Mar 25 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt2
- add some patches

* Sat Feb 24 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.3-alt1
- updated to 2.8.3

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 2.8.2-alt1
- New release 2.8.2

* Thu Sep 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.0-alt1
- Release 2.8.0

* Sat Sep 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.3-alt1
- Release 2.6.3

* Sat Jun 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt2
- Updated dependencies to require e-d-s with new the sonames

* Fri Jun 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt1
- Release 2.6.2

* Sat May 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.1-alt1
- Release 2.6.1
- Disable and exclude gtk-doc documentation

* Sat Mar 18 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- Rebuild with evolution 2.6.0-alt2 that fixes x86_64 installation

* Wed Mar 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- Release 2.6.0
- Removed Debian-style menu
- Added --no-as-needed to ld flags

* Sun Mar 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.92-alt1
- 2.5.92

* Sun Feb 19 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.91-alt1
- Updated to 2.5.91
- Bzip the ChangeLog
- Buildreq

* Wed Nov 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.2-alt1
- 2.4.2
- Explicitly require libnspr and libnss for build

* Thu Oct 20 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt1
- Updated to 2.4.1
- Spec cleanup
- Enhanced summary and description
- Make install section reenterable

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Tue Apr 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Thu Mar 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Fri Feb 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sat Dec 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt0.5
- 2.0.2

* Thu Sep 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt0.5
- 2.0.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt0.5
- 2.0.0

* Sun Sep 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.94.1-alt0.5
- 1.5.94.1

* Wed Aug 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.92-alt0.5
- 1.5.92

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.91-alt0.5
- 1.5.91

* Tue Jul 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.5.90-alt0.5
- 1.5.90 release.

* Wed Jun 16 2004 Alex Gorbachenko <algor@altlinux.ru> 1.5.9-alt1
- initial build.
