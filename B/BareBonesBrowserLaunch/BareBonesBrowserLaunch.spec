BuildRequires: /proc
BuildRequires: jpackage-compat
Name:       BareBonesBrowserLaunch
Version:    3.1
Release:    alt1_3jpp7
Summary:    Simple library to launch a browser window from Java
Group:      Development/Java
License:    Public Domain
URL:        http://www.centerkey.com/java/browser/
Source0:    http://www.centerkey.com/java/browser/myapp/real/bare-bones-browser-launch-%{version}.jar

BuildRequires:  jpackage-utils

Requires:   jpackage-utils
BuildArch:  noarch
Source44: import.info

%description
Utility class to open a web page from a Swing application in the user's 
default browser. Supports: Mac OS X, GNU/Linux, Unix, Windows XP


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}


%prep
%setup -q -c
find * -name *.class -exec rm -f {} \;


%build
%{javac} com/centerkey/utils/BareBonesBrowserLaunch.java
%{jar} -cf %{name}-%{version}.jar .


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
pushd .
cd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd
#javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pR doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_3jpp7
- fc build

