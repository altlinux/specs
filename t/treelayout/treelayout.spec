Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 22
%global core org.abego.treelayout
Name:          treelayout
Version:       1.0.2
Release:       alt1_2jpp8
Summary:       Efficient and customizable Tree Layout Algorithm in Java
License:       BSD
URL:           http://treelayout.sourceforge.net/
# svn export svn://svn.code.sf.net/p/treelayout/code/tags/REL-1.0.2 treelayout-1.0.2
# tar cJf treelayout-1.0.2.tar.xz treelayout-1.0.2
Source0:       %{name}-%{version}.tar.xz
Source1:       %{name}-project-pom.xml

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
%if 0
# Not available
BuildRequires: mvn(org.netbeans.api:org-netbeans-api-visual:RELEASE67)
%endif
%if %{?fedora} > 20
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
%else
BuildRequires: mvn(org.sonatype.oss:oss-parent)
%endif

BuildArch:     noarch
Source44: import.info

%description
Efficiently create compact, highly customizable
tree layouts. The software builds tree layouts
in linear time. I.e. even trees with many nodes
are built fast.

%package demo
Group: Development/Java
Summary:       TreeLayout Core Demo

%description demo
Demo for "org.abego.treelayout.core".

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml
# build core and demo ... for now
%pom_disable_module %{core}.netbeans
%pom_disable_module %{core}.netbeans.demo

cp -p %{core}/CHANGES.txt .
cp -p %{core}/src/LICENSE.TXT .

native2ascii -encoding UTF8 %{core}/src/main/java/org/abego/treelayout/package-info.java \
 %{core}/src/main/java/org/abego/treelayout/package-info.java

%mvn_package :%{core}.project __noinstall

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{core}.core
%dir %{_javadir}/%{name}
%doc CHANGES.txt
%doc LICENSE.TXT

%files demo -f .mfiles-%{core}.demo
%doc %{core}.demo/CHANGES.txt
%doc %{core}.demo/src/LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%doc LICENSE.TXT

%changelog
* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp8
- new version

