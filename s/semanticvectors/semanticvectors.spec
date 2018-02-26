Name: semanticvectors
Version: 1.26
Release: alt1

Summary: The Semantic Vectors Package
License: New BSD License
Group: Sciences/Other
Url: http://code.google.com/p/semanticvectors/
Packager: Kirill Maslinsky <kirill@altlinux.org>

Source: %name-%version.tar

# Common dependencies
BuildRequires(pre): rpm-build-java 
BuildPreReq: /proc jpackage-utils java-devel-default 
# Automatically added by buildreq on Sat Jun 06 2009
BuildRequires: ant junit lucene-demo tzdata

# Example dependency
Requires: lucene-demo

BuildArch: noarch

%description 
Semantic Vector indexes, created by applying a Random Projection
algorithm to term-document matrices created using Apache Lucene.  

The package creates a WordSpace model, of the kind developed by Stanford
University's Infomap Project and other researchers during the 1990s and early
2000s. Such models are designed to represent words and documents in terms of
underlying concepts, and as such can be used for many semantic (concept-aware)
matching tasks such as automatic thesaurus generation, knowledge
representation, and concept matching.

%package javadoc
Summary: Javadoc for %name
Group: Development/Documentation
Requires: java-common

%description javadoc
Javadoc for %name.

%prep
%setup -n %name-%version
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.zip" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;


%build
export CLASSPATH=$(build-classpath junit lucene2 lucene2-demos)
%ant \
	-Dbuild.sysclasspath=only \
	compile doc jardist

%install
# jars
install -d -m 755 %buildroot%_javadir
install -m 644 build/%name-%version.jar %buildroot%_javadir/
ln -s %name-%version.jar %buildroot%_javadir/%name.jar

# javadoc
install -d -m 755 %buildroot%_javadocdir/%name
cp -pr doc/* %buildroot%_javadocdir/%name
rm -rf doc/

%files
%doc AUTHORS LICENSE
%_javadir/*

%files javadoc
%doc %_javadocdir/%name

%changelog
* Thu Sep 15 2011 Kirill Maslinsky <kirill@altlinux.org> 1.26-alt1
- 1.26 (latest version compatible with lucene 2.9)

* Sat Jun 06 2009 Kirill Maslinsky <kirill@altlinux.org> 1.20-alt1
- Initial build for ALT Linux Sisyphus
