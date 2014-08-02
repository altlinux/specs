Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:    c3p0
Version: 0.9.2.1
Release: alt1_2jpp7
Summary: JDBC DataSources/Resource Pools
License: LGPLv2 or EPL
URL:     https://github.com/swaldman/c3p0
Group:   Development/Java

BuildRequires: java-javadoc >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: mchange-commons >= 0.2.3.4

Requires: mchange-commons >= 0.2.3.4
Requires: jpackage-utils

Source0: https://github.com/swaldman/%{name}/archive/%{name}-%{version}-final.tar.gz

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
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}-final

%patch0 -p1 -b .java6
%patch1 -p1 -b .java7

# remove all binary bits
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# remove manifest classpath
sed -i.bak -e "s/<attribute\ name=\"Class-Path\"\ value=\"\${mchange-commons-java\.jar\.file\.name}\"\ \/>//" build.xml

%build
ant \
  -Dbuild.sysclasspath=first \
  -Dmchange-commons-java.jar.file=`build-classpath mchange-commons-java` \
  jar javadoc

sed -i -e "s|@c3p0.version.maven@|%{version}|g" \
  -e "s|@mchange-commons-java.version.maven@|0.2.3.4|g" \
  src/maven/pom.xml

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 build/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 src/maven/pom.xml \
  %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a c3p0:c3p0

%files
%doc src/dist-static/CHANGELOG
%doc src/dist-static/LICENSE*
%doc src/dist-static/RELEASE*
%doc src/doc/index.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-*
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc src/dist-static/LICENSE*
%{_javadocdir}/%{name}

%changelog
* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2.1-alt1_2jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt2_0.9.pre1jpp7
- new fc release

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

