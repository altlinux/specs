BuildRequires: maven-antrun-plugin apache-jar-resource-bundle
Epoch: 0
%define oldname XmlSchema
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           ws-commons-XmlSchema
Version:        1.4.7
Release:        alt3_2jpp7
Summary:        Lightweight schema object model
Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/commons/XmlSchema
# svn export http://svn.apache.org/repos/asf/webservices/commons/tags/XmlSchema/XmlSchema-1.4.7
# tar cJf XmlSchema-1.4.7.tar.xz XmlSchema-1.4.7
Source0:        %{oldname}-%{version}.tar.xz
# ws-commons-java5 is for ancient Java environments
Patch0:         %{oldname}-no-java5.patch
# maven-site-plugin is broken by the lack of cvsjava in maven-scm. 
# cvsjava was removed when netbeans was orphaned.
Patch1:         %{oldname}-no-site-plugin.patch
BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-remote-resources-plugin
BuildRequires: apache-resource-bundles
BuildRequires: bcel
BuildRequires: xalan-j2
BuildRequires: xmlunit
BuildRequires: dos2unix
Requires:      jpackage-utils
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
Requires:     jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{oldname}.

%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild install javadoc:javadoc
dos2unix README.txt RELEASE-NOTE.txt

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{oldname}-%{version}.jar %{buildroot}%{_javadir}/%{oldname}.jar

install -d -m 755 %{buildroot}%{_mavenpomdir}
cp pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{oldname}.pom
%add_maven_depmap JPP-%{oldname}.pom %{oldname}.jar

install -d -m 755 %{buildroot}%{_javadocdir}/%{oldname}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{oldname}

%files
%doc README.txt RELEASE-NOTE.txt
%{_javadir}/%{oldname}.jar
%{_mavenpomdir}/JPP-%{oldname}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{oldname}


%changelog
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

