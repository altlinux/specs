Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 3c0a06622831bd7af6c231c1b5d5398f3afc7271
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          datanucleus-api-jdo
Version:       3.2.8
Release:       alt1_7jpp8
Summary:       DataNucleus JDO API plugin
License:       ASL 2.0
URL:           https://github.com/datanucleus/datanucleus-api-jdo
Source:        https://github.com/datanucleus/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: java-devel

# note this HAS to be jdo-api 3.x, not jdo2-api 2.2
BuildRequires: mvn(javax.jdo:jdo-api)
BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(org.datanucleus:datanucleus-core)
# Test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j)

BuildRequires: maven-local
BuildRequires: datanucleus-maven-parent

BuildArch:     noarch
Source44: import.info

%description
Plugin providing DataNucleus implementation of JDO API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{commit}

sed -i 's/\r//' META-INF/LICENSE.txt META-INF/NOTICE.txt META-INF/README.txt
cp -p META-INF/LICENSE.txt .
cp -p META-INF/NOTICE.txt .
cp -p META-INF/README.txt .

%build

%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_7jpp8
- java update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_6jpp8
- new version

