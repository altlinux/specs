Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             jtidy
Version:          1.0
Release:          alt3_0.29.20100930svn1125jpp8
Epoch:            3
Summary:          HTML syntax checker and pretty printer
License:          zlib
URL:              http://jtidy.sourceforge.net/
# svn export -r1125 https://jtidy.svn.sourceforge.net/svnroot/jtidy/trunk/jtidy/ jtidy
# tar caf jtidy.tar.xz jtidy
Source0:          %{name}.tar.xz
Source1:          %{name}.jtidy.script
BuildArch:        noarch

BuildRequires:    javapackages-local
BuildRequires:    ant
BuildRequires:    mvn(xerces:dom3-xml-apis)
# Explicit javapackages-tools requires since jtidy script uses
# /usr/share/java-utils/java-functions
Requires:         javapackages-tools
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
%mvn_file : %{name}
%mvn_alias : net.sf.jtidy:%{name}
%mvn_artifact pom.xml target/%{name}-*.jar

%mvn_install -J target/javadoc

# shell script
mkdir -p %{buildroot}%{_bindir}
cp -ap %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# ant.d
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
jtidy
EOF


%files -f .mfiles
%doc --no-dereference LICENSE.txt
%attr(755, root, root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt


%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt3_0.29.20100930svn1125jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt3_0.26.20100930svn1125jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt3_0.25.20100930svn1125jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt3_0.23.20100930svn1125jpp8
- new jpp release

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

