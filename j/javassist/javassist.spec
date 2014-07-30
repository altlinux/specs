Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           javassist
Version:        3.16.1
Release:        alt2_5jpp7
Summary:        The Java Programming Assistant provides simple Java bytecode manipulation
Group:          Development/Java
License:        MPLv1.1 or LGPLv2+ or ASL 2.0
URL:            http://www.csg.is.titech.ac.jp/~chiba/javassist/
Source0:        http://downloads.sourceforge.net/jboss/%{name}-%{version}-GA.zip
BuildArch:      noarch

BuildRequires:     jpackage-utils

BuildRequires:     maven-local
BuildRequires:     maven-compiler-plugin
BuildRequires:     maven-install-plugin
BuildRequires:     maven-jar-plugin
BuildRequires:     maven-javadoc-plugin
BuildRequires:     maven-resources-plugin
BuildRequires:     maven-surefire-plugin
BuildRequires:     maven-surefire-provider-junit
BuildRequires:     maven-source-plugin
BuildRequires:     maven-antrun-plugin
BuildRequires:     maven-doxia-sitetools

Requires:          jpackage-utils
Source44: import.info

%description
Javassist enables Java programs to define a new class at runtime and to
modify a class file when the JVM loads it. Unlike other similar
bytecode editors, Javassist provides two levels of API: source level
and bytecode level. If the users use the source-level API, they can
edit a class file without knowledge of the specifications of the Java
bytecode. The whole API is designed with only the vocabulary of the
Java language. You can even specify inserted bytecode in the form of
source text; Javassist compiles it on the fly. On the other hand, the
bytecode-level API allows the users to directly edit a class file as
other editors.

%package javadoc
Summary:           Javadocs for javassist
Group:             Development/Java
Requires:          jpackage-utils
BuildArch: noarch

%description javadoc
javassist development documentation.

%prep
%setup -q -n %{name}-%{version}-GA

mkdir runtest
find . -name \*.jar -type f -delete

%build
mvn-rpmbuild install javadoc:javadoc

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

# jar
install -d $RPM_BUILD_ROOT%{_javadir}
install -m644 target/%{name}-%{version}-GA.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "%{name}:%{name}"

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%doc License.html Readme.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc License.html
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.16.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.16.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.16.1-alt1_2jpp7
- new version

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.9.0-alt1_3jpp6
- new versuin

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.8.0-alt1_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.8.0-alt1_1jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_0.cr1.2jpp1.7
- converted from JPackage by jppimport script

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 3.0-alt1
- Initial build for ALT Linux Sisyphus

