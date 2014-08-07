BuildRequires: maven-plugin-plugin
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-plugin-exec
Version:        1.2.1
Release:        alt4_3jpp7
Summary:        Exec Maven Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://mojo.codehaus.org/exec-maven-plugin
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/1.2.1/exec-maven-plugin-1.2.1-source-release.zip
Patch0:         add_compat.patch
BuildArch: noarch

BuildRequires: maven-local
BuildRequires: plexus-utils
BuildRequires: plexus-container-default
BuildRequires: maven-shared-plugin-testing-harness
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-cobertura
BuildRequires: mojo-signatures
BuildRequires: maven-invoker-plugin
BuildRequires: apache-commons-exec
Requires: maven
Requires: plexus-utils
Requires: plexus-container-default
Requires: maven-shared-plugin-testing-harness
Requires: apache-commons-exec
Source44: import.info

%description
A plugin to allow execution of system and Java programs

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n exec-maven-plugin-%{version}
%patch0

sed -i "s|java14|java15|g" pom.xml

#there is nothing under MIT license
rm -f LICENSE.txt

%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        package javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 target/exec-maven-plugin-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_3jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_3jpp7
- new version

