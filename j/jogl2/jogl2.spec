# baserelease defines which build revision of this version we're building.
# The magical name baserelease is matched by the rpmdev-bumpspec tool, which
# you should use.
%global pkg_name jogl
%global pkg_version 2.0.2
%set_verify_elf_method unresolved=relaxed

Name:           jogl2
Version:        2.0.2
Release:        alt1
Summary:        Java bindings for the OpenGL API

Group:          Development/Java
# For a breakdown of the licensing, see LICENSE.txt 
License:        BSD and MIT and ASL 2.0 and ASL 1.1 
URL:            http://jogamp.org/
Source0:        %pkg_name-v%version.tar
Source1:        %name-pom.xml

# https://github.com/sgothel/jogl/pull/51
Patch1:         %name-0001-fix-gluegen-gl-classpath.patch
Patch2:         %name-0002-deactivate-debug-printf.patch
Patch3:         %name-disable-build-native-broadcom.patch

BuildRequires(pre): rpm-build-java
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  gluegen2-devel
BuildRequires:  eclipse-swt
BuildRequires:  libXt-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  maven
BuildRequires:  junit

Requires:       java >= 1.6.0
Requires:       jpackage-utils
Requires:       gluegen2

%description
The JOGL project hosts the development version of the Java Binding for
the OpenGL API (JSR-231), and is designed to provide hardware-supported 3D
graphics to applications written in Java. JOGL provides full access to the
APIs in the OpenGL 2.0 specification as well as nearly all vendor extensions,
and integrates with the AWT and Swing widget sets. It is part of a suite of
open-source technologies initiated by the Game Technology Group at
Sun Microsystems.

%package javadoc
Summary:        Javadoc for jogl2
Group:          Documentation
Requires:       jpackage-utils
BuildArch:      noarch

Requires:       jpackage-utils
Requires:       %name = %version-%release

%description javadoc
Javadoc for jogl2.

%package doc
Summary:        User manual for jogl2
Group:          Documentation
BuildArch:      noarch
Requires:       %name = %version-%release

%description doc
User manual for jogl2.

%prep
%setup -n %pkg_name-v%version
%patch1 -p1
%patch2 -p1
%patch3 -p2

# Remove bundled dependencies
find -name "*.jar" -type f -exec rm {} \;
find -name "*.apk" -type f -exec rm {} \;
rm -fr make/lib

# Restore the gluegen2 source code from gluegen2-devel
ln -s %_datadir/gluegen2 ../gluegen

# Fix file-not-utf8
for file in README.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

# git executable should not be used, use true (to avoid checkout) instead
sed -i 's/executable="git"/executable="true"/' make/build-common.xml

%build
cd make
ant -Dc.compiler.debug=true \
    -Djavacdebug=false \
    -Dcommon.gluegen.build.done=true \
    \
    -Dantlr.jar=%_javadir/antlr.jar \
    -Djunit.jar=%_javadir/junit.jar \
    -Dant.jar=%_javadir/ant.jar \
    -Dant-junit.jar=%_javadir/ant/ant-junit.jar \
    -Dgluegen.jar=%_javadir/gluegen2.jar \
    -Dgluegen-rt.jar=%_jnidir/gluegen2-rt.jar \
    -Dswt.jar=%_libdir/eclipse/swt.jar \
    \
    -Djavadoc.link=%_javadocdir/java \
    -Dgluegen.link=%_javadocdir/gluegen2 \
    \
    all \
    javadoc.all

%install
mkdir -p %buildroot%_javadir/%name \
    %buildroot%_libdir/%name \
    %buildroot%_jnidir

install build/jar/jogl-all.jar %buildroot%_jnidir/%name.jar
ln -s ../../..%_jnidir/%name.jar %buildroot%_libdir/%name/
install -t %buildroot%_libdir/%name/ build/lib/*.so

# Provide JPP pom
mkdir -p %buildroot%_mavenpomdir
install -pm 644 %SOURCE1 %buildroot%_mavenpomdir/JPP-%name.pom
%add_maven_depmap JPP-%name.pom %name.jar -a "org.jogamp.jogl:jogl-all"

# Make the javadoc package
mkdir -p %buildroot%_javadocdir/%name
cp -rdf build/javadoc/jogl/javadoc/* %buildroot%_javadocdir/%name

# Make the doc package
mkdir -p %buildroot%_docdir/%name
cp -rdf doc/* %buildroot%_docdir/%name

# update links to javadoc
subst "s|/deployment/jogamp-next/javadoc/jogl/javadoc|%_javadocdir/%name|g" \
    $(find %buildroot%_docdir/%name -name '*.html')

%files
%doc README.txt LICENSE.txt CHANGELOG.txt
%_libdir/%name
%_jnidir/%name.jar
%_mavendepmapfragdir/%name
%_mavenpomdir/JPP-%name.pom

%files javadoc
%doc LICENSE.txt
%_javadocdir/%name

%files doc
%doc LICENSE.txt
%_docdir/%name

%changelog
* Sun Nov 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt11.2
- NMU: fixed BR: junit-junit4 no more

* Sun Apr 21 2013 Andrey Cherepanov <cas@altlinux.org> 2.0-alt11.1
- Initial build in Sisyphus (thanks Fedora maintainers)
- Disable Broadcom native support
