# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           h2
Version:        1.2.147
Release:        alt1_5jpp7
Summary:        Java SQL database

Group:          Development/Java
License:        EPL
URL:            http://www.h2database.com
Source0:        http://www.h2database.com/h2-2010-11-21.zip
Patch0:         fix-for-servlet25.patch
Patch1:         fix-build.patch
Patch2:         %{name}-jdbc-4.1-support.patch
BuildArch: noarch
BuildRequires:  ant
BuildRequires:  lucene >= 2.4
BuildRequires:  slf4j >= 1.5
BuildRequires:  felix-osgi-core >= 1.2
BuildRequires:  servlet25
Source44: import.info

%description
H2 is a the Java SQL database. The main features of H2 are:
* Very fast, open source, JDBC API
* Embedded and server modes; in-memory databases
* Browser based Console application
* Small footprint: around 1 MB jar file size 

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
pushd src/test/org/h2/test/unit
%patch0
popd
pushd src/tools/org/h2/build
%patch1
popd
%patch2 -p1
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
export JAVA_HOME=%{java_home}
chmod u+x build.sh
./build.sh jar docs

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p bin/h2-%{version}.jar   \
$RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp docs/javadoc  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc src/docsrc/html/license.html

%files javadoc
%{_javadocdir}/%{name}
%doc src/docsrc/html/license.html

%changelog
* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.147-alt1_5jpp7
- new version

