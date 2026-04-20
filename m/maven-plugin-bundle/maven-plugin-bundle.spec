Name:           maven-plugin-bundle
Version:        5.1.9
Release:        alt2

Summary:        Maven Bundle Plugin
License:        Apache-2.0
Group:          Development/Java
URL:            https://felix.apache.org

Source0:        maven-bundle-plugin-%version-source-release.tar.gz

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.jdom:jdom)

BuildArch:      noarch

%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%javadoc_package

%prep
%setup -n maven-bundle-plugin-%version

find -name '*.jar' -delete

%pom_remove_dep :org.apache.felix.bundlerepository
rm -rf src/main/java/org/apache/felix/obrplugin/

# doxia updated to 2.0.0
rm -f src/main/java/org/apache/felix/bundleplugin/baseline/BaselineReport.java

%build
# Tests disabled due to outdated expectations and missing test resources causing failures
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Tue Apr 14 2026 Evgeniy Serov <scala@altlinux.org> 5.1.9-alt2
- Fixed FTBFS.

* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 5.1.9-alt1.1
- Cosmetic fixes.

* Tue Jan 13 2026 Evgeniy Serov <scala@altlinux.org> 5.1.9-alt1
- Updated to 5.1.9.
- Removed import.info.

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 5.1.1-alt1_3jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 4.2.1-alt1_3jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_4jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_2jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 3.5.0-alt1_1jpp8
- java update

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_2jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_4jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_1jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt1_1jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt3_10jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_4jpp7
- new version

* Mon Sep 05 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_12jpp6
- fixed buildrequires

* Fri Oct 15 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_4jpp6
- new version

