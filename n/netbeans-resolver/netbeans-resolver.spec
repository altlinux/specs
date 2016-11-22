# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define patched_resolver_ver 1.2
%define patched_resolver xml-commons-resolver-%{patched_resolver_ver}

Name:    netbeans-resolver
Version: 6.7.1
Release: alt1_12jpp8
Summary: Resolver subproject of xml-commons patched for NetBeans

Group:   Development/Other
License: ASL 1.1
URL:     http://xml.apache.org/commons/

Source0: http://archive.apache.org/dist/xml/commons/%{patched_resolver}.tar.gz

# see http://hg.netbeans._org/main/file/721f72486327/o.apache.xml.resolver/external/readme.txt
Patch0: %{name}-%{version}-nb.patch
Patch1: %{name}-%{version}-resolver.patch
Patch2: javadoc-source-version.patch

BuildArch: noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: ant
BuildRequires: dos2unix

Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
Resolver subproject of xml-commons, version %{patched_resolver_ver} with 
a patch for NetBeans.

%package javadoc
Summary:    Javadocs for %{name}
Group:      Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q -n %{patched_resolver}
# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -exec rm -f {} \;
rm -rf apidocs

%patch0 -p1 -b .sav
%patch1 -p1 -b .sav
%patch2 -p1 -b .sav

dos2unix -k KEYS
dos2unix -k LICENSE.resolver.txt

%build
ant -f resolver.xml jar docs

%install
mkdir -p %{buildroot}%{_javadir}
cp -p build/resolver.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/apidocs/resolver %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc LICENSE.resolver.txt KEYS

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.resolver.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_6jpp7
- new release

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_5jpp7
- new version

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_3jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_1jpp6
- new version

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 6.1-alt1_5jpp6
- converted from JPackage by jppimport script

