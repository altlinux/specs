# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ swig
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# Webapp is disabled, since Fedora does not have the Java Webapp guidelines
# finished yet: http://fedoraproject.org/wiki/PackagingDrafts/JavaWebApps
#def_with webapp
%bcond_with webapp

Name:           opengrok
Version:        0.9
Release:        alt1_5jpp7
Summary:        Source browser and indexer

Group:          Development/Java
License:        CDDL
URL:            http://hub.opensolaris.org/bin/view/Project+opengrok/
Source0:        http://hub.opensolaris.org/bin/download/Project+opengrok/files/%{name}-%{version}-src.tar.gz
Source1:        opengrok
Source2:        configuration.xml
Source3:        opengrok-README.Fedora.webapp
Source4:        opengrok-README.Fedora.nowebapp
Patch0:         opengrok-0.5-jrcs-import.patch
Patch1:         opengrok-0.9-nocplib.patch
Patch3:         opengrok-0.8.1-manifest-classpath.patch
Patch4:         opengrok-0.6-nooverview.patch
Patch6:         opengrok-0.9-jflex.patch
BuildArch:      noarch

%define common_reqs jakarta-oro ant bcel servlet lucene > 2 lucene-contrib > 2 swing-layout jpackage-utils javacc
Requires:       %{common_reqs}
Requires:       ctags
BuildRequires:  %{common_reqs}
BuildRequires:  jflex >= 1.4
BuildRequires:  java_cup
BuildRequires:  ant-nodeps
# FIXME: As of 0.6-hg275 this should build with java-1.5 again.
# This is just to prevent GCJ from attempting to build this.
# ant scripts from both jrcs and opengrok need to be fixed somehow
BuildRequires:  unzip
BuildRequires:  junit4
BuildRequires:  ant-junit
BuildRequires:  ctags
BuildRequires:  docbook2X
Source44: import.info

%description
OpenGrok is a fast and usable source code search and cross reference
engine, written in Java. It helps you search, cross-reference and navigate
your source tree. It can understand various program file formats and
version control histories like SCCS, RCS, CVS, Subversion and Mercurial.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.


%if %with webapp
%package tomcat5
Summary:        Source browser web application
Group:          Development/Java
Requires:       %{name} tomcat5

%description tomcat5
OpenGrok web application
%endif


%prep
%setup -q -n %{name}-%{version}-src
%{__unzip} -q ext/jrcs.zip
%patch0 -p1 -b .jrcs-import
%patch1 -p1 -b .nocplib
%patch3 -p1 -b .manifest-classpath
%patch4 -p1 -b .nooverview
%patch6 -p1 -b .jflex

# This is not strictly needed, but to nuke prebuilt stuff
# makes us feel warmer while building
find -name '*.jar' -o -name '*.class' -o -name '*.war' -delete

# jrcs' javacc directory
sed '
        s,\(property name="javacc.lib.dir" value="\)[^"]*,\1%{_javadir},;
        s,\(javacchome="\)[^"]*,\1${javacc.lib.dir},;
' -i jrcs/build.xml

# Default war configuration
sed 's,/var/opengrok/etc/configuration.xml,%{_sysconfdir}/%{name}/configuration.xml,' \
        -i web/WEB-INF/web.xml

# README.Fedora
%if %with webapp
cp %{SOURCE3} README.Fedora
%else
cp %{SOURCE4} README.Fedora
%endif


%build
pushd jrcs
CLASSPATH=$(build-classpath oro) %{ant} -v all

popd
CLASSPATH=$(build-classpath jflex java_cup) %{ant} -v jar javadoc                               \
        -Dfile.reference.org.apache.commons.jrcs.diff.jar=jrcs/lib/org.apache.commons.jrcs.diff.jar \
        -Dfile.reference.org.apache.commons.jrcs.rcs.jar=jrcs/lib/org.apache.commons.jrcs.rcs.jar \
        -Dfile.reference.lucene-core-2.2.0.jar=$(build-classpath lucene)                        \
        -Dfile.reference.lucene-spellchecker-2.2.0.jar=$(build-classpath lucene-contrib/lucene-spellchecker) \
        -Dfile.reference.ant.jar=$(build-classpath ant)                                         \
        -Dfile.reference.bcel-5.1.jar=$(build-classpath bcel)                                   \
        -Dfile.reference.jakarta-oro-2.0.8.jar=$(build-classpath jakarta-oro)                   \
        -Dfile.reference.servlet-api.jar=$(build-classpath servlet)                             \
        -Dfile.reference.swing-layout-0.9.jar=$(build-classpath swing-layout)

# SolBook is more-or-less DocBook subset, so this can be done safely
# FIXME: db2x_docbook2man output is not as nice as it should be
sed '
        s,^<!DOCTYPE.*,<!DOCTYPE refentry PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN" "docbookx.dtd">,
        s,^<?Pub Inc>,,
' dist/opengrok.1 |db2x_docbook2man -


%check
pushd jrcs
CLASSPATH=$(build-classpath junit4) %{ant} test

popd
#CLASSPATH=$(build-classpath jflex junit4) %{ant} test


%install

# directories

%if %with webapp
%define webappdir %{_var}/lib/tomcat5/webapps/source
install -d $RPM_BUILD_ROOT%{webappdir}/WEB-INF/lib
%endif

install -d $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jrcs
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -d $RPM_BUILD_ROOT%{_var}/lib/%{name}/data
install -d $RPM_BUILD_ROOT%{_var}/lib/%{name}/src
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps

# jar
install -p -m 644 dist/opengrok.jar $RPM_BUILD_ROOT%{_javadir}/opengrok-%{version}.jar
ln -sf opengrok-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/opengrok.jar

# jrcs
install -d $RPM_BUILD_ROOT%{_javadir}/opengrok-jrcs

install -p -m 644 jrcs/lib/org.apache.commons.jrcs.rcs.jar \
        $RPM_BUILD_ROOT%{_javadir}/opengrok-jrcs/org.apache.commons.jrcs.rcs-%{version}.jar
ln -sf org.apache.commons.jrcs.rcs-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/opengrok-jrcs/org.apache.commons.jrcs.rcs.jar

install -p -m 644 jrcs/lib/org.apache.commons.jrcs.diff.jar \
        $RPM_BUILD_ROOT%{_javadir}/opengrok-jrcs/org.apache.commons.jrcs.diff-%{version}.jar
ln -sf org.apache.commons.jrcs.diff-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/opengrok-jrcs/org.apache.commons.jrcs.diff.jar

# bin
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

# man
install -p -m 644 opengrok.1 $RPM_BUILD_ROOT%{_mandir}/man1

# javadoc
cp -pR dist/javadoc/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pR jrcs/doc/api/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}-jrcs

# Configuration file configuration.xml
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%if %with webapp
# Make love, not war!
unzip -q dist/source.war -d $RPM_BUILD_ROOT%{webappdir}
(IFS=:; for file in $(build-classpath                   \
        bcel jakarta-oro swing-layout                   \
        lucene lucene-contrib/lucene-spellchecker)      \
        %{_javadir}/opengrok.jar                        \
        %{_javadir}/opengrok-jrcs/org.apache.commons.jrcs.diff.jar \
        %{_javadir}/opengrok-jrcs/org.apache.commons.jrcs.rcs.jar
do
        ln -sf $file $RPM_BUILD_ROOT%{webappdir}/WEB-INF/lib
done)
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/opengrok.conf`
touch $RPM_BUILD_ROOT/etc/opengrok.conf


%files
%{_javadir}/*
%{_bindir}/opengrok
%{_mandir}/man1/opengrok.1*
%{_var}/lib/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/configuration.xml
%doc CHANGES.txt LICENSE.txt README.txt doc/EXAMPLE.txt README.Fedora
%config(noreplace,missingok) /etc/opengrok.conf


%files javadoc
%{_javadocdir}/*


%if %with webapp
%files tomcat5
%{webappdir}
%config(noreplace) %{webappdir}/WEB-INF/web.xml
%config(noreplace) %{webappdir}/index_body.html
%endif


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_5jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_4jpp7
- new version

