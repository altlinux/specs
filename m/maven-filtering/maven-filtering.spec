Name: maven-filtering
Version: 1.3
Summary: Shared component providing resource filtering
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-filtering/index.html
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-filtering = 1.3-2.fc23
Provides: maven-shared-filtering = 1.0-99
Provides: mvn(org.apache.maven.shared:maven-filtering) = 1.3
Provides: mvn(org.apache.maven.shared:maven-filtering:pom:) = 1.3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model:2.2.1)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.maven:maven-settings:2.2.1)
Requires: mvn(org.codehaus.plexus:plexus-interpolation)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.sonatype.plexus:plexus-build-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-filtering-1.3-2.fc23.cpio

%description
These Plexus components have been built from the filtering process/code in
Maven Resources Plugin. The goal is to provide a shared component for all
plugins that needs to filter resources.

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

