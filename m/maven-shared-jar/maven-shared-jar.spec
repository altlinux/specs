Name: maven-shared-jar
Version: 1.1
Summary: Maven JAR Utilities
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-shared-jar
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.maven.shared:maven-shared-jar)
Requires: apache-commons-collections
Requires: bcel
Requires: java
Requires: jpackage-utils
Requires: maven
Requires: plexus-digest

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-shared-jar-1.1-2.fc19.cpio

%description
Utilities that help identify the contents of a JAR, including Java class
analysis and Maven metadata analysis.

This is a replacement package for maven-shared-jar

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
* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

