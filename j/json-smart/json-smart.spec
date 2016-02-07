Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global commit 4fe12e8129ccd25498c5d88f5b16bf3984269cc7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:          json-smart
Version:       1.3
Release:       alt1_0.4.20140820jpp8
Summary:       A small and very fast json parser/generator for java
License:       ASL 2.0
URL:           https://github.com/netplex/json-smart-v1
Source0:       https://github.com/netplex/json-smart-v1/archive/%{commit}/%{name}-v1-%{commit}.tar.gz

BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: maven-local

BuildArch:     noarch
Source44: import.info

%description
Json-smart is a performance focused, JSON processor lib.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-v1-%{commit}

cp -p parent/pom.xml .
sed -i "s|<relativePath>../parent/pom.xml</relativePath>|<relativePath>../pom.xml</relativePath>|" %{name}/pom.xml
sed -i "s|<module>../json-smart</module>|<module>json-smart</module>|" pom.xml

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
cp -p %{name}/*.txt .

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog.txt readme.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_0.4.20140820jpp8
- unbootsrap build

