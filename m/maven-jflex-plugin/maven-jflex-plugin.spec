BuildRequires: maven-plugin-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-jflex-plugin
Version:        1.4.3
Release:        alt3_8jpp7
Summary:        Maven JFlex Plugin

Group:          Development/Java
License:        GPLv3+
URL:            http://jflex.sourceforge.net/maven-jflex-plugin/
# Created by
# svn export http://jflex.svn.sourceforge.net/svnroot/jflex/tags/release_1_4_3/maven-jflex-plugin maven-jflex-plugin-1.4.3
# tar cjf maven-jflex-plugin-1.4.3.tar.bz2 maven-jflex-plugin-1.4.3/
Source0:        maven-jflex-plugin-1.4.3.tar.bz2
# http://sf.net/tracker/?func=detail&aid=3475986&group_id=14929&atid=314929
Patch0:         maven-jflex-plugin-1.4.3-srcencoding.patch

BuildArch: noarch

BuildRequires: jflex
BuildRequires: apache-commons-io
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-testing-harness
Requires: jflex
Requires: apache-commons-io
Requires: maven
Source44: import.info

%description
This is a Maven 2 plugin to generate a parser in Java code from
a Lexer definition, using Jflex.de.


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
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap de.jflex %{name} %{version} JPP %{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/%{name}*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt3_8jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt2_8jpp7
- fixed build

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_8jpp7
- fc release

