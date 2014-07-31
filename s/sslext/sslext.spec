# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          sslext
Version:       1.2
Release:       alt2_4jpp7
Summary:       Struts SSL Switching Extension
Group:         Development/Java
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

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-digester
BuildRequires: apache-commons-fileupload
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-validator
BuildRequires: jakarta-oro
BuildRequires: struts
BuildRequires: tomcat-jsp-2.2-api
BuildRequires: tomcat-servlet-3.0-api

Requires:      apache-commons-digester
Requires:      apache-commons-logging
Requires:      struts
Requires:      tomcat-servlet-3.0-api
Requires:      tomcat-jsp-2.2-api

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Extension to the Struts framework that allows developers to configure web
applications to automatically switch between the HTTP and HTTPS protocols.
Configuration is performed within the Struts config XML file.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
mkdir -p web/WEB-INF/classes
%patch0 -p0
%patch1 -p0
cp -p %{SOURCE1} pom.xml
%patch2 -p0
%patch3 -p0

%build

export CLASSPATH=$(build-classpath tomcat-jsp-2.2-api tomcat-servlet-3.0-api)
%ant compile make-jar javadoc

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 web/WEB-INF/lib/%{name}.jar %{buildroot}%{_javadir}/

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

