Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       validator
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.4.0
Release:          alt1_4jpp7
Summary:          Apache Commons Validator
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-digester
BuildRequires:    apache-commons-logging
BuildRequires:    maven-local
BuildRequires:    junit
Requires:         apache-commons-beanutils
Requires:         apache-commons-digester
Requires:         apache-commons-logging
Requires:         jpackage-utils
Source44: import.info


%description
A common issue when receiving data either electronically or from user input is
verifying the integrity of the data. This work is repetitive and becomes even
more complicated when different sets of validation rules need to be applied to
the same set of data based on locale for example. Error messages may also vary
by locale. This package attempts to address some of these issues and speed
development and maintenance of validation rules.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt


%build
mvn-rpmbuild install javadoc:aggregate


%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{short_name}:%{short_name}"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}


%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_4jpp7
- new version

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_9jpp7
- fc update

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_0.r832761.5jpp6
- marked oro as essential dependency due to maven-site-plugin

* Sat Feb 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_0.r832761.5jpp6
- new version

