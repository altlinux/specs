# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jgraphx
Version:        1.9.2.5
Release:        alt1_2jpp7
Summary:        Java Graph Drawing Component

Group:          Development/Java
License:        BSD
URL:            http://www.jgraph.com/jgraph.html
Source0:        http://www.jgraph.com/downloads/jgraphx/archive/%{name}-1_9_2_5.zip

BuildRequires:  ant
BuildRequires:  jpackage-utils
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
JGraphX is the a powerful, easy-to-use and feature-rich graph drawing
component for Java. It is a rewrite of JGraph, also known as JGraph 6.


%package javadoc
Summary:        API Documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
JavaDoc documentation for %{name}


%prep
%setup -q -n %{name}
find -name '*.jar' -delete
rm -rf docs/api


%build
ant


%install

# Code
install -d $RPM_BUILD_ROOT%{_javadir}
install -p -m644 lib/%{name}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# API documentation
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}


%files
%{_javadir}/*
%doc license.txt


%files javadoc
%{_javadocdir}/*


%changelog
* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.2.5-alt1_2jpp7
- new version

