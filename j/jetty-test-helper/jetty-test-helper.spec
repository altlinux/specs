Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jetty-test-helper
Version:        3.1
Release:        alt1_5jpp8
# header-template.txt documents dual licensing
License:        ASL 2.0 or EPL
Summary:        Jetty toolchain test helper
URL:            https://github.com/eclipse/jetty.toolchain
Source0:        https://github.com/eclipse/jetty.toolchain/archive/%{name}-%{version}.tar.gz
# https://github.com/eclipse/jetty.toolchain/issues/5
Source1:        https://github.com/eclipse/jetty.project/blob/jetty-9.3.x/LICENSE-eplv10-aslv20.html
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
Source44: import.info

%description
Unit Testing Support for Jetty (common classes for some unit tests).

%package        javadoc
Group: Development/Java
Summary:        Javadoc %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n jetty.toolchain-%{name}-%{version}/%{name}

find -name '*.?ar' -delete
find -name '*.class' -delete

cp %{SOURCE1} .

%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE-eplv10-aslv20.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-eplv10-aslv20.html

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_5jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_4jpp8
- new version

