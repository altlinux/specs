%define _unpackaged_files_terminate_build 1
%def_with check

# Cross-platform launchers mention optional debuggers and macOS-only helpers.
%filter_from_requires /^\(gdb\|lldb[0-9.]*\|rr\|kdbg\|valgrind\)$/d
%filter_from_requires /^\(open\|xml-utils\|libgio\|systemd-utils\)$/d
%filter_from_requires \,^/usr/bin/\(gdb\|lldb\|rr\|kdbg\|valgrind\|open\|defaults\|osascript\|xmllint\|glxinfo\|chcon\|busctl\|gdbus\)$,d
%filter_from_requires \,^/usr/libexec/java_home$,d
%filter_from_requires \,^/usr/sbin/selinuxenabled$,d

Name: scilab
Version: 2027.0.0
Release: alt1
Epoch: 1

Summary: Open source, cross-platform numerical computational package
License: GPL-2.0-only
Group: Sciences/Mathematics
Url: https://www.scilab.org/
VCS: https://gitlab.com/scilab/scilab.git
ExcludeArch: %ix86

Source: %name-%version.tar.gz
Source1: scilab-smoke.sce
Source2: ScilabJaxbCheck.java
Source3: scilab-symbol-init.cpp
Source4: scilab-smoke.xls
Source5: %name-%version-web-vendor.tar
Source6: build-web.sh
Patch0: %name-%version-alt.patch

# The JVM and external JARs are loaded at runtime via the launcher and classpath.xml.
Requires: java >= 21
Requires: openjfx
Requires: jetbrains-jcef
Requires: jogl
Requires: gluegen
Requires: ecj
Requires: google-gson flexdock jrosetta jgraphx jgoodies-looks skinlf
Requires: jakarta-activation jakarta-activation1 angus-activation
Requires: geronimo-annotation jaxb-api jaxb-runtime jaxb-core
Requires: mvn(com.sun.istack:istack-commons-runtime)
Requires: mvn(org.glassfish.jaxb:txw2)
Requires: lucene lucene-analysis lucene-queryparser
Requires: fop batik xmlgraphics-commons avalon-framework
Requires: apache-commons-logging apache-commons-io xml-commons-apis saxon
Requires: jlatexmath
Requires: jlatexmath-fop
Requires: jeuclid

BuildRequires(pre): rpm-build-java
BuildRequires(pre): rpm-build-xdg
BuildRequires: gcc-c++
BuildRequires: gcc-fortran
BuildRequires: libgomp-devel
BuildRequires: /proc
BuildRequires: node
BuildRequires: esbuild
BuildRequires: libcolpack-devel
BuildRequires: libssl-devel
BuildRequires: zlib-devel
BuildRequires: libhdf5-devel
BuildRequires: xlnt-devel
BuildRequires: pkgconfig(arrow)
BuildRequires: pkgconfig(parquet)
BuildRequires: pkgconfig(cppserver)
BuildRequires: pkgconfig(cppcommon)
BuildRequires: pkgconfig(sundials)
BuildRequires: eigen3-devel
BuildRequires: ocaml
BuildRequires: ocaml-num-devel
BuildRequires: java-25-openjdk-devel
BuildRequires: ant
BuildRequires: ecj
BuildRequires: google-gson
BuildRequires: jetbrains-jcef
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: libarchive-devel
BuildRequires: libcurl-devel
BuildRequires: liblapack-devel
BuildRequires: libarpack-ng-devel
BuildRequires: libsuitesparse-devel
BuildRequires: libfftw3-devel
BuildRequires: libmatio-devel
BuildRequires: libncurses-devel
BuildRequires: libpcre2-devel
BuildRequires: rapidjson
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: flexdock
BuildRequires: jrosetta
BuildRequires: jgraphx
BuildRequires: jgoodies-looks
BuildRequires: skinlf
BuildRequires: jogl
BuildRequires: gluegen
BuildRequires: jakarta-activation
BuildRequires: jakarta-activation1
BuildRequires: angus-activation
BuildRequires: jaxb-api
BuildRequires: jaxb-runtime
BuildRequires: jaxb-core
BuildRequires: mvn(com.sun.istack:istack-commons-runtime)
BuildRequires: mvn(org.glassfish.jaxb:txw2)
BuildRequires: geronimo-annotation
BuildRequires: openjfx
BuildRequires: lucene
BuildRequires: lucene-analysis
BuildRequires: lucene-queryparser
BuildRequires: fop
BuildRequires: batik
BuildRequires: xmlgraphics-commons
BuildRequires: avalon-framework
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-io
BuildRequires: xml-commons-apis
BuildRequires: saxon
BuildRequires: jlatexmath
BuildRequires: jlatexmath-fop
BuildRequires: jeuclid
BuildRequires: ocaml-findlib-devel
BuildRequires: libGL-devel

%if_with check
BuildRequires: xvfb-run
BuildRequires: dbus
BuildRequires: fonts-ttf-dejavu
BuildRequires: junit
BuildRequires: hamcrest
BuildRequires: ant-junit
BuildRequires: node-mocha
BuildRequires: chromium
%endif

%description
Open source, cross-platform numerical computational package and
a high-level, numerically oriented programming language.

%prep
%setup
%autopatch -p1
# Keep the upstream ripOLE sources for legacy XLS support.
rm -rf modules/differential_equations/src/patched_sundials \
    modules/sparse/src/ColPack
rm -f modules/core/src/cpp/hash/*.cpp \
    modules/core/src/cpp/hash/crc32.hxx \
    modules/core/src/cpp/hash/sha1.hxx \
    modules/core/src/cpp/hash/sha256.hxx \
    modules/core/src/cpp/hash/sha3.hxx
tar -xf %SOURCE5
mv scilab-%version-web-vendor .web-vendor
%autoreconf

%build
sh %SOURCE6
export JAVA_HOME=%_jvmdir/java-25-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
%configure --without-emf --disable-static-system-lib \
    --with-system-cppserver \
    --with-system-sundials \
    --with-system-colpack \
    --with-eigen-include=%_includedir/eigen3
%make_build

%install
%makeinstall_std
install -d %buildroot%_datadir/scilab/thirdparty
cp -a thirdparty/web %buildroot%_datadir/scilab/thirdparty/
find %buildroot%_libdir/scilab -name '*.la' -delete
# The FMU archive already contains these architecture-specific test fixtures.
rm -rf \
    %buildroot%_datadir/scilab/modules/fmu/tests/unit_tests/CruiseControl__CruiseControl_FMU/binaries

%check
WEB_ASSET_DIR="$PWD/thirdparty/web" \
    node .web-vendor/monaco-editor/build/monaco/system/test.cjs \
    "$PWD/thirdparty/web/monaco-editor"
%__cxx %optflags -std=c++17 -fno-lto \
    -I modules/ast/includes/symbol -I modules/ast/includes/ast \
    %SOURCE3 modules/ast/src/cpp/symbol/symbol.cpp -o .symbol-init-check
./.symbol-init-check
export JAVA_HOME=%_jvmdir/java-25-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
JAXB_CP=%_javadir/jaxb-api.jar
JAXB_CP="$JAXB_CP:%_javadir/jaxb/jaxb-runtime.jar"
JAXB_CP="$JAXB_CP:%_javadir/jaxb/jaxb-core.jar"
JAXB_CP="$JAXB_CP:%_javadir/jaxb/txw2.jar"
JAXB_CP="$JAXB_CP:%_javadir/angus-activation/angus-activation.jar"
JAXB_CP="$JAXB_CP:%_javadir/jakarta-activation/jakarta.activation-api.jar"
JAXB_CP="$JAXB_CP:%_javadir/jaxb-istack-commons/istack-commons-runtime.jar"
mkdir -p .jaxb-check
javac -cp "modules/xcos/jar/org.scilab.modules.xcos.jar:$JAXB_CP" \
    -d .jaxb-check %SOURCE2
java -cp ".jaxb-check:modules/xcos/jar/org.scilab.modules.xcos.jar:$JAXB_CP" ScilabJaxbCheck
unset JAVA_HOME
xvfb-run -a -s '-screen 0 1280x1024x24' dbus-run-session -- \
    %make check
mkdir -p .scilab-check-home
export HOME="$PWD/.scilab-check-home"
timeout 120 ./bin/scilab-cli -nb -noatomsautoload -nouserstartup -f %SOURCE1
xvfb-run -a -s '-screen 0 1280x1024x24' dbus-run-session -- \
    timeout 120 ./bin/scilab -nb -noatomsautoload -nouserstartup -f %SOURCE1

%files
%doc COPYING COPYING-BSD modules/spreadsheet/src/c/ripole/LICENSE.ripole
%_bindir/scilab*
%_bindir/scinotes
%_bindir/xcos
%_bindir/XML2Modelica
%_bindir/modelicac
%_bindir/modelicat
%_libdir/scilab/
%_pkgconfigdir/scilab.pc
%_includedir/scilab/
%_datadir/scilab/
%_datadir/locale/*/LC_MESSAGES/scilab.mo
%_desktopdir/scilab*.desktop
%_desktopdir/xcos.desktop
%_desktopdir/scinotes.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/mimetypes/application-x-scilab-*.png
%_datadir/appdata/scilab.appdata.xml
%_xdgmimedir/packages/scilab.xml

%changelog
* Thu Nov 12 2026 Ajrat Makhmutov <rauty@altlinux.org> 1:2027.0.0-alt1
- New version.
- Fix aarch64 FTBFS caused by va_list arguments and unsigned plain char.
- Rework packaging around the upstream sources and a cumulative ALT patch.
- Remove obsolete patches and use the upstream desktop files.
- Update package metadata, license information and source repository URL.
- Revise architecture restrictions and exclude 32-bit x86.
- Build with OpenJDK 25 and require Java 21 or newer at runtime.
- Detect distribution-provided Java libraries and JNI directories.
- Skip headless JVMs when automatically selecting Java for GUI startup.
- Reject Saxon implementations without a working transformer factory.
- Migrate Xcos XML bindings and runtime dependencies to Jakarta JAXB.
- Support the system JetBrains JCEF runtime and browser subprocess.
- Wait for browser shutdown before destroying the embedded JVM.
- Set the AWT window-manager hint for Wayland sessions to address
  Swing, Xcos and SciNotes rendering issues.
- Avoid linking private JVM libraries outside macOS.
- Link startup and Xcos modules against their engine dependencies.
- Correct module build and installation order for Xcos and MPI linkage.
- Unregister the Java environment before unloading its native library.
- Load the native library required for Java type transfer methods.
- Accept legacy integer type names regardless of case.
- Fix symbol pool initialization, synchronization and shutdown lifetime.
- Recognize target-prefixed GCC and G++ commands during configuration.
- Require C++20 for compatibility with current Arrow headers.
- Stop the build when macro or function-list generation fails.
- Use system CppServer and CppCommon libraries on Linux.
- Use system SUNDIALS libraries with Scilab extensions on Linux.
- Compile SUN_Clink callbacks against system SUNDIALS headers without
  enforcing an exact version at runtime.
- Suggest installing sundials-devel when SUN_Clink needs system headers.
- Use system ColPack on Linux and resolve boolean header conflicts.
- Replace bundled digest implementations with OpenSSL and zlib.
- Report digest failures instead of accepting empty macro checksums.
- Build browser dependencies offline from bundled source archives.
- Package browser assets and adapt SciNotes assistant and help paths
  to the locally built bundles.
- Support Monaco workers loaded from local file URLs.
- Preserve third-party web dependency licenses and source metadata.
- Restore the native type test, keep its assertions enabled in release
  builds and fix an invalid integer read in the test code.
- Remove the obsolete function manager test target.
- Supply Java test runtime dependencies and skip optional console
  Sikuli tests when their prerequisites are unavailable.
- Update numeric string expectations and the empty Xcos diagram fixture.
- Add regression coverage for legacy Xcos diagram imports.
- Add symbol initialization and Xcos JAXB persistence checks.
- Add CLI and GUI smoke tests for numerical operations, data formats,
  system libraries, plotting, SciNotes, Xcos and JCEF initialization.
- Run upstream make check targets and browser asset checks during the build.
- Preserve legacy XLS support through ripOLE and package its license.
- Remove duplicate FMU test binaries from the installed files.
- Enable shell dependency scanning and filter optional launcher tools
  instead of excluding the launchers from automatic dependency checks.
- Keep explicit Java runtime dependencies and rely on automatic
  dependencies for linked native libraries and standard tools.
- Enforce complete packaging of installed files.
- Spec cleanup.

* Mon May 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1:6.0.2-alt5
- NMU: fix build

* Sat Jun 11 2022 Igor Vlasenko <viy@altlinux.org> 1:6.0.2-alt4
- NMU: support for xml-commons-apis-1.4.01-alt3_35jpp11

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 1:6.0.2-alt3
- NMU: removed checkstyle from BR: and fixed build

* Mon Nov 22 2021 Andrey Cherepanov <cas@altlinux.org> 1:6.0.2-alt2
- Downgrade to working 6.0.2 (ALT #40587).

* Wed Oct 27 2021 Andrey Cherepanov <cas@altlinux.org> 6.1.1-alt2
- Explicitly use java-1.8.0-openjdk.
- Add avalon-framework to requirements (ALT #40586).

* Mon Jul 26 2021 Andrey Cherepanov <cas@altlinux.org> 6.1.1-alt1
- New version (ALT #40149).

* Sat May 02 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.0-alt1
- New version.

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- New version.

* Fri Feb 15 2019 Ivan Razzhivin <underwit@altlinux.org> 6.0.1-alt4
- GCC8 fix

* Thu Nov 29 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt3
- Fix build with gfortran 8.
- Do not build on aarch64.

* Mon Mar 19 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt2
- Use generated documentation on x64_64.

* Fri Feb 16 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.
- Build without docs.

* Sat Dec 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt3.2
- NMU: added batik 1.9 to supported batik versions (ALT #34263)

* Fri Dec 01 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt3.1
- NMU: fixed build with new jgraphx (ALT #34263)

* Mon Nov 20 2017 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt3
- Show scinotes menu only in Development section

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt2
- Build docs (ALT #34037)
- Fix run from menu (ALT #33976)
- Remove duplicate categories

* Wed Jun 07 2017 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.5.2-alt1.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Tue Jan 24 2017 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt1
- New version (ALT #31794)
- Build from upstream git repository
- Require version-independed JDK
- Build with bundled scirenderer
- Add jogl2 and ecj to requirements

* Sun Nov 16 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1
- New version

* Mon Nov 10 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt2
- Add ecj to requirements to fix build documentation

* Mon Apr 14 2014 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1
- New version
- Do not use freehep* package for EMF support

* Fri Feb 28 2014 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt2
- Fix build (use unversioned libgomp-devel)

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.1-alt1.1
- Rebuilt with new libhdf5

* Sun May 26 2013 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version 5.4.1
- Build docs again (fixed in upstream bug 4134)

* Fri May 24 2013 Andrey Cherepanov <cas@altlinux.org> 5.4.0-alt1
- New version 5.4.0 (ALT #25996)
- Translate desktop files into Russian
- Disable build documentation

* Tue Oct 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.1-alt3
- build doc (ALT #21904)

* Sat Sep 12 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.1-alt2
- remove libumfpack-devel from buildrequres

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.1-alt1
- 5.1.1

* Wed Dec 24 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt6
- with gtk2, bugfix for #18307 ALT bugzilla

* Wed Sep 24 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt5
- Fix bug with not working editor (#17318)

* Sat Sep 20 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt4
- repocop suggested change /tmp to /home/denis/tmp for safety

* Tue May 06 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt3
- bug 15556 - BWidged removed and used in-system

* Tue May 06 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt1.M40.1
- Updates to Branch M40

* Tue May 06 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt2
- repocop icondirs

* Tue May 06 2008 Denis Medvedev <nbr@altlinux.ru> 4.1.2-alt1
 - 4.1.2 version from upstream

* Fri Sep 28 2007 Denis Medvedev <nbr@altlinux.ru> 4.1.1-alt1.3
- Debug option, pic option

* Thu Aug 30 2007 Denis Medvedev <nbr@altlinux.ru> 4.1.1-alt1.2
- changes for x86_64 compilation

* Tue Aug 28 2007 Denis Medvedev <nbr@altlinux.ru> 4.1.1-alt1.1
- Taken from orphaned, new version

* Wed Feb 08 2006 ALT QA Team Robot <qa-robot@altlinux.org> 3.1.1-alt1.1
- Rebuild with libXaw3d.so.8 .

* Tue Dec 20 2005 Dimitry V. Ketov <dketov@altlinux.ru> 3.1.1-alt1
- 3.1.1
- app-defaults location fix

* Wed Dec 08 2004 Dimitry V. Ketov <dketov@altlinux.ru> 3.0-alt1
- 3.0
- misc. spec bugfixes, sources clean before build
- menu and new scilab mascot icons

* Tue Apr 08 2003 Stanislav Ievlev <inger@altlinux.ru> 2.7-alt1
- 2.7

* Mon Oct  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.6-alt8
- rebuilt with tcl 8.4

* Wed Sep 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt7
- rebuild with new XFree86

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt6
- rebuild with gcc3
- termcap -> terminfo

* Sat Jun 15 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.6-alt5
- rebuilt in new env

* Mon Dec 24 2001 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt4
- fix links in app-defaults

* Thu Oct 11 2001 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt3
- MDK merges

* Fri May 25 2001 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt2
- path bugfix. Remove doc package.

* Thu Apr 12 2001 Stanislav Ievlev <inger@altlinux.ru> 2.6-alt1
- Up to 2.6. spec clean up and bugfix

* Tue Jan 09 2001 AEN <aen@logic.ru>
- adopted for RE

* Sun Oct 22 2000 Fernando M. Roxo da Motta <roxo@conectiva.com.br>
- inserted documentation package

* Fri Oct 20 2000 Fernando M. Roxo da Motta <roxo@conectiva.com.br>
- Fixed hardwired PATH's

* Wed Oct 18 2000 Fernando M. Roxo da Motta <roxo@conectiva.com.br>
- Packaged for Conectiva Linux
- Fixed a lot of macros

* Tue Sep 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.4.1-3mdk
- build release
- macros
- menu

* Wed May 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.4.1-2mdk
- bzip2 patches
- fix group

* Thu Dec 30 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- bz2 archive

* Wed Aug 18 1999 Tim Powers <timp@redhat.com>
- exludearch alpha

* Wed Jul 21 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Wed May 12 1999 Bill Nottingham <notting@redhat.com>
- clean up dependencies

* Wed May 05 1999 Bill Nottingham <notting@redhat.com>
- update to 2.4.1

* Fri Oct 23 1998 Jeff Johnson <jbj@redhat.com>
- Upgrade to 2.4.

* Thu Oct 22 1998 Jeff Johnson <jbj@redhat.com>
- Fixes to permit compile on alpha.
- Eliminate lurking dependencies on /bin/sh5 and SCILABGS.
- Modify default value of SCI variable to be correct for users.
- Add /usr/bin/scilab symlink.

* Sat Jul 11 1998 Jeff Johnson <jbj@redhat.com>
- Create powertools package.
