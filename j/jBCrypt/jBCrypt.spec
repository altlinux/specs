Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jBCrypt
Version:        0.4
Release:        alt1_9jpp8
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
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_9jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_8jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_5jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_4jpp8
- new jpp release

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

