# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             snappy-java
Version:          1.0.4.1
Release:          alt2_3jpp7
Summary:          Fast compressor/decompresser
Group:            Development/Java
License:          ASL 2.0
URL:              http://code.google.com/p/snappy-java

# hg clone --insecure -r snappy-java-1.0.4.1 https://code.google.com/p/snappy-java/
# cd snappy-java && hg archive -p snappy-java-1.0.4.1/ -X 'lib/*.jar' -t tgz ../snappy-java-1.0.4.1-CLEAN.tgz
Source0:          snappy-java-%{version}-CLEAN.tgz

Patch0:           snappy-java-%{version}-pom.patch

BuildArch:        noarch

BuildRequires:    felix-osgi-core
BuildRequires:    jboss-logging
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin

Requires:         felix-osgi-core
Requires:         jboss-logging
Requires:         jpackage-utils
Source44: import.info

%description
A Java port of the snappy, a fast compresser/decompresser written in C++.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%patch0 -p1

%build
# no xerial package available
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JAR
install -pm 644 target/snappy-java-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE README NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4.1-alt1_3jpp7
- new version

