
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: jaxb-fi
Version: 1.2.18
Summary: Implementation of the Fast Infoset Standard for Binary XML
License: ASL 2.0 and BSD and ASL 1.1
Url: https://github.com/eclipse-ee4j/jaxb-fi
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.org>
Provides: glassfish-fastinfoset = 1.2.18-2.fc34
Provides: mvn(com.sun.xml.fastinfoset:FastInfoset) = 1.2.18
Provides: mvn(com.sun.xml.fastinfoset:FastInfoset:pom:) = 1.2.18
Provides: mvn(com.sun.xml.fastinfoset:FastInfosetUtilities) = 1.2.18
Provides: mvn(com.sun.xml.fastinfoset:FastInfosetUtilities:pom:) = 1.2.18
Provides: mvn(com.sun.xml.fastinfoset:fastinfoset-project:pom:) = 1.2.18
Provides: osgi(com.sun.xml.fastinfoset.FastInfoset) = 1.2.18
Requires: java-headless
Requires: javapackages-filesystem
Requires: mvn(com.sun.xml.stream.buffer:streambuffer)
Requires: mvn(org.glassfish.jaxb:xsom)

BuildArch: noarch
Source: jaxb-fi-1.2.18-2.fc34.cpio


%description
Fast Infoset Project, an Open Source implementation of the Fast Infoset
Standard for Binary XML.

The Fast Infoset specification (ITU-T Rec. X.891 | ISO/IEC 24824-1)
describes an open, standards-based "binary XML" format that is based on
the XML Information Set.

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
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

