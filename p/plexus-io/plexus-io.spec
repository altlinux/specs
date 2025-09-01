%define _unpackaged_files_terminate_build 1

Name: plexus-io
Version: 3.5.1
Release: alt2

Summary: Plexus IO Components
License: Apache-2.0
Group: Development/Java
Url: https://github.com/codehaus-plexus/plexus-io
VCS: https://github.com/codehaus-plexus/plexus-io.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(com.google.inject:guice)

%description
Plexus IO is a set of plexus components, which are designed for use
in I/O operations.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
API documentation for %name.

%prep
%setup

%build
%mvn_file  : plexus/plexus-io plexus/io

%mvn_build -f -- -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=8 \
  #

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference NOTICE.txt

%changelog
* Tue Aug 26 2025 Anton Meleshnikov <alton@altlinux.org> 3.5.1-alt2
- NMU: Added necessary BuildRequires.

* Fri Aug 15 2025 Ivan Khanas <xeno@altlinux.org> 3.5.1-alt1
- New version.
- Rename artifact.

* Thu Jul 07 2022 Igor Vlasenko <viy@altlinux.org> 0:3.2.0-alt1_9jpp11
- fixed build

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.0-alt1_7jpp11
- update

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.0-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_4jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_2jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_6jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

