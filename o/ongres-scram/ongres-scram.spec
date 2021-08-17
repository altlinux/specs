Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global		upstream_name    scram
%global		upstream_version 2.1

Name:		ongres-%upstream_name
Version:	%(echo %upstream_version | sed 's/-/~/g')
Release:	alt1_3jpp11
Summary:	Salted Challenge Response Authentication Mechanism (SCRAM) - Java Implementation
License:	BSD
URL:           https://github.com/ongres/%upstream_name
Source0:       https://github.com/ongres/%upstream_name/archive/%upstream_version/%upstream_name-%upstream_version.tar.gz
BuildRequires:	maven-local
BuildRequires:  ongres-stringprep
BuildRequires:  junit
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

# Retired in Fedora; not required for build
%pom_remove_dep com.google.code.findbugs:annotations
sed -i 's/.*SuppressFBWarnings.*//' common/src/main/java/com/ongres/scram/common/message/ServerFinalMessage.java

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

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
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 2.1-alt1_3jpp11
- new version

* Fri Jul 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0_beta.2-alt1_7jpp8
- fc update & java 8 build

* Tue Jan 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0_beta.2-alt1_6jpp8
- java update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0~beta.2-alt1_5jpp8
- java fc28+ update

* Wed May 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0~beta.2-alt1_1jpp8
- java fc28 update

