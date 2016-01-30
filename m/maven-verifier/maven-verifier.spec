Name: maven-verifier
Version: 1.6
Summary: Maven verifier
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-verifier
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-verifier = 1.6-1.fc23
Provides: maven-verifier = 1.6-1.fc23
Provides: mvn(org.apache.maven.shared:maven-verifier) = 1.6
Provides: mvn(org.apache.maven.shared:maven-verifier:pom:) = 1.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(junit:junit)
Requires: mvn(org.apache.maven.shared:maven-shared-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-verifier-1.6-1.fc23.cpio

%description
Provides a test harness for Maven integration tests.

This is a replacement package for maven-shared-verifier

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

