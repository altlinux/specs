Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-filtering
Version:        3.2.0
Release:        alt1_1jpp11
Summary:        Shared component providing resource filtering
License:        ASL 2.0

URL:            https://maven.apache.org/shared/%{name}/index.html
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
Source44: import.info

%description
These Plexus components have been built from the filtering process/code in 
Maven Resources Plugin. The goal is to provide a shared component for all 
plugins that needs to filter resources.


%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q


%build
# Tests use a package that is no longer present in plexus-build-api (v0.0.7)
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_9jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_7jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_3jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_2jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_2jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_9jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp7
- new release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8jpp7
- full build

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

