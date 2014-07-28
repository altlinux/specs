# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Summary:        Enterprise Job Scheduler for Java
Name:           quartz
Version:        2.1.2
Release:        alt2_7jpp7
Epoch:          0
License:        ASL 2.0
URL:            http://www.quartz-scheduler.org/
Group:          Development/Java
# svn export http://svn.terracotta.org/svn/quartz/tags/quartz-2.1.2
# tar caf quartz-2.1.2.tar.xz quartz-2.1.2
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-%{version}-dep-fixes.patch
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  geronimo-parent-poms
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-pmd-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  rmic-maven-plugin
BuildRequires:  junit
BuildRequires:  c3p0
BuildRequires:  ejb_api
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-dbcp
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-modeler
BuildRequires:  apache-commons-pool
BuildRequires:  apache-commons-validator
BuildRequires:  javamail >= 1.4.3
BuildRequires:  jms
BuildRequires:  jta
BuildRequires:  log4j
BuildRequires:  servlet >= 2.5

Requires:  jpackage-utils
Requires:  apache-commons-beanutils
Requires:  apache-commons-collections
Requires:  apache-commons-dbcp
Requires:  apache-commons-digester
Requires:  apache-commons-logging
Requires:  apache-commons-modeler
Requires:  apache-commons-pool
Requires:  apache-commons-validator
Requires:  ejb_api
Requires:  javamail
Requires:  jms
Requires:  log4j
Requires:  servlet >= 2.5
Requires:  jta

BuildArch:      noarch
Source44: import.info

%description
Quartz is a job scheduling system that can be integrated with, or used 
along side virtually any J2EE or J2SE application. Quartz can be used 
to create simple or complex schedules for executing tens, hundreds, or 
even tens-of-thousands of jobs; jobs whose tasks are defined as standard 
Java components or EJBs. 

%package javadoc
Summary:        API docs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API Documentation for %{name}.

%prep
%setup -q 
%patch0 -b .sav0

%build
# skip tests for now due to requirement on hamcrest 1.2
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}/target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -p %{name}-backward-compat/target/%{name}-backward-compat-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-backward-compat.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom
install -m 644 %{name}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -m 644 %{name}-backward-compat/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-backward-compat.pom

%add_maven_depmap JPP-%{name}-parent.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-backward-compat.pom %{name}-backward-compat.jar

#javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc README.txt NOTICE.txt LICENSE.txt
%{_javadir}/*.jar
%{_mavenpomdir}/JPP-*
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_4jpp7
- new version

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_6jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_4jpp5
- new jpp release

* Mon Oct 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_3jpp5
- full build

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Oct 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

