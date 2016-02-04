Name: jetty-maven-plugin
Version: 9.3.0
Summary: maven-plugin module for Jetty
License: ASL 2.0 or EPL
Url: http://www.eclipse.org/jetty/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jetty-maven-plugin = 9.3.0-6.fc23
Provides: mvn(org.eclipse.jetty:jetty-maven-plugin) = 9.3.0.v20150612
Provides: mvn(org.eclipse.jetty:jetty-maven-plugin:pom:) = 9.3.0.v20150612
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.eclipse.jetty.websocket:javax-websocket-server-impl)
Requires: mvn(org.eclipse.jetty.websocket:websocket-server)
Requires: mvn(org.eclipse.jetty:apache-jsp)
Requires: mvn(org.eclipse.jetty:apache-jstl)
Requires: mvn(org.eclipse.jetty:jetty-annotations)
Requires: mvn(org.eclipse.jetty:jetty-jaas)
Requires: mvn(org.eclipse.jetty:jetty-jmx)
Requires: mvn(org.eclipse.jetty:jetty-jndi)
Requires: mvn(org.eclipse.jetty:jetty-plus)
Requires: mvn(org.eclipse.jetty:jetty-quickstart)
Requires: mvn(org.eclipse.jetty:jetty-server)
Requires: mvn(org.eclipse.jetty:jetty-util)
Requires: mvn(org.eclipse.jetty:jetty-webapp)
Requires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jetty-maven-plugin-9.3.0-6.fc23.cpio

%description

Jetty is a 100% Java HTTP Server and Servlet Container. This means that you
do not need to configure and run a separate web server (like Apache) in order
to use Java, servlets and JSPs to generate dynamic content. Jetty is a fully
featured web server for static and dynamic content. Unlike separate
server/container solutions, this means that your web server and web
application run in the same process, without interconnection overheads
and complications. Furthermore, as a pure java component, Jetty can be simply
included in your application for demonstration, distribution or deployment.
Jetty is available on all Java supported platforms.

This package contains maven-plugin module for Jetty.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 9.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

