Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cssparser
Version:        0.9.7
Release:        alt1_1jpp7
Summary:        CSS Parser

Group:          Development/Java
License:        LGPLv2
URL:            http://cssparser.sourceforge.net/
# sh ./fetch-cssparser.sh
Source0:        cssparser-%{version}.tar.xz
Source1:        fetch-cssparser.sh

BuildArch: noarch

BuildRequires: sac >= 1.3-6
BuildRequires: junit
BuildRequires: javacc-maven-plugin >= 2.6-3
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-shared-reporting-impl
Requires: sac
Source44: import.info

%description
A CSS parser which implements SAC (the Simple API for CSS).

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
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt doc/license.html doc/readme.html

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.7-alt1_1jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.6-alt1_3jpp7
- new version

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt3_1jpp5
- fixed build with javacc 5

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_1jpp5
- fixed build with javacc 5

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_1jpp5
- fixed build with new maven 2.0.8

* Mon Feb 09 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_1jpp5
- new version

