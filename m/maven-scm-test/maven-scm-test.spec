Name: maven-scm-test
Version: 1.9.4
Summary: Tests for maven-scm
License: ASL 2.0
Url: http://maven.apache.org/scm
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-scm-test = 1.9.4-3.fc23
Provides: mvn(org.apache.maven.scm:maven-scm-provider-cvstest) = 1.9.4
Provides: mvn(org.apache.maven.scm:maven-scm-provider-cvstest:pom:) = 1.9.4
Provides: mvn(org.apache.maven.scm:maven-scm-provider-gittest) = 1.9.4
Provides: mvn(org.apache.maven.scm:maven-scm-provider-gittest:pom:) = 1.9.4
Provides: mvn(org.apache.maven.scm:maven-scm-provider-svntest) = 1.9.4
Provides: mvn(org.apache.maven.scm:maven-scm-provider-svntest:pom:) = 1.9.4
Provides: mvn(org.apache.maven.scm:maven-scm-test) = 1.9.4
Provides: mvn(org.apache.maven.scm:maven-scm-test:pom:) = 1.9.4
Requires: java-headless
Requires: jpackage-utils
Requires: maven-scm
Requires: mvn(junit:junit)
Requires: mvn(org.apache.maven.scm:maven-scm-api)
Requires: mvn(org.apache.maven.scm:maven-scm-manager-plexus)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-git-commons)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.sonatype.plexus:plexus-sec-dispatcher)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-scm-test-1.9.4-3.fc23.cpio

%description
Tests for maven-scm.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

