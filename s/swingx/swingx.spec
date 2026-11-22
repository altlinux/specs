%define _unpackaged_files_terminate_build 1
%global real_version 1.6.5-1

Name: swingx
Version: 1.6.5.1
Release: alt3

Summary: Extensions to the Java Swing GUI toolkit
License: LGPL-2.1-or-later
Group: Development/Java
URL: https://github.com/ebourg/swingx
VCS: https://github.com/ebourg/swingx

Source0: %name-project-%real_version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: fonts-ttf-dejavu
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.kohsuke.metainf-services:metainf-services)
BuildRequires: mvn(org.kohsuke:pom:pom:)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.jhlabs:filters)
BuildRequires: mvn(commons-lang:commons-lang)

BuildArch: noarch

%description
SwingX provides extensions to the Swing GUI toolkit, including new and enhanced
components commonly required for rich client applications.

%package common
Summary: Common SwingX APIs and utilities
Group: Development/Java

%description common
Common SwingX APIs and utilities.

%package autocomplete
Summary: Auto-completion support for Swing components
Group: Development/Java

%description autocomplete
Auto-completion support for Swing components.

%package action
Summary: Action and action-manager support for Swing
Group: Development/Java

%description action
Action and action-manager support for Swing.

%package painters
Summary: Painting APIs and painters
Group: Development/Java

%description painters
Painting APIs and painters.

%package graphics
Summary: Graphics and image utilities for Swing
Group: Development/Java

%description graphics
Graphics and image utilities for Swing.

%package plaf
Summary: Pluggable look-and-feel extensions
Group: Development/Java

%description plaf
Pluggable look-and-feel extensions.

%package all
Summary: Upstream aggregate SwingX library
Group: Development/Java

%description all
Upstream aggregate SwingX library.

%package beaninfo
Summary: JavaBeans metadata for SwingX components
Group: Development/Java

%description beaninfo
JavaBeans metadata for SwingX components.

%package javadoc
Summary: Javadocs for %name
Group: Development/Java

%description javadoc
This package contains the API documentation for %name.

%prep
%setup -q -n swingx-project-%real_version
%patch0 -p1

%mvn_package :swingx-project swingx
%mvn_package :swingx-mavensupport __noinstall
%mvn_package :swingx-testsupport __noinstall
%mvn_package :swingx-common common
%mvn_package :swingx-autocomplete autocomplete
%mvn_package :swingx-action action
%mvn_package :swingx-painters painters
%mvn_package :swingx-graphics graphics
%mvn_package :swingx-plaf plaf
%mvn_package :swingx-core swingx
%mvn_package :swingx-all all
%mvn_package :swingx-beaninfo beaninfo

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-swingx
%doc COPYING

%files common -f .mfiles-common

%files autocomplete -f .mfiles-autocomplete

%files action -f .mfiles-action

%files painters -f .mfiles-painters

%files graphics -f .mfiles-graphics

%files plaf -f .mfiles-plaf

%files all -f .mfiles-all

%files beaninfo -f .mfiles-beaninfo

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.6.5.1-alt3
- Restore SwingX in Sisyphus with system Maven dependencies.

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.6.5.1-alt2_14jpp8
- fc update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.5.1-alt2_13jpp8
- build with new mockito

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.5.1-alt2_11jpp8
- new version

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.5.1-alt2_9jpp8
- java update

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.5.1-alt2_8jpp8
- fixed build

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.5.1-alt2_6jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.5.1-alt2_5jpp8
- java 8 mass update

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.5.1-alt1_5jpp8
- java 8 mass update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt5_0jpp6
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt4_0jpp6
- depmap cleanup

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt3_0jpp6
- migration to mvn-rpmbuild

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt2_0jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Feb 28 2013 Paul Wolneykien <manowar@altlinux.ru> 1.6.5-alt1_0jpp6
- Install all target JARs.
- Add "metainf-services" and "mockito" to the set of build requisites.
- Remove the unused POM patch
- Fresh up to v1.6.5.

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt4_1jpp6
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_1jpp6
- build without emma-plugin

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_1jpp6
- new version

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_7jpp6
- new version
