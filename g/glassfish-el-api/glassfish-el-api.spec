Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global artifactId javax.el-api

Name:           glassfish-el-api
Version:        3.0.0
Release:        alt2_8jpp8
Summary:        Expression Language API 2.2.4
# Part of implementation files contain ASL 2.0 copyright
License:        (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:            http://uel.java.net
# ./generate_tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        generate_tarball.sh
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
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
cp -p %{SOURCE1} .

%mvn_file :%{artifactId} %{name}

# missing (unneeded) dep org.glassfish:legal
%pom_remove_plugin :maven-remote-resources-plugin
# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_alias : javax.el:el-api
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt2_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt2_7jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_7jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_1jpp7
- new release

