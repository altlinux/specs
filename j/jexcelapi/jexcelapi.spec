BuildRequires: javapackages-local
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname jxl

Name:           jexcelapi
Version:        2.6.12
Release:        alt4_12jpp8
Summary:        A Java API to read, write and modify Excel spreadsheets
License:        LGPLv3
URL:            http://www.andykhan.com/jexcelapi
Source0:        http://www.andykhan.com/jexcelapi/jexcelapi_2_6_12.tar.gz
Source1:        http://repo1.maven.org/maven2/net/sourceforge/jexcelapi/jxl/2.6.12/jxl-2.6.12.pom
Patch0:         jexcelapi-build.patch
Requires:       log4j12
Requires:       jpackage-utils

BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  java-devel >= 1.5.0
BuildRequires:  ant
BuildRequires:  jflex
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:  log4j12
BuildArch:      noarch
Source44: import.info

%description
Jexcelapi allows Java developers to read Excel spreadsheets and generate Excel
spreadsheets dynamically. In addition, it contains a mechanism which allows
Java applications to read a spreadsheet, modify some cells and write the
modified spreadsheet.

Thanks to jexcelapi non Windows operating systems can run pure Java applications
which process and deliver Excel spreadsheets. Because it is Java, this API may
be invoked from within a servlet, thus giving access to Excel functionality
over internet and intranet web applications.

Features:
- Reads data from Excel 95, 97, 2000 workbooks
- Reads and writes formulas (Excel 97 and later only)
- Generates spreadsheets in Excel 97 format
- Supports font, number and date formatting
- Supports shading and coloring of cells
- Modifies existing worksheets


%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -n %{name} -q

# Clean up binary leftovers
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

# Clean up temp files (confuses javadoc 1.3.1)
find . -name ".#*" -exec rm -f {} \;

%patch0 -p1 -b .build
sed -i "s|%{_javadir}/jflex.jar|%{_javadir}/jflex/jflex.jar|" build/build.xml

%build
pushd build
cat > build.properties <<EOBP
logger=Log4jLogger
loggerClasspath=$(build-classpath log4j12-1.2.17)
EOBP

[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
export CLASSPATH=$(build-classpath jflex)

mkdir out
ant jxlall
popd

# html doc files should not be executable
chmod -x index.html tutorial.html

%install
# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 0644 jxl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/jxl.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/jxl.jar
%doc *.html

%files javadoc
%doc index.html
%{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt4_12jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_6jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_5jpp7
- fc update

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_4jpp7
- fc version

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt3_1jpp6
- target 5 build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt2_1jpp6
- fixed build with java 7

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.12-alt1_1jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt1_5jpp5
- new jpp release

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt1_4jpp1.7
- converted from JPackage by jppimport script

