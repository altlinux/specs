Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xmlgraphics-commons
Version:        2.0.1
Release:        alt1_4jpp8
Epoch:          0
Summary:        XML Graphics Commons

License:        ASL 2.0
URL:            http://xmlgraphics.apache.org/
Source0:        http://apache.org/dist/xmlgraphics/commons/source/%{name}-%{version}-src.tar.gz

BuildArch:      noarch
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-local
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit >= 0:1.6
BuildRequires:  junit
BuildRequires:  apache-commons-io >= 1.3.1
BuildRequires:  apache-commons-logging >= 1.0.4
Requires:       java
Requires:       apache-commons-io >= 1.3.1
Requires:       apache-commons-logging >= 1.0.4
Source44: import.info

%description
Apache XML Graphics Commons is a library that consists of
several reusable components used by Apache Batik and
Apache FOP. Many of these components can easily be used
separately outside the domains of SVG and XSL-FO. You will
find components such as a PDF library, an RTF library,
Graphics2D implementations that let you generate PDF &
PostScript files, and much more.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q %{name}-%{version}
rm -f `find . -name "*.jar"`

# create pom from template
sed "s:@version@:%{version}:g" %{name}-pom-template.pom \
    > %{name}.pom


%build
export CLASSPATH=$(build-classpath commons-logging)
export OPT_JAR_LIST="ant/ant-junit junit"
pushd lib
ln -sf $(build-classpath commons-io) .
popd
ant package javadocs

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -Dpm 0644 build/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -pm 644 %{name}.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc LICENSE NOTICE README

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}


%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_4jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_2jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp7
- new version

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_6jpp7
- fc update

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_4jpp6
- fixed build with java 7

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_4jpp6
- new jpp relase

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp5
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

