Name: maven-surefire
Version: 2.18.1
Summary: Test framework project
License: ASL 2.0 and CPL
Url: http://maven.apache.org/surefire/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-surefire = 0:2.18.1-2.fc23
Provides: mvn(org.apache.maven.surefire:common-java5) = 2.18.1
Provides: mvn(org.apache.maven.surefire:common-java5:pom:) = 2.18.1
Provides: mvn(org.apache.maven.surefire:maven-surefire-common) = 2.18.1
Provides: mvn(org.apache.maven.surefire:maven-surefire-common:pom:) = 2.18.1
Provides: mvn(org.apache.maven.surefire:surefire-api) = 2.18.1
Provides: mvn(org.apache.maven.surefire:surefire-api:pom:) = 2.18.1
Provides: mvn(org.apache.maven.surefire:surefire-booter) = 2.18.1
Provides: mvn(org.apache.maven.surefire:surefire-booter:pom:) = 2.18.1
Provides: mvn(org.apache.maven.surefire:surefire-grouper) = 2.18.1
Provides: mvn(org.apache.maven.surefire:surefire-grouper:pom:) = 2.18.1
Provides: mvn(org.apache.maven.surefire:surefire-providers:pom:) = 2.18.1
Provides: mvn(org.apache.maven.surefire:surefire:pom:) = 2.18.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-io:commons-io)
Requires: mvn(org.apache.commons:commons-lang3)
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
Requires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model:2.2.1)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-plugin-descriptor)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.maven:maven-toolchain)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-surefire-2.18.1-2.fc23.cpio

%description
Surefire is a test framework project.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.18.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.16-alt1_1jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.14-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt2_2jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt1_2jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt2_5jpp7
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt1_5jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

