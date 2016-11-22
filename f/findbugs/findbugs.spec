Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global noupdatechecks_version 20140707gitcce19ac

Name:           findbugs
Version:        3.0.1
Release:        alt1_5jpp8
Summary:        Find bugs in Java code

Group:          Development/Other
License:        LGPLv2+
URL:            http://findbugs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-source.zip
Source1:        findbugs-ant
Source2:        findbugs-tools-README

Source3:        http://repo1.maven.org/maven2/com/google/code/findbugs/findbugs/3.0.1/findbugs-3.0.1.pom
Source4:        http://repo1.maven.org/maven2/com/google/code/findbugs/annotations/3.0.0/annotations-3.0.0.pom

# This archive contains the source for the noUpdateChecks plugin.
# It was created with:
#   $ git clone --bare https://code.google.com/p/findbugs
#   $ git --git-dir=findbugs.git archive --format tgz cce19ac plugins/noUpdateChecks -o noUpdateChecks-plugin-20140707gitcce19ac.tgz
Source5:        noUpdateChecks-plugin-%{noupdatechecks_version}.tgz

Source6:        http://repo1.maven.org/maven2/com/google/code/findbugs/findbugs-ant/3.0.0/findbugs-ant-3.0.0.pom

# This patch has not been submitted upstream, as it contains Fedora-specific
# changes.  It looks in /usr/share/java for jar files at compile time, instead
# of in findbugs' lib directory.
Patch0:         findbugs-build.patch

# Fedora-specific patch:
#  - Remove Class-Path entry from findbugs.jar manifest; use build-classpath
#    instead (#575632)
#  - Simplify shell fragment that determines findbugs_home (also fixes #848612)
Patch1:         findbugs-fedora.patch

# Fedora-specific patch to allow Ant task to work even though findbugs.jar has
# no Class-Path attribute in its manifest (bug #1080682)
Patch2:         findbugs-ant-task-classpath.patch

Patch3:         findbugs-manual.patch

BuildArch:      noarch

BuildRequires:  findbugs-bcel
BuildRequires:  ant
BuildRequires:  docbook-style-xsl
BuildRequires:  apache-commons-lang
BuildRequires:  dom4j
BuildRequires:  jaxen
BuildRequires:  jcip-annotations
BuildRequires:  jdepend
BuildRequires:  jFormatString
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  jsr-305
BuildRequires:  junit
BuildRequires:  objectweb-asm
BuildRequires:  perl
BuildRequires: /usr/bin/latex texlive-latex-recommended
BuildRequires:  texlive-publishers

# For generating HTML version of manual using xsltproc
BuildRequires: libxslt xsltproc
BuildRequires:  docbook-style-xsl

Requires:       findbugs-bcel
Requires:       apache-commons-lang
Requires:       jaxen
Requires:       jcip-annotations
Requires:       jFormatString
Requires: javapackages-tools rpm-build-java
Requires:       jsr-305
Requires:       junit
Requires:       objectweb-asm
Source44: import.info

%description
Findbugs is a program which uses static analysis to look for bugs in Java code.
It can check for null pointer exceptions, multithreaded code errors, and other
bugs.

%package -n ant-findbugs
Group:          Development/Java
Summary:        Ant task for findbugs
Requires:       %{name} = %{version}
Requires:       ant

%description -n ant-findbugs
This package defines an ant task for findbugs for easy integration of findbugs
into your ant-controlled project.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc documentation for findbugs
BuildArch: noarch

%description javadoc
Javadoc documentation for findbugs.

%package tools
Group:          Development/Other
Summary:        Addon tools for findbugs
Requires:       %{name} = %{version}
Requires:       junit

%description tools
This package contains additional tools for use with findbugs.  See
README.fedora for more information.

%prep
%setup -q
%setup -a 5
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

cp -p %{SOURCE2} README.fedora

# Make sure we don't accidentally use any existing JAR files
rm -f lib/*.jar

# Get rid of code for Mac OS X that depends on a jar from Apple
rm -f src/gui/edu/umd/cs/findbugs/gui2/OSXAdapter.java
%pom_remove_dep com.apple:AppleJavaExtensions %{SOURCE3}

%build
# Build the class files and docs
ant docs build

# Build the javadocs
ant apiJavadoc

# Build the architecture PDF
pushd design/architecture
make depend
make
popd

# Package up the tools
pushd build/classes
jar cf ../../lib/findbugs-tools.jar edu/umd/cs/findbugs/tools
popd

# Build the noUpdateChecks plugin
pushd plugins/noUpdateChecks
ant plugin-jar
popd

%install
# Install the jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p lib/annotations.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-annotations.jar
cp -p lib/%{name}-tools.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tools.jar
cp -p lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Install the ant task
mkdir -p $RPM_BUILD_ROOT%{_javadir}/ant
cp -p lib/%{name}-ant.jar $RPM_BUILD_ROOT%{_javadir}/ant/ant-%{name}.jar
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}

# Install the javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a apiJavaDoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# Install the scripts
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for f in $(find bin -maxdepth 1 -type f \! -name '*.bat' \! -name '*.ico'); do
  cp -p $f $RPM_BUILD_ROOT%{_bindir}
done

# Install the shared files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a etc plugin $RPM_BUILD_ROOT%{_datadir}/%{name}

# Install the noUpdateChecks plugin
cp -p plugins/noUpdateChecks/build/noUpdateChecks.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/plugin

# Create /usr/share/findbugs/lib directory containing symlinks to required JARs (bug #1080682)
# List is based on the Class-Path attribute in etc/MANIFEST-findbugs.MF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
for i in findbugs findbugs-bcel dom4j jaxen objectweb-asm/asm-debug-all jsr-305 \
  jFormatString apache-commons-lang; do
    ln -s %{_javadir}/$i.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
done

# Remove now unnecessary build-only manual files so %%doc doesn't get them
rm -f build/doc/manual*.xml build/doc/manual*.xsl

# Install poms
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
sed -i 's/3\.0\.0/3\.0\.1/g' %{SOURCE4} %{SOURCE6}
cp %{SOURCE3} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
cp %{SOURCE4} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-annotations.pom
cp %{SOURCE6} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.ant-ant-%{name}.pom

# Add depmaps
%add_maven_depmap -a net.sourceforge.findbugs:findbugs JPP-%{name}.pom %{name}.jar
%add_maven_depmap -a net.sourceforge.findbugs:annotations JPP-%{name}-annotations.pom %{name}-annotations.jar
%add_maven_depmap -a net.sourceforge.findbugs:findbugs-ant JPP.ant-ant-%{name}.pom ant/ant-findbugs.jar -f ant

# set_javadoc_namelink_check
%pre javadoc
path = "%{_javadocdir}/%{name}"
if [ -L $path ]; then
  rm -f $path
fi ||:



%files -f .mfiles
%doc licenses/LICENSE.txt design/DecouplingFromBCEL.txt design/VisitingAndCaching.txt
%doc README.txt design/eclipse\ findbugs\ plugin\ features.sxw
%doc design/architecture/architecture.pdf build/doc
%{_bindir}/*
%{_datadir}/%{name}

%files -n ant-findbugs -f .mfiles-ant
%doc licenses/LICENSE.txt
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc
%{_javadocdir}/*

%files tools
%doc licenses/LICENSE.txt README.fedora
%{_javadir}/findbugs-tools.jar

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_5jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

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

