# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		xjparse
Version:	1.0
Release:	alt1_9jpp7
Summary:	Wrapper for the Xerces XML Schema validator
Group:		Text tools
License:	ASL 2.0
URL:		http://nwalsh.com/java/xjparse
Source0:	http://nwalsh.com/java/xjparse/xjparse-src-%{version}.zip
Source1:	xjparse.sh
BuildArch:	noarch
BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:  xml-commons-resolver

Requires:	jpackage-utils
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
$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/xjparse

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_bindir}/xjparse

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_8jpp7
- new version

