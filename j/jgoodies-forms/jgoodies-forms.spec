# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define shortname forms

Name:           jgoodies-forms
Version:        1.8.0
Release:        alt1_7jpp8
Summary:        Framework to lay out and implement elegant Swing panels in Java

Group:          Development/Other
License:        BSD
URL:            http://www.jgoodies.com/freeware/forms/
Source0:        http://www.jgoodies.com/download/libraries/%{shortname}/%{name}-%(tr "." "_" <<<%{version}).zip

# Fontconfig and DejaVu fonts needed for tests
BuildRequires:  fonts-ttf-dejavu
BuildRequires:  fontconfig
BuildRequires:  maven-local
BuildRequires:  mvn(com.jgoodies:jgoodies-common) >= 1.8.0
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch
Source44: import.info

%description
The JGoodies Forms framework helps you lay out and implement elegant Swing
panels quickly and consistently. It makes simple things easy and the hard stuff
possible, the good design easy and the bad difficult.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


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

%mvn_file :%{name} %{name} %{name}


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc README.html RELEASE-NOTES.txt
%doc --no-dereference LICENSE.txt


%files javadoc -f .mfiles-javadoc


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1jpp8
- java8 mass update

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2
- NMU: BR: maven-local

* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- update to 1.6.0

* Sun Sep 20 2009 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt3
- jpackage-utils build req replaced by rpm-build-java (closes: #21516)

* Sun Oct 26 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt2
- Added java-devel-default

* Tue Apr 29 2008 Michael Pozhidaev <msp@altlinux.ru> 1.2.0-alt1
- Initial RPM
