BuildRequires: maven-surefire-provider-junit4
BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global bundle org.osgi.foundation
%global felixdir %{_javadir}/felix

Name:    felix-osgi-foundation
Version: 1.2.0
Release: alt2_4jpp6
Summary: Felix OSGi Foundation EE Bundle

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: felix-parent
BuildRequires: jpackage-utils
BuildRequires: maven2
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-compiler
BuildRequires: maven-surefire-plugin
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven-doxia-sitetools


Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
OSGi Foundation Execution Environment (EE) Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%global publicPOM %{_mavenpomdir}/JPP.felix-%{bundle}.pom

%prep
%setup -q -n %{bundle}-%{version}

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%__mkdir_p $MAVEN_REPO_LOCAL

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5  \
  -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
  install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{felixdir}
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{felixdir}/%{bundle}.jar

%add_to_maven_depmap org.apache.felix %{bundle} %{version} JPP/felix %{bundle}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{publicPOM}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
# workaround for rpm bug, can be removed in F-17
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE
%{felixdir}
%{publicPOM}
%config(noreplace) %{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4jpp6
- new version

