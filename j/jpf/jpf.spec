# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define short_version 1.5

Name:		jpf
Version:	1.5.1
Release:	alt2_7jpp7
Summary:	Java Plug-in Framework
Group:		Development/Java
License:	LGPLv2
URL:		http://jpf.sourceforge.net/
BuildArch:	noarch

Source0:	http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.zip

Patch0:		jpf-1.5.1-build_javadoc.patch
Patch1:		jpf-1.5.1-no-class-manifest.patch

BuildRequires:	maven-local
BuildRequires:	jpackage-utils

BuildRequires:	apache-commons-logging

Requires:	jpackage-utils
Requires:	apache-commons-logging
Source44: import.info



%description
JPF is an  open source, LGPL licensed plug-in infrastructure library for
new or existing Java projects. JPF provides a runtime engine that
dynamically discovers and loads "plug-ins". A plug-in is a structured
component that describes itself to JPF using a "manifest". JPF maintains a
registry of available plug-ins and the functions they provide (via
extension points and extensions).

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:       jpackage-utils
BuildArch: noarch
%description javadoc
Documentation for the %{name} Java library.


%prep
%setup -q -c %{name}-%{version}
find . -name "*.jar" | xargs rm

# Build the javadoc all together, but not for the "tools" sub-package
# (it uses the unpackaged "jxp" library)
%patch0 -p1

# Don't put classpaths into the manifests
%patch1 -p1

sed -i "s|\r||g" license.txt


%build
mvn-rpmbuild install -f jpf-pom.xml
mvn-rpmbuild install -f jpf-boot-pom.xml
ant javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 jpf-pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 jpf-target/%{name}-%{short_version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar
install -pm 644 jpf-boot-pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-boot.pom
install -pm 644 jpf-boot-target/%{name}-boot-%{short_version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}-boot.jar
install -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/
cp -r build/docs/api ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-boot.pom %{name}-boot.jar


%files
%doc license.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/%{name}*
%{_mavenpomdir}/JPP-%{name}*.pom

%files javadoc
%doc license.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_5jpp7
- new version

