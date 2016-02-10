Name: jbossws-cxf
Version: 4.2.3
Summary: JBoss Web Services CXF stack
License: LGPLv2+
Url: http://www.jboss.org/jbossws
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jbossws-cxf = 4.2.3-1.fc21
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-addons:pom:) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-client) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-client:pom:) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-factories) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-factories:pom:) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-resources) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-resources::wildfly800:) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-resources:pom:) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-server) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-server:pom:) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-transports-httpserver) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-transports-httpserver:pom:) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-transports-udp) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf-transports-udp:pom:) = 4.2.3.Final
Provides: mvn(org.jboss.ws.cxf:jbossws-cxf:pom:) = 4.2.3.Final
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(asm:asm)
Requires: mvn(com.sun.xml.bind:jaxb-impl)
Requires: mvn(com.sun.xml.bind:jaxb-xjc)
Requires: mvn(com.sun.xml.fastinfoset:FastInfoset)
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(javax.xml.stream:stax-api)
Requires: mvn(log4j:log4j)
Requires: mvn(org.apache.cxf.services.sts:cxf-services-sts-core)
Requires: mvn(org.apache.cxf.services.ws-discovery:cxf-services-ws-discovery-api)
Requires: mvn(org.apache.cxf.xjcplugins:cxf-xjc-boolean)
Requires: mvn(org.apache.cxf.xjcplugins:cxf-xjc-dv)
Requires: mvn(org.apache.cxf.xjcplugins:cxf-xjc-ts)
Requires: mvn(org.apache.cxf:cxf-rt-bindings-coloc)
Requires: mvn(org.apache.cxf:cxf-rt-bindings-object)
Requires: mvn(org.apache.cxf:cxf-rt-bindings-soap)
Requires: mvn(org.apache.cxf:cxf-rt-frontend-jaxws)
Requires: mvn(org.apache.cxf:cxf-rt-management)
Requires: mvn(org.apache.cxf:cxf-rt-transports-http)
Requires: mvn(org.apache.cxf:cxf-rt-transports-jms)
Requires: mvn(org.apache.cxf:cxf-rt-transports-local)
Requires: mvn(org.apache.cxf:cxf-rt-ws-mex)
Requires: mvn(org.apache.cxf:cxf-rt-ws-policy)
Requires: mvn(org.apache.cxf:cxf-rt-ws-rm)
Requires: mvn(org.apache.cxf:cxf-rt-ws-security)
Requires: mvn(org.apache.cxf:cxf-tools-java2ws)
Requires: mvn(org.apache.cxf:cxf-tools-wsdlto-core)
Requires: mvn(org.apache.cxf:cxf-tools-wsdlto-databinding-jaxb)
Requires: mvn(org.apache.cxf:cxf-tools-wsdlto-frontend-jaxws)
Requires: mvn(org.apache.santuario:xmlsec)
Requires: mvn(org.apache.velocity:velocity)
Requires: mvn(org.codehaus.woodstox:woodstox-core-asl)
Requires: mvn(org.jboss.com.sun.httpserver:httpserver)
Requires: mvn(org.jboss.logging:jboss-logging)
Requires: mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
Requires: mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
Requires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
Requires: mvn(org.jboss.spec.javax.xml.bind:jboss-jaxb-api_2.2_spec)
Requires: mvn(org.jboss.spec.javax.xml.rpc:jboss-jaxrpc-api_1.1_spec)
Requires: mvn(org.jboss.spec.javax.xml.soap:jboss-saaj-api_1.3_spec)
Requires: mvn(org.jboss.spec.javax.xml.ws:jboss-jaxws-api_2.2_spec)
Requires: mvn(org.jboss.ws.projects:jaxws-jboss-httpserver-httpspi)
Requires: mvn(org.jboss.ws:jbossws-api)
Requires: mvn(org.jboss.ws:jbossws-common)
Requires: mvn(org.jboss.ws:jbossws-common-tools)
Requires: mvn(org.jboss.ws:jbossws-spi)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jbossws-cxf-4.2.3-1.fc21.cpio

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
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

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

