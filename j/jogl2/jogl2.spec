# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jogl2
Version:        2.3.2
Release:        alt1_2jpp8
%global src_name jogl-v%{version}
Summary:        Java bindings for the OpenGL API

Group:          Development/Other
# For a breakdown of the licensing, see LICENSE.txt 
License:        BSD and MIT and ASL 2.0 and ASL 1.1 
URL:            http://jogamp.org/
Source0:        http://jogamp.org/deployment/v%{version}/archive/Sources/%{src_name}.tar.xz
Source1:        %{name}-pom.xml

Patch2:         %{name}-0002-deactivate-debug-printf.patch
Patch3:         %{name}-0003-delete-not-supported-API.patch
Patch4:         %{name}-0004-disable-some-tests.patch
Patch5:         %{name}-add-secarchs.patch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  gluegen2-devel = %{version}
BuildRequires:  eclipse-swt
BuildRequires:  libXt-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  maven-local

Requires:       java
Requires:       jpackage-utils
Requires:       gluegen2 = %{version}
Source44: import.info
Patch33: jogl2-disable-build-native-broadcom.patch
BuildArch: noarch

%description
The JOGL project hosts the development version of the Java Binding for
the OpenGL API (JSR-231), and is designed to provide hardware-supported 3D
graphics to applications written in Java. JOGL provides full access to the
APIs in the OpenGL 2.0 specification as well as nearly all vendor extensions,
and integrates with the AWT and Swing widget sets. It is part of a suite of
open-source technologies initiated by the Game Technology Group at
Sun Microsystems.

%package doc
Summary:        User manual for jogl2
Group:          Development/Java
BuildArch:      noarch

%description doc
User manual for jogl2.

%prep
%setup -n %{src_name}

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Remove bundled dependencies
find -name "*.jar" -type f -exec rm {} \;
find -name "*.apk" -type f -exec rm {} \;
rm -fr make/lib

# Restore the gluegen2 source code from gluegen2-devel
rm -fr ../gluegen
cp -rdf %{_datadir}/gluegen2 ../gluegen

# Fix file-not-utf8
for file in README.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

# git executable should not be used, use true (to avoid checkout) instead
sed -i 's/executable="git"/executable="true"/' make/build-common.xml
%patch33 -p2

%build
cd make

# As we never cross-compile this package, the SDK root is always /
export TARGET_PLATFORM_ROOT=/

xargs -t ant <<EOF
 -verbose
 -Dc.compiler.debug=true
 -Djavacdebug=true
 -Djavac.memorymax=512m
 -Dcommon.gluegen.build.done=true
 
 -Dantlr.jar=%{_javadir}/antlr.jar 
 -Djunit.jar=%{_javadir}/junit.jar 
 -Dant.jar=%{_javadir}/ant.jar 
 -Dant-junit.jar=%{_javadir}/ant/ant-junit.jar 
 -Dgluegen.jar=%{_javadir}/gluegen2.jar 
 -Dgluegen-rt.jar=%{_jnidir}/gluegen2-rt.jar 
 -Dswt.jar=%{_libdir}/eclipse/swt.jar 

 -Djava.excludes.all='com/jogamp/newt/util/applet*/**/*.java com/jogamp/audio/**/*.java jogamp/opengl/gl2/fixme/**/*.java com/jogamp/opengl/test/**/*.java'

 -Djavadoc.link=%{_javadocdir}/java 
 -Dgluegen.link=%{_javadocdir}/gluegen2 
 
 build.nativewindow build.jogl build.newt one.dir javadoc.public
EOF

%install
mkdir -p %{buildroot}%{_javadir}/%{name} \
    %{buildroot}%{_libdir}/%{name} \
    %{buildroot}%{_javadir}

install build/jar/jogl-all.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s ../../..%{_javadir}/%{name}.jar %{buildroot}%{_libdir}/%{name}/

# Provide JPP pom
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.jogamp.jogl:jogl-all"

# Make the doc package
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -rdf doc/* %{buildroot}%{_docdir}/%{name}
cp -t %{buildroot}%{_docdir}/%{name}/ README.txt LICENSE.txt CHANGELOG.txt

%files -f .mfiles
%{_docdir}/%{name}/README.txt
%{_docdir}/%{name}/LICENSE.txt
%{_docdir}/%{name}/CHANGELOG.txt

%files doc
%{_docdir}/%{name}/LICENSE.txt
%{_docdir}/%{name}

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_2jpp8
- new version

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_4jpp8
- replaced with fc imported package

* Sun Nov 16 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt11.2
- NMU: fixed BR: junit-junit4 no more

* Sun Apr 21 2013 Andrey Cherepanov <cas@altlinux.org> 2.0-alt11.1
- Initial build in Sisyphus (thanks Fedora maintainers)
- Disable Broadcom native support
