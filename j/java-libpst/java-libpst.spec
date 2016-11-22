Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          java-libpst
Version:       0.8.1
Release:       alt1_6jpp8
Summary:       A pure Java library for the reading of Outlook PST and OST files
# see https://github.com/rjohnsondev/java-libpst/issues/23
License:       ASL 2.0 and LGPLv3
URL:           https://github.com/rjohnsondev/java-libpst/
Source0:       https://github.com/rjohnsondev/java-libpst/archive/%{version}.tar.gz
Source1:       https://www.gnu.org/licenses/lgpl.txt
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
BuildArch:     noarch
Source44: import.info

%description
A library to read PST files with java,
without need for external libraries.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find -name '*.class' -print -delete
find -name '*.jar' -print -delete

%pom_xpath_set "pom:project/pom:version" %{version}
cp -p %{SOURCE1} LICENSE.LGPL.txt
sed -i 's/\r//' LICENSE.*.txt README.txt

%mvn_file com.pff:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md README.txt
%doc LICENSE.APACHE-2.0.txt LICENSE.LGPL.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.APACHE-2.0.txt LICENSE.LGPL.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_6jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_5jpp8
- new version

