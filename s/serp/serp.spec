Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          serp
Version:       1.14.2
Release:       alt2_0.2.20120406cvsjpp7
Summary:       Bytecode manipulation framework
Group:         Development/Java
License:       BSD
Url:           http://serp.sourceforge.net/
# cvs -d:pserver:anonymous@serp.cvs.sourceforge.net:/cvsroot/serp login
# cvs -z3 -d:pserver:anonymous@serp.cvs.sourceforge.net:/cvsroot/serp  export -r HEAD serp
# tar czf serp-1.14.2-20120406-src-cvs.tar.gz serp
Source0:       serp-1.14.2-20120406-src-cvs.tar.gz
# change 
#  org.codehaus.mojo jxr-maven-plugin in org.apache.maven.plugins maven-jxr-plugin
#  org.codehaus.mojo surefire-report-maven-plugin in org.apache.maven.plugins >maven-surefire-report-plugin
Patch0:        serp-1.13.1-pom_xml.patch

BuildRequires: jpackage-utils

BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

BuildRequires: junit

Requires:      junit

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The goal of the serp bytecode framework is to tap the full 
power of bytecode modification while lowering its associated
costs. The framework provides a set of high-level APIs for 
manipulating all aspects of bytecode, from large-scale 
structures like class member fields to the individual 
instructions that comprise the code of methods. While in 
order to perform any advanced manipulation, some understanding 
of the class file format and especially of the JVM instruction 
set is necessary, the framework makes it as easy as possible
to enter the world of bytecode development.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p0
sed -i "s|pom.version|project.version|" pom.xml

%build

mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{name}:%{name}"

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.14.2-alt2_0.2.20120406cvsjpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14.2-alt1_0.2.20120406cvsjpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.13.1-alt8_1jpp5
- fixed build

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.13.1-alt7_1jpp5
- fixed build with maven3

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.13.1-alt6_1jpp5
- fixes for maven3

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.13.1-alt5_1jpp5
- fixes for java6 support

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.13.1-alt4_1jpp5
- fixed build

* Sun Feb 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.13.1-alt3_1jpp5
- fixed build with maven 2.0.7

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.13.1-alt2_1jpp5
- fixed velocity conflicts 

* Sun Oct 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.13.1-alt1_1jpp5
- jpackage 5.0

