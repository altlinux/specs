Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           sisu
Summary:        Eclipse dependency injection framework
Epoch:          2
Version:        0.3.4
Release:        alt1_3jpp11
# sisu is EPL-1.0, the bundled asm is BSD
License:        EPL-1.0 and BSD

URL:            http://eclipse.org/sisu
Source0:        http://git.eclipse.org/c/sisu/org.eclipse.sisu.inject.git/snapshot/releases/%{version}.tar.gz#/org.eclipse.sisu.inject-%{version}.tar.gz
Source1:        http://git.eclipse.org/c/sisu/org.eclipse.sisu.plexus.git/snapshot/releases/%{version}.tar.gz#/org.eclipse.sisu.plexus-%{version}.tar.gz

Source100:      sisu-parent.pom
Source101:      sisu-inject.pom
Source102:      sisu-plexus.pom

Patch0:         sisu-OSGi-import-guava.patch
Patch2:         sisu-ignored-tests.patch
Patch3:         sisu-osgi-api.patch
Patch4:         0001-Remove-dependency-on-glassfish-servlet-api.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.inject.extensions:guice-servlet)
BuildRequires:  mvn(com.google.inject:guice::no_aop:)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.testng:testng)

Provides:       bundled(objectweb-asm)
Source44: import.info


%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package        inject
Group: Development/Java
Summary:        Sisu inject
Obsoletes:      %{name}-tests < 1:0.3.2-5

%description    inject
This package contains %{summary}.

%package        plexus
Group: Development/Java
Summary:        Sisu Plexus

%description    plexus
This package contains %{summary}.

%package        javadoc
Group: Development/Java
Summary:        API documentation for Sisu
BuildArch: noarch

%description    javadoc
This package contains %{summary}.

%prep
%setup -q -c -T
tar xf %{SOURCE0} && mv releases/* sisu-inject && rmdir releases
tar xf %{SOURCE1} && mv releases/* sisu-plexus && rmdir releases

cp %{SOURCE100} pom.xml
cp %{SOURCE101} sisu-inject/pom.xml
cp %{SOURCE102} sisu-plexus/pom.xml

%patch0
%patch2
%patch3
%patch4 -p1

%pom_remove_dep :servlet-api sisu-inject

%pom_xpath_set -r /pom:project/pom:version %{version}

%mvn_file ":{*}" @1
%mvn_package ":*{inject,plexus}" @1
%mvn_package : __noinstall
%mvn_alias :org.eclipse.sisu.plexus org.sonatype.sisu:sisu-inject-plexus

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files inject -f .mfiles-inject
%doc sisu-inject/LICENSE.txt

%files plexus -f .mfiles-plexus

%files javadoc -f .mfiles-javadoc
%doc sisu-inject/LICENSE.txt


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2:0.3.4-alt1_3jpp11
- new version

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 2:0.3.3-alt1_8jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2:0.3.3-alt1_7jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2:0.3.3-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.3.3-alt1_2jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2:0.3.2-alt1_7jpp8
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt1_6jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

