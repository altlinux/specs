# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global shortname common

Name:           jgoodies-common
Version:        1.4.0
Release:        alt1_1jpp7
Summary:        Common library shared by JGoodies libraries and applications

Group:          Development/Java
License:        BSD
URL:            http://www.jgoodies.com/
Source0:        http://www.jgoodies.com/download/libraries/%{shortname}/%{name}-%(tr "." "_" <<<%{version}).zip

# fontconfig and DejaVu fonts needed for tests
BuildRequires:  fonts-ttf-dejavu
BuildRequires:  fontconfig
BuildRequires:  jpackage-utils
BuildRequires:  maven1
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-surefire-provider-junit4
Requires:       jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
The JGoodies Common library provides convenience code for other JGoodies
libraries and applications.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.


%prep
%setup -q

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

# Remove DOS line endings
for file in LICENSE.txt RELEASE-NOTES.txt; do
  sed 's|\r||g' $file > $file.new && \
  touch -r $file $file.new && \
  mv $file.new $file
done


%build
mvn-rpmbuild install javadoc:aggregate


%install
install -Dpm 0644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -Dpm 0644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/
cp -a target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc LICENSE.txt README.html RELEASE-NOTES.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom


%files javadoc
%{_javadocdir}/%{name}/


%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1jpp7
- initial build

