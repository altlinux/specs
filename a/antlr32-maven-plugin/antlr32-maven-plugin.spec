Name: antlr32-maven-plugin
Version: 3.2
Summary: Maven plug-in for creating ANTLR-generated parsers
License: BSD
Url: http://www.antlr3.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: antlr32-maven-plugin = 3.2-9.fc23
Provides: mvn(org.antlr:antlr3-maven-plugin:3.1.3-1) = 3.2
Provides: mvn(org.antlr:antlr3-maven-plugin:3.2) = 3.2
Provides: mvn(org.antlr:antlr3-maven-plugin:pom:3.1.3-1) = 3.2
Provides: mvn(org.antlr:antlr3-maven-plugin:pom:3.2) = 3.2
Requires: antlr32-tool
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.antlr:antlr:3.2)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.codehaus.plexus:plexus-compiler-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: antlr32-maven-plugin-3.2-9.fc23.cpio

%description
Maven plug-in for creating ANTLR-generated parsers.

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
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

