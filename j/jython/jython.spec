Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
#BuildRequires(pre): j2se-jdbc = 1.4.2
BuildRequires: jline
# recommends
Requires: jline libreadline-java
AutoReq: yes, nopython
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global cpython_version    2.7
%global scm_tag            v2.7.1

# Turn off the brp-python-bytecompile script
# We generate JVM bytecode instead
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:                      jython
Version:                   2.7.1
Release:                   alt1_3jpp8
Summary:                   Jython is an implementation of Python written in pure Java.
License:                   ASL 1.1 and BSD and CNRI and JPython and Python
URL:                       http://www.jython.org/

# Use the included fetch-jython.sh script to generate the source drop
# Usage: sh fetch-jython.sh %%{scm_tag}
Source0:                   jython-%{scm_tag}.tar.xz
Source1:                   fetch-jython.sh

# Make the cache dir be in the user's home
Patch0:                    jython-cachedir.patch
# Avoid rebuilding and validating poms when installing maven stuff and don't gpg sign
Patch1:                    jython-dont-validate-pom.patch
# Dep for this feature is not yet in Fedora
Patch2:                    jython-no-carrotsearch-sizeof.patch
# Tweak launcher script
Patch3:                    jython-launcher.patch
# Fix failure with "import multiprocessing"
Patch4:                    jython-fix-multiprocessing.patch
# Fix tty detection
Patch5:                    jython-fix-tty-detection.patch

Requires:                  python >= %{cpython_version}
Requires:                  antlr32-java
Requires:                  apache-commons-compress
Requires:                  bouncycastle
Requires:                  bouncycastle-pkix
Requires:                  guava
Requires:                  objectweb-asm
Requires:                  jctools >= 2.0.2
Requires:                  jnr-constants
Requires:                  jnr-ffi
Requires:                  jnr-netdb
Requires:                  jnr-posix
Requires:                  jffi
Requires:                  jffi-native
Requires:                  jline
Requires:                  jansi
Requires:                  icu4j
Requires:                  netty >= 4.1.13
Requires:                  xerces-j2
# We build with ant, but install with maven
BuildRequires:             javapackages-local
BuildRequires:             ant
BuildRequires:             ant-junit
BuildRequires:             glassfish-servlet-api
BuildRequires:             python >= %{cpython_version}
BuildRequires:             antlr32-tool
BuildRequires:             apache-commons-compress
BuildRequires:             bouncycastle
BuildRequires:             bouncycastle-pkix
BuildRequires:             guava
BuildRequires:             objectweb-asm
BuildRequires:             jctools >= 2.0.2
BuildRequires:             jnr-constants
BuildRequires:             jnr-ffi
BuildRequires:             jnr-netdb
BuildRequires:             jnr-posix
BuildRequires:             jffi
BuildRequires:             jffi-native
BuildRequires:             jline
BuildRequires:             jansi
BuildRequires:             icu4j
BuildRequires:             netty >= 4.1.13
BuildRequires:             xerces-j2

BuildArch:                 noarch
Source44: import.info

%description
Jython is an implementation of the high-level, dynamic, object-oriented
language Python seamlessly integrated with the Java platform. The
predecessor to Jython, JPython, is certified as 100% Pure Java. Jython is
freely available for both commercial and non-commercial use and is
distributed with source code. Jython is complementary to Java and is
especially suited for the following tasks: Embedded scripting - Java
programmers can add the Jython libraries to their system to allow end
users to write simple or complicated scripts that add functionality to the
application. Interactive experimentation - Jython provides an interactive
interpreter that can be used to interact with Java packages or with
running Java applications. This allows programmers to experiment and debug
any Java system using Jython. Rapid application development - Python
programs are typically 2-10X shorter than the equivalent Java program.
This translates directly to increased programmer productivity. The
seamless interaction between Python and Java allows developers to freely
mix the two languages both during development and in shipping products.

%package javadoc
Group: Development/Java
Summary:           Javadoc for %{name}
# Obsoletes/Provides added in F25
Obsoletes:         %{name}-manual = %{version}-%{release}
Provides:          %{name}-manual < %{version}-%{release}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package demo
Group: Development/Java
Summary:           Demo for %{name}
Requires:          %{name} = %{?epoch:%epoch:}%{version}-%{release}
AutoReq: yes, nopython
#AutoProv: yes, nopython

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n jython-%{scm_tag}
%patch2 -R -p1
%patch0
%patch1
%patch3
%patch4 -p1
%patch5

rm -rf extlibs/*

# Disable doclint to fix javadoc generation
sed -i -e '/<javadoc/a additionalparam="-Xdoclint:none"' build.xml

# Broader guava compatibility
sed -i -e 's/CharMatcher\.ascii()/CharMatcher.ASCII/' \
  src/org/python/core/PyUnicode.java \
  src/org/python/core/PyBaseCode.java \
  src/org/python/core/Py.java

%build
# Symlink build-time libs
build-jar-repository -p -s extlibs \
  antlr32/antlr antlr32/antlr-runtime stringtemplate antlr \
  jffi jffi-native jnr-constants jnr-ffi jnr-netdb jnr-posix jline/jline jansi/jansi icu4j/icu4j \
  glassfish-servlet-api guava objectweb-asm/asm objectweb-asm/asm-commons objectweb-asm/asm-util \
  commons-compress junit hamcrest/core

ant \
  -Djython.dev.jar=jython.jar \
  -Dhas.repositories.connection=false \
  javatest javadoc

# remove shebangs from python files
find dist -type f -name '*.py' | xargs sed -i "s:#!\s*/usr.*::"

pushd maven
# generate maven pom
ant -Dproject.version=%{version} install
popd

# Symlink run-time libs
rm dist/javalib/*.jar
build-jar-repository -p -s dist/javalib antlr32/antlr-runtime-3.2 \
  objectweb-asm/asm objectweb-asm/asm-commons objectweb-asm/asm-util guava icu4j/icu4j \
  jffi jffi-native jnr-constants jnr-ffi jnr-netdb jnr-posix jline/jline jansi/jansi \
  netty/netty-buffer netty/netty-codec netty/netty-common netty/netty-handler netty/netty-resolver netty/netty-transport \
  jctools/jctools-core apache-commons-compress bcprov bcpkix xerces-j2

# request maven artifact installation
%mvn_artifact build/maven/jython-%{version}.pom dist/jython.jar
%mvn_alias org.python:jython org.python:jython-standalone

%install
# install maven artifacts
%mvn_install -J dist/Doc/javadoc

# jython home dir
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s %{_javadir}/%{name}/jython.jar $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr dist/javalib $RPM_BUILD_ROOT%{_datadir}/%{name}
rm dist/bin/jython_regrtest.bat
cp -pr dist/bin $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 dist/registry $RPM_BUILD_ROOT%{_datadir}/%{name}
# libs without tests
rm -rf dist/Lib/{distutils/tests,email/test,json/tests,test,unittest/test}
cp -pr dist/Lib $RPM_BUILD_ROOT%{_datadir}/%{name}
# demo
cp -pr Demo $RPM_BUILD_ROOT%{_datadir}/%{name}
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/Doc
ln -s %{_javadocdir}/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/Doc/javadoc

# scripts
install -d $RPM_BUILD_ROOT%{_bindir}
ln -s %{_datadir}/%{name}/bin/jython $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/jython.conf`
touch $RPM_BUILD_ROOT/etc/jython.conf

mkdir -p $RPM_BUILD_ROOT%{_var}/lib/jython/cachedir/packages
ln -s $(relative %{_var}/lib/jython/cachedir %{_datadir}/jython/) $RPM_BUILD_ROOT%{_datadir}/jython/

%post 

echo "creating jython cache..."
echo | /usr/bin/jython ||:

%preun
# cleanup
if [ "$1" -eq 0 ]
then
    rm %{_var}/lib/jython/cachedir/packages/*.{pkc,idx}
    find /usr/share/jython/Lib -name "*py.class" -delete
fi || :


%files -f .mfiles
%doc ACKNOWLEDGMENTS NEWS README.txt
%doc LICENSE.txt
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bin
%{_datadir}/%{name}/javalib
%{_datadir}/%{name}/jython.jar
%{_datadir}/%{name}/Lib
%{_datadir}/%{name}/registry
%config(noreplace,missingok) /etc/jython.conf
# package cache
%{_var}/lib/jython
# is it worth ghosting?
#%ghost %{_var}/lib/jython/cachedir/packages
%{_datadir}/jython/cachedir

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt
%{_datadir}/%{name}/Doc

%files demo
%doc LICENSE.txt
%{_datadir}/%{name}/Demo

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_3jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_0.3.b3jpp8
- fixed build

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_0.1.b3jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt7_14jpp7
- new release

* Wed Jul 30 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt7_12jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt7_11jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt6_11jpp7
- fc update

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt6_10jpp7
- applied repocop patches

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt5_10jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt5_8jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt5_7jpp6
- update to new release by jppimport

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt5_0.1.Release_2_2_1.1.2jpp5
- really added pom

* Sat Jan 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt4_0.1.Release_2_2_1.1.2jpp5
- restored pom

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt3_0.1.Release_2_2_1.1.2jpp5
- fix for missing /proc

* Thu Dec 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt2_2.1jpp5
- raised epoch: to 0 (alt rpm quirk)

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_0.1.Release_2_2_1.1.2jpp5
- converted from JPackage by jppimport script

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt4_0.rc2.1jpp5
- fixed build w/java5; 
- python cache creation is now optional

* Wed Jan 16 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt4_0.rc2.1jpp1.7
- rebuild with mysql-connector-java

* Sat Nov 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt3_0.rc2.1jpp1.7
- added cleanup of *py.class in %%postun

* Fri Nov 16 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_0.rc2.1jpp1.7
- added processing jars in %%post

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_0.rc2.1jpp1.7
- converted from JPackage by jppimport script

