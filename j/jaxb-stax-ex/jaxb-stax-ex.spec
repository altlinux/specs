Name:           jaxb-stax-ex
Version:        2.1.0
Release:        alt1.1

Summary:        Extended StAX API
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://github.com/eclipse-ee4j/jaxb-stax-ex
VCS:            https://github.com/eclipse-ee4j/jaxb-stax-ex

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)

BuildArch:      noarch

%description
This project contains a few extensions to complement JSR-173 StAX API in
the following areas:

- Enable parser instance reuse (which is important in the
  high-performance environment like Eclipse Implementation of JAXB and
  Eclipse Metro)
- Improve the support for reading from non-text XML infoset, such as
  FastInfoset.
- Improve the namespace support.

%javadoc_package

%prep
%setup

%pom_remove_parent
%pom_remove_plugin :buildnumber-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md
%doc README.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.1.0-alt1.1
- Cosmetic fixes.

* Thu Jan 15 2026 Evgeniy Serov <scala@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.
- Removed import.info.

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 1.8.3-alt1_8jpp11
- update

* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 1.8.3-alt1_4jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.8.3-alt1_2jpp11
- new version

