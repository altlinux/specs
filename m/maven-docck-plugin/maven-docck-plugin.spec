BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-docck-plugin
Version:        1.0
Release:        alt1_7jpp7
Summary:        Maven Documentation Checker Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-docck-plugin/
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-docck-plugin-1.0/
#tar jcf maven-docck-plugin-1.0.tar.bz2 maven-docck-plugin-1.0/
Source0:        %{name}-%{version}.tar.bz2

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
BuildRequires: maven-shared
BuildRequires: jakarta-commons-httpclient
BuildRequires: maven-plugin-tools
BuildRequires: maven-plugin-descriptor
BuildRequires: plexus-utils

Requires:       maven
Requires:       jpackage-utils
Requires:       apache-commons-logging
Requires:       maven-plugin-tools

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

Obsoletes: maven2-plugin-docck <= 0:2.0.8
Provides: maven2-plugin-docck = 1:%{version}-%{release}
Source44: import.info

%description
Checks for violations of the Plugin Documentation Standard.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins %{name} %{version} JPP %{name}

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

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
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp7
- fc version

