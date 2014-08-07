# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name  discovery
%global short_name commons-%{base_name}

Name:           apache-%{short_name}
Version:        0.5
Release:        alt2_4jpp7
Epoch:          2
Summary:        Apache Commons Discovery
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         %{name}-addosgimanifest.patch
BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  apache-commons-logging >= 1.1.1
Requires:       apache-commons-logging >= 1.1.1

# This should go away with F-17
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} <= 1:0.4
Source44: import.info

%description
The Discovery component is about discovering, or finding, implementations for
pluggable interfaces.  Pluggable interfaces are specified with the intent that
multiple implementations are, or will be, available to provide the service
described by the interface.  Discovery provides facilities for finding and
instantiating classes, and for lifecycle management of singleton (factory)
classes.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils

Obsoletes:      jakarta-%{short_name}-javadoc <= 1:0.4
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0

%build
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  install javadoc:aggregate

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt2_4jpp7
- rebuild with maven-local

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 2:0.5-alt1_4jpp7
- fc update

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.5-alt1_0.r830999.4jpp6
- new version

