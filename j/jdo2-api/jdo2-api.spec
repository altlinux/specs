BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jdo2-api
Version:       2.2
Release:       alt3_13jpp8
Summary:       Implementation of JSR 243: Java Data Objects 2.0
License:       ASL 2.0
Url:           http://db.apache.org/jdo/
Source0:       http://svn.apache.org/repos/asf/db/jdo/tags/2.2/dist/db/jdo/2.2/jdo2-api-2.2-src.tar.gz
Source1:       jdo2-api-2.2-build.xml
# changed javax.transaction transaction-api 1.1 with geronimo-jta_1.1_spec
# fix pom version
Source2:       http://repo1.maven.org/maven2/javax/jdo/jdo2-api/2.2/jdo2-api-2.2.pom

Patch0:        jdo2-api-2.2-pom.patch
BuildRequires: jpackage-utils
BuildRequires: java-devel

BuildRequires: ant
BuildRequires: geronimo-jpa
BuildRequires: geronimo-jta
BuildRequires: junit

Requires:      ant
Requires:      geronimo-jpa
Requires:      geronimo-jta
Requires:      junit

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The Java Data Objects 2 (JDO) API is a standard interface-based 
Java model abstraction of persistence, developed as Java Specification 
Request 243 under the auspices of the Java Community Process.

%package javadoc
Group: Development/Java
Summary:       API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c
cd %{name}-%{version}
cp -p %{SOURCE1} build.xml
cp -p %{SOURCE2} pom.xml
%patch0 -p0

%build
cd %{name}-%{version}
%ant jar javadoc

%install
cd %{name}-%{version}
mkdir -p %{buildroot}%{_javadir}
install -pm 644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr  dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}

%files -f %{name}-%{version}/.mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_13jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_4jpp7
- new version

