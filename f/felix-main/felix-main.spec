BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global project felix
%global bundle org.apache.felix.main
%global groupId org.apache.felix
%global artifactId %{bundle}

Name:    %{project}-main
Version: 2.0.5
Release: alt3_6jpp6
Summary: Apache Felix Main

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

# TODO check availability and use original artifacts:
# - org.apache.felix.shell https://bugzilla.redhat.com/show_bug.cgi?id=615869
Patch0: %{bundle}-%{version}~pom.xml.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: felix-parent
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: felix-framework
BuildRequires: maven2
BuildRequires:    maven2-plugin-antrun
BuildRequires:    maven2-plugin-compiler
BuildRequires:    maven2-plugin-dependency
BuildRequires:    maven2-plugin-install
BuildRequires:    maven2-plugin-invoker
BuildRequires:    maven2-plugin-jar
BuildRequires:    maven2-plugin-javadoc
BuildRequires:    maven2-plugin-release
BuildRequires:    maven2-plugin-resources
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit4
# TODO check availability and use new names
#BuildRequires:    maven2-plugin-bundle
# instead of
BuildRequires:    maven-plugin-bundle

Requires: felix-osgi-compendium
Requires: felix-osgi-core
Requires: felix-framework

Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info
Obsoletes: felix < 2

%description
Apache Felix Main Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%global POM %{_mavenpomdir}/JPP.%{project}-%{bundle}.pom

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1 -b .sav

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%__mkdir_p $MAVEN_REPO_LOCAL
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{project}
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/%{project}/%{bundle}.jar

%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP/%{project} %{bundle}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{POM}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
# workaround for rpm bug, can be removed in F-17
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_javadir}/%{project}/*
%{POM}
%config(noreplace) %{_mavendepmapfragdir}/%{name}
%doc LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt3_6jpp6
- fixed build with maven3

* Sun Jan 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt2_6jpp6
- obsolete felix1

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_6jpp6
- new jpp release

