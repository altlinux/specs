# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jutils
Version:        1.0.1
Release:        alt2_3.20110719svnjpp7
Summary:        Common utilities for the Java Gaming Interface

Group:          Development/Java
License:        BSD
URL:            http://java.net/projects/jutils
### upstream only provides subversion checkout
# tar creation instructions
# svn export -r30 https://svn.java.net/svn/jutils~svn/trunk jutils
# tar cfJ jutils-1.0.1.tar.xz jutils 
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit

Requires:       jpackage-utils
Requires:       maven
Source44: import.info

%description
This is the utils project that contains useful shared functionality
for the other Java Games Initiative APIs.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %%{name}.


%prep
%setup -q -n %{name}
sed -i 's/-SNAPSHOT//' pom.xml

%build
mvn-rpmbuild -e -Dmaven.test.skip=true install javadoc:aggregate

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}

# jar
install -Dp -m 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a target/site/apidocs  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc README.txt 
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3.20110719svnjpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3.20110719svnjpp7
- initial build

