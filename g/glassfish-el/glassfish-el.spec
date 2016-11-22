Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global artifactId javax.el

Name:           glassfish-el
Version:        3.0.0
Release:        alt1_6jpp8
Summary:        J2EE Expression Language Implementation
License:        CDDL or GPLv2 with exceptions
URL:            http://uel.java.net
# ./generate_tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        generate_tarball.sh
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit47)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Source44: import.info


%description
This project provides an implementation of the Expression Language (EL).
The main goals are:
 * Improves current implementation: bug fixes and performance improvements
 * Provides API for use by other tools, such as Netbeans

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%mvn_file :%{artifactId} %{name}
%mvn_alias :%{artifactId} "org.eclipse.jetty.orbit:com.sun.el" "org.glassfish.web:javax.el"

# unbundled from sources
%pom_add_dep javax.el:javax.el-api:3.0.0

# missing (unneeded) dep org.glassfish:legal
%pom_remove_plugin :maven-remote-resources-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_6jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_5jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_2jpp7
- new release

