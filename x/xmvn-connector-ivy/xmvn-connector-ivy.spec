Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xmvn-connector-ivy
Version:        4.0.0
Release:        alt1_3.20210707.d300ce6jpp11
Summary:        XMvn Connector for Apache Ivy
License:        ASL 2.0
URL:            https://fedora-java.github.io/xmvn/
BuildArch:      noarch

#Source0:        https://github.com/fedora-java/xmvn-connector-ivy/releases/download/%{version}/xmvn-%{version}.tar.xz
Source0:        https://github.com/fedora-java/xmvn-connector-ivy/archive/d300ce6.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
Source44: import.info

%description
This package provides XMvn Connector for Apache Ivy, which provides
integration of Apache Ivy with XMvn.  It provides an adapter which
allows XMvn resolver to be used as Ivy resolver.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n xmvn-connector-ivy-d300ce697fda33135c1a60b6606e28e3bca0dec6

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed Jun 29 2022 Igor Vlasenko <viy@altlinux.org> 4.0.0-alt1_3.20210707.d300ce6jpp11
- new version

