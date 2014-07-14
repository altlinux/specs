BuildRequires: /proc
BuildRequires: jpackage-compat
Summary:        Java implementation of a binary protocol for web services 
Name:           hessian
Version:        4.0.7
Release:        alt2_4jpp7
Epoch:          1
License:        ASL 1.1
URL:            http://hessian.caucho.com/
Group:          Development/Java
Source0:        http://caucho.com/download/hessian-4.0.7-src.jar
Source1:        %{name}-build.xml
Source2:        http://repo1.maven.org/maven2/com/caucho/hessian/4.0.7/hessian-4.0.7.pom
Requires:       jpackage-utils >= 0:1.6
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  tomcat-servlet-3.0-api
Requires:       jpackage-utils
Requires:       tomcat-servlet-3.0-api

BuildArch:      noarch
Source44: import.info

%description
This is the Java implementation of Caucho's Hession binary transport
protocol for web services.

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
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
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar 

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp doc/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*.jar
%doc apache.license

%files javadoc
%doc %{_javadocdir}/*
%doc apache.license

%changelog
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

