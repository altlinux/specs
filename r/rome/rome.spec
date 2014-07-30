# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		rome
Version:	0.9
Release:	alt3_13jpp7
Summary:	RSS and Atom Utilities

Group:		Development/Java
License:	ASL 2.0
URL:		https://rome.dev.java.net/
# wget https://rome.dev.java.net/source/browse/*checkout*/rome/www/dist/rome-0.9-src.tar.gz?rev=1.1
Source0:	%{name}-%{version}-src.tar.gz
# wget http://download.eclipse.org/tools/orbit/downloads/drops/R20090825191606/bundles/com.sun.syndication_0.9.0.v200803061811.jar
# unzip com.sun.syndication_0.9.0.v200803061811.jar META-INF/MANIFEST.MF
# sed -i 's/\r//' META-INF/MANIFEST.MF
# # We won't have the same SHA-1 sums (class sometimes spills into # cl\nass)
# sed -i -e "/^Name/d" -e "/^SHA/d" -e "/^\ ass$/d" -e "/^$/d" META-INF/MANIFEST.MF
Source1:	MANIFEST.MF
Source2:    http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
BuildArch:	noarch

Patch0:		%{name}-%{version}-addosgimanifest.patch
# fix maven-surefire-plugin aId
Patch1:     %{name}-%{version}-pom.patch

BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	jdom >= 1.1.2-3
Requires:	jpackage-utils
Requires:	jdom >= 1.1.2-3
Source44: import.info

%description
ROME is an set of open source Java tools for parsing, generating and
publishing RSS and Atom feeds.

%package	javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;
mkdir -p target/lib
ln -s %{_javadir}/jdom.jar target/lib
cp -p %{SOURCE1} .
%patch0
cp -p %{SOURCE2} pom.xml
%patch1

%build
ant -Dnoget=true dist

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp dist/docs/api/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
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

