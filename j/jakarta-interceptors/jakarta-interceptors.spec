%define _unpackaged_files_terminate_build 1

Name: jakarta-interceptors
Version: 2.2.0
Release: alt1

Summary: Jakarta Interceptors
License: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0
Group: Development/Java
URL: https://github.com/jakartaee/interceptors
VCS: https://github.com/jakartaee/interceptors.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(jakarta.annotation:jakarta.annotation-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)
BuildRequires: asciidoctor

Provides: geronimo-interceptor = %version-%release
Obsoletes: geronimo-interceptor < 1.0.1-25
Conflicts: geronimo-interceptor < 1.0.1-alt3

%description
Jakarta Interceptors defines interposition on business method invocations
and lifecycle events in Jakarta EE components and other managed classes.

%package javadoc
Summary: API documentation for Jakarta Interceptors
Group: Development/Java
Provides: geronimo-interceptor-javadoc = %version-%release
Obsoletes: geronimo-interceptor-javadoc < 1.0.1-25

%description javadoc
API documentation for Jakarta Interceptors.

%package manual
License: Eclipse Foundation Specification License v1.0
Summary: Jakarta Interceptors specification
Group: Documentation

%description manual
The complete upstream Jakarta Interceptors specification in HTML format.

%prep
%setup
# Build the specification with the available native Asciidoctor provider.
%pom_disable_module spec
# XMvn installs the genuine POM without OSSRH publication flattening.
%pom_remove_plugin :flatten-maven-plugin api
%pom_remove_plugin :maven-source-plugin api
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions" api
%mvn_file :jakarta.interceptor-api %name/jakarta.interceptor-api

%build
java -version
%mvn_build
asciidoctor -b html5 -d book -a data-uri -a toc=left -a sectanchors \
    -a revnumber=2.2 -a status=DRAFT -a revremark=DRAFT \
    -a idprefix= -a idseparator=- \
    -D target/manual spec/src/main/asciidoc/interceptors-spec.adoc

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/interceptors-spec.html

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 2.2.0-alt1
- New version.
- Package the HTML specification.

* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_3jpp11
- added conflict with jakarta-interceptors (closes: #40740)

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_2jpp11
- new version

