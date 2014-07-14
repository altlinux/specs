Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       compress
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.4.1
Release:          alt2_2jpp7
Summary:          Java API for working with tar, zip and bzip2 files
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    apache-commons-parent
BuildRequires:    junit4
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    xz-java
Requires:         jpackage-utils
Requires:         xz-java
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

# Upstream name change
Provides:         jakarta-%{short_name} = %{version}-%{release}
Obsoletes:        jakarta-%{short_name} < 1.0-2
Source44: import.info

%description
The code in this component came from Avalon's Excalibur, but originally
from Ant, as far as life in Apache goes. The tar package is originally
Tim Endres' public domain package. The bzip2 package is based on the
work done by Keiron Liddle. It has migrated via:
Ant -> Avalon-Excalibur -> Commons-IO -> Commons-Compress. 


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils

# Upstream name change
Provides:         jakarta-%{short_name}-javadoc = %{version}-%{release}
Obsoletes:        jakarta-%{short_name}-javadoc < 1.0-2
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{short_name}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/*
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_2jpp7
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r831574.6jpp6
- new version

