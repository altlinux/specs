# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		signpost-core
Version:	1.2.1.2
Release:	alt1_3jpp7
Summary:	A simple, light-weight, and modular OAuth client library for the Java platform

Group:		Development/Java
License:	ASL 2.0
URL:		http://code.google.com/p/oauth-signpost/
Source0:	%{name}-%{version}.tar.gz
Source1:	build.xml
Source2:	%{name}-generate-tarball.sh
# Source built using the following commands : ./signpost-core-generate-tarball.sh 1.2.1.2
# tarball is built using "git clone https://github.com/kaeppler/signpost.git" and checkout with version parameter


BuildArch:	noarch 
BuildRequires:	jpackage-utils
BuildRequires:	ant
BuildRequires:	commons-codec
Requires:	jpackage-utils
Requires:	commons-codec
Source44: import.info

%description
Signpost is the easy and intuitive solution for signing HTTP messages on the 
Java platform in conformance with the OAuth Core 1.0a standard. 
Signpost follows a modular and flexible design, allowing you to combine it with
different HTTP messaging layers

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
cp %SOURCE1 .

# Remove pre-built JAR and class files
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

# Add depencies 
mkdir lib
build-jar-repository -s -p lib commons-codec


%build
ant javadoc
ant

%install
mkdir -p  %{buildroot}%{_javadir}

install -p -m 644 build/jar/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp javadoc/*  \
  %{buildroot}%{_javadocdir}/%{name}

%files
%doc
%{_javadir}/%{name}.jar


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1.2-alt1_3jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1.2-alt1_2jpp7
- new version

