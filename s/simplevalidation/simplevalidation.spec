BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       simplevalidation
# upstream is pretty bad about version numbering
# this is a guess based on the version of a separate api "release" jar
Version:    1.0
Release:    alt2_0.6.SNAPSHOTjpp8
Summary:    A library for adding user-interface input validation to Swing applications
License:    GPLv2 or CDDL
URL:        http://kenai.com/projects/simplevalidation
# svn export -r331 https://svn.kenai.com/svn/simplevalidation~src/trunk/ simplevalidation-1.0-SNAPSHOT
# tar cJf simplevalidation-1.0-SNAPSHOT-20121212.tar.xz simplevalidation-1.0-SNAPSHOT
Source0:    http://kenai.com/projects/simplevalidation/downloads/download/validation-src.zip
Patch0:     simplevalidation-1.0-disable-doclint.patch

BuildArch:  noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel

BuildRequires:  ant
BuildRequires:  dos2unix

Requires:   jpackage-utils
Requires:   java
Source44: import.info

%description
This is a simple library for quickly adding validation code to Swing
user-interfaces. It handles validating user input when the user changes a
component's value, showing error messages and decorating components to
indicate which component is the source of the problem. It contains a large
number of built-in validators to handle most common situations, such as
validating numbers, email addresses, urls and so forth.

The primary goal is to make it easy to retrofit validation code on existing
UIs without needing to rewrite anything or add more than a few lines of code.

%package javadoc
Group: Development/Java
Summary:    Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}

%prep
%setup -q -c
%patch0 -p0

find . -name '*.class' -delete
find . -name '*.jar' -delete

%pom_xpath_remove "pom:project/pom:profiles" maven

%build

cd ValidationAPI
ant -Dplatforms.JDK_1.5.home=%{_jvmdir}/java jar javadoc

dos2unix dist/javadoc/package-list
dos2unix dist/javadoc/stylesheet.css

%install

mkdir -p %{buildroot}%{_javadir}
cp -a ValidationAPI/dist/ValidationAPI.jar %{buildroot}%{_javadir}/ValidationAPI.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 maven/pom.xml %{buildroot}%{_mavenpomdir}/JPP-ValidationAPI.pom
%add_maven_depmap JPP-ValidationAPI.pom ValidationAPI.jar -a "com.kenai:ValidationAPI"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a ValidationAPI/dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc ValidationAPI/doc/overview.html
%doc ValidationAPI/doc/duckLogo.png
%{_javadir}/ValidationAPI.jar
%{_mavenpomdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.6.SNAPSHOTjpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.6.SNAPSHOTjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.5.SNAPSHOTjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.4.SNAPSHOTjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.1.SNAPSHOTjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_4jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_3jpp7
- update to new release by jppimport

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_1jpp6
- new version

