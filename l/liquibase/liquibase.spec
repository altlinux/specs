# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: liquibase
Summary: Database Refactoring Tool
Version: 3.0.7
Release: alt1_4jpp7
License: ASL 2.0
Group: Databases

# Liquibase does not distribute source releases. To generate:
#   git clone https://github.com/liquibase/liquibase.git
#   cd liquibase/
#   git archive --format=tar.gz --prefix=liquibase-3.0.7/ liquibase-parent-3.0.7 liquibase-core/ changelog.txt LICENSE.txt pom.xml > liquibase-3.0.7.tar.gz
Source0: %{name}-%{version}.tar.gz
Source1: build.xml

BuildRequires: jpackage-utils
%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires: servlet25
%else
BuildRequires: servlet3
%endif
BuildRequires: ant >= 0:1.7.0

Requires: jpackage-utils

BuildArch: noarch
Url: http://liquibase.org/
Source44: import.info

%description
LiquiBase is an open source (Apache 2.0 License), database-independent library
for tracking, managing and applying database changes. It is built on a simple
premise: All database changes are stored in a human readable but tracked in
source control.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q
cp -p %SOURCE1 %{name}-core/

# Remove the Spring wrapper; this is not available as a build dependency:
rm %{name}-core/src/main/java/liquibase/integration/spring/SpringLiquibase.java
rm %{name}-core/src/main/java/liquibase/integration/spring/MultiTenantSpringLiquibase.java

# Liquibase requires snakeyaml which is not available in EPEL.
rm %{name}-core/src/main/java/liquibase/parser/core/yaml/YamlChangeLogParser.java
rm %{name}-core/src/main/java/liquibase/parser/core/json/JsonChangeLogParser.java
rm %{name}-core/src/main/java/liquibase/serializer/core/yaml/YamlChangeLogSerializer.java
rm %{name}-core/src/main/java/liquibase/serializer/core/json/JsonChangeLogSerializer.java

%{__mkdir} -p %{name}-core/lib
build-jar-repository -s -p %{name}-core/lib ant servlet

%build
ant -f %{name}-core/build.xml clean package javadoc

%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -d -m 755 %{buildroot}%{_javadir}/%{name}
%{__install} -m 0644 -D -p %{name}-core/dist/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}/%{name}-core.jar
pushd %{buildroot}%{_javadir}
ln -sf %{name}/%{name}-core.jar %{name}.jar
popd
%jpackage_script liquibase.integration.commandline.Main "" "" %{name} %{name} true

# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp %{name}-core/dist/javadoc %{buildroot}%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files
%doc changelog.txt LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-core.jar
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.7-alt1_4jpp7
- update

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_2jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_8jpp7
- new version

