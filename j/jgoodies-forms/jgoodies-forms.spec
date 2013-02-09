Name: jgoodies-forms
Version: 1.6.0
Release: alt1

License: BSD style
Group: Development/Java
Summary: %name is a framework that helps you lay out and implement elegant Swing panels quickly and consistently

Url: http://www.jgoodies.com/downloads/libraries.html
Packager: Michael Pozhidaev <msp@altlinux.ru>

Source: forms-1_2_0.zip
Patch: jgoodies-forms-1.6.0-build.patch

Requires: java
Requires: jgoodies-common >= 1.4.0
BuildRequires: rpm-build-java ant unzip
BuildRequires: java-devel-default

# Fontconfig and DejaVu fonts needed for tests
BuildRequires:  fonts-ttf-dejavu fontconfig
BuildRequires:  jgoodies-common >= 1.4.0
BuildRequires:  maven
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-surefire-provider-junit4

BuildArch: noarch

%description
%name is a framework that helps you lay out and implement elegant Swing panels quickly and
consistently. Forms makes simple things easy and the hard stuff
possible, the good design easy and the bad difficult.

%package javadoc
Summary: API documentation for %name
Group: Development/Java
Requires: java-common
%description javadoc
Auto-generated API documentation for the %name.jar.

%prep
%setup -q -n forms-%version
%patch0 -p1 -b .build

#msp:There was problem, javadoc on generation never exits.
#rm -rf ./docs/api
#rm -rf ./*.jar

# Unzip source and test files from provided JARs
mkdir -p src/main/java/ src/test/java/
pushd src/main/java/
jar -xf ../../../%{name}-%{version}-sources.jar
popd
pushd src/test/java/
jar -xf ../../../%{name}-%{version}-tests.jar
popd

# Delete prebuild JARs
find -name "*.jar" -exec rm {} \;

# Drop tests that require a running X11 server
rm src/test/java/com/jgoodies/forms/layout/SerializationTest.java
sed -i "/SerializationTest.class,/d" src/test/java/com/jgoodies/forms/layout/AllFormsTests.java

# Delete ClassLoader test
# TODO: fix it to make it work
rm src/test/java/com/jgoodies/forms/layout/ClassLoaderTest.java
sed -i "/ClassLoaderTest.class,/d" src/test/java/com/jgoodies/forms/layout/AllFormsTests.java

# Fix wrong end-of-line encoding
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed -i.orig "s/\r//" $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -Dpm 0644 target/%{name}-%{version}.jar %buildroot%{_javadir}/%{name}.jar
install -Dpm 0644 pom.xml %buildroot%{_mavenpomdir}/JPP-%{name}.pom
install -dm 0755 %buildroot%{_javadocdir}/%{name}/
cp -a target/site/apidocs/* %buildroot%{_javadocdir}/%{name}/

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE.txt README.html RELEASE-NOTES.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- update to 1.6.0

* Sun Sep 20 2009 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21516)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt2
- Added java-devel-default

* Tue Apr 29 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt1
- Initial RPM
