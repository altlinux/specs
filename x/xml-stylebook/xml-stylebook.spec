Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          xml-stylebook
Version:       1.0
Release:       alt2_0.24.b3_xalan2.svn313293jpp8
Summary:       Apache XML Stylebook
License:       ASL 1.1
URL:           http://xml.apache.org/

# How to generate this tarball:
#  $ svn export http://svn.apache.org/repos/asf/xml/stylebook/trunk/@313293 xml-stylebook-1.0
#  $ tar zcf xml-stylebook-1.0.tar.gz xml-stylebook-1.0
Source0:       %{name}-%{version}.tar.gz

# Patch to fix an NPE in Xalan-J2's docs generation (from JPackage)
Patch0:        %{name}-image-printer.patch

# Patch the build script to build javadocs
Patch1:        %{name}-build-javadoc.patch

BuildArch:     noarch

BuildRequires: java-devel >= 1.6.0
BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: xml-commons-apis
BuildRequires: xerces-j2
%if !0%{?_module_build}
# Sans-serif font ("Arial") is required to build examples.
# XXX In modular world lets disable building examples until some fonts
# are properly modularized.
BuildRequires: fonts-ttf-dejavu
%endif

Requires:      xml-commons-apis
Requires:      xerces-j2
Source44: import.info
Provides: stylebook = %{version}
Obsoletes: stylebook < 1.0-alt1

%description
Apache XML Stylebook is a HTML documentation generator.

%package       javadoc
Group: Development/Java
Summary:       API documentation for %{name}
BuildArch: noarch

%description   javadoc
%{summary}.

%package       demo
Group: Development/Other
Summary:       Examples for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description   demo
Examples demonstrating the use of %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

# Remove bundled binaries
find -name *.jar -delete

# Don't include this sample theme because it contains an errant font
rm -r styles/christmas/

%build
ant -Dclasspath=$(build-classpath xml-commons-apis xerces-j2)

# Build the examples (this serves as a good test suite)
%if !0%{?_module_build}
pushd docs
rm run.bat
java -classpath "$(build-classpath xml-commons-apis xerces-j2):../bin/stylebook-%{version}-b3_xalan-2.jar" \
  org.apache.stylebook.StyleBook "targetDirectory=../results" book.xml ../styles/apachexml
popd
%endif

%install
# jars
install -pD -T bin/stylebook-%{version}-b3_xalan-2.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# examples
install -d %{buildroot}%{_datadir}/%{name}
cp -pr docs %{buildroot}%{_datadir}/%{name}
cp -pr styles %{buildroot}%{_datadir}/%{name}
%if !0%{?_module_build}
cp -pr results %{buildroot}%{_datadir}/%{name}
%endif
ln -s xml-stylebook.jar $RPM_BUILD_ROOT/%{_javadir}/stylebook.jar

%files
%{_javadir}/stylebook.jar
%doc LICENSE.txt
%{_javadir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name} 

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.24.b3_xalan2.svn313293jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.20.b3_xalan2.svn313293jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.18.b3_xalan2.svn313293jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.17.b3_xalan2.svn313293jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.14.b3_xalan2.svn313293jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.11.b3_xalan2.svn313293jpp7
- new release

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.10.b3_xalan2.svn313293jpp7
- fc update

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b3_xalan2.5jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b3_xalan2.3jpp5
- converted from JPackage by jppimport script

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b3_xalan2.2jpp1.7
- converted from JPackage by jppimport script

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt0.2_0.b3_xalan2.2jpp1.7
- converted from JPackage by jppimport script

* Tue Apr 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt0.2.b3
- Updated to the latest SVN snapshot
- Use macros from rpm-build-java
- Patch0: set source and target options for javac

* Fri Sep 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt0.1.b3
- Ported to Sisyphus from JPackage
