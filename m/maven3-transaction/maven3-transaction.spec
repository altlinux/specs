Name: maven3-transaction
Version: 1.0
Summary: Maven3 transaction files
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt19jpp

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
