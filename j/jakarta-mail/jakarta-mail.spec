Name:           jakarta-mail
Version:        2.1.5
Release:        alt1.1

Summary:        Jakarta Mail API
License:        EPL-2.0 or GPLv2 with exceptions
Group:          Development/Java
URL:            https://jakartaee.github.io/mail-api/
VCS:            https://github.com/eclipse-ee4j/mail

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch:      noarch

%description
The Jakarta Mail API provides a platform-independent and
protocol-independent framework to build mail and messaging applications.

%javadoc_package

%prep
%setup -n %name-%version/api

%pom_remove_parent
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_dep :angus-activation

%mvn_file :jakarta.mail-api jakarta-mail/jakarta.mail jakarta-mail

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ../LICENSE.md ../NOTICE.md
%doc ../README.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.1.5-alt1.1
- Cosmetic fixes.

* Tue Jan 27 2026 Evgeniy Serov <scala@altlinux.org> 2.1.5-alt1
- Updated to 2.1.5.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.6.7-alt1_3jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.6.5-alt1_8jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.6.5-alt1_4jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.6.5-alt1_2jpp11
- new version

