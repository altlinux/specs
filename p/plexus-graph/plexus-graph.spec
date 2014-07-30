# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# TODO: junit QA tests

Name:           plexus-graph
Version:        0.13.1
Release:        alt1_8jpp7
Summary:        Graph data structures manipulation library

Group:          Development/Java
License:        CPL
URL:            http://plexus.sourceforge.net/
Source0:        http://download.sourceforge.net/plexus/plexus-src-%{version}.tgz

Requires:       log4j apache-commons-collections jpackage-utils
BuildRequires:  %{requires} ant

BuildArch:      noarch
Source44: import.info

%description
Plexus is a Java library with specifications and implementations for
generic graph data structures. Like the Java Collections Framework,
vertices and edges are containers for arbitrary user-defined objects. 


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n plexus-%{version}


%build
CLASSPATH=$(build-classpath commons-collections log4j) ant dist javadoc


%install

# Directory structure
install -d $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# JARs and JavaDoc
install -m 644 build/dist/plexus-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -rp doc/javadoc/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc CHANGELOG LICENSE README


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_8jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_7jpp7
- new version

