BuildRequires: felix-parent
BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global project felix
%global bundle org.apache.felix.framework
%global groupId org.apache.felix
%global artifactId %{bundle}

Name:    %{project}-framework
Version: 2.0.5
Release: alt1_3jpp6
Summary: Apache Felix Framework

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz
Source1: %{name}.demap

# Remove <parent>
# Remove rat-maven-plugin
Patch0: %{bundle}-%{version}~pom.xml.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: maven2
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-invoker
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
# TODO check availability and use new names
#BuildRequires:    maven2-plugin-surefire
#BuildRequires:    maven2-plugin-bundle
# instead of
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-maven-plugin

Requires: felix-osgi-compendium
Requires: felix-osgi-core

Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
Apache Felix Framework Interfaces and Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%global POM %{_mavenpomdir}/JPP.%{project}-%{name}.pom

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1 -b .sav
# remove tests due to rat-maven-plugin is removed
%__rm -rf src/test/java/

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%__mkdir_p $MAVEN_REPO_LOCAL
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file="%{SOURCE1}" \
        install javadoc:javadoc

%install
%__rm -rf %{buildroot}

# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{project}
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/%{project}/%{bundle}-%{version}.jar

# versionless symlinks to jars
(cd %{buildroot}%{_javadir}/%{project} && for jar in *-%{version}*.jar; \
    do %__ln_s -f $jar `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP/%{project} %{bundle}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{POM}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%__rm -rf target/site/api*

%files
%doc LICENSE
%{_javadir}/%{project}/*
%{POM}
%config(noreplace) %{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_3jpp6
- new jpp release

