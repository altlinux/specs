Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname threeten
Name:          time-api
Version:       0.6.4
Release:       alt2_13jpp8
Summary:       JSR-310 - Date and Time API
# GPLv2: src-openjdk/main/java/java/util/GregorianCalendar.java
#        src-openjdk/main/java/java/util/Calendar.java
#        src-openjdk/main/java/java/util/Date.java
# Public Domain:  src/main/tzdata/tzdata200*.tar.gz
License:       BSD and GPLv2+ and Public Domain
URL:           http://threeten.github.com/
Source0:       https://github.com/ThreeTen/%{oname}/archive/v%{version}.tar.gz
Source1:       %{name}-template-pom.xml
Patch0:        %{name}-0.6.4-dont-compile-openjdk-classes.patch
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: javapackages-tools
BuildRequires: maven-local

BuildRequires: ant
BuildRequires: emma
BuildRequires: testng

Requires:      jpackage-utils
BuildArch:     noarch

# https://fedorahosted.org/fpc/ticket/365
Provides:      bundled(openjdk8-javax-time) = %{version}-%{release}
Source44: import.info

%description
This JSR will provide a new and improved date and
time API for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

# Use system libraries
sed -i 's|src="${maven.ibiblio.url}/@{group}/@{artifact}/@{version}/@{artifact}-@{version}@{variant}.jar"|src="file:///usr/share/java/@{artifact}.jar"|' build.xml

%patch0 -p0

cp -p %{SOURCE1} pom.xml
sed -i "s|@VERSION@|%{version}|" pom.xml

sed -i 's/\r//' COPYRIGHT-ASSIGN.txt LICENSE.txt LICENSE_OpenJDK.txt LICENSE_Oracle.txt \
 OpenJDKChallenge.txt README.txt RELEASE-NOTES.txt TODO.txt

%build

%mvn_build -f

%install

%mvn_install

# https://fedoraproject.org/wiki/Packaging:Java#Packages_providing_APIs
mkdir -p %{buildroot}%{_javadir}/javax.time
ln -sf %{_javadir}/%{name}/%{name}.jar %{buildroot}%{_javadir}/javax.time/

%files -f .mfiles
%{_javadir}/javax.time/%{name}.jar
%doc COPYRIGHT-ASSIGN.txt LICENSE.txt LICENSE_OpenJDK.txt LICENSE_Oracle.txt
%doc OpenJDKChallenge.txt README.txt RELEASE-NOTES.txt TODO.txt

%files javadoc -f .mfiles-javadoc
%doc COPYRIGHT-ASSIGN.txt LICENSE.txt LICENSE_OpenJDK.txt LICENSE_Oracle.txt

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt2_13jpp8
- new version

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt2_11jpp8
- new version

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_9
- new version

