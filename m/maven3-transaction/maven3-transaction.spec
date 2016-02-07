Name: maven3-transaction
Version: 1.0
Summary: Maven3 transaction files
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt34jpp

# todo springframework
Provides: mvn(org.springframework.batch:spring-batch-infrastructure)
Provides: mvn(org.springframework.batch:spring-batch-core)
# todo infinicpan
Provides: mvn(org.infinispan:infinispan-lucene-directory)
# todo sonar
#Provides: sonar-batch-bootstrapper
#Provides: objectweb-asm4 = 5
# to build hornetq
Provides: mvn(org.hornetq:hornetq-journal)
# jetty
Provides: jetty = 9
# for apacheds jpp7
Provides: mvn(org.apache.directory.project:project)
Provides: netty-tcnative mvn(io.netty:netty-tcnative)
Provides: eclipse-platform eclipse-rcp
Provides: i586-eclipse-swt = 4.0
Provides: i586-itext
#Requires: springframework
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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt34jpp
- updated dependencies

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt33jpp
- updated dependencies

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt32jpp
- updated dependencies

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt31jpp
- updated dependencies

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt30jpp
- updated dependencies

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt29jpp
- updated dependencies

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt28jpp
- updated dependencies

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt27jpp
- updated dependencies

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt26jpp
- updated dependencies

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt25jpp
- updated dependencies

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt24jpp
- updated dependencies

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt23jpp
- updated dependencies

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt22jpp
- updated dependencies

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt21jpp
- updated dependencies

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt20jpp
- updated dependencies
