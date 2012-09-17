BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		xmlenc
Version:	0.52
Release:	alt1_10jpp7
Summary:	Light-weight XML output library for Java

Group:		Development/Java
License:	BSD
URL:		http://xmlenc.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz

BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	junit

Requires:	jpackage-utils
BuildArch:	noarch
Source44: import.info

%description
This library is a fast stream-based XML output library for Java. 
Main design goals are performance, simplicitity and pureness. 


%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}


%prep
%setup -q
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;
rm -Rf build/*


%build
ant \
	-Djavac.targetvm=1.5 \
	all


%install
install -d -m 755 %{buildroot}%{_javadir}/
cp -pR build/%{name}.jar %{buildroot}%{_javadir}/

install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pR build/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}/


%files
%{_javadir}/*
%doc CHANGES COPYRIGHT README THANKS


%files javadoc
%{_javadocdir}/%{name}-%{version}


%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_10jpp7
- new version

