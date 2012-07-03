BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-rar-plugin
Version:        2.2
Release:        alt1_7jpp7
Summary:        Plugin to create Resource Adapter Archive which can be deployed to a J2EE server

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-rar-plugin/
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-rar-plugin-2.2/
# tar jcf maven-rar-plugin-2.2.tar.bz2 maven-rar-plugin-2.2/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         add-maven-core.patch

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: jpackage-utils
Requires: ant
Requires: maven
Requires: jpackage-utils
Requires(post): jpackage-utils
Requires(postun): jpackage-utils

Obsoletes: maven2-plugin-rar <= 0:2.0.8
Provides: maven2-plugin-rar = 1:%{version}-%{release}
Source44: import.info

%description
A resource adapter is a system-level software driver that 
a Java application to connect to an enterprise 
information system (EIS).The RAR plugin has the capability 
to store these resource adapters to an archive 
(Resource Adapter Archive or RAR) which can be deployed to
 a J2EE server.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0

%build
mvn-rpmbuild \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins %{name} %{version} JPP %{name}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_7jpp7
- complete build

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

