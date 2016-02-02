Name: antlr4-maven-plugin
Version: 4.5
Summary: ANTLR plugin for Apache Maven
License: BSD
Url: http://www.antlr.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: antlr4-maven-plugin = 4.5-4.fc23
Provides: mvn(org.antlr:antlr4-maven-plugin) = 4.5
Provides: mvn(org.antlr:antlr4-maven-plugin:pom:) = 4.5
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.antlr:antlr4)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-compiler-api)
Requires: mvn(org.sonatype.plexus:plexus-build-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: antlr4-maven-plugin-4.5-4.fc23.cpio

%description
This package provides plugin for Apache Maven which can be used to
generate ANTLR parsers during build.

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
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 4.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

