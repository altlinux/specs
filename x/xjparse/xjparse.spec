Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:		xjparse
Version:	1.0
Release:	alt1_14jpp8
Summary:	Wrapper for the Xerces XML Schema validator
License:	ASL 2.0
URL:		http://nwalsh.com/java/xjparse
Source0:	http://nwalsh.com/java/xjparse/xjparse-src-%{version}.zip
BuildArch:	noarch
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:	ant
BuildRequires:  xml-commons-resolver

Requires: javapackages-tools rpm-build-java
Requires:	xml-commons-resolver
Source44: import.info

%description
The xjparse tool is a simple command-line wrapper for the Xerces XML Schema
validator. It accepts several options, notably one which specifies the set
of schemas to be used during validation.

%prep
%setup -qc
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

%build
export CLASSPATH=$(build-classpath xml-commons-resolver)
ant -f build.xml jar -verbose

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/xjparse.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_bindir}

%jpackage_script com.nwalsh.parsers.xjparse "" "" xjparse:xml-commons-resolver xjparse true

%files
%{_javadir}/%{name}.jar
%{_bindir}/xjparse

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_14jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8jpp7
- new version

