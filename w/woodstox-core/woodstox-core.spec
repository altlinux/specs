Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name woodstox
%global core_name %{base_name}-core
%global stax2_ver  3.1.1

Name:           %{core_name}
Version:        4.2.0
Release:        alt1_2jpp7
Summary:        High-performance XML processor
License:        ASL 2.0 or LGPLv2+ or BSD
URL:            http://%{base_name}.codehaus.org/
BuildArch:      noarch

Source0:        http://%{base_name}.codehaus.org/%{version}/%{core_name}-src-%{version}.tar.gz
Patch0:         %{name}-stax2-api.patch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.xml.stream:stax-api)
BuildRequires:  mvn(net.java.dev.msv:msv-core)
BuildRequires:  mvn(net.java.dev.msv:xsdlib)
BuildRequires:  mvn(org.apache.felix:org.osgi.core)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
# Transitive devel dependencies needed because some packages don't
# install effective POMs:
BuildRequires:  mvn(net.java:jvnet-parent)
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
%setup -q -n %{base_name}-%{version}
%patch0

# Create POM from template
sed s/@VERSION@/%{version}/\;s/@REQ_STAX2_VERSION@/%{stax2_ver}/ \
    src/maven/%{name}-asl.pom >pom.xml

# Remove bundled libraries.
rm -rf lib
rm -rf src/maven
rm -rf src/resources
rm -rf src/samples
rm -rf src/java/org
rm -rf src/test/org
rm -rf src/test/stax2

# Bundled libraries were removed, so dependencies on them need to be
# added.
%pom_add_dep net.java.dev.msv:msv-core
%pom_add_dep org.apache.felix:org.osgi.core
%pom_add_dep net.java.dev.msv:xsdlib

# Upstream uses non-standard directory structure.
%pom_xpath_inject pom:project "
    <build>
      <sourceDirectory>src/java</sourceDirectory>
      <testSourceDirectory>src/test</testSourceDirectory>
    </build>"

%mvn_alias ":{woodstox-core}-asl" @1-lgpl
%mvn_file : %{name}{,-asl,-lgpl}

%build
# stax2 missing -> cannot compile tests -> tests skipped
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc release-notes

%files javadoc -f .mfiles-javadoc
%doc release-notes/asl release-notes/lgpl release-notes/bsd

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp7
- new version

