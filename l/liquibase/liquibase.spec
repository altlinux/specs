# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java rpm-macros-fedora-compat
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: liquibase
Summary: Database Refactoring Tool
Version: 2.0.5
Release: alt1_2jpp7
License: ASL 2.0
Group: Databases

# Liquibase does not distribute source releases. To generate:
#   git clone https://github.com/liquibase/liquibase.git
#   cd liquibase-core/
#   git archive --prefix=liquibase-2.0.5/ liquibase-parent-2.0.5 liquibase-core/ samples/ changelog.txt LICENSE.txt | gzip >liquibase-2.0.5.tar.gz
Source0: %{name}-%{version}.tar.gz
Source1: build.xml
# Our custom launcher script:
Source2: liquibase

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

%prep
%setup -q
cp -p %SOURCE1 liquibase-core/
cp -p %SOURCE2 .

# Remove the Spring wrapper, this is not available as a build dependency:
rm liquibase-core/src/main/java/liquibase/integration/spring/SpringLiquibase.java

%build
cd liquibase-core
ant -Dlibdir=%{_datarootdir}/java clean package
javadoc -sourcepath src/main/java/ -d javadoc/ liquibase

%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
%{__install} -m 0644 -D -p liquibase-core/dist/lib/liquibase.jar %{buildroot}%{_javadir}
%{__install} -m 0755 -D -p liquibase %{buildroot}%{_bindir}
%{__install} -m 0755 -D -p liquibase %{buildroot}%{_bindir}
cp -R liquibase-core/javadoc %{buildroot}%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files
%doc samples changelog.txt LICENSE.txt
%{_javadocdir}/liquibase/*
%{_bindir}/%{name}
%{_javadir}/liquibase.jar
%config(noreplace,missingok) /etc/java/%{name}.conf


%changelog
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_2jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_8jpp7
- new version

