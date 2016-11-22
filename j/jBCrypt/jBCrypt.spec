Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jBCrypt
Version:        0.4
Release:        alt1_3jpp8
Summary:        Strong password hashing for Java

License:        ISC
URL:            http://www.mindrot.org/projects/jBCrypt
Source0:        http://www.mindrot.org/files/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  javapackages-local
BuildRequires:  junit

Obsoletes:      %{name}-javadoc < %{version}-%{release}
Source44: import.info

%description
A Java implementation of OpenBSD's Blowfish password hashing code. 

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%mvn_file : %{name}/%{name} %{name}

%build
ant test dist

%install
%mvn_artifact 'org.mindrot:jbcrypt:0.4' jbcrypt.jar
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_8jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_7jpp7
- new version

