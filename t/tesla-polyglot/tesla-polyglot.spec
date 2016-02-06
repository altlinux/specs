Name: tesla-polyglot
Version: 0.1.8
Summary: Modules to enable Maven usage in other JVM languages
License: EPL
Url: https://github.com/takari/maven-polyglot
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(io.takari.polyglot:polyglot:pom:) = 0.1.8
Provides: tesla-polyglot = 0.1.8-4.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.plexus:plexus-component-metadata)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tesla-polyglot-0.1.8-4.fc23.cpio

%description
Polyglot for Maven is an experimental distribution of Maven
that allows the expression of a POM in something other than
XML. A couple of the dialects also have the capability to
write plugins inline: the Groovy, Ruby and Scala dialects
allow this.

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

