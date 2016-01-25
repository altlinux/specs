Name: maven3-transaction
Version: 1.0
Summary: Maven3 transaction files
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt15jpp

Provides: eclipse-swt = 4.0 i586-eclipse-swt = 4.0
Provides: eclipse-platform eclipse-rcp
Provides: /usr/share/java/maven-ant-tasks.jar maven-ant-tasks
Provides: /usr/share/java/slf4j/jcl-over-slf4j.jar /usr/share/java/slf4j/jul-to-slf4j.jar mvn(org.slf4j:jcl-over-slf4j) mvn(org.slf4j:jul-to-slf4j)
Provides: osgi(org.objectweb.asm) = 3.2.0
Requires: activemq
Requires: apache-commons-math
Requires: arquillian-osgi
#Requires: gshell
Requires: hibernate3
Requires: hibernate-validator
Requires: infinispan
#Requires: jaxb2-maven-plugin
#Requires: jbosgi-deployment
#Requires: jbosgi-framework
#Requires: jboss-metadata
#Requires: jboss-naming
#Requires: jboss-remoting
#Requires: jboss-web
#Requires: jersey
Requires: jetty
Requires: maven
#Requires: maven-ant-tasks
#Requires: maven-indexer
Requires: maven-jflex-plugin
Requires: maven-site-plugin
Requires: mojo-signatures
#Requires: plexus-container-default
Requires: springframework
Requires: tomcat6
Requires: weld-api
#Requires: xnio

%description
Maven3 transaction unfinished files.
Temporary package to keep them alive.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT

%files

%changelog
* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt15jpp
- updated dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt14jpp
- updated dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt13jpp
- updated dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt12jpp
- updated dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt11jpp
- updated dependencies

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt10jpp
- updated dependencies

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt9jpp
- updated dependencies

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt8jpp
- updated dependencies

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt7jpp
- updated dependencies

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt6jpp
- updated dependencies

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5jpp
- updated dependencies

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4jpp
- updated dependencies

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3jpp
- updated dependencies

* Thu Feb 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2jpp
- updated dependencies

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1jpp
- updated dependencies
