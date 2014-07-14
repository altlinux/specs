Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       pool
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.6
Release:          alt2_2jpp7
Summary:          Apache Commons Pool Package
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    apache-commons-parent
BuildRequires:    maven-surefire-provider-junit4

Requires:         jpackage-utils

# This should go away with F-17
Provides:         jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:        jakarta-%{short_name} < 0:1.3-14
Obsoletes:        jakarta-%{short_name}-tomcat5 < 0:1.3-14
Obsoletes:        jakarta-%{short_name}-manual < 0:1.3-14
Source44: import.info

%description
The goal of Pool package is it to create and maintain an object (instance) 
pooling package to be distributed under the ASF license. The package should 
support a variety of pool implementations, but encourage support of an 
interface that makes these implementations interchangeable.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
# This should go away with F-17
Obsoletes:        jakarta-%{short_name}-javadoc < 0:1.3-14
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src

%build
mvn-rpmbuild -Dmaven.test.failure.ignore=true install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
(cd %{buildroot}%{_javadir} && for jar in *%{name}*; do ln -sf ${jar} `echo $jar| sed  "s|apache-||g"`; done)
ln -s %{name}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{short_name}:%{short_name}"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc README.txt LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp7
- new version

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_6jpp6
- fixed build

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_6jpp6
- fixed build with maven3

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_6jpp6
- new version

