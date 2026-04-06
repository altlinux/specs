Name:		ongres-scram
Version:	3.2
Release:	alt1

Summary:	SCRAM (RFC 5802) Java implementation
License:	BSD-2-Clause
Group:          Development/Java
URL:            https://github.com/ongres/scram
VCS:            https://github.com/ongres/scram

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(com.ongres.stringprep:saslprep)
BuildRequires:  mvn(org.jetbrains:annotations)

BuildArch:	noarch

%description
SCRAM (Salted Challenge Response Authentication Mechanism) is part of the
family of Simple Authentication and Security Layer (SASL, RFC 4422)
authentication mechanisms. It is described as part of RFC 5802 and RFC 7677.

This project provides a robust and well-tested implementation of the Salted
Challenge Response Authentication Mechanism (SCRAM) in Java. It adheres to the
specifications outlined in RFC 5802 and RFC 7677, ensuring secure user
authentication.

This SCRAM Java implementation can be used for PostgreSQL (which supports SASL
authentication since PostgreSQL 10) through the PostgreSQL JDBC Driver and
others projects that connect from Java.

%javadoc_package

%package        client
Group:          Development/Java
Summary:	Client for %name

%description    client
This package contains the client for %name

%package        parent
Group:          Development/Java
Summary:        Parent POM of %name

%description    parent
This package contains the %name parent POM.

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin scram-parent

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive' '
<manifestEntries>
  <Multi-Release>true</Multi-Release>
</manifestEntries>
' scram-parent

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-scram-common
%doc LICENSE *.md

%files client -f .mfiles-scram-client
%doc LICENSE *.md

%files parent -f .mfiles-scram-parent
%doc LICENSE *.md

%changelog
* Sat Mar 21 2026 Evgeniy Serov <scala@altlinux.org> 3.2-alt1
- Fixed FTBFS.
- Updated to 3.2.

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

