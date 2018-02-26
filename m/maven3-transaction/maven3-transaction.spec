Name: maven3-transaction
Version: 1.0
Summary: Maven3 transaction files
License: ASL 2.0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt0.2jpp

Requires: plexus-runtime-builder
#Requires: maven-embedder
Requires: maven-archetype2
Requires: plexus-maven-plugin
#Requires: plexus-container-artifact
Requires: mojo-maven2-plugins
Requires: maven-ant-tasks
Requires: logback
Requires: hawtjni
Requires: junit4
Requires: jsontools
Requires: gmaven
Requires: jbossorg-docbook-xslt
Requires: eclipse-mylyn-commons
Requires: apache-commons-logging
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
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.2jpp
- updated dependencies

* Fri Jun 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- temporary package

