# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           animal-sniffer
Version:        1.8
Release:        alt1_1jpp7
Summary:        Tools to assist verifying backward compatibility of Java classes

Group:          Development/Java
License:        MIT
URL:            http://mojo.codehaus.org/animal-sniffer/

Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer-parent/%{version}/animal-sniffer-parent-%{version}-source-release.zip
Source1:        %{name}.sh

# this should be upstreamable
Patch2:         0003-Remove-catch-for-unthrown-PlexusConfigurationExcepti.patch

BuildArch:      noarch

BuildRequires:  maven
BuildRequires:  maven-install-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-plugin-cobertura
BuildRequires:  maven-plugin-build-helper
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  plexus-containers-component-javadoc
BuildRequires:  mojo-parent
BuildRequires:  objectweb-asm4

Requires:       maven
Requires:       objectweb-asm4
Requires:       ant
Requires:       mojo-signatures
Source44: import.info


%description
Tools to assist verifying that classes compiled with a newer JDK/API
are compatible with an older JDK/API

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-parent-%{version}
%patch2 -p1
%pom_add_dep org.apache.maven:maven-compat animal-sniffer-enforcer-rule
%pom_add_dep org.apache.maven:maven-compat animal-sniffer-maven-plugin


%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

%add_to_maven_depmap org.codehaus.mojo %{name}-parent %{version} JPP/%{name} parent
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-parent.pom

install -pm 644 %{name}/target/%{name}-*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
%add_to_maven_depmap org.codehaus.mojo %{name} %{version} JPP/%{name} %{name}
install -pm 644 %{name}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom

install -pm 644 %{name}-annotations/target/%{name}-*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/annotations.jar
%add_to_maven_depmap org.codehaus.mojo %{name}-annotations %{version} JPP/%{name} annotations
install -pm 644 %{name}-annotations/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-annotations.pom

install -pm 644 %{name}-ant-tasks/target/original-%{name}-ant-tasks-*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ant-tasks-.jar
%add_to_maven_depmap org.codehaus.mojo %{name}-ant-tasks %{version} JPP/%{name} ant-tasks
install -pm 644 %{name}-ant-tasks/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-ant-tasks.pom

install -pm 644 %{name}-enforcer-rule/target/%{name}-enforcer-rule*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/enforcer-rule.jar
%add_to_maven_depmap org.codehaus.mojo %{name}-enforcer-rule %{version} JPP/%{name} enforcer-rule
install -pm 644 %{name}-enforcer-rule/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-enforcer-rule.pom

install -pm 644 %{name}-maven-plugin/target/%{name}-maven-plugin*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-plugin.jar
%add_to_maven_depmap org.codehaus.mojo %{name}-maven-plugin %{version} JPP/%{name} maven-plugin
install -pm 644 %{name}-maven-plugin/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-maven-plugin.pom

install -pm 644 java-boot-classpath-detector/target/java-boot-classpath-detector*.jar $RPM_BUILD_ROOT%{_javadir}/java-boot-classpath-detector.jar
%add_to_maven_depmap org.codehaus.mojo java-boot-classpath-detector %{version} JPP java-boot-classpath-detector
install -pm 644 java-boot-classpath-detector/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-java-boot-classpath-detector.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_bindir}/%{name}
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_1jpp7
- non-bootstrap build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

