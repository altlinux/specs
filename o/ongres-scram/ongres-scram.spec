Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global		upstream_name    scram
%global		upstream_version 1.0.0-beta.2

Name:		ongres-%upstream_name
Version:	%(echo %upstream_version | sed 's/-/_/g')
Release:	alt1_6jpp8
Summary:	Salted Challenge Response Authentication Mechanism (SCRAM) - Java Implementation
License:	BSD
URL:		https://github.com/ongres/%upstream_name
Source0:	https://github.com/ongres/%upstream_name/archive/%upstream_version/%upstream_name-%upstream_version.tar.gz
BuildRequires:	maven-local
BuildArch:	noarch
Source44: import.info

%description
This is a Java implementation of SCRAM (Salted Challenge Response
Authentication Mechanism) which is part of the family of Simple
Authentication and Security Layer (SASL, RFC 4422) authentication
mechanisms. It is described as part of RFC 5802 and RFC7677.

%package client
Group: Development/Java
Summary:	Client for %{name}

%description client
This package contains the client for %{name}

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}

%package parent
Group: Development/Java
Summary:	Parent POM of %{name}

%description parent
This package contains the %{name} parent POM.

%prep
%setup -q -n %upstream_name-%upstream_version

find \( -name '*.jar' -o -name '*.class' \) -delete
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin client
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-common
%doc --no-dereference LICENSE

%files client -f .mfiles-client
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%files parent -f .mfiles-parent
%doc --no-dereference LICENSE

%changelog
* Tue Jan 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0_beta.2-alt1_6jpp8
- java update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0~beta.2-alt1_5jpp8
- java fc28+ update

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0~beta.2-alt1_1jpp8
- java fc28 update

