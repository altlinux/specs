Name:           plexus-velocity
Version:        2.3.0
Release:        alt1

Summary:        Plexus Velocity Component
License:        Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-velocity/
VCS:            https://github.com/codehaus-plexus/plexus-velocity
BuildArch:      noarch

Source:	        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.apache.velocity:velocity-engine-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)

%description
This package provides Plexus Velocity component - a wrapper for
Apache Velocity template engine, which allows easy use of Velocity
by applications built on top of Plexus container.

%javadoc_package

%prep
%setup

%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md LICENSE

%changelog
* Thu Mar 19 2026 Evgeniy Serov <scala@altlinux.org> 2.3.0-alt1
- Updated to 2.3.0.

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_11jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_8jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_6jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt4_21jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt4_19jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_14jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt2_11jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_11jpp7
- fc update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_10jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_9jpp7
- fc version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt3_1jpp5
- explicit selection of java5 compiler

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt2_1jpp5
- fixed build with maven 2.0.7

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_3jpp1.7
- build with maven2

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

