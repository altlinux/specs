Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jargs
Version:        1.0
Release:        alt1_10jpp7
Summary:        Java command line option parsing suite

Group:          Development/Java
License:        BSD
URL:            http://jargs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  junit

Requires:       jpackage-utils
Source44: import.info

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.


%description
This project provides a convenient, compact, pre-packaged and 
comprehensively documented suite of command line option parsers 
for the use of Java programmers. 
Initially, parsing compatible with GNU-style 'getopt' is provided.

%prep
%setup -q
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;


%build
ant runtimejar javadoc


%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -p lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc README LICENCE TODO doc/CHANGES 
%{_javadir}/%{name}.jar


%files javadoc
%{_javadocdir}/%{name}/


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_10jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_9jpp7
- fc update

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp6
- new version

