# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:	SimplyHTML		
Version:	0.16.5
Release:	alt1_1jpp7
Summary:	Application and a java component for rich text processing

Group:		Development/Java
License:	GPLv2 and BSD
URL:		http://simplyhtml.sourceforge.net/
Source0:	http://downloads.sourceforge.net/simplyhtml/%{name}_src_0_16_05.tar.gz
Source1:	simplyhtml.sh
Patch0:	simplyhtml-build.xml-classpath.patch
Patch1:	simplyhtml-manifest-classpath.patch


BuildRequires:	ant
BuildRequires:	gnu-regexp
BuildRequires:	javahelp2
BuildRequires:	jpackage-utils

Requires:	gnu-regexp
Requires:	javahelp2
Requires:	jpackage-utils

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
Summary: API documentation for %{name}
Group: Development/Java
Requires: %{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q -n simplyhtml-0_16_05
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


cp -a dist/lib/SimplyHTML.jar %{buildroot}%{_javadir}/%{name}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{name}/simplyhtml-%{version}.jar
ln -s simplyhtml-%{version}.jar %{buildroot}%{_javadir}/%{name}/simplyhtml.jar

cp -a dist/lib/SimplyHTMLHelp.jar %{buildroot}%{_javadir}/%{name}/%{name}-help-%{version}.jar
ln -s %{name}-help-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-help.jar
ln -s %{name}-help-%{version}.jar %{buildroot}%{_javadir}/%{name}/simplyhtmlhelp-%{version}.jar
ln -s simplyhtmlhelp-%{version}.jar %{buildroot}%{_javadir}/%{name}/SimplyHTMLHelp-%{version}.jar
ln -s simplyhtmlhelp-%{version}.jar %{buildroot}%{_javadir}/%{name}/simplyhtmlhelp.jar


install -pD -m755 -T %{SOURCE1} %{buildroot}%{_bindir}/%(basename %{SOURCE1})

mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -a dist/help/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/%{name}
%{_bindir}/simplyhtml*
%doc gpl.txt 

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}
%doc readme.txt





%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.5-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_7jpp7
- new version

