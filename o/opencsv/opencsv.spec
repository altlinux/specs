Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           opencsv
Version:        2.3
Release:        alt1_13jpp8
Summary:        A very simple CSV (comma-separated values) parser library for Java
License:        ASL 2.0
URL:            http://opencsv.sourceforge.net/
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}-src-with-libs.tar.gz
# opencsv don't include the license file
# reported @ https://sourceforge.net/p/opencsv/bugs/98/
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Add java.sql missing methods to test suite
Patch0:         %{name}-2.3-java7.patch
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
Source44: import.info

%description
Support for all the basic csv-type things you're likely to want to do.

%package javadoc
Group: Development/Java
Summary:           Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q

### making sure we dont use it
find . -name '*.jar' -delete
find . -name '*.class' -delete
rm -rf lib/* doc deploy

%patch0 -p0

# Unwanted
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :findbugs-maven-plugin
# Drop javadoc jar
%pom_remove_plugin :maven-javadoc-plugin

sed -i 's/\r//' examples/MockResultSet.java
sed -i 's/\r//' examples/JdbcExample.java
sed -i 's/\r//' examples/addresses.csv
sed -i 's/\r//' examples/AddressExample.java

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

%mvn_file :%{name} %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc examples LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_8jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_5jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_3jpp7
- new version

