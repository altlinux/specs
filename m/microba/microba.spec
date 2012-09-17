BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           microba
Version:        0.4.4.3
Release:        alt1_5jpp7
Summary:        Set of JFC (Swing) components

Group:          Development/Java
License:        BSD
URL:            http://microba.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}-full.zip

# sinjdoc doesn't do the job for us in f12, drag in real javadoc
BuildRequires:  java-devel-openjdk
BuildRequires:  jpackage-utils
BuildRequires:  jgraph
BuildRequires:  unzip
BuildRequires:  ant
BuildArch:      noarch
Source44: import.info

%description
Microba is a set of finely crafted & feature rich JFC (Swing) components,
including a date picker, calendar, gradient editor, palette editor and
jgraph bird view,


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -c
unzip -q %{name}-%{version}-sources.jar
find . -name '*.jar' -delete


%build
CLASSPATH=$(build-classpath jgraph) ant bin_release doc_release


%install
install -d $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT/%{_javadocdir}/%{name}-%{version}
install redist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
unzip -qd $RPM_BUILD_ROOT/%{_javadocdir}/%{name}-%{version} redist/%{name}-%{version}-javadoc.jar -x META-INF/\*


%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%doc license.txt


%files javadoc
%{_javadocdir}/%{name}-%{version}



%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_5jpp7
- new version

