Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mockito
Version:        2.28.2
Release:        alt1_1jpp11
Summary:        Tasty mocking framework for unit tests in Java
License:        MIT
URL:            https://site.mockito.org/
BuildArch:      noarch

# Source tarball and the script to generate it
Source0:        %{name}-%{version}.tar.xz
Source1:        make-%{name}-sourcetarball.sh

# A custom build script to allow building with maven instead of gradle
Source2:        mockito-core.pom

# Mockito expects byte-buddy to have a shaded/bundled version of ASM, but
# we don't bundle in Fedora, so this patch makes mockito use ASM explicitly
Patch0:         use-unbundled-asm.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.opentest4j:opentest4j)
BuildRequires:  mvn(org.ow2.asm:asm)
Source44: import.info

%description
Mockito is a mocking framework that tastes really good. It lets you write
beautiful tests with clean & simple API. Mockito doesn't give you hangover
because the tests are very readable and they produce clean verification
errors.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0

# Use our custom build script
sed -e 's/@VERSION@/%{version}/' %{SOURCE2} > pom.xml

# OGGi metadata configuration
cat > osgi.bnd <<EOF
Automatic-Module-Name: org.mockito
Bundle-SymbolicName: org.mockito
Bundle-Name: Mockito Mock Library for Java.
Import-Package: junit.*;resolution:=optional,org.junit.*;resolution:=optional,org.hamcrest;resolution:=optional,org.mockito*;version="%{version}",*
Private-Package: org.mockito.*
-removeheaders: Bnd-LastModified,Include-Resource,Private-Package
EOF

# Compatibility alias
%mvn_alias org.%{name}:%{name}-core org.%{name}:%{name}-all

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc doc/design-docs/custom-argument-matching.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.28.2-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.23.9-alt1_6jpp8
- fc update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.23.9-alt1_4jpp8
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_17jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_13jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_10jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_4jpp8
- java 8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt1_9jpp7
- new version

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt5_0.1jpp6
- fixed build

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt4_0.1jpp6
- fixed build with new testng and xbean

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt3_0.1jpp6
- fixed build

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt2_0.1jpp6
- fixed build

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt1_0.1jpp6
- new version

