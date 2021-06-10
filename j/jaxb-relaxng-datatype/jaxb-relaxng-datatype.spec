
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: jaxb-relaxng-datatype
Version: 2.3.3
Summary: RelaxNG Datatype
License: BSD
Url: https://github.com/eclipse-ee4j/jaxb-ri
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.org>
Provides: mvn(com.github.relaxng:relaxngDatatype) = 2.3.3
Provides: mvn(com.github.relaxng:relaxngDatatype:pom:) = 2.3.3
Provides: mvn(com.sun.xml.bind.external:relaxng-datatype) = 2.3.3
Provides: mvn(com.sun.xml.bind.external:relaxng-datatype:pom:) = 2.3.3
Provides: mvn(relaxngDatatype:relaxngDatatype) = 2.3.3
Provides: mvn(relaxngDatatype:relaxngDatatype:pom:) = 2.3.3
Provides: osgi(com.sun.xml.bind.external.relaxng-datatype) = 2.3.3
Provides: relaxngDatatype = 1:2.3.3-6.fc34
Provides: relaxngDatatype-javadoc = 1:2.3.3-6.fc34
Requires: java-headless
Requires: javapackages-filesystem

BuildArch: noarch
Source: jaxb-relaxng-datatype-2.3.3-6.fc34.cpio


%description
RelaxNG Datatype library.

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
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

