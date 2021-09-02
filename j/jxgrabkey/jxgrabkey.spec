Name: jxgrabkey
Version: 0.3.2
Release: alt4.r55

Summary: Using global X11 hotkeys on Linux from Java.
License: MIT
Group: Development/Java
Url: http://jxgrabkey.sf.net/

# svn co https://jxgrabkey.svn.sourceforge.net/svnroot/jxgrabkey/trunk jxgrabkey
Source0: %name-%version.tar
Patch0: %name-%version-alt-dont-do-tar-thing.patch
Patch1: default-java-path.patch
Patch2: fix-missing-headers.patch
Patch3: jxgrabkey-0.3.2-alt-doc.patch

BuildPreReq: ant gcc-c++ java-devel-default libX11-devel junit

%description
JXGrabKey is a jni library for easy use of global X11 hotkeys on linux
from java. It was inspired by the JIntellitype project. JXGrabKey was
originally created as a subproject of Coopnet
(http://coopnet.sourceforge.net).

%prep
%setup
%patch0 -p1
%patch1 -p2
%patch2 -p2
%patch3 -p2

sed -i '/default.javac/s,1\.4,1.6,g' JXGrabKey/Java/nbproject/build-impl.xml
sed -i '/javac/s,1\.5,1.6,g' JXGrabKey/Java/nbproject/project.properties

%build
pushd misc/Ant
ant
popd

%install
mkdir -p -m755 %buildroot%_jnidir %buildroot%_javadir
pushd misc/Ant
mv %name-%version/lib/libJXGrabKey.so %buildroot%_jnidir
mv %name-%version/lib/JXGrabKey.jar %buildroot%_javadir
popd

%files
%doc misc/Ant/%name-%version/docs misc/Ant/%name-%version/example misc/Ant/%name-%version/AUTHORS.txt misc/Ant/%name-%version/CHANGELOG.txt misc/Ant/%name-%version/LICENSE.txt
%_jnidir/libJXGrabKey.so
%_javadir/JXGrabKey.jar

%changelog
* Thu Sep 02 2021 Igor Vlasenko <viy@altlinux.org> 0.3.2-alt4.r55
- NMU: java 11 support

* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt3.r55
- NMU: fixed build.

* Fri Feb 22 2013 Paul Wolneykien <manowar@altlinux.ru> 0.3.2-alt2.r55
- Fix missing headers (patch).
- Fix the default java path (patch).

* Fri Mar 18 2011 Dmitry Derjavin <dd@altlinux.org> 0.3.2-alt1.r55
- initial build
