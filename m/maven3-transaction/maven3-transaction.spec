Name: maven3-transaction
Version: 1.0
Summary: Maven3 transaction files
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt0.5jpp

Requires: jbossts
Requires: mojo-maven2-plugins
Requires: maven-ant-tasks
Requires: logback
Requires: hawtjni
Requires: jsontools
Requires: gmaven
Requires: eclipse

%description
Maven3 transaction unfinished files.
Temporary package to keep them alive.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT

%files

%changelog
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

