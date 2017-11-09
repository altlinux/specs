Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		uddi4j
Version:	2.0.5
Release:	alt2_15jpp8
Summary:	Universal Description, Discovery and Integration registry API for Java
License:	IBM
URL:		http://sourceforge.net/projects/uddi4j/

Source0:	http://downloads.sf.net/project/uddi4j/uddi4j/%{version}/uddi4j-src-%{version}.zip
Source1:	%{name}-MANIFEST.MF

# Set javac path in build.xml
Patch0:		uddi4j-set-javac-path.patch

# A couple of utf8 incompatible chars prevent compile
Patch1:		uddi4j-remove-nonutf8-chars.patch

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	axis
BuildRequires:	xerces-j2
BuildRequires:	javapackages-local

Requires:	axis
Requires:	xerces-j2
Source44: import.info

%description
UDDI4J is a Java class library that provides an API to interact with a 
UDDI (Universal Description, Discovery and Integration) registry.

%package javadoc
Group: Development/Java
Summary:	Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

ln -s %{_datadir}/java/axis/saaj.jar
ln -s %{_datadir}/java/axis/axis.jar
ln -s %{_datadir}/java/axis/jaxrpc.jar
ln -s %{_datadir}/java/xerces-j2.jar xerces.jar

%build
ant compile javadocs

%install
# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/%{name}.jar META-INF/MANIFEST.MF

%mvn_artifact "org.uddi4j:uddi4j:%{version}" build/lib/uddi4j.jar
%mvn_file ":uddi4j" uddi4j
%mvn_install -J build/javadocs

%files -f .mfiles
%doc LICENSE.html
%doc ReleaseNotes.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.html

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt2_15jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt2_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt2_7jpp7
- new release

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.5-alt1_5jpp7
- new release

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_1jpp1.7
- fixed build with java 7

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_1jpp1.7
- converted from JPackage by jppimport script

