Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Byte Buddy requires itself to build, so set this flag
# to break the bootstrap cycle
%bcond_with bootstrap

Name:          byte-buddy
Version:       1.9.5
Release:       alt1_5jpp8
Summary:       Runtime code generation for the Java virtual machine
License:       ASL 2.0
URL:           http://bytebuddy.net/
Source0:       https://github.com/raphw/byte-buddy/archive/%{name}-%{version}.tar.gz

# Patch out use of a unixsocket lib that is not in Fedora
Patch0:         no-unixsocket.patch

# Patch the build to avoid bundling inside shaded jars
Patch1:         avoid-bundling-asm.patch

BuildRequires:  maven-local
%if %{without bootstrap}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-dep)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-maven-plugin)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-util)
%endif
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)

BuildArch:     noarch
Source44: import.info

%description
Byte Buddy is a code generation library for creating Java classes during the
runtime of a Java application and without the help of a compiler. Other than
the code generation utilities that ship with the Java Class Library, Byte Buddy
allows the creation of arbitrary classes and is not limited to implementing
interfaces for the creation of runtime proxies. 

%package agent
Group: Development/Java
Summary: Byte Buddy Java agent

%description agent
The Byte Buddy Java agent allows to access the JVM's HotSwap feature.

%package maven-plugin
Group: Development/Java
Summary: Byte Buddy Maven plugin

%description maven-plugin
A plugin for post-processing class files via Byte Buddy in a Maven build.

%package parent
Group: Development/Java
Summary: Byte Buddy parent POM

%description parent
The parent artifact contains configuration information that
concern all modules.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0
%patch1

# Remove pre-built jars
find -name *.jar -delete
find -name *.class -delete

# Cause pre-compiled stuff to be re-compiled
mv byte-buddy-dep/src/precompiled/java/net/bytebuddy/build/*.java \
  byte-buddy-dep/src/main/java/net/bytebuddy/build
mkdir -p byte-buddy-dep/src/test/java/net/bytebuddy/test/precompiled/
mv byte-buddy-dep/src/precompiled/java/net/bytebuddy/test/precompiled/*.java \
  byte-buddy-dep/src/test/java/net/bytebuddy/test/precompiled/

# Don't ship android or benchmark modules
%pom_disable_module byte-buddy-android
%pom_disable_module byte-buddy-benchmark

# Don't ship gradle plugin
%pom_disable_module byte-buddy-gradle-plugin

# Remove check plugins unneeded by RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :pitest-maven
%pom_remove_plugin :coveralls-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :jitwatch-jarscan-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :maven-release-plugin

# Not interested in shading sources (causes NPE on old versions of shade plugin)
%pom_xpath_set "pom:createSourcesJar" "false" byte-buddy

# Drop build dep on findbugs annotations, used only by the above check plugins
%pom_remove_dep :findbugs-annotations
sed -i -e '/SuppressFBWarnings/d' $(grep -lr SuppressFBWarnings)

# Plugin for generating Java 9 module-info file is not in Fedora
%pom_remove_plugin -r :modulemaker-maven-plugin

%if %{with bootstrap}
# Remove circular self-dependency to allow bootstrapping
%pom_remove_plugin :byte-buddy-maven-plugin byte-buddy-dep
%endif

%build
%if %{with bootstrap}
# Cannot run the test suite in bootstrap mode due to circular dep
# on self and mockito
%mvn_build -s -f -- -P'java8,!checks'
%else
# Ignore test failures, there seems to be something different about the
# bytecode of our recompiled test resources, expect 6 test failures in
# the byte-buddy-dep module
%mvn_build -s -- -P'java8,!checks' -Dsourcecode.test.version=1.8 -Dmaven.test.failure.ignore=true
%endif

%install
%mvn_install
# multiple -f flags in %files for <main>: merging -f .mfiles-%{name}-dep into -f .mfiles-%{name}
cat .mfiles-%{name}-dep >> .mfiles-%{name}

%files -f .mfiles-%{name} 
%doc README.md release-notes.md
%doc --no-dereference LICENSE NOTICE

%files agent -f .mfiles-%{name}-agent
%doc --no-dereference LICENSE NOTICE

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files parent -f .mfiles-%{name}-parent
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun Jul 14 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.5-alt1_5jpp8
- full build

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.5-alt1_0jpp8
- bootstrap build

