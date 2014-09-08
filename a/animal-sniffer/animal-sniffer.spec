Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           animal-sniffer
Version:        1.9
Release:        alt1_5jpp7
Summary:        Tools to assist verifying backward compatibility of Java classes

License:        MIT and ASL 2.0
URL:            http://mojo.codehaus.org/animal-sniffer/

Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer-parent/%{version}/animal-sniffer-parent-%{version}-source-release.zip
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

# this should be upstreamable
Patch2:         0003-Remove-catch-for-unthrown-PlexusConfigurationExcepti.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-plugin-cobertura
BuildRequires:  maven-plugin-build-helper
BuildRequires:  plexus-containers-component-javadoc
BuildRequires:  mojo-parent
BuildRequires:  objectweb-asm4

Requires:       maven
Requires:       objectweb-asm4
Requires:       ant
Requires:       mojo-signatures
Source44: import.info


%description
Tools to assist verifying that classes compiled with a newer JDK/API
are compatible with an older JDK/API

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-parent-%{version}
%patch2 -p1
cp %{SOURCE2} LICENSE
%pom_add_dep org.apache.maven:maven-compat animal-sniffer-enforcer-rule
%pom_add_dep org.apache.maven:maven-compat animal-sniffer-maven-plugin


%build
%mvn_build

%install
%mvn_install

# install shell script
%jpackage_script org.codehaus.mojo.animal_sniffer.Main "" "" %{name}/%{name} %{name} true

%files -f .mfiles
%doc LICENSE
%{_bindir}/%{name}
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_5jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_3jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_1jpp7
- non-bootstrap build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

