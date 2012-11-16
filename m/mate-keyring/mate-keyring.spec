# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/asn1Parser /usr/bin/gcov /usr/bin/genhtml /usr/bin/glib-genmarshal /usr/bin/gtkdocize /usr/bin/lcov /usr/bin/pkg-config /usr/bin/valgrind libpam0-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-no-export-2.0) pkgconfig(gobject-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-3.0) valgrind-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary:        Framework for managing passwords and other secrets
Name:           mate-keyring
Version:        1.5.0
Release:        alt1_2
License:        GPLv2+ and LGPLv2+
Group:          System/Libraries
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# upstream commits
# https://github.com/mate-desktop/mate-keyring/commit/0269af132af17ecea87f869cda26100cd9b724a8
# https://github.com/mate-desktop/mate-keyring/commit/de7a2884feb7acd6abcd7f0bcb7eac963c787f4f
Patch0:         upstream_commits.patch


BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(mate-keyring-1)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  libtasn1-utils
BuildRequires:  libgcrypt-devel
BuildRequires:  pam-devel
BuildRequires:  mate-common
BuildRequires:  libcap-devel

Requires: libmatekeyring
Source44: import.info
Patch33: mate-keyring-1.3.0-alt-fix-pc.patch
# why is gnome-keyring-daemon setuid root?
# https://bugzilla.redhat.com/show_bug.cgi?id=668831
Patch34: mate-keyring-file-caps.patch
# gnome keyring pam module is starting gnome-keyring with the wrong SELinux context.
# https://bugzilla.redhat.com/show_bug.cgi?id=684225
Patch35: gnome-keyring-2.91.93-pam-selinux.patch
Source45: start-gnome-keyring-in-mate
Source46: start-gnome-keyring-in-mate.desktop

%description
The mate-keyring session daemon manages passwords and other types of
secrets for the user, storing them encrypted with a main password.
Applications can use the mate-keyring library to integrate with the keyring.

%package devel
Summary: Development files for mate-keyring
License: LGPLv2+
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The mate-keyring-devel package contains the libraries and
header files needed to develop applications that use mate-keyring.

%package pam
Group: Development/C
Summary: MATE Desktop pam module for unlocking keyrings
License: LGPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description pam
Shared library for MATE Desktop pam auth


%prep
%setup -q -n mate-keyring-%{version}
%patch0 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static \
           --with-gtk=2.0 \
           --enable-pam \
           --with-pam-dir=/%{_lib}/security \
           --with-root-certs=/usr/share/ca-certificates

# avoid unneeded direct dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

# Fix permissions on mate-keyring-daemon
chmod 0755 %{buildroot}%{_bindir}/mate-keyring-daemon

%find_lang %{name}
# do we need it ?
#start gnome-keyring in mate-session-properties
##cp -f %{SOURCE45}  %{buildroot}%{_bindir}/start-gnome-keyring-in-mate
##cp -f %{SOURCE46}  %{buildroot}%{_sysconfdir}/xdg/autostart/start-gnome-keyring-in-mate.desktop


%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING COPYING.LIB
%{_bindir}/mate-keyring
%{_bindir}/mate-keyring-daemon
%{_sysconfdir}/xdg/autostart/mate-keyring-pkcs11.desktop
%{_sysconfdir}/xdg/autostart/mate-keyring-secrets.desktop
%{_sysconfdir}/xdg/autostart/mate-keyring-ssh.desktop
%{_sysconfdir}/xdg/autostart/mate-keyring-gpg.desktop
%{_libexecdir}/mate-keyring-prompt
%{_libdir}/lib*.so.*
%{_libdir}/mate-keyring/
%{_libdir}/pkcs11/mate-keyring-pkcs11.so
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mategcr/
%{_datadir}/mate-keyring/
%{_datadir}/MateConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.gschema.xml

# unpackaged directory: /usr/lib/mate-keyring/devel
%dir %{_libdir}/mate-keyring/devel
# unpackaged directory: /usr/lib/mate-keyring/standalone
%dir %{_libdir}/mate-keyring/standalone


%files pam
/%{_lib}/security/pam_mate_keyring.so

%files devel
%doc %{_datadir}/gtk-doc/html/mate-gck/
%doc %{_datadir}/gtk-doc/html/mate-gcr-0/
%{_includedir}/mategcr/
%{_includedir}/mate-gck/
%{_includedir}/gck/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

