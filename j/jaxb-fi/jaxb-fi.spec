Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jaxb-fi
Version:        1.2.18
Release:        alt1_4jpp11
Summary:        Implementation of the Fast Infoset Standard for Binary XML
# jaxb-fi is licensed ASL 2.0 and EDL-1.0 (BSD)
# bundled org.apache.xerces.util.XMLChar.java is licensed ASL 1.1
License:        ASL 2.0 and BSD and ASL 1.1

URL:            https://github.com/eclipse-ee4j/jaxb-fi
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.xml.stream.buffer:streambuffer)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.jaxb:xsom)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-fastinfoset = %{version}-%{release}
Obsoletes:      glassfish-fastinfoset < 1.2.15-5

# javadoc subpackage is currently not built
Obsoletes:      glassfish-fastinfoset-javadoc < 1.2.15-5
Source44: import.info

%description
Fast Infoset Project, an Open Source implementation of the Fast Infoset
Standard for Binary XML.

The Fast Infoset specification (ITU-T Rec. X.891 | ISO/IEC 24824-1)
describes an open, standards-based "binary XML" format that is based on
the XML Information Set.


%prep
%setup -q

pushd code
# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and not required
%pom_remove_parent

# disable unnecessary submodules
%pom_disable_module roundtrip-tests
%pom_disable_module samples

# disable unnecessary plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
popd


%build
pushd code
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -f -j -- -DbuildNumber=unknown
popd


%install
pushd code
%mvn_install
popd


%files -f code/.mfiles
%doc --no-dereference LICENSE NOTICE.md
%doc README.md


%changelog
* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt1_2jpp11
- unbootstrap build

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.2.18-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

