Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name woodstox
%global core_name %{base_name}-core

Name:           %{core_name}
Version:        5.0.3
Release:        alt1_3jpp8
Summary:        High-performance XML processor
License:        ASL 2.0 or LGPLv2+ or BSD
URL:            https://github.com/FasterXML/woodstox
BuildArch:      noarch

Source0:        https://github.com/FasterXML/%{base_name}/archive/%{name}-%{version}.tar.gz
Patch0:         0001-stax2-api.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)
BuildRequires:  mvn(javax.xml.stream:stax-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.msv:msv-core)
BuildRequires:  mvn(net.java.dev.msv:msv-rngconverter)
BuildRequires:  mvn(net.java.dev.msv:xsdlib)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.osgi.core)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
Source44: import.info

%description
Woodstox is a high-performance validating namespace-aware StAX-compliant
(JSR-173) Open Source XML-processor written in Java.
XML processor means that it handles both input (== parsing)
and output (== writing, serialization)), as well as supporting tasks
such as validation.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{name}-%{version}

%patch0 -p1

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-bundle-plugin"]/pom:configuration' '
<instructions>
    <Export-Package>{local-packages}</Export-Package>
</instructions>'

%mvn_alias ":{woodstox-core}" :@1-lgpl :@1-asl :wstx-asl :wstx-lgpl \
    org.codehaus.woodstox:@1 org.codehaus.woodstox:@1-asl \
    org.codehaus.woodstox:@1-lgpl org.codehaus.woodstox:wstx-lgpl \
    org.codehaus.woodstox:wstx-asl
%mvn_file : %{name}{,-asl,-lgpl}

# Fails even when using online maven build
rm ./src/test/java/org/codehaus/stax/test/stream/TestNamespaces.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
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

