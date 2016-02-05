Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: rpm-build-java-osgi
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eclipselink-persistence-api
%define version 2.0.5
%global oname javax.persistence
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
Name:          eclipselink-persistence-api
Version:       2.0.5
Release:       alt1_5jpp8
Summary:       JPA 2.0 Spec OSGi Bundle
License:       EPL and ASL 2.0
URL:           http://www.eclipse.org/eclipselink/
#Source0:       https://github.com/eclipse/javax.persistence/archive/2.0.5.v201212031355.tar.gz
Source0:       http://maven.eclipse.org/nexus/content/repositories/build/org/eclipse/persistence/%{oname}/%{namedversion}/%{oname}-%{namedversion}-sources.jar
Source1:       http://maven.eclipse.org/nexus/content/repositories/build/org/eclipse/persistence/%{oname}/%{namedversion}/%{oname}-%{namedversion}.pom
# add org.eclipse.osgi as build dep
# add maven-bundle-plugin conf
Patch0:        %{name}-2.0.5-build.patch

BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle

BuildArch:     noarch
Source44: import.info

%description
EclipseLink definition of the Java Persistence 2.0 API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c

# fixing incomplete source directory structure
mkdir -p src/main/java
mv org src/main/java/
mv javax src/main/java/

mkdir src/main/resources
cp -p *.html src/main/resources/

# clone source directory structure
find src/main/java/ -type d | while read dirname ; do
  newdirname=`echo $dirname | sed "s:src/main/java:src/main/resources:g"`
  mkdir -p $newdirname
done

# copy everything except *.java sources
find src/main/java/ -type f | grep -v "\.java" | while read cpfrom ; do
  cpto=`echo $cpfrom | sed "s:src/main/java:src/main/resources:g"`
  cp $cpfrom $cpto
done

cp -p %{SOURCE1} pom.xml
%patch0 -p0

# fix non ASCII chars
for s in src/main/java/javax/persistence/EntityManager.java\
  src/main/java/javax/persistence/MapsId.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%mvn_file :%{oname} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc about.html readme.html
%doc license.html

%files javadoc -f .mfiles-javadoc
%doc license.html

%changelog
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_5jpp8
- java 8 mass update

