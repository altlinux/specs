Name: jbossws-cxf
Version: 4.1.0
Summary: JBoss Web Services CXF stack
License: LGPLv2+
Url: http://www.jboss.org/jbossws
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf)
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-addons)
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-client)
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-factories)
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-resources)
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-server)
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-transports-httpserver)
Requires: cxf
Requires: cxf-services
Requires: java
Requires: jaxws-jboss-httpserver-httpspi
Requires: jboss-ejb-3.1-api
Requires: jboss-jaxb-2.2-api
Requires: jboss-jms-1.1-api
Requires: jboss-saaj-1.3-api
Requires: jbossws-common
Requires: jpackage-utils
Requires: picketbox

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jbossws-cxf-4.1.0-4.fc19.cpio

%description
JBoss Web Services CXF integration stack

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
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt4_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt3_2jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt2_2jpp7
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_2jpp7
- new version

