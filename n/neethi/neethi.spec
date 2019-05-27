Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          neethi
Version:       3.0.3
Release:       alt1_3jpp8
Summary:       Web Services Policy framework
License:       ASL 2.0
URL:           http://ws.apache.org/neethi/
Source0:       http://archive.apache.org/dist/ws/neethi/%{version}/neethi-%{version}-source-release.zip
BuildArch:     noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.ws.commons.axiom:axiom-api)
BuildRequires:  mvn(org.apache.ws.commons.axiom:axiom-dom)
BuildRequires:  mvn(org.apache.ws.commons.axiom:axiom-impl)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)

Requires:       axiom >= 1.2.14
Source44: import.info

Provides: ws-commons-%name = 0:%version-%release
Conflicts:  ws-commons-%name <= 0:3.0.1-alt2_6jpp7
Obsoletes:  ws-commons-%name <= 0:3.0.1-alt2_6jpp7


%description
Apache Neethi provides general framework for the programmers to
use WS Policy. It is compliant with latest WS Policy specification
which was published in March 2006. This framework is specifically
written to enable the Apache Web services stack to use WS Policy as
a way of expressing it's requirements and capabilities.

%package javadoc
Group: Development/Java
Summary:      API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

# These plugins are not needed for RPM builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt RELEASE-NOTE.txt
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_3jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_1jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_15jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_13jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_13jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_12jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_11jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_10jpp8
- java 8 mass update

