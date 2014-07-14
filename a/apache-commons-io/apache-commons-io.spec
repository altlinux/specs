AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       io
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          2.4
Release:          alt2_2jpp7
Epoch:            1
Summary:          Utilities to assist with developing IO functionality
License:          ASL 2.0
Group:            Development/Java
URL:              http://commons.apache.org/%{base_name}
Source0:          http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    junit4
BuildRequires:    maven
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    apache-commons-parent

Requires:         jpackage-utils
Source44: import.info
# jpackage compat
Provides:       jakarta-%{short_name} = %version
Obsoletes:      jakarta-%{short_name} < %version
Provides:       %{short_name} = %version

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt

%build
mvn-rpmbuild install javadoc:javadoc

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom

%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar -a "org.apache.commons:commons-io"

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
# jpp compat
ln -sf %{name}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*.jar
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt1_2jpp7
- new release

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_13jpp6
- added osgi manifest

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_12jpp6
- added compat mapping

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_12jpp6
- renamed

