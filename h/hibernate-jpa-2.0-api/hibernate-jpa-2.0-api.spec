Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name hibernate-jpa-2.0-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-jpa-2.0-api
Version:          1.0.1
Release:          alt3_18jpp8
Summary:          Java Persistence 2.0 (JSR 317) API
License:          EPL and BSD
URL:              http://www.hibernate.org/
# svn export http://anonsvn.jboss.org/repos/hibernate/jpa-api/tags/hibernate-jpa-2.0-api-1.0.1.Final/ hibernate-jpa-2.0-api-1.0.1.Final
# tar -zcvf hibernate-jpa-2.0-api-1.0.1.Final.tar.gz hibernate-jpa-2.0-api-1.0.1.Final
Source0:          %{name}-%{namedversion}.tar.gz
Patch0:           %{name}-%{namedversion}-encoding.patch
Patch1:           %{name}-%{namedversion}-osgi-manifest.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-release-plugin
Source44: import.info

%description
Hibernate definition of the Java Persistence 2.0 (JSR 317) API.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%patch1 -p1

%pom_xpath_remove pom:build/pom:extensions

%pom_remove_plugin :maven-source-plugin

# Fixing wrong-file-end-of-line-encoding
sed -i 's/\r//' src/main/javadoc/jdstyle.css

%build
%mvn_build

%install
# Fixing wrong-file-end-of-line-encoding
sed -i 's/\r//' target/site/apidocs/jdstyle.css
%mvn_install

# compat symlink for eclipselink-2.3.2-alt1_1jpp7, jasperreports-4.0.2-alt1_3jpp7
mkdir -p $RPM_BUILD_ROOT%{_javadir}/hibernate
ln -s ../%{name}.jar $RPM_BUILD_ROOT%{_javadir}/hibernate/%{name}.jar


%files -f .mfiles
%doc readme.txt
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_18jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_17jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_12jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_11jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_7jpp7
- rebuild with maven-local

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_7jpp7
- added OSGi info

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7jpp7
- added OSGi info

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp7
- new version

