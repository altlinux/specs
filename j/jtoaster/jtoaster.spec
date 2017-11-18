BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jtoaster
Version:       1.0.5
Release:       alt2_7jpp8
Summary:       Java utility class for swing applications
License:       ASL 2.0
URL:           http://jtoaster.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/jtoaster/%{name}/1.0/%{name}-%{version}.jar
Source1:       %{name}-template.pom
BuildRequires: java-devel
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

%build

%javac -encoding UTF-8 $(find src -type f -name "*.java")
(
  cd src
  %jar cvf ../%{name}.jar $(find . -name "*.class")
)
%javadoc -d docs -encoding UTF-8 $(find src -type f -name "*.java")

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{name}.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%doc README com
%doc apache2.0_license.txt

%files javadoc
%{_javadocdir}/%{name}
%doc apache2.0_license.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt2_7jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_7jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_6jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_5jpp8
- new version

