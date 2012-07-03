Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global githash g0d9d058
%global foldhash 5e52ede

Name:           jdependency
Version:        0.7
Release:        alt1_1jpp7
Summary:        This project provides an API to analyse class dependencies

Group:          Development/Java
License:        ASL 2.0
URL:            http://github.com/tcurdt/jdependency
# wget http://github.com/tcurdt/jdependency/tarball/jdependency-0.7
Source0:        tcurdt-jdependency-jdependency-%{version}-0-%{githash}.tar.gz

BuildArch: noarch

BuildRequires:     maven
#BuildRequires:     maven2-common-poms
BuildRequires:     maven-compiler-plugin
BuildRequires:     maven-install-plugin
BuildRequires:     maven-jar-plugin
BuildRequires:     maven-javadoc-plugin
BuildRequires:     maven-resources-plugin
BuildRequires:     maven-surefire-plugin
BuildRequires:     maven-idea-plugin

BuildRequires:  jpackage-utils
BuildRequires:  objectweb-asm
BuildRequires:  apache-commons-io
Requires:  objectweb-asm >= 3.2
Requires:  apache-commons-io

Requires(post):    jpackage-utils
Requires(postun):  jpackage-utils
Source44: import.info


%description
jdependency is small library that helps you analyze class level 
dependencies, clashes and missing classes.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n tcurdt-jdependency-%{foldhash}
# asm >= 3.3
sed -i -e 's,<groupId>asm</groupId>,<groupId>org.objectweb.asm</groupId>,' pom.xml

%build
mvn-rpmbuild -Dmaven.test.failure.ignore=true \
    install javadoc:javadoc

%install

# Jar
mkdir -p %{buildroot}%{_javadir}
install -Dpm 644  target/%{name}-%{version}.jar  \
    %{buildroot}%{_javadir}/%{name}.jar


# Javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*


# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-jdependency.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt README.md

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_1jpp7
- fc version

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_5jpp6
- new version

