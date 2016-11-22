Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          xml-stylebook
Version:       1.0
Release:       alt2_0.18.b3_xalan2.svn313293jpp8
Summary:       Apache XML Stylebook
Group:         Development/Other
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

BuildRequires: java-javadoc
BuildRequires: javapackages-tools rpm-build-java
BuildRequires: ant
BuildRequires: xml-commons-apis
BuildRequires: xerces-j2
BuildRequires: fonts-ttf-dejavu
Requires: javapackages-tools rpm-build-java
Requires:      xml-commons-apis
Requires:      xerces-j2
Source44: import.info
Provides: stylebook = %{version}
Obsoletes: stylebook < 1.0-alt1

%description
Apache XML Stylebook is a HTML documentation generator.

%package       javadoc
Summary:       API documentation for %{name}
Group:         Development/Java
Requires:      java-javadoc
BuildArch: noarch

%description   javadoc
%{summary}.

%package       demo
Summary:       Examples for %{name}
Group:         Development/Other
Requires:      %{name} = %{version}

%description   demo
Examples demonstrating the use of %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

# Remove bundled binaries
rm -r bin/*.jar

# Don't include this sample theme because it contains an errant font
rm -r styles/christmas/

# Make sure upstream hasn't sneaked in any jars we don't know about
JARS=""
for j in `find -name "*.jar"`; do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
   echo "These jars should be deleted and symlinked to system jars: $JARS"
   exit 1
fi

%build
ant

# Build the examples (this serves as a good test suite)
pushd docs
rm run.bat
java -classpath "$(build-classpath xml-commons-apis):$(build-classpath jaxp_parser_impl):../bin/stylebook-%{version}-b3_xalan-2.jar" \
  org.apache.stylebook.StyleBook "targetDirectory=../results" book.xml ../styles/apachexml
popd

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
cp -pr results %{buildroot}%{_datadir}/%{name}
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
