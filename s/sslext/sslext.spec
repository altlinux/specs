Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          sslext
Version:       1.2
Release:       alt2_11jpp8
Summary:       Struts SSL Switching Extension
License:       ASL 1.1
Url:           http://sslext.sourceforge.net/
#cvs -d:pserver:anonymous@sslext.cvs.sourceforge.net:/cvsroot/sslext login
#cvs -z3 -d:pserver:anonymous@sslext.cvs.sourceforge.net:/cvsroot/sslext export -r Release1_2_1 sslext120
#rm -rf sslext120/web/WEB-INF/lib/*.jar
#rm -rf sslext120/sslext-struts1.2-*.*
#rm -rf $(find sslext120 -name "CVS")
#rm -rf $(find sslext120 -name "*.class")
#rm -rf $(find sslext120 -name "*.bak")
# non free
# rm -rf sslext120/web/WEB-INF/web-app_2_3.dtd
#mv sslext120 sslext-1.2
#tar czf sslext-1.2-realclean-src-cvs.tar.gz sslext-1.2
Source0:       %{name}-%{version}-realclean-src-cvs.tar.gz
Source1:       http://repo1.maven.org/maven2/%{name}/%{name}/%{version}-0/%{name}-%{version}-0.pom
Patch0:        %{name}-%{version}-build.patch
# fix build java5+
Patch1:        %{name}-%{version}-SecureRequestUtils.patch
# update struts reference
Patch2:        %{name}-%{version}-pom.patch
# build apis documentation
Patch3:        %{name}-%{version}-javadocs.patch

BuildRequires: java-devel
BuildRequires: javapackages-local

BuildRequires: ant
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-digester
BuildRequires: apache-commons-fileupload
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-validator
BuildRequires: jakarta-oro
BuildRequires: struts
BuildRequires: tomcat-jsp-2.3-api
BuildRequires: tomcat-servlet-3.1-api

BuildArch:     noarch
Source44: import.info

%description
Extension to the Struts framework that allows developers to configure web
applications to automatically switch between the HTTP and HTTPS protocols.
Configuration is performed within the Struts config XML file.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
mkdir -p web/WEB-INF/classes
%patch0 -p0
sed -i "s|tomcat-servlet-3.0-api|tomcat-servlet-api|" build.xml
sed -i "s|tomcat-jsp-2.2-api|tomcat-jsp-api|" build.xml
sed -i "s|1.5|1.6|" build.xml
%patch1 -p0
cp -p %{SOURCE1} pom.xml
%patch2 -p0
%patch3 -p0

%build

export CLASSPATH=$(build-classpath tomcat-servlet-api tomcat-jsp-api)
%ant compile make-jar javadoc

%install
%mvn_artifact pom.xml web/WEB-INF/lib/%{name}.jar
%mvn_file %{name}:%{name} %{name}
%mvn_install -J docs

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_11jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_10jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_9jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_8jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

