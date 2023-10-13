# Version of scala-altered objectweb-asm
%global asmver 9.5.0
%global asmrel 1

# Version of jquery bundled in scaladoc
%global jqueryver 3.7.1

# Version of jline to use
%global jlinever 3.22.0

%global scaladir %{_datadir}/scala

# Scala needs itself to compile.  Use this if the version in the repository
# cannot build the current version.
%def_without bootstrap

Name:           scala
Version:        2.13.9
Release:        alt3
Summary:        Hybrid functional/object-oriented language for the JVM

ExcludeArch: %ix86 armh

# Used to generate OSGi data
%global date    20230901
%global seqnum  134811
%global commit  80514f73a6c7db32df9887d9a5ca9ae921e25118
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global osgiver %{version}.v%{date}-%{seqnum}-VFINAL-%{shortcommit}
%global majver  %(cut -d. -f1-2 <<< %{version})

# The project as a whole is Apache-2.0.
# The bundled ASM is BSD-3-Clause.
# The bundled jquery is MIT.
License:        Apache-2.0 and BSD-3-Clause and MIT
Group: Development/Java
URL:            https://www.scala-lang.org/
# Source code
Source0:        https://github.com/scala/scala/archive/v%{version}/%{name}-%{version}.tar.gz
%if_with bootstrap
# Binary form, used to bootstrap
Source1:        https://downloads.lightbend.com/scala/%{version}/%{name}-%{version}.tgz
%endif
# Scala-modified version of objectweb-asm
Source2:        https://github.com/scala/scala-asm/archive/v%{asmver}-scala-%{asmrel}.tar.gz

# POMs from maven central
Source3:        https://repo1.maven.org/maven2/org/scala-lang/scala-library/%{version}/scala-library-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/scala-lang/scala-reflect/%{version}/scala-reflect-%{version}.pom
Source5:        https://repo1.maven.org/maven2/org/scala-lang/scala-compiler/%{version}/scala-compiler-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/scala-lang/scalap/%{version}/scalap-%{version}.pom

# Bundled version of jquery for scaladoc
Source7:        https://code.jquery.com/jquery-%{jqueryver}.min.js
Source8:        https://code.jquery.com/jquery-%{jqueryver}.slim.min.js

# OSGi properties for the reflect jar
Source9:        scala-reflect-bnd.properties
# OSGi properties for the library jar
Source10:       scala-library-bnd.properties
# OSGi properties for the compiler jar
Source11:       scala-compiler-bnd.properties

# Properties file for scala-compiler
Source12:       compiler.properties
# Properties file for scala-asm
Source13:       asm.properties
# Properties file for scala-buildcharacter
Source14:       buildcharacter.properties

# MIME information
Source15:       scala.keys
Source16:       scala.mime
Source17:       scala-mime-info.xml

# Use the Fedora way of finding the JVM to invoke
Patch0:         %{name}-tooltemplate.patch

# Unbundle fonts from scaladoc
Patch1:         %{name}-unbundle-fonts.patch

BuildRequires(pre): rpm-macros-java
BuildRequires(pre): java-11-openjdk-devel
BuildRequires:  /proc rpm-build-java
BuildRequires:  aqute-bnd
BuildRequires:  font(lato)
BuildRequires:  font(materialicons)
BuildRequires:  font(opensans)
BuildRequires:  font(sourcecodepro)
BuildRequires:  maven-local
BuildRequires:  mvn(io.github.java-diff-utils:java-diff-utils)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(org.jline:jline-builtins)
BuildRequires:  mvn(org.jline:jline-terminal-jna)
BuildRequires:  mvn(org.openjdk.jol:jol-core)

%filter_from_requires /osgi(org.apache.ant*/d

%if_without bootstrap
BuildRequires:  scala
%endif

Requires:       %{name}-reflect = %{version}-%{release}
Requires:       javapackages-tools

# scaladoc depends on a specific version of jquery, which may differ from the
# version in the js-jquery package
Provides:       bundled(js-jquery) = %{jqueryver}

# The bundled version of objectweb-asm has been altered for Scala purposes.
Provides:       bundled(objectweb-asm) = %{asmver}

# This can be removed when Fedora 36 reaches EOL
Obsoletes:      ant-%{name} < 2.13.4
Obsoletes:      %{name}-swing < 2.13.4

%description
Scala is a general purpose programming language designed to express
common programming patterns in a concise, elegant, and type-safe way.
It smoothly integrates features of object-oriented and functional
languages.  It is also fully interoperable with Java.

This package contains the Scala compiler and bytecode parser.

%package        library
Summary:        Scala standard library
Group: Development/Java

%description    library
Scala is a general purpose programming language designed to express
common programming patterns in a concise, elegant, and type-safe way.
It smoothly integrates features of object-oriented and functional
languages.  It is also fully interoperable with Java.

This package contains the standard library for the Scala programming
language.

%package        reflect
Summary:        Scala reflection library
Group: Development/Java
Requires:       %{name}-library = %{version}-%{release}

%description    reflect
Scala is a general purpose programming language designed to express
common programming patterns in a concise, elegant, and type-safe way.
It smoothly integrates features of object-oriented and functional
languages.  It is also fully interoperable with Java.

This package contains the reflection library for the Scala programming
language.

%package        apidoc
Summary:        Documentation for the Scala programming language
Group: Development/Java
Requires:       font(lato)
Requires:       font(materialicons)
Requires:       font(opensans)
Requires:       font(sourcecodepro)

%description    apidoc
Scala is a general purpose programming language designed to express
common programming patterns in a concise, elegant, and type-safe way.
It smoothly integrates features of object-oriented and functional
languages.  It is also fully interoperable with Java.

This package provides reference and API documentation for the Scala
programming language.

%prep
%setup
%if_with bootstrap
%setup -T -D -a 1
%endif
%setup -T -D -a 2
%autopatch -p1

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not use env
for fil in scripts/stability-test.sh \
  src/compiler/templates/tool-unix.tmpl \
  test/script-tests/jar-manifest/run-test \
  tools/scaladoc-diff; do
  sed -i.orig 's,%{_bindir}/env bash,/bin/bash,' $fil
  fixtimestamp $fil
done

# Unbundle fonts
# The CSS uses local() references, so these should not be needed anyway.
rm src/scaladoc/scala/tools/nsc/doc/html/resource/lib/{lato,MaterialIcons,open-sans,source-code-pro}*

# Fetch upstream's POMs
cp -p %{SOURCE3} src/library/pom.xml
cp -p %{SOURCE4} src/reflect/pom.xml
cp -p %{SOURCE5} src/compiler/pom.xml
cp -p %{SOURCE6} src/scalap/pom.xml

# Fedora has a split jline3, so split up the dependency
%pom_change_dep org.jline:jline org.jline:jline-terminal-jna src/compiler
%pom_add_dep org.jline:jline-reader:%{jlinever} src/compiler
%pom_add_dep org.jline:jline-style:%{jlinever} src/compiler
%pom_add_dep org.jline:jline-builtins:%{jlinever} src/compiler

%build
export LC_ALL=C.UTF-8

%if_with bootstrap
PATH=$PATH:$PWD/%{name}-%{version}/bin
COMPJAR=$PWD/%{name}-%{version}/lib/scala-compiler.jar
%else
COMPJAR=%{_javadir}/scala/scala-compiler.jar
%endif

JAVA_VER=$(java -version 2>&1 | sed -n 's/.*"\([[:digit:]]*\)[.[:digit:]]*[^[:digit:]]*".*/\1/p')
JLINE_JARS=$(build-classpath jna jline/jline-terminal jline/jline-terminal-jna \
    jline/jline-reader jline/jline-style jline/jline-builtins)
JAVAC_FLAGS="-g -parameters -source $JAVA_VER -target $JAVA_VER"
SCALAC_FLAGS="-g:vars -release $JAVA_VER -J-Xmx512M -J-Xms32M"
SCALADOC_FLAGS='-J-Xmx512M -J-Xms32M -doc-footer epfl -diagrams -implicits -groups -doc-version %{version} -doc-source-url https://github.com/scala/scala/blob/v%{version}/src/€{FILE_PATH_EXT}#L€{FILE_LINE}'
DIFFUTILS_JAR=$(build-classpath java-diff-utils)

mkdir -p target/{compiler,library,manual,reflect,scalap,tastytest,testkit}
mkdir -p target/html/{compiler,library,reflect}

# Build the bundled objectweb-asm
cd scala-asm-%{asmver}-scala-%{asmrel}
javac $JAVAC_FLAGS -d ../target/compiler $(find src -name \*.java)
cd -

# Build the library
cd src
javac $JAVAC_FLAGS -d ../target/library -cp $(build-classpath junit) \
    $(find library -name \*.java)
scalac $SCALAC_FLAGS -d ../target/library -classpath ../target/library \
    $(find library -name \*.scala | sort)

# Skip docs to avoid jquery bug
# scaladoc $SCALADOC_FLAGS -doc-title 'Scala Standard Library' \
#     -sourcepath $PWD/library -doc-no-compile $PWD/library-aux \
#     -skip-packages scala.concurrent.impl \
#     -doc-root-content $PWD/library/rootdoc.txt \
#     $(find library -name \*.scala | sort)
# mv scala ../target/html/library

# Build the reflection library
javac $JAVAC_FLAGS -d ../target/reflect $(find reflect -name \*.java)
scalac $SCALAC_FLAGS -d ../target/reflect -classpath ../target/reflect \
    $(find reflect -name \*.scala | sort)

# scaladoc $SCALADOC_FLAGS -doc-title 'Scala Reflection Library' \
#    -sourcepath $PWD/reflect \
#     -skip-packages scala.reflect.macros.internal:scala.reflect.internal:scala.reflect.io \
#     $(find reflect -name \*.scala | sort)
# mv scala ../target/html/reflect

# Build the compiler
javac $JAVAC_FLAGS -d ../target/compiler -cp $COMPJAR \
    $(find compiler -name \*.java)
scalac $SCALAC_FLAGS -d ../target/compiler \
    -classpath ../target/compiler:$DIFFUTILS_JAR \
    -feature $(find compiler -name \*.scala)

# Build the interactive compiler
scalac $SCALAC_FLAGS -d ../target/compiler -classpath ../target/compiler \
    -feature $(find interactive -name \*.scala)

# Build the REPL
scalac $SCALAC_FLAGS -d ../target/compiler -classpath ../target/reflect \
    -feature $(find repl -name \*.scala)

# Build the REPL frontend
javac $JAVAC_FLAGS -d ../target/compiler $(find repl-frontend -name \*.java)
scalac $SCALAC_FLAGS -d ../target/compiler \
    -classpath ../target/compiler:$JLINE_JARS \
    -feature $(find repl-frontend -name \*.scala)
# scaladoc $SCALADOC_FLAGS -doc-title 'Scala Compiler' \
#     -sourcepath $PWD/compiler:$PWD/interactive:$PWD/repl:$PWD/repl-frontend \
#    -doc-root-content $PWD/compiler/rootdoc.txt \
#    -classpath $PWD/../target/library:$PWD/../target/reflect:$JLINE_JARS:$DIFFUTILS_JAR \
#     $(find compiler -name \*.scala) $(find interactive -name \*.scala) \
#     $(find repl -name \*.scala) $(find repl-frontend -name \*.scala)
# mv scala ../target/html/compiler

# Build the documentation generator
# The order of the source files matters!  Some orderings end with this error:
# error: scala.reflect.internal.Symbols$CyclicReference: illegal cyclic reference involving <refinement of scala.tools.nsc.doc.model.ModelFactory with scala.tools.nsc.doc.model.ModelFactoryImplicitSupport with scala.tools.nsc.doc.model.ModelFactoryTypeSupport with scala.tools.nsc.doc.model.diagram.DiagramFactory with scala.tools.nsc.doc.model.CommentFactory with scala.tools.nsc.doc.model.TreeFactory with scala.tools.nsc.doc.model.MemberLookup>
# I do not know why that happens.  This is one order that works.  There are
# no doubt many more.
scalac $SCALAC_FLAGS -d ../target/compiler \
    $(find scaladoc -name \*.scala | sort)

# Build the bytecode parser
scalac $SCALAC_FLAGS -d ../target/scalap $(find scalap -name \*.scala)

# Build the testing tool
javac $JAVAC_FLAGS -d ../target/testkit \
    -cp ../target/library:$(build-classpath junit) \
    $(find testkit -name \*.java)
scalac $SCALAC_FLAGS -d ../target/testkit \
    -classpath ../target/testkit:$(build-classpath junit) -feature \
    $(find testkit -name \*.scala)

# TODO: build the parser testing tool.  This cannot be done without some sbt
# classes.  If we have sbt, then we don't need to build manually anyway.

# Build the integration tests
scalac $SCALAC_FLAGS -d ../target/tastytest -classpath $DIFFUTILS_JAR \
    $(find tastytest -name \*.scala)

# Build the man page builder
scalac $SCALAC_FLAGS -d ../target/manual -classpath ../target/library \
    $(find manual -name \*.scala)
cd -

# Copy source files into target before constructing jars
for dir in reflect library compiler scalap; do
  cp -p LICENSE NOTICE target/$dir
done
cp -p src/library/rootdoc.txt target/library
cp -p src/compiler/rootdoc.txt target/compiler
cp -a src/compiler/templates target/compiler
# cp -a src/scaladoc/scala/tools/nsc/doc/html/resource \
#       target/compiler/scala/tools/nsc/doc/html
cp -p src/scalap/decoder.properties target/scalap

# Build the compiler jar
cd target
mkdir -p compiler/META-INF/services
cat > compiler/META-INF/services/javax.script.ScriptEngineFactory << EOF
scala.tools.nsc.interpreter.shell.Scripted\$Factory
EOF
propdate=$(date -u -d %{date})
jnaver=$(sed -n 's,^  <version>\(.*\)</version>,\1,p' %{_datadir}/maven-poms/jna.pom)
cp -p %{SOURCE7} compiler/jquery.min.js
cp -p %{SOURCE8} compiler/jquery.slim.min.js
sed -e "s/@@DATE@@/$propdate/;s/@@VER@@/%{version}/;s/@@OSGI@@/%{osgiver}/" \
  %{SOURCE12} > compiler/compiler.properties
cp -p compiler/compiler.properties compiler/interactive.properties
cp -p compiler/compiler.properties compiler/repl.properties
cp -p compiler/compiler.properties compiler/replFrontend.properties
cp -p compiler/compiler.properties compiler/scaladoc.properties
sed -e "s/@@DATE@@/$propdate/;s/@@VER@@/%{version}/;s/@@MAJVER@@/%{majver}/" \
  -e "s/@@ASMVER@@/%{asmver}/;s/@@ASMREL@@/%{asmrel}/" \
  %{SOURCE13} > compiler/scala-asm.properties
sed -e "s/@@DATE@@/$propdate/;s/@@VER@@/%{version}/;s/@@OSGI@@/%{osgiver}/" \
  -e "s/@@ASMVER@@/%{asmver}/;s/@@ASMREL@@/%{asmrel}/" \
  -e "s/@@JLINEVER@@/%{jlinever}/;s/@@JNAVER@@/$jnaver/" \
  %{SOURCE14} > compiler/scala-buildcharacter.properties
jar cf scala-compiler.jar.no -C compiler .
bnd wrap --properties %{SOURCE11} --output scala-compiler.jar \
    --version "%{osgiver}" scala-compiler.jar.no

# Build the reflect jar
cp -p compiler/compiler.properties reflect/reflect.properties
jar cf scala-reflect.jar.no -C reflect .
bnd wrap --properties %{SOURCE9} --output scala-reflect.jar \
    --version "%{osgiver}" scala-reflect.jar.no

# Build the library jar
cp -p compiler/compiler.properties library/library.properties
jar cf scala-library.jar.no -C library .
bnd wrap --properties %{SOURCE10} --output scala-library.jar \
    --version "%{osgiver}" scala-library.jar.no

# Build the decoder jar
cp -p compiler/compiler.properties scalap/scalap.properties
jar cf scalap-%{version}.jar -C scalap .
cd -

# Build the man pages
mkdir -p html man/man1
cd src
scala -classpath ../target/manual:../target/scala-library.jar scala.tools.docutil.ManMaker 'fsc, scala, scalac, scaladoc, scalap' ../html ../man
cd -

# Prepare to install
%mvn_artifact src/library/pom.xml target/scala-library.jar
%mvn_artifact src/reflect/pom.xml target/scala-reflect.jar
%mvn_artifact src/compiler/pom.xml target/scala-compiler.jar
%mvn_artifact src/scalap/pom.xml target/scalap-%{version}.jar

%mvn_package org.scala-lang:scala-library library
%mvn_package org.scala-lang:scala-reflect reflect

%install
%mvn_install

# Create the binary scripts
mkdir -p %{buildroot}%{_bindir}
CLASSPATH=$(build-classpath jna jline/jline-terminal \
            jline/jline-terminal-jna jline/jline-reader jline/jline-style \
            jline/jline-builtins)\
:%{_javadir}/scala/scala-library.jar\
:%{_javadir}/scala/scala-reflect.jar\
:%{_javadir}/scala/scala-compiler.jar
JAVAFLAGS="-Xmx256M -Xms32M"

sed -e "s,@classpath@,$CLASSPATH," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.nsc.fsc.CompileClient," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/fsc

sed -e "s,@classpath@,$CLASSPATH," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.nsc.MainGenericRunner," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/scala

sed -e "s,@classpath@,$CLASSPATH," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.nsc.Main," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/scalac

sed -e "s,@classpath@,$CLASSPATH," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.nsc.ScalaDoc," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/scaladoc

sed -e "s,@classpath@,$CLASSPATH:$(build-classpath scala/scalap)," \
    -e "s,@javaflags@,$JAVAFLAGS," \
    -e "s,@properties@ ,," \
    -e "s,@class@,scala.tools.scalap.Main," \
    -e "s,@toolflags@ ,," \
    -e "s,@@,@,g" \
    src/compiler/templates/tool-unix.tmpl > %{buildroot}%{_bindir}/scalap

chmod 0755 %{buildroot}%{_bindir}/{fsc,scala*}

# Install the MIME info
install -d %{buildroot}%{_datadir}/mime-info
install -p -m 644 %{SOURCE15} %{SOURCE16} %{buildroot}%{_datadir}/mime-info/

install -d %{buildroot}%{_datadir}/mime/packages/
install -p -m 644 %{SOURCE17} %{buildroot}%{_datadir}/mime/packages/

# Install the man pages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/man1/* %{buildroot}%{_mandir}/man1

%files -f .mfiles
%{_bindir}/fsc
%{_bindir}/scala*
%{_datadir}/mime-info/scala.*
%{_datadir}/mime/packages/scala-mime-info.xml
%{_mandir}/man1/fsc.1*
%{_mandir}/man1/scala*

%files library -f .mfiles-library
%doc LICENSE NOTICE doc/LICENSE.md doc/License.rtf

%files reflect -f .mfiles-reflect

%files apidoc
%doc target/html/*

%changelog
* Fri Oct 13 2023 Andrey Cherepanov <cas@altlinux.org> 2.13.9-alt3
- Build classes for scaladoc (ALT #47749).

* Fri Sep 22 2023 Andrey Cherepanov <cas@altlinux.org> 2.13.9-alt2
- Build without bootstrapping.

* Fri Sep 22 2023 Andrey Cherepanov <cas@altlinux.org> 2.13.9-alt1
- New version (fixes: CVE-2022-36944).

* Fri Sep 22 2023 Andrey Cherepanov <cas@altlinux.org> 2.13.5-alt3
- Build with added method knownSize

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 2.13.5-alt2_1jpp11
- fixed build; build w/o scalsdoc

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 2.13.5-alt1_1jpp11
- new version

* Mon Jun 14 2021 Igor Vlasenko <viy@altlinux.org> 2.13.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Jun 13 2021 Igor Vlasenko <viy@altlinux.org> 2.10.6-alt3_17jpp8
- use jline2

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_17jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_15jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_8jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt2_3jpp8
- added BR: javapackages-local for javapackages 5

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.6-alt1_3jpp8
- new version

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt2_9jpp8
- updated dependencies

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_8jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

