
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: jaxb-xjc
Version: 2.3.3
Summary: JAXB XJC
License: BSD
Url: https://github.com/eclipse-ee4j/jaxb-ri
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.org>
Provides: glassfish-jaxb-xjc = 2.3.3-6.fc34
Provides: mvn(com.sun.xml.bind:jaxb-xjc) = 2.3.3
Provides: mvn(com.sun.xml.bind:jaxb-xjc:pom:) = 2.3.3
Provides: mvn(org.glassfish.jaxb:jaxb-xjc) = 2.3.3
Provides: mvn(org.glassfish.jaxb:jaxb-xjc:pom:) = 2.3.3
Requires: java-headless
Requires: javapackages-filesystem
Requires: mvn(com.sun.istack:istack-commons-runtime)
Requires: mvn(com.sun.istack:istack-commons-tools)
Requires: mvn(com.sun.xml.bind.external:rngom)
Requires: mvn(com.sun.xml.dtd-parser:dtd-parser)
Requires: mvn(org.glassfish.jaxb:codemodel)
Requires: mvn(org.glassfish.jaxb:jaxb-runtime)
Requires: mvn(org.glassfish.jaxb:xsom)

BuildArch: noarch
Source: jaxb-xjc-2.3.3-6.fc34.cpio


%description
JAXB Binding Compiler. Contains source code needed for binding
customization files into java sources. In other words: the tool to
generate java classes for the given xml representation.

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

