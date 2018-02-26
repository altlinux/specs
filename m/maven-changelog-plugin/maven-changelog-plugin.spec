BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-changelog-plugin
Version:        2.2
Release:        alt1_9jpp7
Summary:        Produce SCM changelog reports

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-changelog-plugin/
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-changelog-plugin-2.2/
#tar jcf maven-changelog-plugin-2.2.tar.bz2 maven-changelog-plugin-2.2/
Source0:        %{name}-%{version}.tar.bz2
Patch0:		pom.patch
Patch1:		ChangeLog.java.patch

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
BuildRequires: maven-site-plugin
BuildRequires: maven-shared
BuildRequires: maven-doxia
BuildRequires: maven-scm
BuildRequires: plexus-utils
BuildRequires: junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: plexus-container-default
BuildRequires: netbeans-cvsclient

Requires:       maven
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       plexus-container-default

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

Obsoletes: maven2-plugin-changelog <= 0:2.0.8
Provides: maven2-plugin-changelog = 1:%{version}-%{release}
Source44: import.info

%description
The Maven Changelog Plugin generates reports regarding the recent changes 
in your Software Configuration Management or SCM. These reports include 
the changelog report, developer activity report and the file activity report.

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
%patch1 -p2

%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins %{name} %{version} JPP %{name}

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
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_9jpp7
- new version

