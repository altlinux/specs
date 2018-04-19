Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /usr/bin/xsltproc
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# the package is arch-dependent because scripts contain arch dependent paths
# the debuginfo package will be empty if produced
%global debug_package %{nil}

Name:       dbus-java
Version:    2.7
Release:    alt2_27jpp8
Summary:    Java implementation of the DBus protocol
License:    AFL or LGPLv2
URL:        http://freedesktop.org/wiki/Software/DBusBindings
Source0:    http://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz

# OSGi manifests
Source1:    %{name}-osgi-MANIFEST.MF

Patch1:     classpath_fix.patch
# fedora specific paths
Patch2:     parallel.patch
# java-7 compatibility patch
# https://bugs.freedesktop.org/show_bug.cgi?id=44791
Patch3:     utf-8-encoding.patch
Patch4:     version-less-jars.patch

BuildRequires:  javapackages-local
BuildRequires:  texlive-collection-basic
BuildRequires:  texlive-collection-basic
BuildRequires:  texlive-base
BuildRequires:  texlive-collection-basic
BuildRequires:  texlive-collection-fontsextra
BuildRequires:  texlive texlive-collection-basic
BuildRequires:  texlive texlive-collection-basic
BuildRequires:  texlive texlive-collection-basic
BuildRequires:  texlive texlive-collection-basic texlive-dist
BuildRequires:  texlive-dist
BuildRequires:  texlive texlive-collection-basic texlive-dist
BuildRequires:  texlive texlive-collection-basic
BuildRequires:  docbook-utils
BuildRequires:  gettext gettext-tools
BuildRequires:  libmatthew-java
BuildRequires:  docbook2X
BuildRequires:  tex(fullpage.sty)

Requires:   java >= 1.6.0
Requires:   javapackages-tools
Requires:   libmatthew-java
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
Group: Development/Other
Summary:    Javadocs for %{name}
BuildArch: noarch


%description javadoc
Javadocs for %{name}


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

sed -i "s|!doctype|!DOCTYPE|g" *.sgml
sed -i 's|<!DOCTYPE refentry PUBLIC "-//OASIS//DTD DocBook V4.1//EN"|<!DOCTYPE refentry PUBLIC "-//OASIS//DTD DocBook V4.1//EN" "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd"|g' *.sgml

%build

# no configure file
%make_build \
    DOCBOOKTOMAN="db2x_docbook2man --to-stdout"\
    -j1 \
    JARPREFIX=%{_javadir}/%{name} \
    BINPREFIX=%{_bindir} \
    MANPREFIX=%{_mandir}/man1 \
    DOCPREFIX=%{_defaultdocdir}/%{name} \
    JAVADOCPREFIX=%{_javadocdir}/%{name} \
    JAVAUNIXLIBDIR=%{_libdir}/libmatthew-java \
    JAVAUNIXJARDIR=%{_jnidir} \
    JAVADOC="javadoc -Xdoclint:none"

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
    JAVAUNIXJARDIR=%{_jnidir} \
    JAVADOC="javadoc -Xdoclint:none"


%install
make install \
    DESTDIR=$RPM_BUILD_ROOT \
    JARPREFIX=%{_javadir}/%{name} \
    BINPREFIX=%{_bindir} \
    MANPREFIX=%{_mandir}/man1 \
    DOCPREFIX=%{_defaultdocdir}/%{name} \
    JAVADOCPREFIX=%{_javadocdir}/%{name} \
    JAVAUNIXLIBDIR=%{_libdir}/libmatthew-java \
    JAVAUNIXJARDIR=%{_jnidir} \
    JAVADOC="javadoc -Xdoclint:none"

%files
%{_javadir}/%{name}
%{_bindir}/CreateInterface
%{_bindir}/DBusCall
%{_bindir}/DBusDaemon
%{_bindir}/DBusViewer
%{_bindir}/ListDBus
%doc %{_defaultdocdir}/%{name}
%doc %{_mandir}/man1/CreateInterface.1*
%doc %{_mandir}/man1/DBusCall.1*
%doc %{_mandir}/man1/DBusDaemon.1*
%doc %{_mandir}/man1/DBusViewer.1*
%doc %{_mandir}/man1/ListDBus.1*
%doc AUTHORS INSTALL README
%doc --no-dereference COPYING

%files javadoc
%{_javadocdir}/%{name}
%doc --no-dereference COPYING


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_27jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_26jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_23jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_22jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_20jpp8
- %%_jnidir set to /usr/lib/java

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_20jpp8
- java8 mass update

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_12jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_9jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_8jpp7
- fc build

