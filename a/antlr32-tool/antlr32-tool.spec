Name: antlr32-tool
Version: 3.2
Summary: Command line tool for creating ANTLR-generated parsers
License: BSD
Url: http://www.antlr3.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: antlr32-tool = 3.2-9.fc23
Provides: mvn(org.antlr:antlr:3.1.3) = 3.2
Provides: mvn(org.antlr:antlr:3.2) = 3.2
Provides: mvn(org.antlr:antlr:pom:3.1.3) = 3.2
Provides: mvn(org.antlr:antlr:pom:3.2) = 3.2
Requires: antlr32-java
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.antlr:antlr-runtime:3.2)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: antlr32-tool-3.2-9.fc23.cpio

%description
Command line tool for creating ANTLR-generated parsers.

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

