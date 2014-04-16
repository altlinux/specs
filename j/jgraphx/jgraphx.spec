# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:           jgraphx
Version:        2.5.1.0
Release:        alt1
Summary:        Java Graph Drawing Component

Group:          Development/Java
License:        BSD
URL:            https://github.com/jgraph/jgraphx
Source0:        %{name}-%{version}.tar

BuildRequires:  ant
BuildRequires:  jpackage-utils
Requires:       jpackage-utils

BuildArch:      noarch

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
%setup
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
* Mon Apr 14 2014 Andrey Cherepanov <cas@altlinux.org> 2.5.1.0-alt1
- New version (ALT #30003)

* Tue May 28 2013 Andrey Cherepanov <cas@altlinux.org> 1.9.2.5-alt1_2jpp6.M60P.1
- Backport new version to p6 branch

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.2.5-alt1_2jpp7
- new version

