Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# SVN revision used
%global svnrel 1340

Name:           jide-oss
Version:        2.7.6
Release:        alt1_17.1340svnjpp8
Summary:        Swing component library built on top of Java/Swing
License:        GPLv2 with exceptions
URL:            https://jide-oss.dev.java.net/
# Newer release are available here https://github.com/jidesoft/jide-oss
# This is an svn snapshot, to get this tarball :
# then to checkout the project source repository :
# svn checkout https://jide-oss.dev.java.net/svn/jide-oss/branches/trunk_%%{version} jide-oss --username guest
# create the tarball : tar -cjvf jide-oss-%%{version}-%%{svnrel}svn.tar.bz2 jide-oss

Source0:        %{name}-%{version}-%{svnrel}svn.tar.bz2

#Patch1: use a standard component instead of a vendor specific extension
Patch1:         jide-oss-AquaJidePopupMenuUI.java.patch
Patch2:         jide-oss-name-clash.patch

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  java-javadoc
BuildRequires:  javapackages-local

Requires:	java >= 1.6.0
Source44: import.info

%description
JIDE Common Layer is Swing component library built on top of Java/Swing.
It is also the foundation of other component products from JIDE.
This project has over 30 Swing components and over 100k lines of code.
It greatly enhanced the default component set provided by Swing and allow 
developers to focus on business logic layer instead of making components.

JIDE Common Layer was originally developed by JIDE Software developers
as a foundation in order to build other more advanced components.
In April of 2007, JIDE Software decided to open source this common layer
so that more and more developers can leverage them instead of wasting time
building them again.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package doc
Group: Development/Java
Summary:        User documentation for %{name}
BuildArch: noarch

%description doc
User documentation for %{name}.

%prep
%setup -q -n %{name}
find -name '*.jar' -delete
find -name '*.class' -delete
sed -i "s|\r||g" LICENSE.txt


%patch1 -p1 -b .replace_aquapopupmenuui

# fix non ASCII chars
for s in src/com/jidesoft/utils/DateUtils.java \
   src/com/jidesoft/swing/CheckBoxListWithSelectable.java \
   src/com/jidesoft/plaf/eclipse/Eclipse3xJideTabbedPaneUI.java
 do
  native2ascii -encoding UTF8 ${s} ${s}
done
%patch2 -p2

sed -i.crosslink "s|http://java.sun.com/j2se/1.5.0/docs/api/|%{_javadocdir}/java|" build.xml
sed -i.doclint 's|destdir="${javadoc_dir}"|destdir="${javadoc_dir}" additionalparam="-Xdoclint:none"|' build.xml
sed -i.javac "s|1.5|1.6|" build.properties

%mvn_file com.jidesoft:%{name} %{name}

%build
%ant javadoc jar

%install
%mvn_artifact pom.xml %{name}-%{version}.jar
%mvn_install -J javadoc

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%files doc
%doc docs/JIDE_Common_Layer_Developer_Guide.pdf
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_17.1340svnjpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_16.1340svnjpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_15.1340svnjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_13.1340svnjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_12.1340svnjpp8
- new version

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_11.1340svnjpp7
- converted from JPackage by jppimport script

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_7.1340svnjpp7
- new version

