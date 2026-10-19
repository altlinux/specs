Epoch: 0
Group: System/Libraries
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

Name:          dnsjava
Version:       3.6.3
Release:       alt1
Summary:       Java DNS implementation

License:       BSD-3-Clause
URL:           https://github.com/dnsjava/dnsjava
VCS:           https://github.com/dnsjava/dnsjava

Source0:       https://github.com/dnsjava/dnsjava/archive/v%{version}.tar.gz
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.projectlombok:lombok-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.openjdk.jcstress:jcstress-core)

%description
dnsjava is an implementation of DNS in Java. It supports all of the common
record types and the DNSSEC types. It can be used for queries, zone transfers,
and dynamic updates. It includes a cache which can be used by clients, and a
minimal implementation of a server. It supports TSIG authenticated messages,
partial DNSSEC verification, and EDNS0.

dnsjava provides functionality above and beyond that of the InetAddress class.
Since it is written in pure Java, dnsjava is fully threadable, and in many
cases is faster than using InetAddress.

dnsjava provides both high and low level access to DNS. The high level
functions perform queries for records of a given name, type, and class, and
return an array of records. There is also a clone of InetAddress, which is
even simpler. A cache is used to reduce the number of DNS queries sent. The
low level functions allow direct manipulation of dns messages and records, as
well as allowing additional resolver properties to be set.

A 'dig' clone and a dynamic update program are included, as well as a
primary-only server.

%prep
%setup

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :spotless-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :properties-maven-plugin

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%changelog
* Fri Oct 16 2026 Anton Meleshnikov <alton@altlinux.org> 0:3.6.3-alt1
- new version
- added vcs tag
- removed import.info

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:2.1.3-alt3_18jpp8
- build w/o xmvn to support xmvn4

* Fri May 27 2022 Igor Vlasenko <viy@altlinux.org> 0:2.1.3-alt2_18jpp8
- build with compat bnd4

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_18jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_16jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_15jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_13jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_12jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_11jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_4jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_3jpp7
- new fc release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_9jpp7
- update to new release by jppimport

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_8jpp6
- update to new release by jppimport

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt2_1jpp5
- explicitly selected java5 as default

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.6-alt1_1jpp5
- new jpp release

