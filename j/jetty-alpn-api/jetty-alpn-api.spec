Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global addver v20141014

Name:           jetty-alpn-api
Version:        1.1.0
Release:        alt1_4jpp8
Summary:        Jetty ALPN API
License:        ASL 2.0 and EPL
URL:            http://www.eclipse.org/jetty
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.alpn.git/snapshot/alpn-api-%{version}.%{addver}.tar.bz2
Source1:        http://www.eclipse.org/legal/epl-v10.html
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)
Source44: import.info

%description
Jetty API for Application-Layer Protocol Negotiation.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.


%prep
%setup -q -n alpn-api-%{version}.%{addver}

# Use packaging=bundle to get the manifest into jar
%pom_remove_plugin :maven-jar-plugin
%pom_xpath_inject pom:project '<packaging>bundle</packaging>'

cp %{SOURCE1} %{SOURCE2} .

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc epl-v10.html LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc epl-v10.html LICENSE-2.0.txt


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_4jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_3jpp8
- new version

