Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		classloader-leak-test-framework
Version:	1.1.1
Release:	alt1_4jpp8
Summary:	Detection and verification of Java ClassLoader leaks
License:	ASL 2.0
URL:		https://github.com/mjiderhamn/classloader-leak-prevention/tree/master/%{name}
Source0:	https://github.com/mjiderhamn/classloader-leak-prevention/archive/%{name}-%{version}.tar.gz

BuildArch:	noarch

# build
BuildRequires:	maven-local
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.apache.bcel:bcel)
# test dependencies
BuildRequires:	mvn(javax.el:el-api)
BuildRequires:	mvn(com.sun.faces:jsf-api)
BuildRequires:	mvn(com.sun.faces:jsf-impl)
Source44: import.info

%description
Stand-alone test framework for detecting and/or verifying the existence or
non-existence of Java ClassLoader leaks. It is also possible to test leak
prevention mechanisms to confirm that the leak really is avoided. The framework
is an built upon JUnit.

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n classloader-leak-prevention-%{name}-%{version}
rm -r classloader-leak-prevention
cp -r %{name}/* .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3jpp8
- new jpp release

