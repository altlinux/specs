Name: maven3-transaction
Version: 1.0
Summary: Maven3 transaction files
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt4jpp

Requires: activemq
Requires: apache-commons-math
Requires: arquillian-osgi
Requires: eclipse-cdt
Requires: eclipse-jgit
Requires: eclipse-swtbot
#Requires: fest-assert
Requires: gshell
Requires: hibernate3
Requires: hibernate-validator
Requires: infinispan
Requires: jacoco
Requires: jasypt
Requires: jaxb2-maven-plugin
Requires: jbosgi-deployment
Requires: jbosgi-framework
Requires: jboss-metadata
Requires: jboss-naming
Requires: jboss-remoting
Requires: jboss-web
Requires: jersey
Requires: jetty
Requires: maven
Requires: maven-ant-tasks
Requires: maven-indexer
Requires: maven-jflex-plugin
Requires: maven-site-plugin
Requires: mojo-signatures
Requires: plexus-container-default
Requires: springframework
Requires: tomcat6
Requires: weld-api
Requires: xnio

%description
Maven3 transaction unfinished files.
Temporary package to keep them alive.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT

%files

%changelog
* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4jpp
- updated dependencies

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3jpp
- updated dependencies

* Thu Feb 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2jpp
- updated dependencies

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1jpp
- updated dependencies

* Fri Sep 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.9jpp
- updated dependencies

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.8jpp
- updated dependencies

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.7jpp
- updated dependencies

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.6jpp
- updated dependencies

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.5jpp
- updated dependencies

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.4jpp
- updated dependencies

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.3jpp
- updated dependencies

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.2jpp
- updated dependencies

* Fri Jun 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- temporary package

