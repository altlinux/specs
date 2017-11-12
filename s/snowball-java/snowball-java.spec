Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          snowball-java
Version:       0
Release:       alt1_0.9.20130902jpp8
Summary:       Java stemming algorithm library
License:       BSD
URL:           http://snowball.tartarus.org/index.php
Source0:       http://snowball.tartarus.org/dist/libstemmer_java.tgz
# Custom pom file
Source1:       snowball-template-pom.xml
# http://snowball.tartarus.org/license.php
Source2:       snowball-notice.txt
# see http://snowball.tartarus.org/license.php
# http://www.opensource.org/licenses/bsd-license.html
Source3:       snowball-BSD-license.txt
# Build fix remove 'break;' 
Patch0:        snowball-remove-unreachable-statement.patch

BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
Snowball is a small string processing language
designed for creating stemming algorithms
for use in Information Retrieval.

This package contains all you need to include the
snowball stemming algorithms into a Java
project of your own. If you use this,
you don't need to use the snowball compiler,
or worry about the internals of the
stemmers in any way.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n libstemmer_java

%patch0 -p0

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

cp -p %{SOURCE2} notice.txt
cp -p %{SOURCE3} license.txt
sed -i 's/\r//' license.txt notice.txt

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.9.20130902jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.8.20130902jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.7.20130902jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.5.20130902jpp8
- java 8 mass update

