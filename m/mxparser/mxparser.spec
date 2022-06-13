Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mxparser
Version:        1.2.2
Release:        alt1_3jpp11
Summary:        Parser of xpp3_min 1.1.7 with merged changes of the Plexus fork
License:        xpp
URL:            https://github.com/x-stream/%{name}
BuildArch:      noarch

Source0:        https://github.com/x-stream/%{name}/archive/v-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(xmlpull:xmlpull)
Source44: import.info

%description
MXParser is a fork of xpp3_min 1.1.7 containing only the parser with merged
changes of the Plexus fork. It is an implementation of the XMLPULL V1 API
(parser only).

%{?javadoc_package}

%prep
%setup -q -n %{name}-v-%{version}


%pom_remove_plugin :maven-changes-plugin .
%pom_remove_plugin :maven-javadoc-plugin .
%pom_remove_plugin :maven-source-plugin .

%pom_xpath_set 'pom:project/pom:properties/pom:version.java.source' 1.8
%pom_xpath_set 'pom:project/pom:properties/pom:version.java.target' 1.8
%pom_xpath_set 'pom:project/pom:properties/pom:version.java.test.source' 1.8
%pom_xpath_set 'pom:project/pom:properties/pom:version.java.test.target' 1.8

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc README.md

%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 1.2.2-alt1_3jpp11
- new version

