%define _unpackaged_files_terminate_build 1

Name: httpcomponents-asyncclient
Version: 4.1.5
Release: alt1

Summary: Apache asynchronous HTTP client
License: Apache-2.0
Group: Development/Java
URL: https://hc.apache.org/httpcomponents-asyncclient-4.1.x/
VCS: https://github.com/apache/httpasyncclient.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.httpcomponents:httpcomponents-parent:pom:)
BuildRequires: mvn(org.apache.httpcomponents:httpcore)
BuildRequires: mvn(org.apache.httpcomponents:httpcore-nio)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
# Maven loads all reactor models before it selects the core module.
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
The Apache HttpComponents asynchronous HTTP client.

%package parent
Summary: Maven parent POM for Apache HttpComponents AsyncClient
Group: Development/Java

%description parent
The upstream Maven parent POM for Apache HttpComponents AsyncClient.

%javadoc_package

%prep
%setup
%autopatch -p1
# Contributor checks unavailable in the offline build root.
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin org.apache.rat:apache-rat-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin

%build
%mvn_build -s -- -pl httpasyncclient -am \
    -Dmaven.compiler.source=8 -Dmaven.compiler.target=8 -Dmaven.source.skip=true

%install
%mvn_install

%files -f .mfiles-httpasyncclient
%doc LICENSE.txt NOTICE.txt

%files parent -f .mfiles-httpcomponents-asyncclient

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 4.1.5-alt1
- Initial build for ALT.
