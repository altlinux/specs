Name:           plexus-resources
Version:        1.3.1
Release:        alt1.1

Summary:        Plexus Resource Manager
License:        Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-resources/
VCS:            https://github.com/codehaus-plexus/plexus-resources

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(org.mockito:mockito-core)
# TODO: switch to mvn() prov, after fixing mockito bug
BuildRequires:  osgi(org.mockito.junit-jupiter)
BuildRequires:  mvn(org.simplify4u:slf4j-mock)

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
%doc *.md LICENSE

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 1.3.1-alt1.1
- Cosmetic fixes.

* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:1.2.0-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.1.0-alt1_7jpp11
- update

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:1.1.0-alt1_4jpp11
- fixed build

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.1.0-alt1_2jpp11
- new version

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.26.a7jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.25.a7jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.23.a7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.22.a7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.21.a7jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.20.a7jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.19.a7jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.14.a7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.13.a7jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.9.a7jpp7
- rebuild with maven-local

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.9.a7jpp7
- new fc release

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.8.a7jpp7
- fixed plexus component generation

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.8.a7jpp7
- fc version

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.1.a4.4jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.1.a4.4jpp6
- rebuild w/new maven2; disabled tests

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a3.1jpp1.7
- converted from JPackage by jppimport script

