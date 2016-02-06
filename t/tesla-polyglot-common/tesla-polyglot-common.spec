Name: tesla-polyglot-common
Version: 0.1.8
Summary: Polyglot Tesla :: Common
License: EPL
Url: https://github.com/takari/maven-polyglot
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(io.takari.polyglot:polyglot-common) = 0.1.8
Provides: mvn(io.takari.polyglot:polyglot-common:pom:) = 0.1.8
Provides: mvn(io.tesla.polyglot:tesla-polyglot-common) = 0.1.8
Provides: mvn(io.tesla.polyglot:tesla-polyglot-common:pom:) = 0.1.8
Provides: mvn(org.sonatype.pmaven:pmaven-common) = 0.1.8
Provides: mvn(org.sonatype.pmaven:pmaven-common:pom:) = 0.1.8
Provides: tesla-polyglot-common = 0.1.8-4.fc23
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tesla-polyglot-common-0.1.8-4.fc23.cpio

%description
Polyglot Tesla :: Common.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

