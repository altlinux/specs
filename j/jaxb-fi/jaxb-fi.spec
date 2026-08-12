Name:           jaxb-fi
Version:        2.1.1
Release:        alt3

Summary:        Implementation of the Fast Infoset Standard for Binary XML
License:        Apache-2.0
Group:		Development/Java
VCS:            https://github.com/eclipse-ee4j/jaxb-fi

Source:		%name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(com.sun.xml.stream.buffer:streambuffer)
BuildRequires:  mvn(org.glassfish.jaxb:xsom)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

BuildArch:      noarch

%description
Fast Infoset Project, an Open Source implementation of the Fast Infoset
Standard for Binary XML.

The Fast Infoset specification (ITU-T Rec. X.891 | ISO/IEC 24824-1)
describes an open, standards-based "binary XML" format that is based on
the XML Information Set.

%package -n     FastInfoset
Group:		Development/Java
Summary:	FastInfoset

%description -n FastInfoset
%summary.

%package -n     FastInfosetRoundTripTests
Group: 		Development/Java
Summary:        FastInfoset Roundtrip Tests

%description -n FastInfosetRoundTripTests
%summary.

%package -n     FastInfosetSamples
Group: 		Development/Java
Summary:        FastInfoset Samples

%description -n FastInfosetSamples
%summary.

%package -n     FastInfosetUtilities
Group: 		Development/Java
Summary:        FastInfoset Utilities

%description -n FastInfosetUtilities
%summary.

%prep
%setup

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin

%mvn_package :fastinfoset-project __noinstall
%mvn_package :FastInfoset:jar:sources: FastInfoset

%build
%mvn_build -j -s -- org.apache.maven.plugins:maven-source-plugin:jar-no-fork

%install
%mvn_install

%files -n FastInfoset -f .mfiles-FastInfoset
%doc LICENSE NOTICE.md
%doc README.md

%files -n FastInfosetRoundTripTests -f .mfiles-FastInfosetRoundTripTests
%files -n FastInfosetSamples -f .mfiles-FastInfosetSamples
%files -n FastInfosetUtilities -f .mfiles-FastInfosetUtilities

%changelog
* Wed Aug 12 2026 Evgeniy Serov <scala@altlinux.org> 2.1.1-alt3
- Added FastInfoset sources artifact.

* Mon Jan 26 2026 Anton Meleshnikov <alton@altlinux.org> 2.1.1-alt2
- Fixed FTBFS.

* Thu Jan 15 2026 Evgeniy Serov <scala@altlinux.org> 2.1.1-alt1
- Updated to 2.1.1.
- Removed import.info.

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt1_7jpp11
- update

* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt1_2jpp11
- unbootstrap build

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

