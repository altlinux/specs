Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: perl(FileHandle.pm) unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# GCJ note: findbugs currently cannot be compiled with GCJ.  There are several
# problems, most of which could be fixed with a little effort.  However,
# findbugs uses java.util.regex.Pattern.LITERAL, which is part of the Java 5
# specification, but Classpath does not support it.  This is a fatal problem.

Name:           findbugs
Version:        1.3.9
Release:        alt2_15jpp7
Summary:        Find bugs in Java code

Group:          Development/Java
License:        LGPLv2+
URL:            http://findbugs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-source.zip
Source1:        findbugs-ant
Source2:        findbugs-tools-README

# Versions will be fixed in a patch
Source3:        http://repo1.maven.org/maven2/net/sourceforge/findbugs/findbugs/1.3.7/findbugs-1.3.7.pom
Source4:        http://repo1.maven.org/maven2/net/sourceforge/findbugs/annotations/1.3.2/annotations-1.3.2.pom

# This patch has not been submitted upstream, as it contains Fedora-specific
# changes.  It looks in /usr/share/java for jar files at both compile time and
# run time, instead of in findbugs' lib directory.
Patch0:         findbugs-1.3.9-build.patch

# Build against ASM 3.3 instead of 3.1. Already changed upstream; see:
# http://code.google.com/p/findbugs/source/detail?r=12605
# http://code.google.com/p/findbugs/source/detail?r=12606
Patch1:         findbugs-asm-version.patch
%define asm_version 3.3

# Updates the version information in POMs, as we don't have up to date POM's :(
Patch2:         findbugs-1.3.9-pom.patch

# Fedora-specific patch: use Fedora JAR filenames
Patch3:         findbugs-jar-filenames.patch

# Fedora-specific patch to cope with removal of Class-Path & Main-Class entries
# from findbugs.jar manifest
Patch4:         findbugs-remove-classpath.patch

# Fedora-specific patch to allow FindBugs launcher scripts to be run from
# /bin or /usr/bin (#848612)
Patch5:         findbugs-home.patch

BuildArch:      noarch

BuildRequires:  findbugs-bcel
BuildRequires:  ant
BuildRequires:  docbook-style-xsl
BuildRequires:  apache-commons-lang
BuildRequires:  jaxen
BuildRequires:  jcip-annotations
BuildRequires:  jdepend
BuildRequires:  jFormatString
BuildRequires:  jpackage-utils
BuildRequires:  jsr-305
BuildRequires:  junit4
BuildRequires:  objectweb-asm >= %{asm_version}
BuildRequires:  perl
BuildRequires: /usr/bin/latex texlive-latex-recommended
BuildRequires:  texlive-publishers
Requires:       findbugs-bcel
Requires:       apache-commons-lang
Requires:       jaxen
Requires:       jcip-annotations
Requires:       jFormatString
Requires:       jpackage-utils
Requires:       jsr-305
Requires:       junit4
Requires:       objectweb-asm >= %{asm_version}
Source44: import.info

%description
Findbugs is a program which uses static analysis to look for bugs in Java code.
It can check for null pointer exceptions, multithreaded code errors, and other
bugs.

%package -n ant-findbugs
Group:          Development/Java
Summary:        Ant task for findbugs
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       ant

%description -n ant-findbugs
This package defines an ant task for findbugs for easy integration of findbugs
into your ant-controlled project.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc documentation for findbugs
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc documentation for findbugs.

%package tools
Group:          Development/Java
Summary:        Addon tools for findbugs
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       junit4

%description tools
This package contains additional tools for use with findbugs.  See
README.fedora for more information.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

cp -p %{SOURCE3} findbugs.pom
cp -p %{SOURCE4} annotations.pom

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

cp -p %{SOURCE2} README.fedora

# Make sure we don't accidentally use any existing JAR files
rm -f lib/*.jar

# Use the system jcip-annotations instead of building it in
rm -fr src/java5/net

# Get rid of code for Mac OS X that depends on a jar from Apple
rm -f src/java/edu/umd/cs/findbugs/gui/OSXAdapter.java
rm -f src/java5/edu/umd/cs/findbugs/gui2/OSXAdapter.java

# Turn on the executable bits for some auxiliary scripts
chmod a+x etc/summarizeBugs etc/diffBugSummaries design/architecture/mkdep.pl

# Remove Class-Path & Main-Class entries from findbugs.jar manifest
sed -i '/class-path/I d' etc/MANIFEST-findbugs.MF
sed -i '/Main-Class/ d' etc/MANIFEST-findbugs.MF

%build
# Build the class files
ant

# Build the javadocs
ant apiJavadoc

# Build the architecture PDF
pushd design/architecture
make depend
make
popd

# Package up the tools
cd build/classes
jar cf ../../lib/findbugs-tools.jar edu/umd/cs/findbugs/tools

%install
# Install the jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p lib/annotations.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-annotations-%{version}.jar
ln -s %{name}-annotations-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-annotations.jar
cp -p lib/%{name}-tools.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tools-%{version}.jar
ln -s %{name}-tools-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tools.jar
cp -p lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Install the ant task
mkdir -p $RPM_BUILD_ROOT%{_javadir}/ant
cp -p lib/%{name}-ant.jar $RPM_BUILD_ROOT%{_javadir}/ant/ant-%{name}-%{version}.jar
ln -s ant-%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/ant/ant-%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}

# Install the javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a apiJavaDoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install the scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for f in $(find bin -maxdepth 1 -type f \! -name '*.bat'); do
  cp -p $f $RPM_BUILD_ROOT%{_bindir}
done

# Install the shared files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a etc plugin $RPM_BUILD_ROOT%{_datadir}/%{name}

# Remove now unnecessary build-only manual files so %%doc doesn't get them
rm -f doc/manual*.xml doc/manual*.xsl

# Install poms
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp findbugs.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
cp annotations.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-annotations.pom

# Add depmaps
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-annotations.pom %{name}-annotations.jar

%files
%doc LICENSE.txt design/DecouplingFromBCEL.txt design/VisitingAndCaching.txt
%doc README.txt design/eclipse\ findbugs\ plugin\ features.sxw
%doc design/architecture/architecture.pdf doc
%{_bindir}/*
%{_datadir}/%{name}
%{_javadir}/findbugs-annotations*
%{_javadir}/findbugs-%{version}.jar
%{_javadir}/findbugs.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files -n ant-findbugs
%doc LICENSE.txt
%{_javadir}/ant/*
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc
%{_javadocdir}/*

%files tools
%doc LICENSE.txt README.fedora
%{_javadir}/findbugs-tools*

%changelog
* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt2_15jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt2_12jpp7
- converted from JPackage by jppimport script

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt2_5jpp6
- build with saxon6

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt1_5jpp6
- new release

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt1_2jpp6
- new version

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt2_2jpp5
- removed obsolete update_menus

