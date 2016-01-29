Name: maven-plugin-tools-beanshell
Version: 3.4
Summary: Maven Plugin Tool for Beanshell
License: ASL 2.0
Url: http://maven.apache.org/plugin-tools/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-plugin-tools-beanshell = 0:3.4-3.fc23
Provides: maven-shared-plugin-tools-beanshell = 0:3.4-3.fc23
Provides: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-beanshell) = 3.4
Provides: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-beanshell:pom:) = 3.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.beanshell:bsh)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-tools-beanshell-3.4-3.fc23.cpio

%description
Descriptor extractor for plugins written in Beanshell.

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

