Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jmdns
Version:        3.5.5
Release:        alt1_1jpp11
Summary:        Java implementation of multi-cast DNS

License:        ASL 2.0
URL:            https://github.com/jmdns/jmdns
Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:      noarch
Source44: import.info

%description
JmDNS is a Java implementation of multi-cast DNS
and can be used for service registration and discovery
in local area networks. JmDNS is fully compatible
with Apple's Bonjour.


%prep
%setup -q -n %{name}-%{name}-%{version}


# Remove duplicate jar execution
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions"

# Javadoc temporary disabled while upsteam not fix javadoc generation
# https://github.com/jmdns/jmdns/issues/199
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']"
%pom_xpath_remove "pom:properties[pom:javadoc.opts]"

chmod -x README.md


%build
# Tests are disabled because they try to use network
%mvn_build -f --skip-javadoc -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md



%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:3.5.5-alt1_1jpp11
- java11 build

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:3.5.5-alt1_1jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_16jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_15jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_13jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_12jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4.1-alt1_10jpp8
- new version

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp1.7
- added ant-junit BR:

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

