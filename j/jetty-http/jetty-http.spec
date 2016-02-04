Name: jetty-http
Version: 9.3.0
Summary: http module for Jetty
License: ASL 2.0 or EPL
Url: http://www.eclipse.org/jetty/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jetty-http = 9.3.0-6.fc23
Provides: mvn(org.eclipse.jetty:jetty-http) = 9.3.0.v20150612
Provides: mvn(org.eclipse.jetty:jetty-http:pom:) = 9.3.0.v20150612
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.eclipse.jetty:jetty-util)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jetty-http-9.3.0-6.fc23.cpio

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

This package contains http module for Jetty.

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

