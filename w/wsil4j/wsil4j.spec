# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		wsil4j
Version:	1.0
Release:	alt2_6jpp7
Summary:	Web Services Inspection Language for Java API

Group:		Development/Java
License:	ASL 1.1
URL:		http://svn.apache.org/repos/asf/webservices/archive/wsil4j/

# svn co http://svn.apache.org/repos/asf/webservices/archive/wsil4j/trunk/java/ wsil4j-1.0
# tar -cJf wsil4j-1.0.tar.xz wsil4j-1.0
Source0:	%{name}-%{version}.tar.xz
Source1:	%{name}-MANIFEST.MF
Source2:	%{name}-%{version}.pom
BuildArch:	noarch

BuildRequires:	zip
BuildRequires:	ant
BuildRequires:	uddi4j
BuildRequires:	wsdl4j
BuildRequires:	jpackage-utils

Requires:	uddi4j
Requires:	wsdl4j
Requires:	jpackage-utils
Source44: import.info

%description
The Web Services Inspection Language (WS-Inspection) provides a distributed Web
service discovery method, by specifying how to inspect a web site for available
Web services. The WS-Inspection specification defines the locations on a Web
site where you could look for Web service descriptions.

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

ln -s %{_javadir}/uddi4j.jar
ln -s %{_javadir}/wsdl4j.jar

%build
ant -lib ./ compile javadocs

%install
# inject OSGi manifest
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/%{name}.jar META-INF/MANIFEST.MF

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POMs
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%doc docs
%doc LICENSE
%doc README.htm
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc docs
%doc LICENSE
%doc README.htm
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- new version

