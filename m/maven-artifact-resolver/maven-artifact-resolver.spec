Name: maven-artifact-resolver
Version: 1.0
Summary: Maven Artifact Resolution API
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-artifact-resolver
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-artifact-resolver = 1:1.0-13.fc23
Provides: maven-shared-artifact-resolver = 1:1.0-13.fc23
Provides: mvn(org.apache.maven.shared:maven-artifact-resolver) = 1.0
Provides: mvn(org.apache.maven.shared:maven-artifact-resolver:pom:) = 1.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven:maven-compat)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: maven-artifact-resolver-1.0-13.fc23.cpio

%description
Provides a component for plugins to easily resolve project dependencies.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_7jpp7
- new release

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_4jpp7
- update

