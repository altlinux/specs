Name: tesla-polyglot-atom
Version: 0.1.8
Summary: Polyglot Tesla :: Atom
License: EPL
Url: https://github.com/takari/maven-polyglot
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(io.takari.polyglot:polyglot-atom) = 0.1.8
Provides: mvn(io.takari.polyglot:polyglot-atom:pom:) = 0.1.8
Provides: mvn(io.tesla.polyglot:tesla-polyglot-atom) = 0.1.8
Provides: mvn(io.tesla.polyglot:tesla-polyglot-atom:pom:) = 0.1.8
Provides: mvn(org.sonatype.pmaven:pmaven-atom) = 0.1.8
Provides: mvn(org.sonatype.pmaven:pmaven-atom:pom:) = 0.1.8
Provides: tesla-polyglot-atom = 0.1.8-4.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(io.takari.polyglot:polyglot-common)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tesla-polyglot-atom-0.1.8-4.fc23.cpio

%description
Polyglot Tesla :: Atom.

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

