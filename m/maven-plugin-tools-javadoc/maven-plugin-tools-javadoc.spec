Name: maven-plugin-tools-javadoc
Version: 3.4
Summary: Maven Plugin Tools Javadoc
License: ASL 2.0
Url: http://maven.apache.org/plugin-tools/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-plugin-tools-javadoc = 0:3.4-3.fc23
Provides: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-javadoc) = 3.4
Provides: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-javadoc:pom:) = 3.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.sun:tools)
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-java)
Requires: mvn(org.apache.maven:maven-compat)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-tools-javadoc-3.4-3.fc23.cpio

%description
The Maven Plugin Tools Javadoc provides several Javadoc taglets to be used when
generating Javadoc.

Java API documentation for maven-plugin-tools is contained in
maven-plugin-tools-javadocs package. This package does not contain it.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

