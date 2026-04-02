Name:           jakarta-activation
Version:        2.1.4
Release:        alt1.1

Summary:        Jakarta Activation Specification project
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://jakartaee.github.io/jaf-api/
VCS:            https://github.com/jakartaee/jaf-api

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch:      noarch

%description
Jakarta Activation lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to
it; discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%javadoc_package

%prep
%setup -n %name-%version/api

%pom_remove_parent
%pom_remove_plugin :buildnumber-maven-plugin

%mvn_alias jakarta.activation:jakarta.activation-api com.sun.activation:jakarta.activation
%mvn_file jakarta.activation:jakarta.activation-api jakarta-activation/jakarta.activation jakarta-activation
%mvn_file jakarta.activation:jakarta.activation-api jakarta-activation/jakarta.activation-api jakarta-activation

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ../*.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.1.4-alt1.1
- Cosmetic fixes.

* Fri Jan 16 2026 Evgeniy Serov <scala@altlinux.org> 2.1.4-alt1
- Updated to 2.1.4.
- Removed import.info.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.2.2-alt1_4jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.2.2-alt1_1jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt2_5jpp11
- fixed build

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt1_5jpp11
- new version

