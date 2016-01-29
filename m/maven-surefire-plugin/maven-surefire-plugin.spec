Name: maven-surefire-plugin
Version: 2.18.1
Summary: Surefire plugin for maven
License: ASL 2.0 and CPL
Url: http://maven.apache.org/surefire/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-surefire-plugin = 0:2.18.1-2.fc23
Provides: mvn(org.apache.maven.plugins:maven-surefire-plugin) = 2.18.1
Provides: mvn(org.apache.maven.plugins:maven-surefire-plugin:pom:) = 2.18.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
Requires: mvn(org.apache.maven.surefire:maven-surefire-common)
Requires: mvn(org.apache.maven.surefire:surefire-api)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-toolchain)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-surefire-plugin-2.18.1-2.fc23.cpio

%description
Maven surefire plugin for running tests via the surefire framework.

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

