Provides: /etc/java/antlr4.conf
Name: antlr4
Version: 4.5
Summary: Java parser generator
License: BSD
Url: http://www.antlr.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: antlr4 = 4.5-4.fc23
Provides: mvn(org.antlr:antlr4) = 4.5
Provides: mvn(org.antlr:antlr4:pom:) = 4.5
Requires: /bin/bash
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.antlr:ST4)
Requires: mvn(org.antlr:antlr-runtime)
Requires: mvn(org.antlr:antlr4-runtime)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: antlr4-4.5-4.fc23.cpio

%description
ANTLR (ANother Tool for Language Recognition) is a powerful parser
generator for reading, processing, executing, or translating
structured text or binary files.  It's widely used to build languages,
tools, and frameworks. From a grammar, ANTLR generates a parser that
can build and walk parse trees.

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

