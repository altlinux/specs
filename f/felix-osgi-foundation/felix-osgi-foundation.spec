BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global bundle org.osgi.foundation
%global felixdir %{_javadir}/felix
%global POM %{_mavenpomdir}/JPP.felix-%{bundle}.pom

Name:    felix-osgi-foundation
Version: 1.2.0
Release: alt3_10jpp7
Summary: Felix OSGi Foundation EE Bundle

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-provider-junit4
Source44: import.info


%description
OSGi Foundation Execution Environment (EE) Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%build
mvn-rpmbuild install javadoc:javadoc

%install
install -d -m 755 %{buildroot}%{felixdir}
install -d -m 755 %{buildroot}%{_mavenpomdir}

# jar
install -p -m 644 target/%{bundle}-%{version}.jar \
  %{buildroot}%{felixdir}/%{bundle}.jar

# pom
install -p -m 644 pom.xml %{buildroot}%{POM}
%add_maven_depmap JPP.felix-%{bundle}.pom felix/%{bundle}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE NOTICE
%{felixdir}
%{POM}
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_10jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_10jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4jpp6
- new version

