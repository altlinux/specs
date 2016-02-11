Name: avro-maven-plugin
Version: 1.7.5
Summary: Apache Avro Maven Plugin
License: ASL 2.0
Url: http://avro.apache.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: avro-maven-plugin = 1.7.5-12.fc23
Provides: mvn(org.apache.avro:avro-maven-plugin) = 1.7.5
Provides: mvn(org.apache.avro:avro-maven-plugin:pom:) = 1.7.5
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.avro:avro-compiler)
Requires: mvn(org.apache.maven.shared:file-management)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: avro-maven-plugin-1.7.5-12.fc23.cpio

%description
Avro Maven plugin for Avro IDL and Specific API Compilers

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
* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

