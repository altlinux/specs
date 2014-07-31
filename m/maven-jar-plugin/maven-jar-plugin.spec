# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-jar-plugin
Version:        2.4
Release:        alt2_5jpp7
Summary:        Maven JAR Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-jar-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Some classes from maven-artifact come in maven-core, added a dep in pom.xml
Patch0:         %{name}-maven-core-dep.patch

BuildArch: noarch

BuildRequires: javapackages-tools >= 0.7.0
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-archiver
BuildRequires: plexus-archiver
BuildRequires: apache-commons-lang
BuildRequires: plexus-utils
BuildRequires: junit
Requires: maven
Requires: maven-archiver
Requires: plexus-archiver
Requires: maven-archiver
Requires: apache-commons-lang
Requires: plexus-utils
Requires: maven-plugin-testing-harness
Requires: junit

Provides:       maven2-plugin-jar = %{version}-%{release}
Obsoletes:      maven2-plugin-jar <= 0:2.0.8
Source44: import.info

%description
Builds a Java Archive (JAR) file from the compiled
project classes and resources.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

#let plexus-container-default be retrieved as a dependency
sed -i -e "s|plexus-container-default|plexus-container|g" pom.xml

%build
# Test class MockArtifact doesn't override method getMetadata
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.skip

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_5jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_2jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_2jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

