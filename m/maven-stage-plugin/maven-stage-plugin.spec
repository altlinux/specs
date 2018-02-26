BuildRequires: /proc
BuildRequires: jpackage-compat
%global project_version 1.0-alpha-2
Name:           maven-stage-plugin
Version:        1.0
Release:        alt1_0.3.alpha2jpp7
Summary:        Plugin to copy artifacts from one repository to another

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-stage-plugin/
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-stage-plugin-1.0-alpha-2/
# tar jcf maven-stage-plugin-1.0-alpha-2.tar.bz2 maven-stage-plugin-1.0-alpha-2/
Source0:        %{name}-%{project_version}.tar.bz2

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: jpackage-utils
Requires: ant
Requires: maven
Requires: jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils

Obsoletes: maven2-plugin-stage <= 0:2.0.8
Provides: maven2-plugin-stage = 1:%{version}-%{release}
Source44: import.info

%description
The Maven Stage Plugin copies artifacts from one repository to another. 
Its main use is for copying artifacts from a staging repository to 
the real repository.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{project_version}

%build
mvn-rpmbuild \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{project_version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins %{name} %{project_version} JPP %{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.alpha2jpp7
- new version

