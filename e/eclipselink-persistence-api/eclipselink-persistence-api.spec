Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: rpm-build-java-osgi
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.1.0
%global oname javax.persistence
%global namedreltag .v201304241213
%global namedversion %{version}%{?namedreltag}
%global api_version 2.1
Name:          eclipselink-persistence-api
Version:       2.1.0
Release:       alt1_5jpp8
Summary:       JPA 2.1 Spec OSGi Bundle
License:       EPL and ASL 2.0
URL:           http://www.eclipse.org/eclipselink/
#Source0:       https://github.com/eclipse/javax.persistence/archive/%%{namedversion}.tar.gz
Source0:       http://git.eclipse.org/c/eclipselink/javax.persistence.git/snapshot/%{oname}-%{namedversion}.tar.xz
Source1:       eclipse-javax.persistence-template.pom.xml

BuildRequires: java-javadoc
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)

BuildArch:     noarch
Source44: import.info

%description
EclipseLink definition of the Java Persistence 2.1 API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{namedversion}

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml
sed -i "s|@API_VERSION@|%{api_version}|" pom.xml
sed -i "s|@IMPL_VERSION@|%{namedversion}|" pom.xml

cp -p resource/{about,license,readme}.html .

mkdir -p target/classes
rm -r META-INF/MANIFEST.MF
mv META-INF target/classes/

# fix non ASCII chars
for s in src/javax/persistence/EntityManager.java\
  src/javax/persistence/MapsId.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%mvn_file :%{oname} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc about.html changes readme.html changes readme.txt
%doc --no-dereference license.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.html readme.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_5jpp8
- java 8 mass update

