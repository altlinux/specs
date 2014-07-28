# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Summary:        High-Availability JDBC
Name:           ha-jdbc
Version:        2.0.16
Release:        alt1_0.5.rc1jpp7
Epoch:          0
License:        LGPLv2+
URL:            http://ha-jdbc.sourceforge.net/
Group:          Development/Java
Source0:        http://sourceforge.net/projects/ha-jdbc/files/HA-JDBC%%202.0%%20_%%20Stable/2.0.16-rc-1/ha-jdbc-2.0.16-rc-1-src.tar.gz
Patch0:         %{name}-build-fixes.patch
Patch1:         %{name}-jdk7.patch
Patch2:         %{name}-jgroups3.patch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  jgroups212
BuildRequires:  junit
BuildRequires:  slf4j
BuildRequires:  jibx
BuildRequires:  quartz
BuildRequires:  bcel
BuildRequires:  tomcat-servlet-3.0-api
Requires:       jpackage-utils >= 0:1.6
Requires:       jgroups212
Requires:       jibx
Requires:       quartz
Requires:       tomcat-servlet-3.0-api
Requires:       xml-commons-apis
Requires:       slf4j

BuildArch:      noarch
Source44: import.info

%description
High-Availability JDBC - a JDBC driver proxy that adds light-weight, 
transparent, fault tolerant clustering capability to any underlying
JDBC driver.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}-rc-1
# remove all binary libs
rm -rf lib lib-1.4 lib-1.5

# This code is no longer compatible with JGroups
# pushd src/net/sf/hajdbc/distributable
# rm AbstractMembershipListener.java
# rm DistributableDatabaseClusterDecorator.java
# rm DistributableLockManager.java
# rm DistributableStateManager.java
# popd

%patch0 -p1
%patch1 -p1
# %patch2 -p1

%build
export CLASSPATH=$( build-classpath jgroups212 jibx/jibx-run quartz slf4j/slf4j-api bcel jibx/jibx-bind tomcat-servlet-api )
ant jar-1.6
ant javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}-rc-1-jdk1.6.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr doc/src/content/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/%{name}*.jar

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.16-alt1_0.5.rc1jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.16-alt1_0.4.rc1jpp7
- new version

