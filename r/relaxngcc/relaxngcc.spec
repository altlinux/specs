Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: relaxngcc
Version: 1.12
Release: alt2_5jpp7
Summary: RELAX NG Compiler Compiler
Group: Development/Java

License: ASL 1.1

Url: http://relaxngcc.sourceforge.net/en/index.htm

Source0: http://prdownloads.sourceforge.net/relaxngcc/relaxngcc-20031218.zip
Source1: %{name}-build.xml

BuildRequires: ant
BuildRequires: javacc
BuildRequires: jpackage-utils
BuildRequires: msv-msv
BuildRequires: msv-xsdlib
BuildRequires: relaxngDatatype
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: dos2unix

Requires: msv-msv
Requires: msv-xsdlib
Requires: relaxngDatatype
Requires: xerces-j2
Requires: xml-commons-apis

BuildArch: noarch
Source44: import.info


%description
RelaxNGCC is a tool for generating Java source code from a given RELAX NG
grammar. By embedding code fragments in the grammar like yacc or JavaCC, you can
take appropriate actions while parsing valid XML documents against the grammar.


%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains javadoc for %{name}.


%prep

# Prepare the original sources:
%setup -q -n relaxngcc-20031218

# Remove all the binary files:
find . -name '*.class' -delete
find . -name '*.jar' -delete

# Remove the sources that will be generated with JavaCC:
rm src/relaxngcc/javabody/*.java

# Remove to avoid dependency on commons-jelly:
rm src/relaxngcc/maven/ChildAntProjectTag.java

# Some of the sources don't use the correct end of line encoding, so to be
# conservative fix all of them:
find . -type f -exec dos2unix {} \;

# Some of the source files contain characters outside of the ASCII set that
# cause problems when compiling, so make sure that they are translated to
# ASCCI:
sources='
src/relaxngcc/builder/SwitchBlockInfo.java
'
for source in ${sources}
do
  native2ascii -encoding UTF8 ${source} ${source}
done


%build

# Populate the lib directory with references to the jar files required for the
# build:
mkdir lib
pushd lib
  ln -sf $(build-classpath msv-msv) .
  ln -sf $(build-classpath relaxngDatatype) .
  ln -sf $(build-classpath xerces-j2) .
  ln -sf $(build-classpath msv-xsdlib) .
  ln -sf $(build-classpath javacc) .
popd

# Put the ant build files in place:
cp %{SOURCE1} build.xml

# Run the ant build:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc


%install

# Jar files:
mkdir -p %{buildroot}%{_javadir}
install -pm 644 relaxngcc.jar %{buildroot}%{_javadir}/%{name}.jar

# Javadoc files:
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}/.


%files
%{_javadir}/*
%doc src/HOWTO-readAutomata.txt LICENSE.txt readme.txt
%doc doc/*


%files javadoc
%{_javadocdir}/*
%doc LICENSE.txt

%changelog
* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt2_5jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt2_4jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt2_2jpp6
- new jpp relase

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt2_1jpp5
- fixed build with java 5

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt1_1jpp1.7
- converted from JPackage by jppimport script

