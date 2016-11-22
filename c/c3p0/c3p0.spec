Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:    c3p0
Version: 0.9.5
Release: alt1_0.3.pre8jpp8
Summary: JDBC DataSources/Resource Pools
License: LGPLv2 or EPL
URL:     https://github.com/swaldman/c3p0
Group:   Development/Other

BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: mchange-commons >= 0.2.7

Requires: mchange-commons >= 0.2.7

Source0: https://github.com/swaldman/c3p0/archive/c3p0-%{version}-pre8.tar.gz

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
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}-pre8

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# remove manifest classpath
sed -i -e "/Class-Path/d" build.xml

%build
ant \
  -Dbuild.sysclasspath=first \
  -Dmchange-commons-java.jar.file=$(build-classpath mchange-commons-java) \
  jar javadoc

sed -i -e "s|@c3p0.version.maven@|%{version}|g" \
  -e "s|@mchange-commons-java.version.maven@|0.2.7|g" \
  src/maven/pom.xml

%mvn_artifact src/maven/pom.xml build/c3p0-%{version}-pre8.jar
%mvn_alias : c3p0:c3p0

%install
%mvn_install

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc src/dist-static/LICENSE*
%doc src/dist-static/RELEASE*
%doc src/dist-static/CHANGELOG
%doc src/dist-static/README
%doc src/doc/index.html
%dir %{_javadir}/%{name}

%files javadoc
%doc src/dist-static/LICENSE*
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.3.pre8jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_0.2.pre8jpp8
- unbootsrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2.1-alt1_4jpp7
- new release

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

