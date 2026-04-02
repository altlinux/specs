Name:           plexus-i18n
Version:        1.1.0
Release:        alt1.1

Summary:        Plexus I18N Component
License:        Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-i18n/
VCS:            https://github.com/codehaus-plexus/plexus-i18n

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)

BuildArch:      noarch

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%javadoc_package

%prep
%setup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1.1.0-alt1.1
- Cosmetic fixes.

* Wed Feb 18 2026 Evegeniy Serov <scala@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:1.0-alt7_0.23.b10.4jpp11
- java11 build

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.15.b10.4jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.13.b10.4jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.11.b10.4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.10.b10.4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.9.b10.4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.8.b10.4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.7.b10.4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.b10.2.5jpp7
- rebuild with maven-local

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.b10.2.5jpp7
- new fc release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.2.5jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.2.2jpp7
- fc version

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.1jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b6.5jpp5
- new jpackage release

* Sun Nov 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b6.5jpp1.7
- build with maven2

* Tue Oct 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b6.5jpp1.7
- bootstrap build for maven2

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b6.5jpp1.7
- updated to new jpackage release

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b6.4jpp1.7
- converted from JPackage by jppimport script

