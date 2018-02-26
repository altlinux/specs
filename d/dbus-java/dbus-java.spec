BuildRequires: /usr/bin/xsltproc
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:       dbus-java
Version:    2.7
Release:    alt1_8jpp7
Summary:    Java implementation of the DBus protocol
Group:      Development/Java
License:    AFL or LGPLv2
URL:        http://freedesktop.org/wiki/Software/DBusBindings
#URL2:      http://dbus.freedesktop.org/doc/dbus-java/
Source0:    http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

# OSGi manifests
Source1:    %{name}-osgi-MANIFEST.MF

Patch1:     classpath_fix.patch
# fedora specific paths
Patch2:     parallel.patch
# java-7 compatibility patch
# https://bugs.freedesktop.org/show_bug.cgi?id=44791
Patch3:     utf-8-encoding.patch

BuildRequires:  jpackage-utils
BuildRequires:  texlive-latex-recommended
BuildRequires:  tex4ht
BuildRequires:  docbook-utils
BuildRequires:  gettext
BuildRequires:  libmatthew-java
BuildRequires:  docbook2X

Requires:   jpackage-utils
Requires:   libmatthew-java

BuildArch:      noarch
Source44: import.info

%description
D-Bus is a message bus system, a simple way for applications to
talk to one another. In addition to interprocess communication,
D-Bus helps coordinate process lifecycle; it makes it simple and
reliable to code a "single instance" application or daemon, and to
launch applications and daemons on demand when their services are
needed.

This is a complete independent implementation of the D-Bus protocol
in Java. It comprises a library to write programs in Java which
access D-Bus, a tool for generating stubs from D-Bus introspection
data and a simple daemon. Being written in Java it works on both
Windows and Linux (and other Unix-like systems).

When using a TCP transport it is entirely Java-based; when using
Unix-sockets it requires a small JNI library to use Unix-Sockets.


%package javadoc
Summary:    Javadocs for %{name}
Group:      Development/Java
Requires:   jpackage-utils
BuildArch: noarch


%description javadoc
Javadocs for %{name}


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i "s|!doctype|!DOCTYPE|g" *.sgml
sed -i 's|<!DOCTYPE refentry PUBLIC "-//OASIS//DTD DocBook V4.1//EN"|<!DOCTYPE refentry PUBLIC "-//OASIS//DTD DocBook V4.1//EN" "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd"|g' *.sgml

%build
# no configure file
make %{?_smp_mflags} \
    DOCBOOKTOMAN="db2x_docbook2man --to-stdout"\
    -j1 \
    JARPREFIX=%{_javadir}/%{name} \
    BINPREFIX=%{_bindir} \
    MANPREFIX=%{_mandir}/man1 \
    DOCPREFIX=%{_defaultdocdir}/%{name} \
    JAVADOCPREFIX=%{_javadocdir}/%{name} \
    JAVAUNIXLIBDIR=%{_libdir}/libmatthew-java \
    JAVAUNIXJARDIR=%{_libdir}/libmatthew-java

# Inject OSGi manifests
jar umf %{SOURCE1} libdbus-java-%{version}.jar

%check
make check \
    JARPREFIX=%{_javadir}/%{name} \
    BINPREFIX=%{_bindir} \
    MANPREFIX=%{_mandir}/man1 \
    DOCPREFIX=%{_defaultdocdir}/%{name} \
    JAVADOCPREFIX=%{_javadocdir}/%{name} \
    JAVAUNIXLIBDIR=%{_libdir}/libmatthew-java \
    JAVAUNIXJARDIR=%{_libdir}/libmatthew-java


%install
make install \
    DESTDIR=$RPM_BUILD_ROOT \
    JARPREFIX=%{_javadir}/%{name} \
    BINPREFIX=%{_bindir} \
    MANPREFIX=%{_mandir}/man1 \
    DOCPREFIX=%{_defaultdocdir}/%{name} \
    JAVADOCPREFIX=%{_javadocdir}/%{name} \
    JAVAUNIXLIBDIR=%{_libdir}/libmatthew-java \
    JAVAUNIXJARDIR=%{_libdir}/libmatthew-java

%files
%{_javadir}/%{name}
%{_bindir}/CreateInterface
%{_bindir}/DBusCall
%{_bindir}/DBusDaemon
%{_bindir}/DBusViewer
%{_bindir}/ListDBus
%doc %{_defaultdocdir}/%{name}
%doc %{_mandir}/man1/CreateInterface.1.gz
%doc %{_mandir}/man1/DBusCall.1.gz
%doc %{_mandir}/man1/DBusDaemon.1.gz
%doc %{_mandir}/man1/DBusViewer.1.gz
%doc %{_mandir}/man1/ListDBus.1.gz
%doc AUTHORS COPYING INSTALL README

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING


%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_8jpp7
- fc build

