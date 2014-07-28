# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global pkgname ST

Name:      stringtemplate4
Version:   4.0.4
Release:   alt2_5jpp7
Summary:   A Java template engine
URL:       http://www.stringtemplate.org/
Source0:   http://www.stringtemplate.org/download/%{pkgname}-%{version}-src.zip

# missing from source tarball so we add it here for now
Source1:   https://raw.github.com/antlr/stringtemplate4/master/src/org/stringtemplate/v4/compiler/STLexer.tokens
Source2:   https://raw.github.com/antlr/antlr/revision-3.4/runtime/Java/src/main/java/org/antlr/runtime/misc/DoubleKeyMap.java
Source3:   https://raw.github.com/antlr/stringtemplate4/master/pom.xml

License:   BSD
Group:     Development/Java
BuildArch: noarch

BuildRequires: ant-antlr3 ant-junit
BuildRequires: antlr3
BuildRequires: stringtemplate
# yup...it needs itself...
BuildRequires: stringtemplate4
# Standard deps
BuildRequires: jpackage-utils
Requires:      jpackage-utils
Source44: import.info

%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{pkgname}-%{version}

# copy sources missing in source archive into places
cp %{SOURCE1} src/org/stringtemplate/v4/compiler/STLexer.tokens
mkdir -p src/org/antlr/runtime/misc
# this is temporary until we build new antlr3 properly
cp %{SOURCE2} src/org/antlr/runtime/misc/DoubleKeyMap.java
cp %{SOURCE3} pom.xml

rm -rf lib/* target
ln -sf $(build-classpath antlr3) lib/antlr-3.3-complete.jar
ln -sf $(build-classpath ant/ant-antlr3) lib/ant-antlr3.jar

sed -i \
's:location="${ant-antlr3.jar}":location="/usr/share/java/antlr3-runtime.jar":' build.xml
sed -i 's:<path id="classpath">:<path id="classpath">\n<pathelement location="'\
$(build-classpath stringtemplate4)'"/>:' build.xml

%build
export CLASSPATH="`build-classpath ant/ant-antlr3 antlr3 antlr3-runtime antlr`"
ant build-jar

%javadoc -d javadoc -public `find build/src build/gen -name '*.java'`

%install
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 dist/ST-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}.jar


install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}/


%files
%doc LICENSE.txt README.txt
%{_datadir}/java/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_4jpp7
- new version

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

