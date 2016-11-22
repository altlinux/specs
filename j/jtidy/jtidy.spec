Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global jtidyversion r938

Name:             jtidy
Version:          1.0
Release:          alt3_0.22.20100930svn1125jpp8
Epoch:            3
Summary:          HTML syntax checker and pretty printer
License:          zlib
URL:              http://jtidy.sourceforge.net/
# svn export -r1125 https://jtidy.svn.sourceforge.net/svnroot/jtidy/trunk/jtidy/ jtidy
# tar caf jtidy.tar.xz jtidy
Source0:          %{name}.tar.xz
Source1:          %{name}.jtidy.script
BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    ant
BuildRequires:    xml-commons-apis

Requires: javapackages-tools rpm-build-java
Requires:         xml-commons-apis
Source44: import.info

%description
JTidy is a Java port of HTML Tidy, a HTML syntax checker and pretty
printer.  Like its non-Java cousin, JTidy can be used as a tool for
cleaning up malformed and faulty HTML.  In addition, JTidy provides a
DOM interface to the document that is being processed, which
effectively makes you able to use JTidy as a DOM parser for real-world
HTML.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}

%pom_remove_dep xerces:dom3-xml-apis


%build
ant -Dant.build.javac.source=1.4

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{name}-%{jtidyversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a net.sf.jtidy:%{name}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}/
cp -pr target/javadoc/* %{buildroot}%{_javadocdir}/%{name}/

# shell script
mkdir -p %{buildroot}%{_bindir}
cp -ap %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# ant.d
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
jtidy
EOF


%files -f .mfiles
%doc LICENSE.txt
%attr(755, root, root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt3_0.22.20100930svn1125jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt3_0.21.20100930svn1125jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt1_0.13.20100930svn1125jpp7
- new release

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt1_0.10.20100930svn1125jpp6
- new version

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 2:8.0-alt1_0.813.1jpp5
- jpackage 5.0

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 2:1.0-alt2.2_0.2.r7dev.1jpp5
- rebuild with java 5

