Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:	SimplyHTML		
Version:	0.16.7
Release:	alt1_7jpp8
Summary:	Application and a java component for rich text processing

License:	GPLv2 and BSD
URL:		http://simplyhtml.sourceforge.net/
Source0:	http://downloads.sourceforge.net/simplyhtml/%{name}_src_0_16_07.tar.gz
Patch0:	simplyhtml-build.xml-classpath.patch
Patch1:	simplyhtml-manifest-classpath.patch

BuildRequires:	ant
BuildRequires:	gnu-regexp
BuildRequires:	javahelp2
BuildRequires: javapackages-tools rpm-build-java

Requires:	gnu-regexp
Requires:	javahelp2
Requires: javapackages-tools rpm-build-java

BuildArch: noarch
Source44: import.info

%description
SimplyHTML is an application for text processing. 
It stores documents as HTML files in combination with 
Cascading Style Sheets (CSS). SimplyHTML is not intended 
to be used as an editor for web pages. 
The application combines text processing features as known from 
popular word processors with a simple and generic way of 
storing textual information and styles.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n simplyhtml-0_16_07
%patch0 -p1
%patch1 -p1
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
export CLASSPATH=
CLASSPATH=
cd src
ant full-dist dist
cd ..

%install
mkdir -p %{buildroot}%{_javadir}/%{name}


cp -a dist/lib/SimplyHTML.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar

cp -a dist/lib/SimplyHTMLHelp.jar %{buildroot}%{_javadir}/%{name}/%{name}-help.jar

%jpackage_script com.lightdev.app.shtm.App "" "" gnu-regexp:javahelp2:SimplyHTML simplyhtml true

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a dist/help/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}
%{_bindir}/simplyhtml*
%doc gpl.txt 

%files javadoc
%{_javadocdir}/%{name}
%doc readme.txt


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_7jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_6jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_2jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_1jpp7
- new version

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.5-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_7jpp7
- new version

