Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		jpf
Version:	1.5.1
Release:	alt2_18jpp8
Summary:	Java Plug-in Framework
License:	LGPLv2
URL:		http://jpf.sourceforge.net/
BuildArch:	noarch

Source0:	http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.zip

# Custom pom to build all artifacts in a single reactor
Source1:        pom.xml

Patch0:		jpf-1.5.1-build_javadoc.patch
Patch1:		jpf-1.5.1-no-class-manifest.patch

BuildRequires:	maven-local
BuildRequires:	apache-commons-logging
BuildRequires:  mvn(log4j:log4j)
Source44: import.info

%description
JPF is an  open source, LGPL licensed plug-in infrastructure library for
new or existing Java projects. JPF provides a runtime engine that
dynamically discovers and loads "plug-ins". A plug-in is a structured
component that describes itself to JPF using a "manifest". JPF maintains a
registry of available plug-ins and the functions they provide (via
extension points and extensions).

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
Documentation for the %{name} Java library.

%prep
%setup -q -c %{name}-%{version}
find . -name "*.jar" | xargs rm

# Build the javadoc all together, but not for the "tools" sub-package
# (it uses the unpackaged "jxp" library)
%patch0 -b .jadoc -p0

# Don't put classpaths into the manifests
%patch1 -p1

sed -i "s|\r||g" license.txt

files=$(ls)
%pom_add_parent "net.sf.jpf:jpf-parent:%{version}" $PWD/jpf-pom.xml
%pom_add_parent "net.sf.jpf:jpf-parent:%{version}" $PWD/jpf-boot-pom.xml
%pom_xpath_set "pom:project/pom:version" "%{version}" $PWD/jpf-pom.xml
%pom_xpath_set "pom:project/pom:version" "%{version}" $PWD/jpf-boot-pom.xml
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId='jpf']/pom:version" "%{version}" $PWD/jpf-boot-pom.xml

%pom_xpath_inject "pom:project" "<properties><project.build.sourceEncoding>UTF-8</project.build.sourceEncoding></properties>" $PWD/jpf-pom.xml
%pom_xpath_inject "pom:project" "<properties><project.build.sourceEncoding>UTF-8</project.build.sourceEncoding></properties>" $PWD/jpf-boot-pom.xml

mkdir jpf && cp -pr $files jpf && mv jpf/jpf-pom.xml jpf/pom.xml
mkdir jpf-boot && cp -pr $files jpf-boot && mv jpf-boot/jpf-boot-pom.xml jpf-boot/pom.xml
cp -p %{SOURCE1} .

%build
%mvn_build -X

%install
%mvn_install
mkdir -p %{buildroot}%{_mavenpomdir}/jpf

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_18jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_16jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_12jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_5jpp7
- new version

