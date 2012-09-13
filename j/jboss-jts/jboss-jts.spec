Name: jboss-jts
Version: 4.16.2
Summary: Distributed Transaction Manager
License: LGPLv2+
Url: https://community.jboss.org/wiki/JBossJTS
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: antlr-tool
Requires: avalon-logkit
Requires: byteman
Requires: emma
#Requires: hornetq
#Requires: ironjacamar
Requires: jacorb
Requires: java
#Requires: java-service-wrapper
Requires: jboss-logging
Requires: jboss-logging-tools
Requires: jboss-transaction-1.1-api
Requires: jboss-transaction-spi
Requires: jfreechart
Requires: jpackage-utils
Requires: slf4j

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jboss-jts-4.16.2-9.fc19.cpio

%description
A set of JBoss modules that fully supports ACID transactions
spread across multiple resource managers and application servers.
It implements a Distributed Transaction Manager (DTM) with support
for two-phase commit (2PC) across XA resource managers, JBoss
server instances, and CORBA OTS resources.

JBossJTS implements the Java Transaction Service (JTS) and CORBA
Transaction Service (OTS) specifications.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 4.16.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

