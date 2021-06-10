
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: jaxb-xsom
Version: 2.3.3
Summary: XML Schema Object Model
License: BSD
Url: https://github.com/eclipse-ee4j/jaxb-ri
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.org>
Provides: mvn(com.sun.xsom:xsom) = 2.3.3
Provides: mvn(com.sun.xsom:xsom:pom:) = 2.3.3
Provides: mvn(org.glassfish.jaxb:xsom) = 2.3.3
Provides: mvn(org.glassfish.jaxb:xsom:pom:) = 2.3.3
Provides: osgi(org.glassfish.jaxb.xsom) = 2.3.3
Provides: xsom = 2.3.3-6.fc34
Provides: xsom-javadoc = 2.3.3-6.fc34
Requires: java-headless
Requires: javapackages-filesystem
Requires: mvn(com.sun.xml.bind.external:relaxng-datatype)

BuildArch: noarch
Source: jaxb-xsom-2.3.3-6.fc34.cpio


%description
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.

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

