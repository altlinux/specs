Name: maven-reporting-exec
Version: 1.2
Summary: Classes to manage report plugin executions with Maven 3
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-reporting-exec/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-reporting-exec = 1.2-3.fc23
Provides: mvn(org.apache.maven.reporting:maven-reporting-exec) = 1.2
Provides: mvn(org.apache.maven.reporting:maven-reporting-exec:pom:) = 1.2
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-settings)
Requires: mvn(org.apache.maven:maven-settings-builder)
Requires: mvn(org.eclipse.aether:aether-util)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-reporting-exec-1.2-3.fc23.cpio

%description
Classes to manage report plugin executions with Maven 3. Contains classes for
managing and configuring reports and their execution.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_2jpp7
- rebuild with maven-local

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new release

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

