Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Summary:       Java implementation of a binary protocol for web services 
Name:          hessian
Version:       4.0.7
Release:       alt2_12jpp8
Epoch:         1
License:       ASL 1.1
URL:           http://hessian.caucho.com/
Source0:       http://caucho.com/download/hessian-4.0.7-src.jar
Source1:       %{name}-build.xml
Source2:       http://repo1.maven.org/maven2/com/caucho/hessian/4.0.7/hessian-4.0.7.pom
BuildRequires: javapackages-local
BuildRequires: ant >= 0:1.6
BuildRequires: tomcat-servlet-3.1-api

BuildArch:     noarch
Source44: import.info

%description
This is the Java implementation of Caucho's Hession binary transport
protocol for web services.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -c
cp %{SOURCE1} build.xml

%build
ant jar 
ant javadoc 

%install
%mvn_artifact %{SOURCE2} %{name}.jar
%mvn_file com.caucho:%{name} %{name}
%mvn_install -J doc/api

%files -f .mfiles
%doc apache.license

%files javadoc -f .mfiles-javadoc
%doc apache.license

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.0.7-alt1_4jpp7
- new version

* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt2_1jpp5
- fixed Sisyphus build 

* Fri Jul 25 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt2_1jpp1.7
- rebuild with java 1.4.2

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt1_1jpp1.7
- converted from JPackage by jppimport script

