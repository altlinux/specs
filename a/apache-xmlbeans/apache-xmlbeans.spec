%def_without bootstrap
%global reldate 20241203

Name: apache-xmlbeans
Version: 5.3.0
Release: alt2
Summary: XMLBeans is a technology for accessing XML by binding it to Java types
License: Apache-2.0
Group: Development/Java
URL: http://xmlbeans.apache.org/

ExclusiveArch: x86_64 aarch64 loongarch64

Source0: %{name}-src-%{version}-%{?reldate}.tar.gz
Source1: gradle-8.7-rc-4-bin.zip
Source2: gradle-cache.tar
Patch0: apache-xmlbeans-alt-java-version.patch

BuildArch: noarch

BuildRequires: gcc-c++ rpm-build-java swig unzip
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: pom2metadata
BuildRequires: xmlstarlet

%description
XMLBeans is a technology for accessing XML by binding it to Java types.
XMLBeans provides several ways to get at the XML, including:

* Through XML schema that has been compiled to generate Java types that
represent schema types. In this way, you can access instances of the schema
through JavaBeans-style accessors after the fashion of "getFoo" and "setFoo".

* The XMLBeans API also allows you to reflect into the XML schema itself
through an XML Schema Object model.

* A cursor model through which you can traverse the full XML infoset.

* Support for XML DOM.

%prep
%setup -n %{name}-src-%{version}-%{?reldate}
%patch0 -p1
unzip %SOURCE1
test -d ~/.gradle && rm -rf ~/.gradle
%if_without bootstrap
tar xf %SOURCE2 -C ~
%endif

%build
export PATH=$PATH:$PWD/gradle-8.7-rc-4/bin
%global gradle_target -x javadoc -x rat -x test build srcDistTar generatePomFileForPOIPublication
%if_without bootstrap
gradle --no-daemon --offline %gradle_target
%else
gradle --no-daemon %gradle_target
%endif

%install
install -Dpm0644 build/libs/xmlbeans-%version.jar %buildroot%_javadir/xmlbeans/xmlbeans.jar
# Remove deprecated requirement
xmlstarlet ed -N m="http://maven.apache.org/POM/4.0.0" -d "//m:dependency[m:groupId='com.sun.org.apache.xml.internal' and m:artifactId='resolver']" build/dist/maven/xmlbeans-%version.pom > pom-new.xml && /bin/mv -f pom-new.xml build/dist/maven/xmlbeans-%version.pom
install -Dpm0644 build/dist/maven/xmlbeans-%version.pom %buildroot%_mavenpomdir/xmlbeans/xmlbeans.pom
mkdir -p %buildroot%_datadir/maven-metadata
pom2metadata build/dist/maven/xmlbeans-%version.pom %buildroot%_datadir/maven-metadata/xmlbeans.xml xmlbeans

%files
%doc README.md
%_javadir/xmlbeans/*.jar
%_mavenpomdir/xmlbeans/*.pom
%_datadir/maven-metadata/*.xml

%changelog
* Mon Jan 12 2026 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt2
- Packaged xmvn metadata file.
- Removed com.sun.org.apache.xml.internal:resolver from requirements.

* Sun Jul 06 2025 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- Initial build for Sisyphus.
