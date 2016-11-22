Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apacheds-jdbm
%define version 2.0.0
%global reltag -M3
%global namedversion %{version}%{?reltag}
Name:          apacheds-jdbm
Version:       2.0.0
Release:       alt1_0.5.M3jpp8
Summary:       ApacheDS specific JDBM Implementation
# This package is a fork of http://jdbm.sourceforge.net/ the original/more files
# are under BSD license.
License:       ASL 2.0 and BSD
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/jdbm/tags/2.0.0-M3/ apacheds-jdbm-2.0.0-M3
# tar cJf apacheds-jdbm-2.0.0-M3.tar.xz apacheds-jdbm-2.0.0-M3
Source0:       %{name}-%{namedversion}.tar.xz
# apacheds-jdbm package don't include the license file
# https://issues.apache.org/jira/browse/DIR-318
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
# wget -O jdbm-LICENSE.txt http://jdbm.cvs.sourceforge.net/viewvc/jdbm/jdbm/LICENSE.txt
Source2:       jdbm-LICENSE.txt

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:annotations)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)

BuildArch:     noarch
Source44: import.info

%description
A JDBM entry store which does not have any dependency on
core interfaces. The JDBM partition will use this store
and build on it to adapt this to server specific partition
interfaces. Having this separate module without
dependencies on core interfaces makes it easier to avoid
cyclic dependencies between modules. This is especially
important for use within the bootstrap plugin which needs
to build the schema partition used for bootstrapping the
server.

%package -n %{name}1
Group: Development/Java
Summary:       ApacheDS Original JDBM Implementation
# https://fedorahosted.org/fpc/ticket/564
Provides:      bundled(jdbm1)

%description -n %{name}1
Original JDBM Implementation.

%package -n %{name}2
Group: Development/Java
Summary:       ApacheDS JDBM Implementation MVCC

%description -n %{name}2
Specific JDBM Implementation with
Multi Version Concurrency Control (MVCC).

%package -n %{name}-parent
Group: Development/Java
Summary:       ApacheDS JDBM Parent POM

%description -n %{name}-parent
Specific ApacheDS JDBM Implementation - Parent POM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

%pom_remove_parent
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-site-plugin

%pom_remove_dep -r :junit-addons
%pom_change_dep -r findbugs:annotations com.google.code.findbugs:annotations

cp -p %{SOURCE1} .
cp -p %{SOURCE2} LICENSE.txt
sed -i 's/\r//' LICENSE*

%build

# No test dep org.apache.directory.junit:junit-addons:0.1
%mvn_build -s -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -n %{name}1 -f .mfiles-%{name}1
%doc LICENSE*

%files -n %{name}2 -f .mfiles-%{name}2
%doc LICENSE*

%files -n %{name}-parent -f .mfiles-%{name}-parent
%doc LICENSE*

%files javadoc -f .mfiles-javadoc
%doc LICENSE*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.5.M3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.4.M3jpp8
- new version

