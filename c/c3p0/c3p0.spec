Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global prerel pre1

Name:    c3p0
Version: 0.9.2
Release: alt2_0.7.pre1jpp7
Summary: JDBC DataSources/Resource Pools
License: LGPLv2
URL:     http://sourceforge.net/projects/c3p0
Group:   Development/Java

BuildRequires: java-javadoc 
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: mchange-commons

Requires: mchange-commons
Requires: jpackage-utils

Source0: http://download.sourceforge.net/c3p0/%{name}-%{version}-%{prerel}.src.tgz

# POM based on the one found at http://mvnrepository.com/artifact/c3p0/c3p0
Source1: c3p0.pom

# Patch to build on java 1.6
Patch0: %{name}-build-on-1.6.patch

# Patch to build on java 1.7 (intentionally kept separate from above)
Patch1: %{name}-build-on-1.7.patch

BuildArch: noarch
Source44: import.info

%description
c3p0 is an easy-to-use library for augmenting traditional JDBC drivers with
JNDI-bindable DataSources, including DataSources that implement Connection
and Statement Pooling, as described by the jdbc3 spec and jdbc2 standard
extension.

%package  javadoc
Summary:  API documentation for %{name}
Group:    Development/Java
Requires: jpackage-utils
Requires: java-javadoc
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}-%{prerel}.src

%patch0 -p0 -b .java6
%patch1 -p0 -b .java7

# remove all binary bits
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# remove manifest classpath
sed -i.bak -e "s/<attribute\ name=\"Class-Path\"\ value=\"\${mchange-commons\.jar\.file\.name}\"\ \/>//" build.xml

%build
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dbuild.sysclasspath=first \
  -Dmchange-commons.jar.file.dir=/usr/share/java \
  -Dmchange-commons.jar.file.name=mchange-commons.jar \
  jar javadocs

%install
# jar
install -pD -T build/%{name}-%{version}-%{prerel}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# pom
install -pD -m 644 -T %{SOURCE1} \
  %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc src/dist-static/CHANGELOG
%doc src/dist-static/LICENSE
%doc src/dist-static/RELEASE*
%doc src/doc/index.html
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%doc src/dist-static/LICENSE
%{_javadocdir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt2_0.7.pre1jpp7
- fc version

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt1_0.pre1.1jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt3_2jpp5
- selected java5 compiler explicitly

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt2_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Mon Mar 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt2_2jpp1.7
- fixed alternatives intersection

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

