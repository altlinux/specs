Name: maven-verifier
Version: 1.4
Summary: Maven verifier
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-verifier
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-verifier
Provides: mvn(org.apache.maven.shared:maven-verifier)
Requires: java
Requires: jpackage-utils
Requires: mvn(junit:junit)
Requires: mvn(org.apache.maven.shared:maven-shared-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-verifier-1.4-3.fc19.cpio

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
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

