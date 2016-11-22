Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:       rome
Version:    0.9
Release:    alt3_20jpp8
Summary:    RSS and Atom Utilities

License:    ASL 2.0
URL:        https://rome.dev.java.net/
# wget https://rome.dev.java.net/source/browse/*checkout*/rome/www/dist/rome-0.9-src.tar.gz?rev=1.1
Source0:    %{name}-%{version}-src.tar.gz
# wget http://download.eclipse.org/tools/orbit/downloads/drops/R20090825191606/bundles/com.sun.syndication_0.9.0.v200803061811.jar
# unzip com.sun.syndication_0.9.0.v200803061811.jar META-INF/MANIFEST.MF
# sed -i 's/\r//' META-INF/MANIFEST.MF
# # We won't have the same SHA-1 sums (class sometimes spills into # cl\nass)
# sed -i -e "/^Name/d" -e "/^SHA/d" -e "/^\ ass$/d" -e "/^$/d" META-INF/MANIFEST.MF
Source1:    MANIFEST.MF
Source2:    http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
BuildArch:  noarch

Patch0:     %{name}-%{version}-addosgimanifest.patch
# fix maven-surefire-plugin aId
Patch1:     %{name}-%{version}-pom.patch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  jdom >= 1.1.2
Requires: jdom >= 1.1.2
Source44: import.info

%description
ROME is an set of open source Java tools for parsing, generating and
publishing RSS and Atom feeds.

%package	javadoc
Group: Development/Java
Summary:  Javadocs for %{name}
Requires: %{name} = %{version}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;
cp -p %{SOURCE1} .
%patch0
cp -p %{SOURCE2} pom.xml
%patch1

%build
mkdir -p target/lib
build-jar-repository -p target/lib jdom
ant -Dnoget=true dist

%mvn_artifact pom.xml target/rome-%{version}.jar

%install
%mvn_install -J dist/docs/api

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_20jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_19jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_13jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_12jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_12jpp7
- fc version

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_7jpp6
- update to new release by jppimport

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_1jpp5
- fixed build

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1jpp5
- new version

