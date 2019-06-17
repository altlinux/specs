Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jinput
Version:        2.0.9
Release:        alt1_2jpp8
Summary:        Java Game Controller API

License:        BSD
URL:            https://github.com/jinput/jinput
Source0:        https://github.com/jinput/jinput/archive/%{version}/%{name}-%{version}.tar.gz
# Fedora-specific patch: will not be sent upstream.  Remove dependencies on
# Windows and OSX code, and fix build issues with the AWT plugin.
Patch0:         001_jinput_build.patch
# Fedora-specific patch: will not be sent upstream.  Do not strip the native
# library.
Patch1:         002_jinput_dontstripso.patch
# Fedora-specific patch: will not be sent upstream.  Load the shared library
# from the Fedora-mandated location.
Patch2:         003_jinput_usesystemload.patch
# Patch from https://java.net/jira/browse/JINPUT-51 to fix a resource leak
Patch4:         005_jinput_leak.patch

BuildRequires:  gcc
BuildRequires:  java-javadoc >= 1:1.6.0
BuildRequires:  jutils-javadoc
BuildRequires:  maven-local
BuildRequires:  mvn(net.java.jutils:jutils)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
Source44: import.info

%description
jinput is an implementation of an API for game controller discovery and
polled input.  It is part of a suite of open-source technologies
initiated by the Game Technology Group at Sun Microsystems with the
intention of making the development of high performance games in Java a
reality.  The API itself is pure Java and presents a platform-neutral,
completely portable model of controller discovery and polling.  It can
handle arbitrary controllers and returns both human and machine
understandable descriptions of the inputs available.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jutils-javadoc
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch4 -p0

# Use Fedora's CFLAGS and LDFLAGS
sed -i "s|-O2 -Wall|$RPM_OPT_FLAGS|;s|-shared|& $RPM_LD_FLAGS|" \
    plugins/linux/build.xml

# Remove unnecessary maven plugins
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin -r :maven-nativedependencies-plugin

# The examples have a jar (rather than pom) dependency on the main project
%pom_xpath_remove pom:project/pom:dependencies/pom:dependency/pom:type \
  examples/pom.xml

# The native plugin is included
%mvn_package net.java.jinput:linux-plugin::natives-linux:%{version}-SNAPSHOT

%build
# Get the latest definitions from <linux/input-event-codes.h>
gawk -f plugins/linux/src/main/native/getDefinitions \
  %{_includedir}/linux/input.h \
  %{_includedir}/linux/input-event-codes.h \
  > plugins/linux/src/main/java/net/java/games/input/NativeDefinitions.java

# Build
%mvn_build

%install
%mvn_install

# jni
install -Dp -m 755 plugins/linux/target/natives/libjinput*.so \
    %{buildroot}%{_libdir}/%{name}/libjinput.so
ln -s ../../..%{_jnidir}/%{name}/%{name}.jar %{buildroot}%{_libdir}/%{name}/

%files -f .mfiles
%doc README.md
%{_libdir}/%{name}/

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.9-alt1_2jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_12.20170607git.294629ajpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_11.20170607git.294629ajpp8
- new fc release

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_10.20170607git.294629ajpp8
- fc update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_7.20160519git.b813d55jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_6.20160519git.b813d55jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt2_5.20140526svnjpp8
- %%_jnidir set to /usr/lib/java

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1_5.20140526svnjpp8
- java8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_6.20130309svnjpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_2.20110801svnjpp7
- initial build

