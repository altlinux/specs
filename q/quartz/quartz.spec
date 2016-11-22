Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Summary:        Enterprise Job Scheduler for Java
Name:           quartz
Version:        2.2.1
Release:        alt1_5jpp8
Epoch:          0
License:        ASL 2.0
URL:            http://www.quartz-scheduler.org/
# svn export http://svn.terracotta.org/svn/quartz/tags/quartz-2.2.1
# tar caf quartz-2.2.1.tar.xz quartz-2.2.1
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-checkstyle-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-shared
BuildRequires:  rmic-maven-plugin
BuildRequires:  mvn(com.mchange:c3p0)
BuildRequires:  mvn(javax.mail:mail) >= 1.4.3
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-commonj_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-ejb_2.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:  mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-log4j12)
# test deps
BuildRequires:  mvn(asm:asm)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.derby:derby)
BuildRequires:  mvn(org.hamcrest:hamcrest-library) >= 1.2

BuildArch:      noarch
Source44: import.info

%description
Quartz is a job scheduling system that can be integrated with, or used 
along side virtually any J2EE or J2SE application. Quartz can be used 
to create simple or complex schedules for executing tens, hundreds, or 
even tens-of-thousands of jobs; jobs whose tasks are defined as standard 
Java components or EJBs. 

%package javadoc
Group: Development/Java
Summary:        API docs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API Documentation for %{name}.

%prep
%setup -q
# Unwated modules
%pom_disable_module quartz-jboss
%pom_disable_module quartz-oracle
%pom_disable_module quartz-weblogic

# Unavailable deps
# org.terracotta.toolkit:terracotta-toolkit-api,terracotta-toolkit-api-internal:2.1.0
%pom_disable_module terracotta

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
# Unwated plugin disable source JARs
%pom_remove_plugin :maven-source-plugin

# Fix c3p0 groupId
sed -i -e 's/groupId>c3p0</groupId>com.mchange</' **/pom.xml pom.xml
# Fix junit artifactId
sed -i -e 's/artifactId>junit-dep</artifactId>junit</' **/pom.xml pom.xml

# Use available javax apis
%pom_remove_dep org.apache.openejb:javaee-api quartz-core
%pom_add_dep org.apache.geronimo.specs:geronimo-jta_1.1_spec::provided quartz-core
%pom_add_dep org.apache.tomcat:tomcat-servlet-api::provided quartz-core
%pom_remove_dep org.apache.openejb:javaee-api quartz-jobs
%pom_add_dep org.apache.geronimo.specs:geronimo-ejb_2.1_spec::provided quartz-jobs
%pom_add_dep org.apache.geronimo.specs:geronimo-jms_1.1_spec::provided quartz-jobs 
%pom_remove_dep org.apache.openejb:javaee-api quartz-plugins
%pom_add_dep org.apache.geronimo.specs:geronimo-jta_1.1_spec::provided quartz-plugins
# Disable javadoc jar
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions" quartz-jobs

# Fix log4j version
sed -i -e 's/<log4j.version>1.2.16/<log4j.version>1.2.17/' pom.xml
# This artefact bundled all quartz modules
%pom_disable_module quartz
%if 0
# Unavailable plugins
# org.terracotta:maven-forge-plugin:1.0.7
%pom_remove_plugin org.terracotta:maven-forge-plugin quartz
%pom_remove_plugin :gmaven-plugin quartz
# Disable javadoc jar
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions" quartz
# Unavailable deps
%pom_remove_dep org.quartz-scheduler.internal:quartz-jboss quartz
%pom_remove_dep org.quartz-scheduler.internal:quartz-oracle quartz
%pom_remove_dep org.quartz-scheduler.internal:quartz-terracotta-bootstrap quartz
%pom_remove_dep org.quartz-scheduler.internal:quartz-weblogic quartz
# Remove unavailable libraries references, ( TODO provide a OSGi MANIFEST.MF file ).
sed -i '/org.jboss/d' quartz/pom.xml
sed -i '/org.terracotta.toolkit/d' quartz/pom.xml
sed -i '/weblogic.jdbc/d' quartz/pom.xml
sed -i '/oracle.sql/d' quartz/pom.xml
%endif

cp -p distribution/src/main/assembly/root/licenses/LICENSE.txt .
sed -i 's/\r//' LICENSE.txt

%mvn_file :%{name}-core %{name}/%{name}-core %{name}/%{name} %{name}
%mvn_alias :%{name}-core org.quartz-scheduler:%{name}

%build

# skip tests for now due to requirement on hamcrest 1.2
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt1_5jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt1_4jpp8
- java 8 mass update

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt3_7jpp7
- added BR: for xmvn

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

