Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             apache-scout
Version:          1.2.6
Release:          alt2_8jpp7
Summary:          JSR 93 (JAXR) implementation
License:          ASL 2.0
URL:              http://juddi.apache.org/scout
# svn export http://svn.apache.org/repos/asf/juddi/scout/tags/scout-1.2.6/ apache-scout
# tar cafJ apache-scout-1.2.6.tar.xz apache-scout
Source0:          %{name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local

BuildRequires:    axis
BuildRequires:    mvn(axis:axis)
BuildRequires:    mvn(org.apache.geronimo.specs:geronimo-jaxrpc_1.1_spec)
BuildRequires:    mvn(org.apache.juddi:juddi-client)
BuildRequires:    mvn(org.jboss.spec.javax.xml.bind:jboss-jaxb-api_2.2_spec)
BuildRequires:    mvn(org.jboss.spec.javax.xml.registry:jboss-jaxr-api_1.0_spec)
BuildRequires:    geronimo-parent-poms
BuildRequires:    mvn(org.aspectj:aspectjweaver)
BuildRequires:    wsdl4j


%if 0
# test deps
BuildRequires:    mvn(axis:axis-jaxrpc)
BuildRequires:    mvn(axis:axis-saaj)
BuildRequires:    mvn(commons-discovery:commons-discovery)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(log4j:log4j)
BuildRequires:    mvn(org.apache.derby:derby)
BuildRequires:    mvn(org.apache.juddi:juddi:2.0.1)
BuildRequires:    mvn(org.aspectj:aspectjrt)
BuildRequires:    mvn(org.aspectj:aspectjweaver)
%endif
Source44: import.info

%description
Apache Scout is an implementation of the JSR 93 Java API For XML Registries
(JAXR). It provides an implementation to access UDDI registries (particularly
Apache jUDDI) in a standard way.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%pom_remove_dep :geronimo-activation_1.1_spec
%pom_remove_dep :geronimo-jaxb_2.1_spec
%pom_add_dep org.jboss.spec.javax.xml.bind:jboss-jaxb-api_2.2_spec:1.0.4.Final
%pom_remove_dep :geronimo-jaxr_1.0_spec
%pom_add_dep org.jboss.spec.javax.xml.registry:jboss-jaxr-api_1.0_spec:1.0.2.Final
%pom_remove_dep :geronimo-stax-api_1.0_spec
%pom_add_dep org.codehaus.woodstox:stax2-api:3.1.1

# fedora aspectjweaver package provides aspectjrt
%pom_remove_dep org.aspectj:aspectjrt
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId = 'aspectjweaver' ]/pom:groupId" org.aspectj

sed -i 's/\r//' README

# build fix for apache juddi 3.1.5
sed -i "s|UDDIClerkManager|UDDIClient|" \
 src/main/java/org/apache/ws/scout/registry/ConnectionImpl.java

%build

%mvn_file :scout %{name}
# Skipped because of many test resources not packaged
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1_3jpp7
- new version

