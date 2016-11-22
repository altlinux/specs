Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# fedora __isa_bits tmp hack
%ifarch x86_64
%define __isa_bits 64
%else
%define __isa_bits 32
%endif
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hornetq
%define version 2.4.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global customnamedversion 2_4_1_Final

# Use this switch to rebuild without narayana
# This is useful to break the hornetq circular dependency
%define with_narayana 1

Name:             hornetq
Version:          2.4.1
Release:          alt1_7jpp8
Summary:          High performance messaging system
License:          ASL 2.0
URL:              http://www.jboss.org/hornetq
Source0:          https://github.com/hornetq/hornetq/archive/HornetQ_%{customnamedversion}.tar.gz

BuildRequires:    automake-common libtool-common autoconf-common
BuildRequires:    apiviz
BuildRequires:    aether
BuildRequires:    apache-commons-logging
BuildRequires:    javacc
BuildRequires:    jboss-connector-1.6-api
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-ejb3-ext-api
BuildRequires:    jboss-jaspi-1.0-api
BuildRequires:    jboss-jms-1.1-api
BuildRequires:    jboss-logging
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-transaction-spi
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-remoting
BuildRequires:    jboss-naming
BuildRequires:    jbossws-parent
BuildRequires:    jdepend
BuildRequires:    libaio-devel

%if 0%{?fedora} > 20
BuildRequires:    netty
%else
BuildRequires:    netty4
%endif

BuildRequires:    maven-local
BuildRequires:    maven-license-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    javacc-maven-plugin
BuildRequires:    java-service-wrapper
BuildRequires:    jgroups
BuildRequires:    jboss-integration
BuildRequires:    mvn(org.jboss.resteasy:resteasy-jaxrs)
BuildRequires:    mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.1_spec)

%if %{with_narayana}
BuildRequires:    narayana
%endif

BuildRequires:    xml-maven-plugin
BuildRequires:    saxon
BuildRequires:    qpid-proton-java
BuildRequires:    mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec)
BuildRequires:    mvn(org.jboss.spec.javax.jms:jboss-jms-api_2.0_spec)
BuildRequires:    nar-maven-plugin >= 3.0.0
Source44: import.info

%description
HornetQ is an open source project to build a multi-protocol, embeddable,
very high performance, clustered, asynchronous messaging system.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n hornetq-HornetQ_%{customnamedversion}

# Remove bundled .so files
find -name "*.so" -delete

%pom_remove_dep "org.jboss.jbossts.jts:jbossjts-jacorb" hornetq-jms-server/pom.xml
%pom_add_dep "org.jboss.narayana.jta:jta" hornetq-jms-server/pom.xml

%pom_disable_module hornetq-service-sar
%pom_disable_module hornetq-bootstrap
%pom_disable_module tests
%pom_disable_module examples
%pom_disable_module hornetq-rest

%pom_disable_module integration/hornetq-jboss-as-integration
%pom_disable_module integration/hornetq-spring-integration
%pom_disable_module integration/hornetq-twitter-integration
%pom_disable_module integration/hornetq-aerogear-integration

%if !%{with_narayana}
%pom_disable_module hornetq-jms-server
%pom_disable_module hornetq-ra
%pom_disable_module hornetq-tools
%endif

%pom_remove_plugin ":maven-checkstyle-plugin"

%pom_remove_dep "org.jboss.microcontainer:jboss-kernel"

# Use netty version 4, always
sed -i 's|>4.0.13.Final<|>4<|' pom.xml

# Replace old jca
%pom_remove_dep "org.jboss.javaee:jboss-jca-api" hornetq-ra/pom.xml
%pom_add_dep "org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec" hornetq-ra/pom.xml

# Make xslt 2.0 avaialble!
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'xml-maven-plugin']/pom:configuration" "<transformerFactory>net.sf.saxon.TransformerFactoryImpl</transformerFactory>" hornetq-core-client/pom.xml

sed -i "s|>com.mycila<|>com.mycila.maven-license-plugin<|g" pom.xml
sed -i "s|>license-maven-plugin<|>maven-license-plugin<|g" pom.xml

%build
# Workaround for building native bits
# Currently the build script uses the .so in the hornetq-nativebin/ directory
# but we need to rebuild them. The issue is that the mvn build process does not
# use the new .so files we've built. Here is a simple workaround.

%if %{with_narayana}
pushd hornetq-native
# Let's build the .so files
%mvn_build -i -f -- -Pnative-build
# Copy them to hornetq-native/bin/ dir
find -name "*.so" -exec cp {} bin/libHornetQAIO.so \;
find -name "*.so" -exec cp {} bin/libHornetQAIO%{__isa_bits}.so \;
popd
%endif

# This will rebuild one more time the hornet-native stuff,
# but this time will include the correct native libraries

# Tests are skipped because required modules are disabled
%mvn_build -f -- -Pmaven-release

%install
%mvn_install

# Install native stuff
%if %{with_narayana}
install -d -m 755 %{buildroot}/%{_libdir}
cp -L hornetq-native/bin/libHornetQAIO.so %{buildroot}/%{_libdir}/libHornetQAIO.so
%endif

%files -f .mfiles
%dir %{_javadir}/%{name}
%if %{with_narayana}
%{_libdir}/libHornetQAIO.so
%endif
%doc distribution/hornetq/src/main/resources/licenses/LICENSE.txt
%doc NOTICE
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc distribution/hornetq/src/main/resources/licenses/LICENSE.txt
%doc NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_7jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_6jpp8
- build with narayana

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_0jpp8
- new version. build w/o narayana

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt1_5jpp7
- new version

