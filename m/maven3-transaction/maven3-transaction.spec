Name: maven3-transaction
Version: 1.0
Summary: Maven3 transaction files
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt24jpp

# jetty
Provides: /usr/share/java/tomcat-el-2.2-api.jar
Provides: /usr/share/java/tomcat-servlet-3.0-api.jar
Provides: /usr/share/java/tomcat/tomcat-jsp-2.2-api.jar
Provides: /usr/share/java/glassfish-jsp-api.jar
# gradle 
Provides: /usr/share/java/plexus/container-default.jar plexus-container-default
Provides: /usr/share/java/aqute-bnd.jar
# for apacheds jpp7
Provides: mvn(org.apache.directory.project:project)
Provides: netty-tcnative mvn(io.netty:netty-tcnative)
Provides: eclipse-platform eclipse-rcp
Provides: /usr/share/java/maven-ant-tasks.jar maven-ant-tasks
Provides: i586-eclipse-swt = 4.0
#Requires: springframework
#Requires: tomcat6
#Requires: weld-api
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

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt19jpp
- updated dependencies

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt18jpp
- updated dependencies

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt17jpp
- updated dependencies

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt16jpp
- updated dependencies

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
