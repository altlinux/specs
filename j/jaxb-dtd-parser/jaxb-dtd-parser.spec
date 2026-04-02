Name:           jaxb-dtd-parser
Version:        1.5.1
Release:        alt1.1

Summary:        SAX-like API for parsing XML DTDs
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
VCS:            https://github.com/eclipse-ee4j/jaxb-dtd-parser

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:      noarch

%description
SAX-like API for parsing XML DTDs.

%javadoc_package

%prep
%setup -n %name-%version/dtd-parser

%pom_remove_parent
%pom_remove_plugin :buildnumber-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ../LICENSE.md ../NOTICE.md
%doc ../README.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1.5.1-alt1.1
- Cosmetic fixes.

* Thu Jan 15 2026 Evgeniy Serov <scala@altlinux.org> 1.5.1-alt1
- Updated to 1.5.1.
- Removed import.info.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_3jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.4.5-alt1_3jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.4.3-alt1_4jpp11
- new version

