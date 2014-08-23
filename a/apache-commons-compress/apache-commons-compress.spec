Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat maven-surefire-provider-junit4                  
%global base_name       compress
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.5
Release:        alt1_1jpp7
Summary:        Java API for working with compressed files and archivers
Group:          Development/Java
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  javapackages-tools >= 0.10.0
BuildRequires:  apache-commons-parent
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  xz-java

Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < 1.0-2
Source44: import.info

%description
The Apache Commons Compress library defines an API for working with
ar, cpio, Unix dump, tar, zip, gzip, XZ, Pack200 and bzip2 files.


%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Provides:       jakarta-%{short_name}-javadoc = %{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < 1.0-2
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

%build
%mvn_file  : %{short_name} %{name}
%mvn_alias : commons:
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_2jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_2jpp7
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r831574.6jpp6
- new version

