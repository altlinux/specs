Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global core org.abego.treelayout

Name:          treelayout
Version:       1.0.3
Release:       alt1_13jpp11
Summary:       Efficient and customizable Tree Layout Algorithm in Java
License:       BSD
URL:           http://treelayout.sourceforge.net/
Source0:       https://github.com/abego/treelayout/archive/v%{version}/%{name}-%{version}.tar.gz
# Dummy POM to ease building with RPM
Source1:       pom.xml

BuildArch:     noarch
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
Efficiently create compact, highly customizable tree layouts.  The
software builds tree layouts in linear time; i.e., even trees with many
nodes are built quickly.

%package       demo
Group: Development/Java
Summary:       TreeLayout Core Demo

%description   demo
Demo for "org.abego.treelayout.core".

%package       javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description   javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

cp -p %{SOURCE1} .

# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent %{core} %{core}.demo %{core}.netbeans %{core}.netbeans.demo

# update the source and target JDK
sed -i 's/1\.5/1.8/g' $(find . -name pom.xml)

# fix non ASCII chars for JDK 8 and earlier
if [ -x %{_bindir}/native2ascii ]; then
  native2ascii -encoding UTF8 \
    %{core}/src/main/java/org/abego/treelayout/package-info.java \
    %{core}/src/main/java/org/abego/treelayout/package-info.java
fi

%mvn_package :%{core}.project __noinstall

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-%{core}.core
%doc %{core}/CHANGES.txt README.md
%doc --no-dereference %{core}/src/LICENSE.TXT

%files demo -f .mfiles-%{core}.demo
%doc %{core}.demo/CHANGES.txt
%doc --no-dereference %{core}.demo/src/LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%doc --no-dereference %{core}/src/LICENSE.TXT

%changelog
* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.0.3-alt1_13jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.0.3-alt1_10jpp11
- update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_8jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp8
- new version

