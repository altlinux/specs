# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

%global short_name   gson
%global group_id     com.google.code.gson

Name:             google-%{short_name}
Version:          2.2.4
Release:          alt1_1jpp7
Summary:          Java lib for conversion of Java objects into JSON representation
License:          ASL 2.0
Group:            Development/Java
URL:              http://code.google.com/p/%{name}
# request for tarball: http://code.google.com/p/google-gson/issues/detail?id=283
# svn export http://google-gson.googlecode.com/svn/tags/gson-%{version} google-gson-%{version}
# tar caf google-gson-%{version}.tar.xz google-gson-%{version}
Source0:          %{name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-enforcer-plugin

Requires:         jpackage-utils
Source44: import.info

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE

%build
# LANG="C" or LANG="en_US.utf8" needed for the tests
mvn-rpmbuild -Dmaven.test.failure.ignore=true install 

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE README
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%doc %{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3jpp7
- new version

