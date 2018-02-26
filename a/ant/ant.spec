Name: ant
Version: 1.8.3
Release: alt3

%def_enable check
%def_disable debug
%def_without bootstrap
%def_with repolib
%def_without stylebook
%def_without antlibhack
%def_without manifest_only
%def_without style_xsl

Summary: Platform-independent build tool for Java
Group: Development/Java
License: Apache Software License 2.0
URL: http://ant.apache.org/
Packager: Java Maintainers Team <java at packages.altlinux.org>

%global namedversion %{version}
%define major_version 1.8
%define repodir %{_javadir}/repository.jboss.com/org/apache/ant/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define ant_home	%_datadir/ant

Requires: java-devel /proc
Requires: jpackage-utils java-common
Requires: jaxp_parser_impl xml-commons-apis

BuildArch: noarch

Source: http://www.apache.org/dist/ant/source/apache-%name-%version-src.tar
Source1:        apache-ant-%{major_version}.ant.conf
Source2:        ant-component-info.xml
Source102: ant.sh.in

#Source5:        http://repo1.maven.org/maven2/org/apache/ant/ant-starteam/%version/ant-starteam-%{version}.pom
#Source6:        http://repo1.maven.org/maven2/org/apache/ant/ant-stylebook/%version/ant-stylebook-%{version}.pom
#Source7:        http://repo1.maven.org/maven2/org/apache/ant/ant-weblogic/%version/ant-weblogic-%{version}.pom

# Fix some places where copies of classes are included in the wrong jarfiles
#Patch0:         apache-ant-jars.patch
Patch1:         apache-ant-bz163689.patch
#Patch2:         apache-ant-gnu-classpath.patch
Patch3:         apache-ant-no-test-jar.patch
Patch4:         apache-ant-class-path-in-manifest.patch

Patch101:       ant-1.8.0-alt-script-cleanup.patch
Patch102:	ant-1.8.3-alt-javadoc-maxmemory.patch

BuildPreReq: rpm-build-java
BuildRequires: /proc
BuildRequires: java-devel >= 1.5.0
# for non-bootstrap
#BuildRequires: jaxp_parser_impl xml-commons-apis
# patch3 saves form junit
#BuildRequires: junit

# for scripts
#BuildRequires: python

Obsoletes:      %{name}-nodeps < %{version}
Provides:       %{name}-nodeps = %{version}
Obsoletes:      ant-nodeps < %{version}
Provides:       ant-nodeps = %{version}
Obsoletes:      %{name}-trax < %{version}
Provides:       %{name}-trax = %{version}
Obsoletes:      ant-trax < %{version}
Provides:       ant-trax = %{version}
%if_without stylebook
Provides:       ant-stylebook = %{version}
%endif
%if_without style_xsl
Obsoletes:      ant-style-xsl < %{version}
Provides:       ant-style-xsl = %{version}
%endif

Requires:      %name-testutil = %version-%release

%description
Ant is a Java based build tool.
Ant is used to build Jakarta & XML projects by the Apache Group.

%package testutil
Summary:        Test utility classes for %{name}
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}
Requires:       junit
Provides:       ant-testutil = 0:%{version}-%{release}

%description testutil
Test utility tasks for %{name}.

%package scripts
Summary:       Additional scripts for %{name}
Group:         Development/Other
Requires:      %name = %version-%release
AutoReq: yes, nopython

%description scripts
Additional Perl and Python scripts for ant,
a platform-independent build tool for Java.

%package manual
Summary: Documentation for ant
Group: Development/Java
Requires: %name = %version-%release
AutoReqProv: no

%description manual
Documentation for ant, a platform-independent build tool for Java.

%package javadoc
Summary: Javadoc for ant
Group: Development/Java
AutoReqProv: no
Provides: ant-task-reference = %version-%release
Obsoletes: ant-task-reference < 1.8.0

%description javadoc
Javadoc-generated documentation for ant, a platform-independent
build tool for Java.

%if_with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
# for jpp compatibility in req:
Epoch: 0

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%if_with style_xsl
%package style-xsl
Summary: XSL stylesheets for Ant
Group: Text tools

%description style-xsl
Useful XSL stylesheets included in the Ant distribution.
%endif

# --------------------------------
# merged from ant-optional
# --------------------------------
%if_without bootstrap
%package -n %{name}-optional
Summary: Optional tasks for Ant
Group: Development/Java

Requires: %name-antlr = %version-%release
Requires: %name-apache-bcel = %version-%release
Requires: %name-commons-logging = %version-%release
Requires: %name-commons-net = %version-%release
Requires: %name-jai = %version-%release
Requires: %name-apache-oro = %version-%release
Requires: %name-apache-regexp = %version-%release
Requires: %name-javamail = %version-%release
Requires: %name-jdepend = %version-%release
Requires: %name-jmf = %version-%release
Requires: %name-jsch = %version-%release
Requires: %name-junit = %version-%release
Requires: %name-apache-log4j = %version-%release
Requires: %name-stylebook = %version-%release
Requires: %name-swing = %version-%release
Requires: %name-trax = %version-%release
Requires: %name-apache-resolver = %version-%release
Requires: %name-apache-bsf = %version-%release

BuildRequires: jaxp_parser_impl 
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: antlr
BuildRequires: bcel
BuildRequires: jaf
BuildRequires: jai
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-net
BuildRequires: jakarta-oro
BuildRequires: regexp
BuildRequires: javamail
BuildRequires: jdepend
BuildRequires: jsch
BuildRequires: junit junit4
BuildRequires: log4j
BuildRequires: xml-stylebook
BuildRequires: xalan-j2 >= 2.0
BuildRequires: xml-commons-resolver12
BuildRequires: xerces-j2

%description -n %{name}-optional
Optional build tasks for ant, a platform-independent build tool for Java.

%if_with manifest_only
%package -n %{name}-manifest-only
Summary: Manifest-only jars for ant
Group: Development/Java
Requires: %name = %version
Provides: ant-icontract = 0:%version-%release
Provides: ant-netrexx = 0:%version-%release
Provides: ant-starteam = 0:%version-%release
%if_with stylebook
# we have full-fledged ant-stylebook package
%else
Provides: ant-stylebook = 0:%version-%release
%endif
Provides: ant-vaj = 0:%version-%release
Provides: ant-weblogic = 0:%version-%release
Provides: ant-xalan1 = 0:%version-%release
Provides: ant-xslp = 0:%version-%release

%description -n %{name}-manifest-only
Manifest-only jars for ant.
%endif

%package -n %{name}-antlr
Summary: AntLR task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: antlr

%description -n %{name}-antlr
AntLR task support for ant, a platform-independent build tool for Java.

%package -n %{name}-apache-bcel
Summary: BCEL task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: bcel
Provides: ant-bcel = %version-%release
Obsoletes: ant-bcel < 1.8.0

%description -n %{name}-apache-bcel
BCEL task support for ant, a platform-independent build tool for Java.

%package -n %{name}-commons-logging
Summary: Jakarta Commons Logging task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: jakarta-commons-logging

%description -n %{name}-commons-logging
Jakarta Commons Logging task support for ant,
a platform-independent build tool for Java.

%package -n %{name}-commons-net
Summary: Jakarta Commons Net task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: jakarta-commons-net

%description -n %{name}-commons-net
Jakarta Commons Net task support for ant,
a platform-independent build tool for Java.

%package -n %{name}-jai
Summary: JAI task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: jai

%description -n %{name}-jai
Java Advanced Imaging task support for ant,
a platform-independent build tool for Java.

%package -n %{name}-apache-oro
Summary: Jakarta ORO task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: jakarta-oro
Provides: ant-jakarta-oro = %version-%release
Obsoletes: ant-jakarta-oro < 1.8.0

%description -n %{name}-apache-oro
Jakarta ORO task support for ant, a platform-independent build tool for Java.

%package -n %{name}-apache-regexp
Summary: Jakarta Regexp task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: jakarta-regexp
Provides: ant-jakarta-regexp = %version-%release
Obsoletes: ant-jakarta-regexp < 1.8.0

%description -n %{name}-apache-regexp
Jakarta Regexp task support for ant,
a platform-independent build tool for Java.

%package apache-xalan2
Summary:        Optional apache xalan2 tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}
Requires:       regexp
BuildRequires:  regexp
Requires:       xalan-j2
Provides:       ant-apache-xalan2 = 0:%{version}-%{release}
Obsoletes:      %{name}-xalan2 < %{version}
Provides:       %{name}-xalan2 = %{version}
Obsoletes:      ant-xalan2 < %{version}
Provides:       ant-xalan2 = %{version}

%description apache-xalan2
Optional apache xalan2 tasks for %{name}.

%description apache-xalan2 -l fr
Taches apache xalan2 optionelles pour %{name}.

%package -n %{name}-javamail
Summary: Javamail task support for Ant
Group: Development/Java
Requires: %name = %version
Requires:       javamail >= 0:1.2-5jpp
Requires:       jaf >= 0:1.0.1-5jpp

%description -n %{name}-javamail
Javamail task support for ant, a platform-independent build tool for Java.

%package -n %{name}-jdepend
Summary: JDepend task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: jdepend

%description -n %{name}-jdepend
JDepend task support for ant, a platform-independent build tool for Java.

%package -n %{name}-jmf
Summary: JMF task support for Ant
Group: Development/Java
Requires: %name = %version

%description -n %{name}-jmf
Java Media Framework task support for ant,
a platform-independent build tool for Java.

%package -n %{name}-jsch
Summary: JSch task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: jsch

%description -n %{name}-jsch
JSch task support for ant, a platform-independent build tool for Java.

%package -n %{name}-junit
Summary: JUnit task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: junit

%description -n %{name}-junit
JUnit task support for ant, a platform-independent build tool for Java.

%package -n %{name}-junit4
Summary: JUnit task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: junit4

%description -n %{name}-junit4
JUnit task support for ant, a platform-independent build tool for Java.

%package -n %{name}-apache-log4j
Summary: Log4j task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: log4j
Provides: ant-log4j = %version-%release
Obsoletes: ant-log4j < 1.8.0

%description -n %{name}-apache-log4j
Log4j task support for ant, a platform-independent build tool for Java.

%if_with stylebook
%package -n %{name}-stylebook
Summary: Stylebook task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: xml-stylebook

%description -n %{name}-stylebook
Stylebook task support for ant, a platform-independent build tool for Java.
%endif

%package -n %{name}-swing
Summary: Swing support for Ant
Group: Development/Java
Requires: %name = %version

%description -n %{name}-swing
Swing support for ant, a platform-independent build tool for Java.

%package -n %{name}-apache-resolver
Summary: XML Commons Resolver task support for Ant
Group: Development/Java
Requires: %name = %version
Requires: xml-commons-resolver12
Provides: ant-xml-resolver = %version-%release
Obsoletes: ant-xml-resolver < 1.8.0

%description -n %{name}-apache-resolver
XML Commons Resolver task support for ant,
a platform-independent build tool for Java.

%package -n %{name}-apache-bsf
Summary: Optional apache bsf tasks for %name
Group: Development/Java
Requires: %name = %version
Requires: bsf
BuildRequires: bsf
Provides: ant-apache-bsf = 0:%version-%release
Provides: ant-bsf = %version-%release
Obsoletes: ant-bsf < 1.8.0

%description -n %{name}-apache-bsf
Optional apache bsf tasks for %name.

%endif
# --------------------------------


%prep
%setup -q -n apache-%name-%version
find docs -name '*.orig' -print0 | xargs -r0 rm -f

#Fixup version
find -name build.xml -o -name pom.xml | xargs sed -i -e s/-SNAPSHOT//

# Fix some places where copies of classes are included in the wrong jarfiles
#patch0 -p1

# Disable the style and xmlvalidate tasks on ppc64 and s390x (#163689).
%ifarch ppc64 s390x
%patch1 -p1 -b .sav1
%endif

# Update ant to work with recent versions of GNU Classpath
#patch2 -p1

# When bootstrapping, we don't have junit
%patch3

# Fix class-path-in-manifest rpmlint warning
%patch4

# script cleanup
%patch101 -p2

%patch102 -p1

mv LICENSE LICENSE.orig
mv KEYS KEYS.orig
%{_bindir}/iconv -f iso-8859-1 -t utf8 -o KEYS KEYS.orig
%{_bindir}/iconv -f iso-8859-1 -t utf8 -o LICENSE LICENSE.orig

perl -pi -e 's/\r$//g' manual/stylesheets/style.css manual/LICENSE manual/stylesheets/antmanual.css
perl -pi -e 's/\r$//g' LICENSE README WHATSNEW KEYS NOTICE
perl -pi -e 's/\r$//g' src/script/runant.py

# clean jar files
find . -name "*.jar" | %{_bindir}/xargs -t rm

# scripts: remove dos and os/2 scripts
rm src/script/*.bat
rm src/script/*.cmd

%build
#export JAVA_HOME=%{java_home}
#export CLASSPATH=$JAVA_HOME/lib/tools.jar
#sh ./build.sh --noconfig jars

mkdir -p lib/optional
%if_with bootstrap
CLASSPATH=$CLASSPATH:$(build-classpath jaxp_parser_impl xml-commons-apis junit junit4)
for jars in jaxp_parser_impl xml-commons-apis junit junit4; do
%else
for jars in \
xerces-j2 \
xml-commons-jaxp-1.3-apis \
antlr \
bcel \
jaf \
activation \
xml-stylebook \
xalan-j2 \
xalan-j2-serializer \
jai/jai_core \
jai/jai_codec \
javamail \
jdepend \
junit \
junit4 \
log4j \
oro \
regexp \
bsf \
commons-logging \
commons-net \
jsch \
xml-commons-resolver12 \
; do
%endif
	CLASSPATH=$(build-classpath $jars):$CLASSPATH
	ln -s $(build-classpath $jars) lib/optional/
done
export CLASSPATH
echo CLASSPATH

sh ./build.sh --noconfig -Dpom.version=%{version} \
%if_enabled debug
    -Doptimize=false \
%else
    -Ddebug=false \
%endif
    dist jars test-jar distribution

# TODO: fc sync
#remove empty netrexx jars. Due to missing dependencies they contain only manifests.
#rm -fr build/lib/ant-netrexx.jar
# -----------------------------------------------------------------------------

%install
# hack to copypaste from jpp spec; no need - ant distribution does the magic
#if ! [ -d java-repository/org/apache/ant/%{namedversion} ]; then
#   mkdir -p java-repository/org/apache/ant
#   for i in apache-ant-%{namedversion}/lib/*.pom; do
#      j=`basename $i`; k=`echo $j| sed -e s,.pom,,`;
#      install -Dm644 $i java-repository/org/apache/ant/$k/%{namedversion}/$k-%{namedversion}.pom
#   done
#fi
mkdir -p %{buildroot}%_bindir
mkdir -p %{buildroot}%_sysconfdir
install -d -m755 %{buildroot}%ant_home
install -d -m755 %{buildroot}%ant_home/etc
install -d -m755 %{buildroot}%ant_home/lib
install -d -m755 %{buildroot}%ant_home/bin

# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms

pushd java-repository
%{__cp} -p org/apache/ant/ant/%{namedversion}/ant-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%{__ln_s} %{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-nodeps.pom
%{__ln_s} %{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-trax.pom
%{__cp} -p org/apache/ant/ant-antlr/%{namedversion}/ant-antlr-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-antlr.pom
%{__cp} -p org/apache/ant/ant-apache-bcel/%{namedversion}/ant-apache-bcel-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-bcel.pom
%{__cp} -p org/apache/ant/ant-apache-bsf/%{namedversion}/ant-apache-bsf-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-bsf.pom
%{__cp} -p org/apache/ant/ant-apache-log4j/%{namedversion}/ant-apache-log4j-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-log4j.pom
%{__cp} -p org/apache/ant/ant-apache-oro/%{namedversion}/ant-apache-oro-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-oro.pom
%{__cp} -p org/apache/ant/ant-apache-regexp/%{namedversion}/ant-apache-regexp-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-regexp.pom
%{__cp} -p org/apache/ant/ant-apache-resolver/%{namedversion}/ant-apache-resolver-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-resolver.pom
%if 1
%{__cp} -p org/apache/ant/ant-apache-xalan2/%{namedversion}/ant-apache-xalan2-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-xalan2.pom
%endif
%{__cp} -p org/apache/ant/ant-commons-logging/%{namedversion}/ant-commons-logging-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-commons-logging.pom
%{__cp} -p org/apache/ant/ant-commons-net/%{namedversion}/ant-commons-net-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-commons-net.pom
%if 1
%{__cp} -p org/apache/ant/ant-jai/%{namedversion}/ant-jai-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-jai.pom
%endif
%{__cp} -p org/apache/ant/ant-javamail/%{namedversion}/ant-javamail-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-javamail.pom
%{__cp} -p org/apache/ant/ant-jdepend/%{namedversion}/ant-jdepend-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-jdepend.pom
%{__cp} -p org/apache/ant/ant-jmf/%{namedversion}/ant-jmf-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-jmf.pom
%{__cp} -p org/apache/ant/ant-jsch/%{namedversion}/ant-jsch-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-jsch.pom
%{__cp} -p org/apache/ant/ant-junit/%{namedversion}/ant-junit-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-junit.pom
%if 1
%{__cp} -p org/apache/ant/ant-junit4/%{namedversion}/ant-junit4-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-junit4.pom
%endif
%{__cp} -p org/apache/ant/ant-launcher/%{namedversion}/ant-launcher-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-launcher.pom
%if_with manifest_only
%{__cp} -p org/apache/ant/ant-netrexx/%{namedversion}/ant-netrexx-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-netrexx.pom
%endif
%{__cp} -p org/apache/ant/ant-parent/%{namedversion}/ant-parent-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%{__cp} -p org/apache/ant/ant-swing/%{namedversion}/ant-swing-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-swing.pom
%{__cp} -p org/apache/ant/ant-testutil/%{namedversion}/ant-testutil-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-testutil.pom
popd

install -p -m 644 build/lib/ant.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -p -m 644 build/lib/ant-bootstrap.jar %{buildroot}%{_javadir}/%{name}-bootstrap-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name} %{version} JPP %{name}
%add_to_maven_depmap ant %{name} %{version} JPP %{name}
install -p -m 644 build/lib/ant-launcher.jar %{buildroot}%{_javadir}/%{name}-launcher-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-launcher %{version} JPP %{name}-launcher
%add_to_maven_depmap ant %{name}-launcher %{version} JPP %{name}-launcher

install -p -m 644 build/lib/ant-testutil.jar %{buildroot}%{_javadir}/%{name}-testutil-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-testutil %{version} JPP %{name}-testutil
%add_to_maven_depmap ant %{name}-testutil %{version} JPP %{name}-testutil
install -p -m 644 build/lib/ant-jmf.jar %{buildroot}%{_javadir}/%{name}/ant-jmf-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-jmf %{version} JPP/%{name} ant-jmf
%add_to_maven_depmap ant %{name}-jmf %{version} JPP/%{name} ant-jmf
ln -s %{_javadir}/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/ant-nodeps-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-nodeps %{version} JPP/%{name} ant-nodeps
%add_to_maven_depmap ant %{name}-nodeps %{version} JPP/%{name} ant-nodeps
install -p -m 644 build/lib/ant-swing.jar %{buildroot}%{_javadir}/%{name}/ant-swing-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-swing %{version} JPP/%{name} ant-swing
%add_to_maven_depmap ant %{name}-swing %{version} JPP/%{name} ant-swing
ln -s %{_javadir}/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/ant-trax-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-trax %{version} JPP/%{name} ant-trax
%add_to_maven_depmap ant %{name}-trax %{version} JPP/%{name} ant-trax

# optional jars
%if_without bootstrap
%if_with manifest_only
cp -p build/lib/ant-icontract.jar %{buildroot}%{_javadir}/%{name}/ant-icontract-%{version}.jar
cp -p build/lib/ant-netrexx.jar %{buildroot}%{_javadir}/%{name}/ant-netrexx-%{version}.jar
%add_to_maven_depmap org.apache.ant ant-netrexx %{version} JPP/%{name} ant-netrexx
%add_to_maven_depmap ant ant-netrexx %{version} JPP/%{name} ant-netrexx
cp -p build/lib/ant-starteam.jar %{buildroot}%{_javadir}/%{name}/ant-starteam-%{version}.jar
%add_to_maven_depmap org.apache.ant ant-starteam %{version} JPP/%{name} ant-starteam
%add_to_maven_depmap ant ant-starteam %{version} JPP/%{name} ant-starteam
cp -p build/lib/ant-stylebook.jar %{buildroot}%{_javadir}/%{name}/ant-stylebook-%{version}.jar
%add_to_maven_depmap org.apache.ant ant-stylebook %{version} JPP/%{name} ant-stylebook
%add_to_maven_depmap ant ant-stylebook %{version} JPP/%{name} ant-stylebook
cp -p build/lib/ant-vaj.jar %{buildroot}%{_javadir}/%{name}/ant-vaj-%{version}.jar
cp -p build/lib/ant-weblogic.jar %{buildroot}%{_javadir}/%{name}/ant-weblogic-%{version}.jar
%add_to_maven_depmap org.apache.ant ant-weblogic %{version} JPP/%{name} ant-weblogic
%add_to_maven_depmap ant ant-weblogic %{version} JPP/%{name} ant-weblogic
cp -p build/lib/ant-xalan1.jar %{buildroot}%{_javadir}/%{name}/ant-xalan1-%{version}.jar
cp -p build/lib/ant-xslp.jar %{buildroot}%{_javadir}/%{name}/ant-xslp-%{version}.jar
%endif
%if_with stylebook
install -p -m 644 build/lib/ant-stylebook.jar %{buildroot}%{_javadir}/%{name}/ant-stylebook-%{version}.jar
%endif
install -p -m 644 build/lib/ant-antlr.jar %{buildroot}%{_javadir}/%{name}/ant-antlr-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-antlr %{version} JPP/%{name} ant-antlr
%add_to_maven_depmap ant %{name}-antlr %{version} JPP/%{name} ant-antlr
install -p -m 644 build/lib/ant-apache-bsf.jar %{buildroot}%{_javadir}/%{name}/ant-apache-bsf-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-apache-bsf %{version} JPP/%{name} ant-apache-bsf
%add_to_maven_depmap ant %{name}-apache-bsf %{version} JPP/%{name} ant-apache-bsf
install -p -m 644 build/lib/ant-apache-resolver.jar %{buildroot}%{_javadir}/%{name}/ant-apache-resolver-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-apache-resolver %{version} JPP/%{name} ant-apache-resolver
%add_to_maven_depmap ant %{name}-apache-resolver %{version} JPP/%{name} ant-apache-resolver
install -p -m 644 build/lib/ant-commons-logging.jar %{buildroot}%{_javadir}/%{name}/ant-commons-logging-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-commons-logging %{version} JPP/%{name} ant-commons-logging
%add_to_maven_depmap ant %{name}-commons-logging %{version} JPP/%{name} ant-commons-logging
install -p -m 644 build/lib/ant-commons-net.jar %{buildroot}%{_javadir}/%{name}/ant-commons-net-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-commons-net %{version} JPP/%{name} ant-commons-net
%add_to_maven_depmap ant %{name}-commons-net %{version} JPP/%{name} ant-commons-net
%if 1
install -p -m 644 build/lib/ant-jai.jar %{buildroot}%{_javadir}/%{name}/ant-jai-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-jai %{version} JPP/%{name} ant-jai
%add_to_maven_depmap ant %{name}-jai %{version} JPP/%{name} ant-jai
%endif
install -p -m 644 build/lib/ant-apache-bcel.jar %{buildroot}%{_javadir}/%{name}/ant-apache-bcel-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-apache-bcel %{version} JPP/%{name} ant-apache-bcel
%add_to_maven_depmap ant %{name}-apache-bcel %{version} JPP/%{name} ant-apache-bcel
install -p -m 644 build/lib/ant-apache-log4j.jar %{buildroot}%{_javadir}/%{name}/ant-apache-log4j-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-apache-log4j %{version} JPP/%{name} ant-apache-log4j
%add_to_maven_depmap ant %{name}-apache-log4j %{version} JPP/%{name} ant-apache-log4j
install -p -m 644 build/lib/ant-apache-oro.jar %{buildroot}%{_javadir}/%{name}/ant-apache-oro-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-apache-oro %{version} JPP/%{name} ant-apache-oro
%add_to_maven_depmap ant %{name}-apache-oro %{version} JPP/%{name} ant-apache-oro
install -p -m 644 build/lib/ant-apache-regexp.jar %{buildroot}%{_javadir}/%{name}/ant-apache-regexp-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-apache-regexp %{version} JPP/%{name} ant-apache-regexp
%add_to_maven_depmap ant %{name}-apache-regexp %{version} JPP/%{name} ant-apache-regexp
install -p -m 644 build/lib/ant-apache-xalan2.jar %{buildroot}%{_javadir}/%{name}/ant-apache-xalan2-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-apache-xalan2 %{version} JPP/%{name} ant-apache-xalan2
%add_to_maven_depmap ant %{name}-apache-xalan2 %{version} JPP/%{name} ant-apache-xalan2
ln -sf %{name}-apache-bcel.jar %{buildroot}%{_javadir}/%{name}/ant-jakarta-bcel.jar
ln -sf %{name}-apache-log4j.jar %{buildroot}%{_javadir}/%{name}/ant-jakarta-log4j.jar
ln -sf %{name}-apache-oro.jar %{buildroot}%{_javadir}/%{name}/ant-jakarta-oro.jar
ln -sf %{name}-apache-regexp.jar %{buildroot}%{_javadir}/%{name}/ant-jakarta-regexp.jar
install -p -m 644 build/lib/ant-javamail.jar %{buildroot}%{_javadir}/%{name}/ant-javamail-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-javamail %{version} JPP/%{name} ant-javamail
%add_to_maven_depmap ant %{name}-javamail %{version} JPP/%{name} ant-javamail
install -p -m 644 build/lib/ant-jdepend.jar %{buildroot}%{_javadir}/%{name}/ant-jdepend-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-jdepend %{version} JPP/%{name} ant-jdepend
%add_to_maven_depmap ant %{name}-jdepend %{version} JPP/%{name} ant-jdepend
install -p -m 644 build/lib/ant-jsch.jar %{buildroot}%{_javadir}/%{name}/ant-jsch-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-jsch %{version} JPP/%{name} ant-jsch
%add_to_maven_depmap ant %{name}-jsch %{version} JPP/%{name} ant-jsch
install -p -m 644 build/lib/ant-junit.jar %{buildroot}%{_javadir}/%{name}/ant-junit-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-junit %{version} JPP/%{name} ant-junit
%add_to_maven_depmap ant %{name}-junit %{version} JPP/%{name} ant-junit
install -p -m 644 build/lib/ant-junit4.jar %{buildroot}%{_javadir}/%{name}/ant-junit4-%{version}.jar
%add_to_maven_depmap org.apache.ant %{name}-junit4 %{version} JPP/%{name} ant-junit4
%add_to_maven_depmap ant %{name}-junit4 %{version} JPP/%{name} ant-junit4
%add_to_maven_depmap org.apache.ant %{name}-parent %{version} JPP %{name}-parent
%add_to_maven_depmap ant %{name}-parent %{version} JPP %{name}-parent
%endif

# jar aliases
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# scripts
%if %without bootstrap
install -m755 src/script/* %{buildroot}%{ant_home}/bin
%else
install -m755 src/script/ant{,Run} %{buildroot}%{ant_home}/bin
%endif

for script in %{buildroot}%{ant_home}/bin/*; do
    s=`/bin/basename ${script}`
    ln -s %{ant_home}/bin/${s} %{buildroot}%{_bindir}/${s}
done
#install -p -m 755 dist/bin/ant %{buildroot}%_bindir/
#install -p -m 755 dist/bin/antRun %{buildroot}%_bindir/
#install -p -m 755 dist/bin/*.p[ly] %{buildroot}%_bindir/

# configuration
install -p -m 644 %SOURCE1 %{buildroot}%_sysconfdir/ant.conf
install -d -m 755 %{buildroot}%_sysconfdir/ant.d

# stylesheets
cp -p src/etc/*.xsl %{buildroot}%{ant_home}/etc
# do we need them?
cp -a src/etc/checkstyle %{buildroot}%{ant_home}/etc

# javadoc
mkdir -p %{buildroot}%_javadocdir
cp -a build/javadocs %{buildroot}%_javadocdir/%name

# keep until ant.sh will be fixed
%if_with antlibhack
rmdir %{buildroot}%ant_home/lib
ln -snf $(relative %_javadir/%name %ant_home/) \
    %{buildroot}%ant_home/lib
cp %{buildroot}%_javadir/%name-%version.jar %{buildroot}%_javadir/%name/%name.jar 
cp %{buildroot}%_javadir/%name-launcher-%version.jar %{buildroot}%_javadir/%name/%name-launcher.jar
rm -f %{buildroot}/usr/bin/ant
install -m755 %SOURCE102 %{buildroot}/usr/bin/ant
%endif

# manifest-only
%if_with manifest_only
mkdir ./META-INF
cat > ./META-INF/MANIFEST.MF <<EOF
Manifest-Version: 1.0
Ant-Version: Apache Ant %version
Created-By: 1.4.2_13-b06 (Sun Microsystems Inc.)

Name: org/apache/tools/ant/taskdefs/optional/
Extension-name: org.apache.tools.ant
Specification-Title: Apache Ant
Specification-Version: %version
Specification-Vendor: Apache Software Foundation
Implementation-Title: org.apache.tools.ant
Implementation-Version: %version
Implementation-Vendor: Apache Software Foundation
EOF

for i in icontract netrexx starteam stylebook vaj weblogic xalan1 xslp; do
    if [ -e build/lib/ant-$i.jar ]; then
       	echo "manifest-only file exists; skipped"
    else
	jar cf %{buildroot}%_javadir/%{name}/ant-$i-%version.jar ./META-INF
	ln -s ant-$i-%version.jar %{buildroot}%_javadir/%{name}/ant-$i.jar
    fi
done
%endif

# OPT_JAR_LIST fragments
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
echo "%{name}/ant-jmf" > %{buildroot}%{_sysconfdir}/%{name}.d/jmf
echo "" > %{buildroot}%{_sysconfdir}/%{name}.d/nodeps
echo "%{name}/ant-swing" > %{buildroot}%{_sysconfdir}/%{name}.d/swing
ln -s nodeps %{buildroot}%{_sysconfdir}/%{name}.d/trax
%if_without bootstrap
echo "antlr %{name}/ant-antlr" > %{buildroot}%{_sysconfdir}/%{name}.d/antlr
echo "bsf %{name}/ant-apache-bsf" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-bsf
echo "xml-commons-resolver12 %{name}/ant-apache-resolver" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-resolver
echo "jakarta-commons-logging %{name}/ant-commons-logging" > %{buildroot}%{_sysconfdir}/%{name}.d/commons-logging
echo "jakarta-commons-net %{name}/ant-commons-net" > %{buildroot}%{_sysconfdir}/%{name}.d/commons-net
echo "jai %{name}/ant-jai" > %{buildroot}%{_sysconfdir}/%{name}.d/jai
echo "bcel %{name}/ant-apache-bcel" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-bcel
echo "log4j %{name}/ant-apache-log4j" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-log4j
echo "oro %{name}/ant-apache-oro" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-oro
echo "regexp %{name}/ant-apache-regexp" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-regexp
echo "xalan-j2 xalan-j2-serializer ant/ant-apache-xalan2" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-xalan2
echo "javamail jaf %{name}/ant-javamail" > %{buildroot}%{_sysconfdir}/%{name}.d/javamail
echo "jdepend %{name}/ant-jdepend" > %{buildroot}%{_sysconfdir}/%{name}.d/jdepend
echo "jsch %{name}/ant-jsch" > %{buildroot}%{_sysconfdir}/%{name}.d/jsch
echo "junit %{name}/ant-junit" > %{buildroot}%{_sysconfdir}/%{name}.d/junit
echo "junit4 %{name}/ant-junit4" > %{buildroot}%{_sysconfdir}/%{name}.d/junit4
# we have full-fledged ant-stylebook in ALT
echo "xml-stylebook %{name}/ant-stylebook" > %{buildroot}%{_sysconfdir}/ant.d/stylebook
echo "junit %{name}/ant-testutil" > %{buildroot}%{_sysconfdir}/%{name}.d/testutil
%endif

# -----------------------------------------------------------------------------

%if_with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
#{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH1} %{buildroot}%{repodirsrc}
#{__install} -p -m 644 %{PATCH2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH3} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/ant.pom
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/ant.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-launcher.pom %{buildroot}%{repodirlib}/ant-launcher.pom
%{__cp} -p %{buildroot}%{_javadir}/%{name}-launcher-%{version}.jar %{buildroot}%{repodirlib}/ant-launcher.jar
%if_without bootstrap
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-ant-junit.pom %{buildroot}%{repodirlib}/ant-junit.pom
%{__cp} -p %{buildroot}%{_javadir}/%{name}/ant-junit-%{version}.jar %{buildroot}%{repodirlib}/ant-junit.jar
%endif
%endif

# -----------------------------------------------------------------------------

%files
%doc NOTICE LICENSE README WHATSNEW
%_bindir/ant
%_bindir/antRun
%config(noreplace) %_sysconfdir/ant.conf
%dir %_sysconfdir/ant.d
%dir %ant_home
%dir %ant_home/bin
%dir %ant_home/etc
%{ant_home}/etc/ant-update.xsl
%{ant_home}/etc/changelog.xsl
%{ant_home}/etc/coverage-frames.xsl
%{ant_home}/etc/log.xsl
%{ant_home}/etc/tagdiff.xsl
%{ant_home}/etc/junit-frames-xalan1.xsl
%{ant_home}/etc/mmetrics-frames.xsl
%{ant_home}/etc/printFailingTests.xsl
%{ant_home}/etc/checkstyle
%ant_home/bin/*
%if_without bootstrap
%{ant_home}/etc/common2master.xsl
%endif
%ant_home/lib
%dir %_javadir/%name
%_javadir/ant-%version.jar
%_javadir/ant.jar
%_javadir/ant-bootstrap-%version.jar
%_javadir/ant-bootstrap.jar
%_javadir/ant-launcher-%version.jar
%_javadir/ant-launcher.jar
# poms
%{_mavendepmapfragdir}/%{name}
%{_datadir}/maven2/poms/JPP-%{name}-launcher.pom
%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_datadir}/maven2/poms/JPP.%{name}-ant-nodeps.pom
%{_datadir}/maven2/poms/JPP.%{name}-ant-trax.pom
%{_javadir}/%{name}/ant-nodeps.jar
%{_javadir}/%{name}/ant-nodeps-%{version}.jar
%{_javadir}/%{name}/ant-trax.jar
%{_javadir}/%{name}/ant-trax-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/nodeps
%config(noreplace) %{_sysconfdir}/%{name}.d/trax
%if_with antlibhack
%_javadir/%{name}/ant.jar
%_javadir/%{name}/ant-launcher.jar
%endif

%files testutil
%{_javadir}/%{name}-testutil-%{version}.jar
%{_javadir}/%{name}-testutil.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/testutil
%{_datadir}/maven2/poms/JPP-%{name}-testutil.pom

%files scripts
%_bindir/*.pl
%_bindir/*.py

%files manual 
#-f manual.list
%doc manual/*

%files javadoc
%doc %_javadocdir/%name

%if_with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%if_with style_xsl
%files style-xsl
%ant_home/etc/*.xsl
%ant_home/etc/checkstyle
%endif

# --------------------------------
# merged from ant-optional
# --------------------------------
%if_without bootstrap
%files -n %{name}-optional

%if_with manifest_only
%files -n %{name}-manifest-only
#defattr(0644,root,root,0755)
%_javadir/%{name}/ant-icontract-%version.jar
%_javadir/%{name}/ant-icontract.jar
%_javadir/%{name}/ant-netrexx-%version.jar
%_javadir/%{name}/ant-netrexx.jar
%_javadir/%{name}/ant-starteam-%version.jar
%_javadir/%{name}/ant-starteam.jar
%if_with stylebook
# we have full-fledged ant-stylebook package
%else
%_javadir/%{name}/ant-stylebook-%version.jar
%_javadir/%{name}/ant-stylebook.jar
%endif
%_javadir/%{name}/ant-vaj-%version.jar
%_javadir/%{name}/ant-vaj.jar
%_javadir/%{name}/ant-weblogic-%version.jar
%_javadir/%{name}/ant-weblogic.jar
%_javadir/%{name}/ant-xalan1-%version.jar
%_javadir/%{name}/ant-xalan1.jar
%_javadir/%{name}/ant-xslp-%version.jar
%_javadir/%{name}/ant-xslp.jar
%{_datadir}/maven2/poms/JPP.%{name}-ant-netrexx.pom
%endif

%files -n %{name}-antlr
%_javadir/%{name}/ant-antlr.jar
%_javadir/%{name}/ant-antlr-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/antlr
%{_datadir}/maven2/poms/JPP.%{name}-ant-antlr.pom

%files -n %{name}-apache-bcel
%_javadir/%{name}/ant-apache-bcel.jar
%_javadir/%{name}/ant-apache-bcel-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-bcel
%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-bcel.pom
# old ant compat symlink
%_javadir/%{name}/ant-jakarta-bcel.jar

%files -n %{name}-commons-logging
%_javadir/%{name}/ant-commons-logging.jar
%_javadir/%{name}/ant-commons-logging-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/commons-logging
%{_datadir}/maven2/poms/JPP.%{name}-ant-commons-logging.pom

%files -n %{name}-commons-net
%_javadir/%{name}/ant-commons-net.jar
%_javadir/%{name}/ant-commons-net-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/commons-net
%{_datadir}/maven2/poms/JPP.%{name}-ant-commons-net.pom

%files -n %{name}-jai
%_javadir/%{name}/ant-jai.jar
%_javadir/%{name}/ant-jai-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/jai
%{_datadir}/maven2/poms/JPP.%{name}-ant-jai.pom

%files -n %{name}-apache-oro
%_javadir/%{name}/ant-apache-oro.jar
%_javadir/%{name}/ant-apache-oro-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-oro
%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-oro.pom
# old ant compat symlink
%_javadir/%{name}/ant-jakarta-oro.jar

%files -n %{name}-apache-regexp
%_javadir/%{name}/ant-apache-regexp.jar
%_javadir/%{name}/ant-apache-regexp-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-regexp
%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-regexp.pom
# old ant compat symlink
%_javadir/%{name}/ant-jakarta-regexp.jar

%files apache-xalan2
%{_javadir}/%{name}/ant-apache-xalan2.jar
%_javadir/%{name}/ant-apache-xalan2-%version.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-xalan2
%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-xalan2.pom

%files -n %{name}-javamail
%_javadir/%{name}/ant-javamail.jar
%_javadir/%{name}/ant-javamail-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/javamail
%{_datadir}/maven2/poms/JPP.%{name}-ant-javamail.pom

%files -n %{name}-jdepend
%_javadir/%{name}/ant-jdepend.jar
%_javadir/%{name}/ant-jdepend-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/jdepend
%{_datadir}/maven2/poms/JPP.%{name}-ant-jdepend.pom

%files -n %{name}-jmf
%_javadir/%{name}/ant-jmf.jar
%_javadir/%{name}/ant-jmf-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/jmf
%{_datadir}/maven2/poms/JPP.%{name}-ant-jmf.pom

%files -n %{name}-jsch
%_javadir/%{name}/ant-jsch.jar
%_javadir/%{name}/ant-jsch-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/jsch
%{_datadir}/maven2/poms/JPP.%{name}-ant-jsch.pom

%files -n %{name}-junit
%_javadir/%{name}/ant-junit.jar
%_javadir/%{name}/ant-junit-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/junit
%{_datadir}/maven2/poms/JPP.%{name}-ant-junit.pom

%files -n %{name}-junit4
%_javadir/%{name}/ant-junit4.jar
%_javadir/%{name}/ant-junit4-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/junit4
%{_datadir}/maven2/poms/JPP.%{name}-ant-junit4.pom

%files -n %{name}-apache-log4j
%_javadir/%{name}/ant-apache-log4j.jar
%_javadir/%{name}/ant-apache-log4j-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-log4j
%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-log4j.pom
# old ant compat symlink
%_javadir/%{name}/ant-jakarta-log4j.jar

%if_with stylebook
%files -n %{name}-stylebook
%_javadir/%{name}/ant-stylebook.jar
%_javadir/%{name}/ant-stylebook-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/stylebook
%endif stylebook

%files -n %{name}-swing
%_javadir/%{name}/ant-swing.jar
%_javadir/%{name}/ant-swing-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/swing
%{_datadir}/maven2/poms/JPP.%{name}-ant-swing.pom

%files -n %{name}-apache-resolver
%_javadir/%{name}/ant-apache-resolver.jar
%_javadir/%{name}/ant-apache-resolver-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-resolver
%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-resolver.pom

%files -n %{name}-apache-bsf
%_javadir/%{name}/ant-apache-bsf.jar
%_javadir/%{name}/ant-apache-bsf-%version.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-bsf
%{_datadir}/maven2/poms/JPP.%{name}-ant-apache-bsf.pom
%endif
# --------------------------------

%changelog
* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt3
- added ant: jpp depmaps

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt2
- added ant-junit4 subpackage

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1
- new version

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt4
- fixed ant-testutil thanks to Alexey Morozov.

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2-alt3.1
- Rebuild with Python-2.7

* Thu Sep 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt3
- added ant-testutil

* Sat Mar 05 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2
- bugfix

* Fri Mar 04 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2
- added alt-specific -Djavadoc.maxmemory patch

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt6
- added alt-specific -Djavadoc.maxmemory patch

* Sun Sep 05 2010 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt5
- reverted to 1.7.1.

* Thu Sep 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt4test
- 1.8.0 pretest for sisyphus rebuild

* Thu Sep 02 2010 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1
- new version

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt3
- reverted back to alt2 due to regression
- TODO: fix ant script

* Tue Feb 17 2009 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2
- fixed ANTLIB

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1
- new version
- moved the rest of docs to manual

* Mon Nov 03 2008 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt12
- added support for /etc/ant.d parts in /usr/bin/ant

* Tue Sep 30 2008 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt11
- updated classpath (replaced obsolete jars that no more exist)
  fixed ant-junit: serializer class not found bug.
- replaced obsolete java-common functions w/jpackage ones
- added /etc/ant.d 
- added maven2 poms

* Thu Aug 14 2008 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt10
- removed obsolete j2se requires

* Tue Feb 12 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt9
- Packaged %_javadir/%name
- Built with python 2.5

* Tue Dec 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt8
- Bumped release to match ant-optional

* Mon Jun 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt7
- Bumped release to match ant-optional

* Sat Jun 16 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt6
- Bumped release to match ant-optional

* Sat Jun 09 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt5
- Bumped release to match ant-optional

* Thu May 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt4
- Added symlinks for %_javadir/ant.jar and %_javadir/ant-launcher.jar
- Fixed ant launcher to use %%_datadir/java-common instead of %%_libdir/java-common

* Sat May 05 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt3
- Added Provides: ant-nodeps for jpackage compatibility

* Thu Feb 22 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt2
- Fix Java executable search (#10857)

* Sun Feb 04 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt1.1
- Raised release to match release of ant-optional package

* Sat Feb 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.7.0-alt1
- New version

* Sat Mar 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.5-alt2
- Dropped buildtime dependency on xml-commons-apis and jaxp_parser_impl,
  require JDK >= 1.4 instead
- Added serializer.jar from Xalan to the runtime classpath

* Mon Jun 06 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.5-alt1
- New upstream release

* Sat May 28 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.4-alt1
- New upstream release

* Fri Apr 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.3-alt1
- New upstream release
- rpm-build-java cosmetics
- Removed ANT_HOME setting from /etc/ant.conf as it interfered
  with the bootstrap script

* Wed Mar 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.2-alt3.1
- Rebuilt with python-2.4.

* Wed Jan 12 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.2-alt3
- Rebuild for ant-optional

* Sat Aug 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.2-alt2
- BuildRequire /proc

* Wed Jul 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.2-alt1
- New upstream release

* Mon Jun 14 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.1-alt2
- Add all the optional library dependencies to classpath in the launcher script
- Conditionally disable debug info (off by default)

* Sun Feb 22 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.1-alt1
- Updated to the upstream release 1.6.1
- Updated the ant script
- Substitute directory names in the apt script
- Set config(noreplace) attribute for /etc/apt.conf

* Fri Oct 24 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.4-alt2
- Shipped ant-optional off to a separate spec with extensive build dependencies
- Take scripts from dist/bin where <fixcrlf/> task is performed

* Sun Aug 17 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.4-alt1
- 1.5.4

* Mon Mar 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.2-alt1
- 1.5.2
- Synced with 1.5.2-2jpp: added scripts subpackage, changed URL

* Mon Nov 18 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.1-alt1
- 1.5.1
- refurbished for the new java packaging system derived from JPackage
- docs separated to main package stuff (introductory),
  manual, javadoc and task-reference (a bulky PDF document)
- style-xsl subpackage

* Wed May 29 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt3
- both ant script and build search /usr/lib for JDK
- build compatible with jdk-1.3.1 package

* Sun May 19 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt2
- ant-optional subpackage
- build probes known JDK locations when JAVA_HOME is not set

* Thu Apr 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt1
- 1.4.1
- Borrowed a start script from Henri once more, and cleaned it up

* Tue May 01 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.3-alt1
- Adapted for ALTLinux
- Renamed ant-manual back to ant-doc
- Returned jars back into ant tree for the sake of tidyness
- Revision 0.5 of ant.sh
- Set group to Development/Java

* Thu Mar 23 2001 Henri Gomez <hgomez@slib.fr>
- ant-1.3 RPM Release 2
- rebuild with updated ant-optional.jar, the previously
  used was missing some classes.

* Mon Mar 05 2001 Henri Gomez <hgomez@slib.fr>
- ant 1.3
- build CLASSPATH=/usr/share/java/bsf.jar:/usr/share/java/jakarta-regexp.jar:/usr/share/java/xalan.jar:/usr/share/java/xerces.jar

* Mon Feb 27 2001 Henri Gomez <hgomez@slib.fr>
- ant-1.3b2 release 3
- fix manual permissions

* Mon Feb 26 2001 Henri Gomez <hgomez@slib.fr>
- ant-1.3b2 release 2
- fix /usr/local/bin/perl references

* Fri Feb 09 2001 Henri Gomez <hgomez@slib.fr>
- ant-1.3b1
- build CLASSPATH=/usr/share/java/bsf.jar:/usr/share/java/jakarta-regexp.jar:/usr/share/java/xalan.jar:/usr/share/java/xerces.jar

* Wed Oct 25 2000 Henri Gomez <hgomez@slib.fr>
- ant-1.2 RPM Release 2
- renamed ant-doc to ant-manual (follow apache RPM naming)
- RH 7.0 changes location of docdir and DocumentRoot. The spec file is modified
  to place manual in right place when rebuilded under RH 6.x or RH 7.0
- compiled on Redhat 6.1 box plus updates with rpm-3.0.5

* Tue Oct 24 2000 Henri Gomez <hgomez@slib.fr>
- ant-1.2
- added optional.jar
- read WHATSNEW for changes in ant 1.2

* Fri Oct 20 2000 Henri Gomez <hgomez@slib.fr>
- ant-1.2rc
- added optional.jar (from jarkata site)
- source file is renamed from jakarta-ant-src.tar.gz to
  jakarta-ant-src-v1.2rc.tar.gz to allow multiple source file
  in my RPM source dir
- build CLASSPATH=

* Mon Oct 16 2000 Henri Gomez <hgomez@slib.fr>
- ant-1.1 RPM Release 5
- follow Debian policy about java stuff, libs in /usr/share/java,
  executable in /usr/bin
- prepare transition to RH 7.0 new document root (/var/www)
- build CLASSPATH=/usr/share/java/bsf.jar:/usr/share/java/xalan.jar

* Fri Oct 06 2000 Henri Gomez <hgomez@slib.fr>
- v1.1-4
- tomcat build failed if ANT_HOME is set to /usr.
  ant shell script set ANT_HOME to /usr/share/ant
  to fix 'antRun not found' and allow tomcat build ;-?!
- reorganized group packages for javas RPM :
  Development/Tools (ant)
  Developement/Libraries(xalan, xerces)
  Documentation (all ;-)
- build CLASSPATH=/usr/lib/java/bsf.jar:/usr/lib/java/bsfengines.jar:/usr/lib/java/xalan.jar

* Fri Sep 29 2000 Henri Gomez <hgomez@slib.fr>
- v1.1-3- jars are now installed on /usr/lib/java since /opt is
  mounted read-only on many systems <summer@os2.ami.com.au>
- correct bad URL in apidocs
- try to use jikes if present
- rebuilded with IBM JDK 1.3.0 (cx130-20000815)

* Fri Jul 21 2000 Henri Gomez <hgomez@slib.fr>
- v1.1-2
- Rebuild rpm with IBM JDK 1.3 (cx130-20000623) to allow ant
  work under both JDK 1.1.8 and JDK 1.3.
- minor spec file correction (patch ant after install)

* Thu Jul 20 2000 Henri Gomez <hgomez@slib.fr>
- v1.1 final release
- ant need now a JAXP compatible parser. Sun's jaxp 1.0.1 are
  allready included in .tar.gz and so we will use and export
  these jar (jaxp.jar & parser.jar).
  You could also use Apache xerces 1.1.2 or later.
- removed export CLASSPATH= at build time, but you'll have to
  ensure now you have a minimal CLASSPATH (ie: xml parser jars)
- Try to use now the Linux Software Map and Redhat Map.
  exec goes /usr/bin and classes in /usr/lib/ant.
  documentation stay in /home/httpd/html/manual/ant
- Compiled on Redhat 6.1 with latest IBM JDK 1.1.8 (l118-20000515)

* Tue May 02 2000 Henri Gomez <hgomez@slib.fr>
- v0.3.1
- From jakarta/tomcat 3.1 final release. Need now to
  have a consistent version number ;-)
- Fixed classpath problem at compile time by cleaning CLASSPATH before
  build/install stages.
- Compiled on Redhat 6.1 with IBM JDK 1.1.8 (20000328)

* Thu Apr 13 2000 Henri Gomez <hgomez@slib.fr>
- v0.3.1_rc1
- Version renamed to 0.3.1_rc1 to follow Sam Ruby (rubys@us.ibm.com)
  recommandation since the next major release will be 1.0

* Wed Mar 08 2000 Henri Gomez <gomez@slib.fr>
- v3.1b1
- removed moo from ant RPM. Will be now in watchdog RPM.

* Tue Feb 29 2000 Henri Gomez <gomez@slib.fr>
- v3.1_m2rc2

* Fri Feb 25 2000 Henri Gomez <gomez@slib.fr>
- v3.1_m2rc1
- moo is no more in the tar packages, will be released
  in another RPM
- added doc package

* Fri Jan 28 2000 Henri Gomez <gomez@slib.fr>
- v3.1_m1

* Tue Jan 18 2000 Henri Gomez <gomez@slib.fr>
- first RPM of v3.1_m1_rc1

* Tue Jan  4 2000 Henri Gomez <gomez@slib.fr>
- moved from /opt/jakarta/jakarta-tools to /opt/ant

* Tue Jan  4 2000 Henri Gomez <gomez@slib.fr>
- CVS 4 Jan 2000
- added servlet.jar from tomcat in SRPM
   to allow first build of moo.

* Thu Dec 30 1999 Henri Gomez <gomez@slib.fr>
- Initial release for jakarta-tools cvs
