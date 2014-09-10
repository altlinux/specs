Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: jarjar
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cglib
Version:        2.2
Release:        alt2_17jpp7
Summary:        Code Generation Library for Java
License:        ASL 2.0 and BSD
Group:          Development/Java
Url:            http://cglib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.jar
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source2:        bnd.properties
# Remove the repackaging step that includes other jars into the final thing
Patch0:         %{name}-build_xml.patch

Requires: objectweb-asm

BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  objectweb-asm
BuildRequires:  unzip
BuildRequires:  aqute-bnd
BuildArch:      noarch
Source44: import.info
Source45: cglib-nodep-2.2.pom

%description
cglib is a powerful, high performance and quality code generation library 
for Java. It is used to extend Java classes and implements interfaces 
at runtime.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch
%description javadoc
Documentation for the cglib code generation library.

%prep
%setup -q -c %{name}-%{version}
rm lib/*.jar
# for jarjar
pushd lib
ln -s $(build-classpath objectweb-asm/asm) asm-3.1.jar
popd
#patch0 -p1

%build
export CLASSPATH=`build-classpath objectweb-asm jarjar`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc
# Convert to OSGi bundle
pushd dist
java -Dcglib.bundle.version="%{version}" \
  -jar $(build-classpath aqute-bnd) wrap -output %{name}-%{version}.bar -properties %{SOURCE2} %{name}-%{version}.jar
popd

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_mavenpomdir}
cp %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
# yes, this is really *.bar - aqute bnd created it
install -p -m 644 dist/%{name}-%{version}.bar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a net.sf.cglib:cglib
%add_maven_depmap -a cglib:cglib-full

cp -rp docs/* %{buildroot}%{_javadocdir}/%{name}
# jpp6 compat
cp -p dist/%{name}-nodep-%{version}.jar %{buildroot}%{_javadir}/%{name}-nodep.jar
cp -p %{SOURCE45} %{buildroot}%{_mavenpomdir}/JPP-%{name}-nodep.pom
%add_to_maven_depmap cglib cglib-nodep %{version} JPP %{name}-nodep
%add_to_maven_depmap net.sf.cglib cglib-nodep %{version} JPP %{name}-nodep


%files
%doc LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
# jpp6 compat
%{_javadir}/%{name}-nodep.jar
%{_mavenpomdir}/JPP-%{name}-nodep.pom


%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_17jpp7
- new release

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_15jpp7
- fc update

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_4jpp6
- added net.sf.cglib group id

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp6
- added pom

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_4jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_3jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_2jpp1.7
- converted from JPackage by jppimport script

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt4_2jpp1.7
- fixed provides to avoid unmets on cglib

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_2jpp1.7
- imported with jppimport script; note: bootstrapped version

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_2jpp1.7
- fixed cglib provides

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp1.7
- imported with jppimport script; note: bootstrapped version

