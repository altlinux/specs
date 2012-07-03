BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             cookcc
Version:          0.3.3
Release:          alt1_5jpp7
Summary:          Lexer and Parser Generator
Group:            Development/Java
License:          BSD
URL:              http://code.google.com/p/cookcc/

# svn export -r 678 http://cookcc.googlecode.com/svn/trunk/ cookcc-0.3.3
# tar -J -cf cookcc-0.3.3.tar.xz cookcc-0.3.3
Source0:          %{name}-%{version}.tar.xz
Source1:          %{name}-%{version}-pom.xml

Patch0:           %{name}-%{version}-xerces.patch
Patch1:           %{name}-%{version}-buildxml.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    cookxml
BuildRequires:    freemarker
BuildRequires:    xerces-j2

Requires:         freemarker
Requires:         cookxml
Requires:         xerces-j2
Requires:         jpackage-utils
Source44: import.info

%description
CookCC is a lexer and parser (LALR (1)) generator project, combined.
It is written in Java, but the target languages can vary. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

find . -name '*.jar' -delete

%build
CLASSPATH=$(build-classpath xerces-j2 freemarker cookxml) ant cookcc_jar javadocs

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# APIDOCS
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE_cookcc.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE_cookcc.txt

%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_5jpp7
- new version

