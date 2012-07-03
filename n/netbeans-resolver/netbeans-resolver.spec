BuildRequires: /proc
BuildRequires: jpackage-compat
%define patched_resolver_ver 1.2
%define patched_resolver xml-commons-resolver-%{patched_resolver_ver}

Name:    netbeans-resolver
Version: 6.7.1
Release: alt1_3jpp6
Summary: Resolver subproject of xml-commons patched for NetBeans

Group:   Development/Java
License: ASL 1.1
URL:     http://xml.apache.org/commons/

Source0: http://www.apache.org/dist/xml/commons/%{patched_resolver}.tar.gz

# see http://hg.netbeans._org/main/file/721f72486327/o.apache.xml.resolver/external/readme.txt
Patch0: %{name}-%{version}-nb.patch
Patch1: %{name}-%{version}-resolver.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: dos2unix

Requires: jpackage-utils
Source44: import.info

%description
Resolver subproject of xml-commons, version %{patched_resolver_ver} with 
a patch for NetBeans.

%prep
%setup -q -n %{patched_resolver}
# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -exec rm -f {} \;
%{__rm} -rf docs

%patch0 -p1 -b .sav
%patch1 -p1 -b .sav

dos2unix -k KEYS
dos2unix -k LICENSE.resolver.txt

%build
%{ant} -f resolver.xml jar

%install

# JARs
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/resolver.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar

%files
%{_javadir}/*
%doc LICENSE.resolver.txt KEYS

%changelog
* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_3jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_1jpp6
- new version

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 6.1-alt1_5jpp6
- converted from JPackage by jppimport script

