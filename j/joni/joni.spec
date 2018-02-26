Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global  git_commit bb99ccb
%global cluster jruby

Name:             joni
Version:          1.1.3
Release:          alt1_6jpp7
Summary:          Java port of Oniguruma regexp library 
Group:            Development/Java
License:          MIT
URL:              http://github.com/%{cluster}/%{name}
Source0:          %{url}/tarball/%{version}/%{cluster}-%{name}-%{git_commit}.tar.gz
Patch0:           add_build_lib_deps.patch

BuildRequires:    ant
BuildRequires:    jcodings
BuildRequires:    jpackage-utils
BuildRequires:    objectweb-asm
Requires:         jpackage-utils
Requires:         objectweb-asm
Requires:         jcodings

BuildArch:      noarch
Source44: import.info


%description
joni is a port of Oniguruma, a regular expressions library,
to java. It is used by jruby.

%prep
%setup -q -n jruby-%{name}-bb99ccb
%patch0 -p0

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

mkdir build_lib
build-jar-repository -s -p build_lib objectweb-asm/asm jcodings

%build
ant build

%install

install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# fixes rpmlint warning about wrong-file-end-of-line-encoding
sed -i -e 's|\r||' test/org/joni/test/TestC.java
sed -i -e 's|\r||' test/org/joni/test/TestU.java
sed -i -e 's|\r||' test/org/joni/test/TestA.java


%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%doc build.xml
%doc test

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_6jpp7
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp5
- fixes for java6 support

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- converted from JPackage by jppimport script

