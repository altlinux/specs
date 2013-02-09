Name: jgoodies-looks
Version: 2.5.2
Release: alt1

License: BSD style
Group: Development/Java
Summary: JGoodies Looks is a library that makes your Swing applications and applets look better

Url: http://www.jgoodies.com/downloads/libraries.html
Packager: Michael Pozhidaev <msp@altlinux.ru>

Source: looks-%version.zip

Patch0: %{name}-2.5.2-build.patch

BuildRequires: rpm-build-java ant unzip
BuildRequires: java-devel-default

# Fontconfig and DejaVu fonts needed for tests
BuildRequires:  fonts-ttf-dejavu
BuildRequires:  fontconfig
BuildRequires:  jgoodies-common >= 1.4.0
BuildRequires:  maven
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-surefire-provider-junit4
Requires:       jgoodies-common >= 1.4.0


BuildArch: noarch

%description
JGoodies Looks is a library that makes your Swing applications and applets look better. The package
consists of a Windows look&feel and the Plastic look&feel family. These
have been optimized for readability, precise micro-design and
usability.

%package javadoc
Summary: API documentation for %name
Group: Development/Java
Requires: java-common
%description javadoc
Auto-generated API documentation for the %name.jar.

%prep
%setup -q -n looks-%version
%patch0 -p1 -b .build

# Unzip source and test files from provided JARs
mkdir -p src/main/java/ src/test/java/
pushd src/main/java/
jar -xf ../../../%{name}-%{version}-sources.jar
popd
pushd src/test/java/
jar -xf ../../../%{name}-%{version}-tests.jar
popd

# Move the resources into a "resources" directory so they end up packaged
# properly
mkdir -p src/main/resources/com/jgoodies/looks/plastic/
mv src/main/java/com/jgoodies/looks/plastic/icons/ src/main/resources/com/jgoodies/looks/plastic/
mkdir -p src/main/resources/com/jgoodies/looks/common
mv src/main/java/com/jgoodies/looks/common/*.png src/main/resources/com/jgoodies/looks/common/

# Delete prebuild JARs
find -name "*.jar" -exec rm {} \;

# Fix wrong end-of-line encoding
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed -i.orig "s/\r//" $file && \
  touch -r $file.orig $file && \
  rm $file.orig
done

%build
mvn-rpmbuild install javadoc:aggregate 

%install
install -Dpm 0644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -Dpm 0644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -dm 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}/
cp -a target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE.txt README.html RELEASE-NOTES.txt
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1
- update to 2.5.2

* Wed Sep 23 2009 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21517)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt2
- Added java-devel-default

* Wed Apr 30 2008 Michael Pozhidaev <msp@altlinux.ru> 2.1.4-alt1
- Initial RPM.

