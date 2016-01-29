Name: maven-archiver
Version: 2.6
Summary: Maven Archiver
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-archiver/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-archiver = 0:2.6-2.fc23
Provides: maven-shared-archiver = 2.6-2.fc23
Provides: mvn(org.apache.maven:maven-archiver) = 2.6
Provides: mvn(org.apache.maven:maven-archiver:pom:) = 2.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model:2.2.1)
Requires: mvn(org.codehaus.plexus:plexus-archiver)
Requires: mvn(org.codehaus.plexus:plexus-interpolation)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-archiver-2.6-2.fc23.cpio

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_3jpp7
- rebuild with maven-local

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_3jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

