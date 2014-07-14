Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: glassfish-jaxb
Version: 2.2.5
Release: alt2_3jpp7
Summary: JAXB Reference Implementation

Group: Development/Java
License: CDDL and GPLv2 with exceptions
URL: http://jaxb.java.net

# svn export https://svn.java.net/svn/jaxb~version2/tags/jaxb-2_2_5/ glassfish-jaxb-2.2.5
# find glassfish-jaxb-2.2.5/ -name '*.class' -delete
# find glassfish-jaxb-2.2.5/ -name '*.jar' -delete
# find glassfish-jaxb-2.2.5/ -name '*.zip' -delete
# find glassfish-jaxb-2.2.5/ -name '*.dll' -delete
# tar czf glassfish-jaxb-2.2.5.tar.gz glassfish-jaxb-2.2.5
Source0: %{name}-%{version}.tar.gz

# JAXB implementation POM:
Source1: http://repo1.maven.org/maven2/com/sun/xml/bind/jaxb-impl/2.2.5/jaxb-impl-2.2.5.pom

# JAXB XJC POM:
Source2: http://repo1.maven.org/maven2/com/sun/xml/bind/jaxb-xjc/2.2.5/jaxb-xjc-2.2.5.pom

# Ant build file used to generate the Javadoc (this is not part of the original
# source but written on purpose for the packaging):
Source3: build-javadoc.xml

# Use resolver from xml-commons-resolver instead of an internal rebundled one:
Patch0: %{name}-dont-use-internal-resolver.patch

# Don't try to generate the 1.0 runtime:
Patch1: %{name}-dont-generate-1.0-runtime.patch

# Removing Jing driver because of incompatibility issues:
Patch2: %{name}-dont-generate-jing-rnc-driver.patch

# Don't bundle the contents of other jar files in the XJC compiler jar file:
Patch3: %{name}-dont-bundle-other-jars.patch

# Remove the class-path entry from the generated manifest files:
Patch4: %{name}-remove-classpath-from-manifests.patch

# Patch the POM files to include the dependencies corresponding to the jar
# files that we aren't bundling within the jat files of this package:
Patch5: %{name}-add-dependencies.patch

# Don't use the prebuilt javadocs:
Patch6: %{name}-dont-use-prebuilt-javadocs.patch

# Don't build the examples as they need additional dependencies:
Patch7: %{name}-dont-build-examples.patch

BuildArch: noarch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: codemodel
BuildRequires: istack-commons
BuildRequires: relaxngcc
BuildRequires: xml-commons-resolver
BuildRequires: txw2
BuildRequires: relaxngDatatype
BuildRequires: glassfish-dtd-parser
BuildRequires: glassfish-jaxb-api
BuildRequires: glassfish-fastinfoset
BuildRequires: jing
BuildRequires: stax-ex
BuildRequires: isorelax
BuildRequires: xsom
BuildRequires: rngom

Requires: glassfish-dtd-parser
Requires: xml-commons-resolver
Requires: xsom
Requires: rngom
Requires: isorelax
Requires: jing
Requires: stax-ex
Requires: glassfish-fastinfoset
Requires: glassfish-jaxb-api
Requires: relaxngDatatype
Requires: txw2
Requires: relaxngcc
Requires: istack-commons
Requires: codemodel
Requires: jpackage-utils
Source44: import.info


%description
GlassFish JAXB Reference Implementation.


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.


%prep

# Unpack the sources:
%setup -q

# Put the POM files in place (we do this before patching because we need to
# patch the POMs in order to add the dependencies for the artifacts that we are
# not bundling):
cp %{SOURCE1} jaxb-impl.pom
cp %{SOURCE2} jaxb-xjc.pom

# Apply the patches:
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# Link the libraries where the build script expects them:
ln -s $(build-classpath codemodel) tools/lib/rebundle/compiler/codemodel.jar
ln -s $(build-classpath glassfish-dtd-parser) tools/lib/rebundle/compiler/dtd-parser.jar
ln -s $(build-classpath istack-commons-tools) tools/lib/rebundle/compiler/istack-commons-tools.jar
ln -s $(build-classpath relaxngDatatype) tools/lib/rebundle/compiler/relaxngDatatype.jar
ln -s $(build-classpath xml-commons-resolver) tools/lib/rebundle/compiler/resolver.jar
ln -s $(build-classpath rngom) tools/lib/rebundle/compiler/rngom.jar
ln -s $(build-classpath xsom) tools/lib/rebundle/compiler/xsom.jar
ln -s $(build-classpath isorelax) tools/lib/rebundle/runtime/isorelax.jar
ln -s $(build-classpath msv-msv) tools/lib/rebundle/runtime/msv.jar
ln -s $(build-classpath relaxngDatatype) tools/lib/rebundle/runtime/relaxngDatatype.jar
ln -s $(build-classpath istack-commons-runtime) tools/lib/rebundle/runtime2/istack-commons-runtime.jar
ln -s $(build-classpath txw2) tools/lib/rebundle/runtime2/txw2.jar
ln -s $(build-classpath jaxb-api) tools/lib/redist/jaxb-api.jar
ln -s $(build-classpath FastInfoset) tools/lib/util/FastInfoset.jar
ln -s $(build-classpath args4j) tools/lib/util/args4j.jar
ln -s $(build-classpath codemodel-annotation-compiler) tools/lib/util/codemodel-annotation-compiler.jar
ln -s $(build-classpath dom4j) tools/lib/util/dom4j.jar
ln -s $(build-classpath jing) tools/lib/util/jing.jar
ln -s $(build-classpath relaxngcc) tools/lib/util/relaxngcc.jar
ln -s $(build-classpath stax-ex) tools/lib/util/stax-ex.jar
ln -s $(build-classpath txwc2) tools/lib/util/txwc2.jar

# Put the Javadoc build file in place (no patching needed here, as this is not
# part of the original source):
cp %{SOURCE3} build-javadoc.xml


%build

# Build the binaries:
ant \
  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dbuild.sysclasspath=last \
  -Dbuild.number=1 \
  dist

# Build the javadoc for the runtime and the compiler:
ant \
  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dbuild.sysclasspath=last \
  -f build-javadoc.xml


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -m 644 dist/lib/jaxb-impl.jar %{buildroot}%{_javadir}/%{name}/jaxb-impl.jar
install -m 644 dist/lib/jaxb-xjc.jar %{buildroot}%{_javadir}/%{name}/jaxb-xjc.jar
install -m 644 tools/pretty-printer/build/pretty-printer.jar %{buildroot}%{_javadir}/%{name}/pretty-printer.jar
install -m 644 tools/xmllint/build/xmllint.jar %{buildroot}%{_javadir}/%{name}/xmllint.jar

# compat symkink till jbossas
ln -s ../jaxb-api.jar %{buildroot}%{_javadir}/%{name}/jaxb-api.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 jaxb-impl.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb-impl.pom
install -m 644 jaxb-xjc.pom  %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxb-xjc.pom

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# Dependencies map:
%add_maven_depmap JPP.%{name}-jaxb-impl.pom %{name}/jaxb-impl.jar
%add_maven_depmap JPP.%{name}-jaxb-xjc.pom %{name}/jaxb-xjc.jar


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc License.txt
%doc License.html


%files javadoc
%{_javadocdir}/%{name}
%doc License.txt
%doc License.html


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt1_3jpp7
- fc version
- jaxb 2.2 api
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt3_7jpp6
- built with java 6

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt2_7jpp6
- removed compat symlink

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt1_7jpp6
- new version

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_7jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_6jpp5
- converted from JPackage by jppimport script

