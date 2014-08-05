Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             joni
Version:          1.1.9
Release:          alt1_1jpp7
Summary:          Java port of Oniguruma regexp library 
Group:            Development/Java
License:          MIT
URL:              http://github.com/jruby/%{name}
Source0:          https://github.com/jruby/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:           joni-add-build-lib-deps.patch
Patch1:           joni-remove-useless-wagon-dependency.patch

BuildRequires:    jcodings
BuildRequires:    jpackage-utils
BuildRequires:    junit
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    objectweb-asm4

Requires:         jcodings
Requires:         jpackage-utils
Requires:         objectweb-asm4

BuildArch:      noarch
Source44: import.info


%description
joni is a port of Oniguruma, a regular expressions library,
to java. It is used by jruby.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

mkdir build_lib
build-jar-repository -s -p build_lib objectweb-asm4/asm jcodings

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# fixes rpmlint warning about wrong-file-end-of-line-encoding
sed -i -e 's|\r||' test/org/joni/test/TestC.java
sed -i -e 's|\r||' test/org/joni/test/TestU.java
sed -i -e 's|\r||' test/org/joni/test/TestA.java

%files
%doc MANIFEST.MF
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.9-alt1_1jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_7jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_6jpp7
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp5
- fixes for java6 support

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- converted from JPackage by jppimport script

