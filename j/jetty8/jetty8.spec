Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# jetty8 is a compat package and as such it shouldn't have any OSGi provides


%global addver v20150415

Name:           jetty8
Version:        8.1.17
Release:        alt1_3jpp8
Summary:        Java Webserver and Servlet Container
# Jetty is dual licensed under both ASL 2.0 and EPL 1.0, see NOTICE.txt
# some MIT-licensed code (from Utf8Appendable) is used too
License:        (ASL 2.0 or EPL) and MIT
URL:            http://www.eclipse.org/jetty
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.project.git/snapshot/jetty-%{version}.%{addver}.tar.bz2

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-artifact-remote-resources)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-assembly-descriptors)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-build-support)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-version-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-test-policy)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)

Requires:       %{name}-rewrite = %{version}
Requires:       %{name}-client = %{version}
Requires:       %{name}-xml = %{version}
Requires:       %{name}-websocket = %{version}
Requires:       %{name}-webapp = %{version}
Requires:       %{name}-util = %{version}
Requires:       %{name}-servlet = %{version}
Requires:       %{name}-server = %{version}
Requires:       %{name}-security = %{version}
Requires:       %{name}-jmx = %{version}
Requires:       %{name}-io = %{version}
Requires:       %{name}-http = %{version}
Requires:       %{name}-continuation = %{version}
Source44: import.info
%filter_from_provides /^osgi\\(/d

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

%package        rewrite
Group: Development/Java
Summary:        Jetty rewrite handler
%description    rewrite
This package contains %{summary}.

%package        client
Group: Development/Java
Summary:        Jetty asynchronous HTTP client
%description    client
This package contains %{summary}.

%package        xml
Group: Development/Java
Summary:        Jetty XML utilities
%description    xml
This package contains %{summary}.

%package        websocket
Group: Development/Java
Summary:        Jetty websocket
%description    websocket
This package contains %{summary}.

%package        webapp
Group: Development/Java
Summary:        Jetty web application support
%description    webapp
This package contains %{summary}.

%package        util
Group: Development/Java
Summary:        Jetty utility classes
%description    util
This package contains %{summary}.

%package        servlet
Group: Development/Java
Summary:        Jetty servlet container
%description    servlet
This package contains %{summary}.

%package        server
Group: Development/Java
Summary:        Jetty server artifact
%description    server
This package contains %{summary}.

%package        security
Group: Development/Java
Summary:        Jetty security infrastructure
%description    security
This package contains %{summary}.

%package        jmx
Group: Development/Java
Summary:        Jetty JMX management artifact
%description    jmx
This package contains %{summary}.

%package        io
Group: Development/Java
Summary:        Jetty IO utility
%description    io
This package contains %{summary}.

%package        http
Group: Development/Java
Summary:        Jetty HTTP utility
%description    http
This package contains %{summary}.

%package        continuation
Group: Development/Java
Summary:        Jetty asynchronous API
%description    continuation
This package contains %{summary}.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n jetty-%{version}.%{addver}
find -name "*.jar" -delete
find -name "*.war" -delete
find -name "*.class" -delete

%mvn_compat_version : 8.1 %{version}.%{addver} 8.1.14.v20131031

# aggregating POM belongs to main package
%mvn_package :jetty-project::pom

%pom_change_dep -r org.eclipse.jetty.orbit:javax.servlet org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec

# Disable unneeded modules. This is a compat package and only a
# minimal set of modules are being built.
%pom_xpath_remove "pom:modules"
%pom_xpath_inject "pom:project" "<modules/>"
for mod in continuation http io jmx security server servlet util webapp websocket xml client rewrite; do
  %pom_xpath_inject pom:modules "<module>jetty-$mod</module>"
  %pom_xpath_inject 'pom:plugin[pom:artifactId="maven-bundle-plugin"]/pom:executions/pom:execution' '
     <phase>process-classes</phase>' jetty-$mod
done

# PMD plugin is not useful in Fedora.
%pom_remove_plugin -r :maven-pmd-plugin

%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-site-plugin

# this needs jetty6 things, so just remove it
# shouldn't cause any trouble since it handled only in loadClass elsewhere
%pom_remove_dep org.mortbay.jetty:jetty-util jetty-continuation
rm jetty-continuation/src/main/java/org/eclipse/jetty/continuation/Jetty6Continuation.java

# CCLAs and CLAs, we don't want to install these
rm -Rf LICENSE-CONTRIBUTOR/

%build
# Tests disabled because of missing dependencies
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-jetty-project
%{!?_licensedir:%global license %%doc}
%doc NOTICE.txt README.txt VERSION.txt LICENSE*

%files rewrite -f .mfiles-jetty-rewrite
%files client -f .mfiles-jetty-client
%files xml -f .mfiles-jetty-xml
%files websocket -f .mfiles-jetty-websocket
%files webapp -f .mfiles-jetty-webapp
%files util -f .mfiles-jetty-util
%doc NOTICE.txt LICENSE*
%files servlet -f .mfiles-jetty-servlet
%files server -f .mfiles-jetty-server
%files security -f .mfiles-jetty-security
%files jmx -f .mfiles-jetty-jmx
%files io -f .mfiles-jetty-io
%files http -f .mfiles-jetty-http
%files continuation -f .mfiles-jetty-continuation

%files javadoc -f .mfiles-javadoc
%doc NOTICE.txt LICENSE*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 8.1.17-alt1_3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 8.1.17-alt1_2jpp8
- java8 mass update

