Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:             jansi
Version:          2.4.0
Release:          alt1_7jpp11
Summary:          Generate and interpret ANSI escape sequences in Java
License:          ASL 2.0
URL:              http://fusesource.github.io/jansi/

# ./generate-tarball.sh
Source0:          %{name}-%{version}.tar.gz
# Remove bundled binaries which cannot be easily verified for licensing
Source1:          generate-tarball.sh

# Change the location of the native artifact to where Fedora wants it
Patch0:           %{name}-jni.patch

BuildRequires:    gcc
%if %{with bootstrap}
BuildRequires:    javapackages-bootstrap
%else
BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:    mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:    mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires:    mvn(org.junit.jupiter:junit-jupiter-engine)
%endif
Source44: import.info

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences.

%package javadoc
Group: Development/Java
BuildArch:        noarch
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jansi-jansi-%{version}
%patch0 -p1


# We don't need the Fuse JXR skin
%pom_xpath_remove "pom:build/pom:extensions"

# Plugins not needed for an RPM build
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

# We don't want GraalVM support in Fedora
%pom_remove_plugin :exec-maven-plugin
%pom_remove_dep :picocli-codegen

# Build for JDK 1.8 at a minimum
%pom_xpath_set "//pom:properties/pom:jdkTarget" 1.8

# Remove prebuilt shared objects
rm -fr src/main/resources/org/fusesource/jansi/internal

# Unbundle the JNI headers
rm src/main/native/inc_linux/*.h
ln -s %{java_home}/include/jni.h src/main/native/inc_linux
ln -s %{java_home}/include/linux/jni_md.h src/main/native/inc_linux

# Set the JNI path
sed -i 's,@LIBDIR@,%{_prefix}/lib,' \
    src/main/java/org/fusesource/jansi/internal/JansiLoader.java

%build

CC="${CC:-gcc}"
# Build the native artifact
CFLAGS="$CFLAGS -I. -I%{java_home}/include -I%{java_home}/include/linux -fPIC -fvisibility=hidden"
cd src/main/native
$CC $CFLAGS -c jansi.c
$CC $CFLAGS -c jansi_isatty.c
$CC $CFLAGS -c jansi_structs.c
$CC $CFLAGS -c jansi_ttyname.c
$CC $CFLAGS $LDFLAGS -shared -o libjansi.so *.o -lutil
cd -

# Build the Java artifacts
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dlibrary.jansi.path=$PWD/src/main/native

%install
# Install the native artifact
mkdir -p %{buildroot}%{_prefix}/lib/%{name}
cp -p src/main/native/libjansi.so %{buildroot}%{_prefix}/lib/%{name}

# Install the Java artifacts
%mvn_install

%files -f .mfiles
%doc --no-dereference license.txt
%doc readme.md changelog.md
%{_prefix}/lib/%{name}/

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt

%changelog
* Wed Mar 22 2023 Igor Vlasenko <viy@altlinux.org> 0:2.4.0-alt1_7jpp11
- update

* Sat Jul 02 2022 Igor Vlasenko <viy@altlinux.org> 0:2.4.0-alt1_3jpp11
- new version

* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 0:2.3.3-alt1_2jpp11
- new version

* Sun Jun 13 2021 Igor Vlasenko <viy@altlinux.org> 0:2.1.1-alt1_3jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.18-alt1_2jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.17.1-alt1_3jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.17-alt1_1jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.16-alt1_3jpp8
- java update

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.16-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_10jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_9jpp8
- unbootsrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_3jpp7
- new release

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new release

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_4jpp7
- added Requires: fusesource-pom

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- added jansi:jansi depmap for jpp packages

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp7
- fixed pom

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp7
- fc version

* Sat Feb 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp6
- new version

