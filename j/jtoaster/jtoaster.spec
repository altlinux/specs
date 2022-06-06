Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jtoaster
Version:       1.0.5
Release:       alt4_12jpp11
Summary:       Java utility class for swing applications
License:       ASL 2.0
URL:           http://jtoaster.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/jtoaster/%{name}/1.0/%{name}-%{version}.jar
Source1:       %{name}-template.pom
BuildRequires: javapackages-local
BuildRequires: jpackage-utils

Requires:      java
Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Java Toaster is a java utility class for your swing applications
that show an animate box coming from the bottom of your screen
with a notification message and/or an associated image (like MSN
online/offline notifications).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.class" -delete

cp -p %{SOURCE1} %{name}.pom
sed -i "s|@version@|%{version}|" %{name}.pom

mkdir -p src/com/nitido/utils/toaster docs
mv ./\ com/nitido/utils/toaster/Toaster.java src/com/nitido/utils/toaster/

# install in _javadir
%mvn_file com.nitido:%{name} %{name}

%build

%javac -source 8 -target 8 -encoding UTF-8 $(find src -type f -name "*.java")
(
  cd src
  %jar cvf ../%{name}.jar $(find . -name "*.class")
)
%javadoc -source 8 -d docs -encoding UTF-8 $(find src -type f -name "*.java")

%mvn_artifact %{name}.pom %{name}.jar

%install
%mvn_install -J docs

%files -f .mfiles
%doc README com
%doc --no-dereference apache2.0_license.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference apache2.0_license.txt

%changelog
* Mon Jun 06 2022 Igor Vlasenko <viy@altlinux.org> 1.0.5-alt4_12jpp11
- migrated to %%mvn_artifact

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 1.0.5-alt3_12jpp11
- java11 build
- added BR: unzip

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_12jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_10jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_7jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_7jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_6jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_5jpp8
- new version

