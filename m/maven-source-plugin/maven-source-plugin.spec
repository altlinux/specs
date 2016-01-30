Name: maven-source-plugin
Version: 2.4
Summary: Plugin creating source JAR
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-source-plugin/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-source-plugin = 2.4-3.fc23
Provides: mvn(org.apache.maven.plugins:maven-source-plugin) = 2.4
Provides: mvn(org.apache.maven.plugins:maven-source-plugin:pom:) = 2.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven:maven-archiver)
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-model:2.2.1)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.codehaus.plexus:plexus-archiver)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-source-plugin-2.4-3.fc23.cpio

%description
The Maven Source Plugin creates a JAR archive of the
source files of the current project.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_5jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt3_8jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt2_8jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_8jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_7jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

