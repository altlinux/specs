BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-ant-plugin
Version:        2.3
Release:        alt1_8jpp7
Summary:        Maven Ant Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-ant-plugin
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-ant-plugin-2.3/
#tar jcf maven-ant-plugin-2.3.tar.bz2 maven-ant-plugin-2.3/
Source0:        %{name}-%{version}.tar.bz2
Patch0:        %{name}-pom.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: plexus-container-default
BuildRequires: maven-plugin-testing-harness
BuildRequires: junit

Requires:       maven
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       ant
Requires:       plexus-container-default
Requires:       junit

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

Obsoletes: maven2-plugin-ant <= 0:2.0.8
Provides: maven2-plugin-ant = 0:%{version}-%{release}
Source44: import.info

%description
Generates an Ant build file from a POM.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0 -p0

%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

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
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_8jpp7
- complete build

* Sat Mar 10 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

