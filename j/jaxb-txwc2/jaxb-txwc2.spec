
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: jaxb-txwc2
Version: 2.3.3
Summary: TXW2 Compiler
License: BSD
Url: https://github.com/eclipse-ee4j/jaxb-ri
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.org>
Provides: glassfish-jaxb-txwc2 = 2.3.3-6.fc34
Provides: mvn(org.glassfish.jaxb:txwc2) = 2.3.3
Provides: mvn(org.glassfish.jaxb:txwc2:pom:) = 2.3.3
Requires: java-headless
Requires: javapackages-filesystem
Requires: mvn(com.sun.xml.bind.external:rngom)
Requires: mvn(org.glassfish.jaxb:codemodel)
Requires: mvn(org.glassfish.jaxb:txw2)
Requires: mvn(org.glassfish.jaxb:xsom)

BuildArch: noarch
Source: jaxb-txwc2-2.3.3-6.fc34.cpio


%description
JAXB schema generator. The tool to generate XML schema based on java
classes.

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

