Name:    jogl
Version: 2.6.0
Release: alt1
Epoch: 1
%global src_name jogl-v%{version}
Summary: Java bindings for the OpenGL API

# For a breakdown of the licensing, see LICENSE.txt
License: BSD and MIT and Apache-2.0 and Apache-1.1
Group: Development/Java
URL: http://jogamp.org/
VCS: https://github.com/sgothel/jogl
Source0: %name-%version.tar

Patch0: cc-attributes-in-build.patch
Patch1: build-only-for-x11.patch
Patch2: skip-Win-and-Mac.patch
Patch3: jogl2-disable-build-native-broadcom.patch
Patch4: aarch64-build.patch

ExcludeArch: armh %ix86

BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-utils
BuildRequires: gluegen-devel = %{version}
BuildRequires: eclipse-swt
BuildRequires: libXt-devel
BuildRequires: libXrender-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXi-devel
BuildRequires: maven-local

Requires: jpackage-utils
Requires: gluegen = %{version}

Provides: jogl2 = %EVR
Obsoletes: jogl2 < %EVR

%add_findreq_skiplist %_libdir/jogl/libnativewindow_awt.so

%description
The JOGL project hosts the development version of the Java Binding for
the OpenGL API (JSR-231), and is designed to provide hardware-supported 3D
graphics to applications written in Java. JOGL provides full access to the
APIs in the OpenGL 2.0 specification as well as nearly all vendor extensions,
and integrates with the AWT and Swing widget sets. It is part of a suite of
open-source technologies initiated by the Game Technology Group at
Sun Microsystems.

%package doc
Group: Development/Java
Summary: User manual for jogl
Provides: jogl2-doc = %EVR
Obsoletes: jogl2-doc < %EVR

%description doc
User manual for jogl.

%prep
%setup
%autopatch -p1

rm -rf src/nativewindow/classes/jogamp/nativewindow/jawt/{drm,ios,macosx,windows}
rm -rf src/nativewindow/classes/jogamp/nativewindow/{javafx,drm,ios,macosx,windows}
rm -rf src/nativewindow/classes/com/jogamp/nativewindow/{javafx,macosx,ios,windows}
rm -rf src/jogl/classes/jogamp/opengl/{macosx,ios,windows}
rm -rf src/newt/classes/jogamp/newt/driver/{egl/gbm,macosx,ios,windows}
rm -rf src/newt/classes/jogamp/newt/{javafx,swt}
rm -rf src/newt/classes/com/jogamp/newt/{javafx,swt}

# Remove bundled dependencies
find -name "*.jar" -type f -exec rm {} \;
find -name "*.apk" -type f -exec rm {} \;
rm -fr make/lib

# Restore the gluegen source code from gluegen-devel
rm -fr ../gluegen
cp -rdf %{_datadir}/gluegen ../gluegen

# Fix file-not-utf8
for file in README.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

# git executable should not be used, use true (to avoid checkout) instead
sed -i 's/executable="git"/executable="true"/' make/build-common.xml

# install in _javadir
%mvn_file org.jogamp.jogl:jogl %{name}
%mvn_alias org.jogamp.jogl:jogl "org.jogamp.jogl:jogl-all"

%build
# zerg's girar armh hack:
(while true; do date; sleep 7m; done) &
# end armh hack, kill it when girar will be fixed
cd make

# As we never cross-compile this package, the SDK root is always /
export TARGET_PLATFORM_ROOT=/

export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
xargs -t ant <<EOF
 -verbose
 -Dc.compiler.debug=true
 -Djavacdebug=true
 -Djavac.memorymax=512m
 -Dcommon.gluegen.build.done=true
 -Dtarget.sourcelevel=1.8
 -Dtarget.targetlevel=1.8
 -Dantlr.jar=%{_javadir}/antlr.jar
 -Djunit.jar=%{_javadir}/junit.jar
 -Dant.jar=%{_javadir}/ant.jar
 -Dant-junit.jar=%{_javadir}/ant/ant-junit.jar
 -Dgluegen.jar=%{_javadir}/gluegen.jar
 -Dgluegen-rt.jar=%{_jnidir}/gluegen-rt.jar
 -Dswt.jar=%{_javadir}/swt.jar

 -Djava.excludes.all='com/jogamp/newt/util/applet*/**/*.java com/jogamp/audio/**/*.java jogamp/opengl/gl2/fixme/**/*.java com/jogamp/opengl/test/**/*.java'

 -Djavadoc.link=%{_javadocdir}/java
 -Dgluegen.link=%{_javadocdir}/gluegen

 build.nativewindow build.jogl build.newt build.graphui build.oculusvr one.dir javadoc.public
EOF

cd ..
export JAVA_HOME=/usr/lib/jvm/java

%install
%mvn_install
mkdir -p %{buildroot}%{_javadir}/%{name} \
    %{buildroot}%{_libdir}/%{name} \
    %{buildroot}%{_javadir}
install -Dpm 0644 build/jar/jogl-all.jar %{buildroot}%{_jnidir}/%{name}.jar
ln -s ../../..%{_jnidir}/%{name}.jar %{buildroot}%{_libdir}/%{name}/
install -t %{buildroot}%{_libdir}/%{name}/ build/lib/*.so

# Make the doc package
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -rdf doc/* %{buildroot}%{_docdir}/%{name}
cp -t %{buildroot}%{_docdir}/%{name}/ README.md LICENSE.txt CHANGELOG.txt

%files
%doc README.md LICENSE.txt CHANGELOG.txt
%{_libdir}/%{name}
%{_jnidir}/%{name}.jar

%files doc
%{_docdir}/%{name}

%changelog
* Fri Jun 12 2026 Andrey Cherepanov <cas@altlinux.org> 1:2.6.0-alt1
- New version.
- Renamed to jogl.

* Mon Jan 05 2026 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt2
- FTBFS: remove strictly build with Java 11.x.

* Wed Apr 16 2025 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- New version

* Mon May 13 2024 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt9
- Rebuild with openjdk17

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt8_9jpp8
- xmvn4 support

* Mon Jun 06 2022 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt7_9jpp8
- migrated to %%mvn_artifact
- jogl2.jar moved to _jnidir

* Fri May 27 2022 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt6_9jpp8
- fixed build with new libs.req

* Sat Nov 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt5_9jpp8
- use patch for new Mesa from Mageia (ALT #41445)
- fix license names according to SPDX
- fix file conflicts between jogl2 and jogl2-doc

* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt4_9jpp8
- use zerg@'s hack for armh

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt3_9jpp8
- fixed build with new java

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_6jpp8
- java update

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_5jpp8
- restored arch libs (closes: #34087)

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_3jpp8
- new jpp release

* Mon Jan 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt2_2jpp8
- package libraries for scilab (ALT #33025)

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
