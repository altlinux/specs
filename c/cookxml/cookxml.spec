# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             cookxml
Version:          3.0.2
Release:          alt1_3jpp7
Summary:          Dynamic XML data binding tool
Group:            Development/Java
License:          BSD
URL:              http://cookxml.yuanheng.org/

Source0:          http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_src-%{version}.zip
Source1:          %{name}-build.xml
Source2:          %{name}-pom.xml

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant

Requires:         jpackage-utils
Source44: import.info

%description
CookXml is a powerful general purpose dynamic XML data binding tool.
It is designed to be easy to use and easily extensible. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -qc

find . -name '*.jar' -exec rm -rf {} \;

sed -i 's/\r//' LICENSE

%build
cp %{SOURCE1} .
ant -f %{name}-build.xml cookxml_jar apidoc

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# JAVADOC
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp apidoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_3jpp7
- new version

