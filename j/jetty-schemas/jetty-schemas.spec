Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global reltag b07
Name:       jetty-schemas
Version:    4.0.0
Release:    alt1_3.b07jpp8
Summary:    XML Schemas for Jetty
License:    CDDL-1.1 or GPLv2 with exceptions
URL:        http://www.eclipse.org/jetty/
BuildArch:  noarch

Source0:    https://github.com/eclipse/jetty.toolchain/archive/%{name}-%{version}-%{reltag}.tar.gz
Source1:    https://glassfish.dev.java.net/public/CDDL+GPL_1_1.html

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
Source44: import.info

%description
%{summary}.

%prep
%setup -q -n jetty.toolchain-%{name}-%{version}-%{reltag}/%{name}
cp %SOURCE1 .

%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CDDL+GPL_1_1.html

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_3.b07jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_7jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_4jpp8
- java 8 mass update

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

