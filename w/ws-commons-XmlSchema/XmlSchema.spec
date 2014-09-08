Epoch: 0
%define oldname XmlSchema
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           ws-commons-XmlSchema
Version:        1.4.7
Release:        alt3_7jpp7
Summary:        Lightweight schema object model
Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/commons/XmlSchema
# svn export http://svn.apache.org/repos/asf/webservices/commons/tags/XmlSchema/XmlSchema-1.4.7
# tar cJf XmlSchema-1.4.7.tar.xz XmlSchema-1.4.7
Source0:        %{oldname}-%{version}.tar.xz
Source1:        LICENSE-2.0.txt
# maven-site-plugin is broken by the lack of cvsjava in maven-scm. 
# cvsjava was removed when netbeans was orphaned.
Patch1:         %{oldname}-no-site-plugin.patch
BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-shared
BuildRequires: maven-remote-resources-plugin
BuildRequires: apache-resource-bundles
BuildRequires: bcel
BuildRequires: xalan-j2
BuildRequires: xmlunit
BuildRequires: dos2unix
Requires:      bcel
Requires:      xalan-j2
Requires:      xmlunit
Source44: import.info

%description
Commons XMLSchema is a lightweight schema object model that can be 
used to manipulate or generate a schema. 

%package javadoc
Summary:      API documentation for %{oldname}
Group:        Development/Java
BuildArch: noarch

%description javadoc
This package contains API documentation for %{oldname}.

%prep
%setup -q -n %{oldname}-%{version}
%patch1 -p1

# This is provided by modern Java environments
%pom_remove_dep "org.apache.ws.commons:ws-commons-java5"

# Fix line endings
cp -p %{SOURCE1} .
dos2unix LICENSE-2.0.txt README.txt RELEASE-NOTE.txt

%mvn_file :%{oldname} %{oldname}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.txt RELEASE-NOTE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.7-alt3_7jpp7
- new release

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.7-alt3_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.7-alt3_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.7-alt2_2jpp7
- new version

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.7-alt2_1jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.7-alt1_1jpp6
- new jpp relase

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.5-alt1_2jpp6
- new jpp release

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp5
- new version

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

