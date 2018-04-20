Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1.6
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:          wildfly-build-tools
Version:       1.1.6
Release:       alt1_4jpp8
Summary:       Wildfly build and provisioning tools
License:       ASL 2.0
URL:           https://github.com/wildfly/wildfly-build-tools
Source0:       https://github.com/wildfly/wildfly-build-tools/archive/%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven:maven-aether-provider)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-settings-builder)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.eclipse.aether:aether-api)
BuildRequires: mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires: mvn(org.eclipse.aether:aether-impl)
BuildRequires: mvn(org.eclipse.aether:aether-spi)
BuildRequires: mvn(org.eclipse.aether:aether-transport-file)
BuildRequires: mvn(org.eclipse.aether:aether-transport-http)
BuildRequires: mvn(org.eclipse.aether:aether-util)
BuildRequires: mvn(org.jboss:jandex)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss:staxmapper)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-annotations)

BuildArch:     noarch
Source44: import.info

%description
Tools used for building and provisioning the Wildfly server.

%package -n wildfly-feature-pack-build-maven-plugin
Group: Development/Java
Summary:       WildFly Build Tools: Feature Pack Build Maven Plugin

%description -n wildfly-feature-pack-build-maven-plugin
This package contains WildFly Build Tools Feature Pack Build Maven Plugin.

%package -n wildfly-server-provisioning
Group: Development/Java
Summary:       WildFly Build Tools: Server Provisioning

%description -n wildfly-server-provisioning
This package contains WildFly Build Tools Server Provisioning.

%package -n wildfly-server-provisioning-maven-plugin
Group: Development/Java
Summary:       WildFly Build Tools: Server Provisioning Maven Plugin

%description -n wildfly-server-provisioning-maven-plugin
This package contains WildFly Build Tools Server Provisioning Maven Plugin.

%package -n wildfly-server-provisioning-standalone
Group: Development/Java
Summary:       WildFly Build Tools: Server Provisioning Standalone

%description -n wildfly-server-provisioning-standalone
This package contains WildFly Build Tools Server Provisioning Standalone.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Use not available org.wildfly.checkstyle:wildfly-checkstyle-config:jar:1.0.0.Final
%pom_remove_plugin -r :maven-checkstyle-plugin

%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_dep -r :wildfly-checkstyle-config

%pom_remove_dep -r org.sonatype.aether:

# disable maven-invoker-plugin
%pom_xpath_remove pom:profiles provisioning-maven-plugin

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-wildfly-build-tools-parent
%doc --no-dereference LICENSE.txt

%files -n wildfly-feature-pack-build-maven-plugin -f .mfiles-wildfly-feature-pack-build-maven-plugin

%files -n wildfly-server-provisioning -f .mfiles-wildfly-server-provisioning
%doc --no-dereference LICENSE.txt

%files -n wildfly-server-provisioning-maven-plugin -f .mfiles-wildfly-server-provisioning-maven-plugin
%files -n wildfly-server-provisioning-standalone -f .mfiles-wildfly-server-provisioning-standalone

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_4jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_3jpp8
- new version

