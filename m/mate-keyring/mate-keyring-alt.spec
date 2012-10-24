# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/asn1Parser /usr/bin/gcov /usr/bin/genhtml /usr/bin/glib-genmarshal /usr/bin/gtkdocize /usr/bin/lcov /usr/bin/pkg-config /usr/bin/valgrind libcap-devel libpam0-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) valgrind-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define glib2_version 2.25.0
%define gtk2_version 2.20.0
%define dbus_version 1.0
%define gcrypt_version 1.2.2
%define libtasn1_version 0.3.4

Summary: 	Framework for managing passwords and other secrets
Name: 		mate-keyring
Version: 	1.4.0
Release: 	alt1_1.1
License: 	GPLv2+ and LGPLv2+
Group: 		System/Libraries
URL: 		http://pub.mate-desktop.org
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Source1: 	start-gnome-keyring-in-mate
Source2: 	start-gnome-keyring-in-mate.desktop

# why is gnome-keyring-daemon setuid root?
# https://bugzilla.redhat.com/show_bug.cgi?id=668831
Patch4: file-caps.patch

# gnome keyring pam module is starting gnome-keyring with the wrong SELinux context.
# https://bugzilla.redhat.com/show_bug.cgi?id=684225
Patch5: gnome-keyring-2.91.93-pam-selinux.patch

Patch6: mate-keyring_fix_desktop-file.patch


BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libdbus-devel >= %{dbus_version}
BuildRequires: libgcrypt-devel >= %{gcrypt_version}
BuildRequires: libtasn1-devel >= %{libtasn1_version}
BuildRequires: pam-devel
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libtasn1-utils
BuildRequires: libmatekeyring-devel
BuildRequires: gtk-doc
BuildRequires: mate-common
BuildRequires: libcap-ng-devel
BuildRequires: libselinux-devel

# for smooth transition since the core was split
Requires: libmatekeyring
Patch33: mate-keyring-1.3.0-alt-fix-pc.patch

%description
The mate-keyring session daemon manages passwords and other types of
secrets for the user, storing them encrypted with a main password.
Applications can use the mate-keyring library to integrate with the keyring.

%package devel
Summary: Development files for mate-keyring
License: LGPLv2+
Group: Development/C
Requires: mate-keyring = %{version}-%{release}
# for smooth transition since the core was split

%description devel
The mate-keyring-devel package contains the libraries and
header files needed to develop applications that use mate-keyring.

%package pam
Summary: Pam module for unlocking keyrings
License: LGPLv2+
Group: Development/C
Requires: mate-keyring = %{version}-%{release}
# for /lib64/security
Requires: pam

%description pam
The mate-keyring-pam package contains a pam module that can
automatically unlock the "login" keyring when the user logs in.


%prep
%setup -q -n mate-keyring-%{version}
%patch4 -p1 -b .file-caps
%patch5 -p1 -b .pam-selinux
%patch6 -p1 -b .mate-keyring_fix_desktop-file
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1

%build
autoreconf -i -f

%configure --with-root-certs=/usr/share/ca-certificates --disable-gtk-doc \
           --with-pam-dir=/%{_lib}/security \
           --enable-pam \
           --with-gtk=2.0 \

# avoid unneeded direct dependencies
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

#start gnome-kering in mate-session-properties
cp -f %{SOURCE1}  %{buildroot}%{_bindir}/start-gnome-keyring-in-mate
cp -f %{SOURCE2}  %{buildroot}%{_sysconfdir}/xdg/autostart/start-gnome-keyring-in-mate.desktop

rm $RPM_BUILD_ROOT/%{_lib}/security/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/pkcs11/*.la
rm $RPM_BUILD_ROOT%{_libdir}/mate-keyring/devel/*.la
rm $RPM_BUILD_ROOT%{_libdir}/mate-keyring/standalone/*.la

%find_lang mate-keyring

%files -f mate-keyring.lang
%doc AUTHORS NEWS README COPYING COPYING.LIB
# LGPL
%{_libdir}/lib*.so.*
%dir %{_libdir}/mate-keyring
%dir %{_libdir}/mate-keyring/devel
%{_libdir}/mate-keyring/devel/*.so
%{_libdir}/mate-keyring/standalone/gkm-secret-store-standalone.so
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/*.so
# GPL
%attr(0755,root,root)  %{_bindir}/mate-keyring-daemon
%{_bindir}/mate-keyring
%{_bindir}/start-gnome-keyring-in-mate
%{_libexecdir}/*
# wildcard _libexecdir/*
%exclude %_prefix/lib/debug
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mategcr
%{_datadir}/mate-keyring
%{_sysconfdir}/xdg/autostart/*
%{_datadir}/MateConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.gschema.xml

# unpackaged directory: /usr/lib/mate-keyring/devel
%dir %{_libdir}/mate-keyring/devel
# unpackaged directory: /usr/lib/mate-keyring/standalone
%dir %{_libdir}/mate-keyring/standalone


%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%doc %{_datadir}/gtk-doc

%files pam
/%{_lib}/security/pam_mate_keyring.so


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

