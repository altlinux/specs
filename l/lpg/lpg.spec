Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: gcc-c++
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global    _version 2.0.17
%global    _compat_version 1.1.0

Name:      lpg
Version:   %{_version}
Release:   alt1_19jpp8
Summary:   LALR Parser Generator
# although the text of the licence isn't distributed with some of the source,
# the author has exlicitly stated that everything is covered under the EPL
# see: http://sourceforge.net/forum/forum.php?thread_id=3277926&forum_id=523519
License:   EPL
URL:       http://lpg.sourceforge.net/

Source0:   http://downloads.sourceforge.net/lpg/lpg-java-runtime-src-%{version}.zip
Source1:   http://downloads.sourceforge.net/lpg/lpg-generator-cpp-src-%{version}.zip
Source2:   http://downloads.sourceforge.net/lpg/lpg-generator-templates-%{version}.zip

# source archive for the java compat lib
Source3:   http://downloads.sourceforge.net/lpg/lpgdistribution-05-16-06.zip

# upstream does not provide a build script or manifest file for the java
# compat lib
Source4:   %{name}-build.xml
Source5:   %{name}-manifest.mf

# TODO: drop Source3, 4, 5 and obsolete the java-compat package when dependent
# projects are ported to LPG 2.x.x

# executable name in the bootstrap make target is wrong; sent upstream, see:
# https://sourceforge.net/tracker/?func=detail&aid=2794057&group_id=155963&atid=797881
Patch0:    %{name}-bootstrap-target.patch

# change build script to build the base jar with osgi bundle info
Patch1:    %{name}-osgi-jar.patch

# fix segfault caused by aggressive optimisation of null checks in gcc 4.9
Patch2:    %{name}-segfault.patch
Source44: import.info

%description
The LALR Parser Generator (LPG) is a tool for developing scanners and parsers
written in Java, C++ or C. Input is specified by BNF rules. LPG supports
backtracking (to resolve ambiguity), automatic AST generation and grammar
inheritance.

%package       java
Group: Development/Java
Summary:       Java runtime library for LPG

BuildArch:     noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: ant-apache-regexp
Requires: javapackages-tools rpm-build-java

%description   java
Java runtime library for parsers generated with the LALR Parser Generator
(LPG).

%package       java-compat
Group: Development/Java
Version:       %{_compat_version}
Summary:       Compatibility Java runtime library for LPG 1.x

BuildArch:     noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: ant
Requires: javapackages-tools rpm-build-java

%description   java-compat
Compatibility Java runtime library for parsers generated with the LALR Parser
Generator (LPG) 1.x.

%prep
%setup -q -T -c -n %{name}-%{version}

# because you can't use setup to unzip to subdirectories when your source
# archives do not create top level directories
unzip -qq %{SOURCE0} -d lpg-java-runtime
unzip -qq %{SOURCE1} -d lpg-generator-cpp
unzip -qq %{SOURCE2} -d lpg-generator-templates
chmod -Rf a+rX,u+w,g-w,o-w .

# setup java compat stuff
%setup -q -D -T -a 3 -n %{name}-%{version}
cp -p %{SOURCE4} lpgdistribution/build.xml
cp -p %{SOURCE5} lpgdistribution/MANIFEST.MF

# apply patches
%patch0 -p0 -b .orig
%patch1 -p0 -b .orig
%patch2 -p0 -b .orig

%build
# build java stuff
(cd lpg-java-runtime && ant -f exportPlugin.xml)

# build java compat stuff
(cd lpgdistribution && ant)

# build native stuff
pushd lpg-generator-cpp/src

# ARCH just tells us what tools to use, so this can be the same on all arches
# we build twice in order to bootstrap the grammar parser
make clean install ARCH=linux_x86 \
  LOCAL_CFLAGS="%{optflags} -Wno-strict-overflow" LOCAL_CXXFLAGS="%{optflags} -Wno-strict-overflow"
make bootstrap ARCH=linux_x86
make clean install ARCH=linux_x86 \
  LOCAL_CFLAGS="%{optflags} -Wno-strict-overflow" LOCAL_CXXFLAGS="%{optflags} -Wno-strict-overflow"

popd

%install
install -pD -T lpg-java-runtime/%{name}runtime.jar \
  %{buildroot}%{_javadir}/%{name}runtime.jar
install -pD -T lpgdistribution/%{name}javaruntime.jar \
  %{buildroot}%{_javadir}/%{name}javaruntime.jar
install -pD -T lpg-generator-cpp/bin/%{name}-linux_x86 \
  %{buildroot}%{_bindir}/%{name}

%files
%doc lpg-generator-templates/docs/*
%{_bindir}/%{name}

%files java
%doc lpg-java-runtime/Eclipse*.htm
%{_javadir}/%{name}runtime.jar

%files java-compat
%doc lpg-java-runtime/Eclipse*.htm
%{_javadir}/%{name}javaruntime.jar

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.17-alt1_19jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.17-alt1_18jpp8
- new version

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 2.0.17-alt1_18jpp7
- new jpp release

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.17-alt1_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.17-alt1_10jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.17-alt1_8.1jpp7
- update

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.17-alt1_5.1jpp6
- OSGi manifest for new eclipse-mdt-ocl

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.17-alt1_4jpp6
- new version

