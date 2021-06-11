Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name woodstox

Name:           woodstox-core
Summary:        High-performance XML processor
Version:        6.2.3
Release:        alt1_2jpp11
License:        ASL 2.0 or LGPLv2+ or BSD

URL:            https://github.com/FasterXML/woodstox
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# Port to latest OSGi APIs
Patch0:         0001-Allow-building-against-OSGi-APIs-newer-than-R4.patch
# Drop requirements on defunct optional dependencies: msv and relaxng
Patch1:         0002-Patch-out-optional-support-for-msv-and-relax-schema-.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.osgi:osgi.core)
Source44: import.info

%description
Woodstox is a high-performance validating namespace-aware StAX-compliant
(JSR-173) Open Source XML-processor written in Java.
XML processor means that it handles both input (== parsing)
and output (== writing, serialization)), as well as supporting tasks
such as validation.


%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{base_name}-%{name}-%{version}
%patch0 -p1
%patch1 -p1


%pom_remove_dep relaxngDatatype:relaxngDatatype
%pom_remove_dep net.java.dev.msv:
rm -rf src/main/java/com/ctc/wstx/msv

# Remove tests for msv and relaxng functionality
rm -rf src/test/java/wstxtest/msv src/test/java/wstxtest/vstream/TestRelaxNG.java src/test/java/stax2/vwstream/W3CSchemaWrite*Test.java \
  src/test/java/failing/{TestRelaxNG,TestW3CSchemaTypes,TestW3CSchemaComplexTypes,TestW3CDefaultValues}.java

# Unnecessary for RPM builds
%pom_remove_plugin :nexus-staging-maven-plugin

# we don't care about Java 9 modules (yet)
%pom_remove_plugin :moditect-maven-plugin

# replace felix-osgi-core with osgi-core
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core

%mvn_alias ":{woodstox-core}" :@1-lgpl :@1-asl :wstx-asl :wstx-lgpl \
    org.codehaus.woodstox:@1 org.codehaus.woodstox:@1-asl \
    org.codehaus.woodstox:@1-lgpl org.codehaus.woodstox:wstx-lgpl \
    org.codehaus.woodstox:wstx-asl

%mvn_file : %{name}{,-asl,-lgpl}


%build
%mvn_build --xmvn-javadoc -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 6.2.3-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 6.2.1-alt1_5jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 6.0.2-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_6jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.2-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp7
- new version

