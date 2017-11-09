Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          serp
Version:       1.15.2
Release:       alt1_0.7.20150412cvsjpp8
Summary:       Byte-code manipulation framework
License:       BSD
Url:           http://serp.sourceforge.net/
# cvs -d:pserver:anonymous@serp.cvs.sourceforge.net:/cvsroot/serp login
# cvs -z3 -d:pserver:anonymous@serp.cvs.sourceforge.net:/cvsroot/serp  export -r HEAD serp
# tar cJf serp-1.15.2-20150412-cvs.tar.xz serp
Source0:       serp-1.15.2-20150412-cvs.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)

BuildArch:     noarch
Source44: import.info

%description
The goal of the serp byte-code framework is to tap the full 
power of byte-code modification while lowering its associated
costs. The framework provides a set of high-level APIs for 
manipulating all aspects of byte-code, from large-scale 
structures like class member fields to the individual 
instructions that comprise the code of methods. While in 
order to perform any advanced manipulation, some understanding 
of the class file format and especially of the JVM instruction 
set is necessary, the framework makes it as easy as possible
to enter the world of byte-code development.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%pom_remove_plugin :jxr-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :surefire-report-maven-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']"

%mvn_file :%{name} %{name}
%mvn_alias :%{name} %{name}:%{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.15.2-alt1_0.7.20150412cvsjpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.15.2-alt1_0.6.20150412cvsjpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.15.2-alt1_0.5.20150412cvsjpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.15.2-alt1_0.4.20150412cvsjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.15.2-alt1_0.2.20150412cvsjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.14.2-alt2_0.6.20120406cvsjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.14.2-alt2_0.4.20120406cvsjpp7
- new release

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

