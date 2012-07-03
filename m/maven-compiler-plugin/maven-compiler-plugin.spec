BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-compiler-plugin
Version:        2.3.2
Release:        alt1_5jpp7
Summary:        Maven Compiler Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-compiler-plugin
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-compiler-plugin-2.3.2 maven-compiler-plugin-2.3.2
#tar caf maven-compiler-plugin-2.3.2.tar.xz maven-compiler-plugin-2.3.2/
Source0:        %{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-toolchain
BuildRequires: plexus-utils
BuildRequires: plexus-compiler

Requires:      maven
Requires:      maven-toolchain
Requires:      plexus-utils
Requires:      plexus-compiler
Requires:      jpackage-utils

Provides:       maven2-plugin-compiler = %{version}-%{release}
Obsoletes:      maven2-plugin-compiler <= 0:2.0.8
Source44: import.info

%description
The Compiler Plugin is used to compile the sources of your project.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q #You may need to update this according to your Source0

%build
mvn-rpmbuild -e \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom


%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

