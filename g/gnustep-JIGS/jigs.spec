%set_verify_elf_method unresolved=strict

Name: gnustep-JIGS
Version: 1.6.2
Release: alt1.4
Summary: Java Interface for GnuStep
License: LGPLv2.1
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.it/jigs/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildRequires: gnustep-gui-devel
BuildRequires: libgmp-devel libgnutls-devel libgcrypt-devel
BuildRequires: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildRequires: java-devel-default texlive-latex-base

Requires: lib%name = %EVR
Requires: gnustep-back

%description
JIGS stands for Java Interface for GnuStep. It is a package allowing
integration between Java and Objective-C. The main purpose of JIGS is
to allow Java programmers to use the GNUstep libraries from Java.
JIGS is more than a set of bindings for GNUstep from Java; JIGS takes
advantage of the fact that Objective-C and Java are very similar
languages to make it possible to use Objective-C classes from Java
using exactly the same API (and vice versa). You have to learn the
GNUstep API only once, and then you can use it both from Objective-C
and from Java in the same way! Moreover, JIGS can generate
automatically wrappers for your own Objective-C GNUstep libraries.

%package -n lib%name
Summary: Shared libraries of JIGS, Java Interface for GnuStep
Group: System/Libraries

%description -n lib%name
JIGS stands for Java Interface for GnuStep. It is a package allowing
integration between Java and Objective-C. The main purpose of JIGS is
to allow Java programmers to use the GNUstep libraries from Java.
JIGS is more than a set of bindings for GNUstep from Java; JIGS takes
advantage of the fact that Objective-C and Java are very similar
languages to make it possible to use Objective-C classes from Java
using exactly the same API (and vice versa). You have to learn the
GNUstep API only once, and then you can use it both from Objective-C
and from Java in the same way! Moreover, JIGS can generate
automatically wrappers for your own Objective-C GNUstep libraries.

This package contains shared libraries of JIGS.

%package -n lib%name-devel
Summary: Development files of JIGS, Java Interface for GnuStep
Group: Development/Other
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
JIGS stands for Java Interface for GnuStep. It is a package allowing
integration between Java and Objective-C. The main purpose of JIGS is
to allow Java programmers to use the GNUstep libraries from Java.
JIGS is more than a set of bindings for GNUstep from Java; JIGS takes
advantage of the fact that Objective-C and Java are very similar
languages to make it possible to use Objective-C classes from Java
using exactly the same API (and vice versa). You have to learn the
GNUstep API only once, and then you can use it both from Objective-C
and from Java in the same way! Moreover, JIGS can generate
automatically wrappers for your own Objective-C GNUstep libraries.

This package contains development files of JIGS.

%package docs
Summary: Documentation for JIGS, Java Interface for GnuStep
Group: Development/Documentation
BuildArch: noarch

%description docs
JIGS stands for Java Interface for GnuStep. It is a package allowing
integration between Java and Objective-C. The main purpose of JIGS is
to allow Java programmers to use the GNUstep libraries from Java.
JIGS is more than a set of bindings for GNUstep from Java; JIGS takes
advantage of the fact that Objective-C and Java are very similar
languages to make it possible to use Objective-C classes from Java
using exactly the same API (and vice versa). You have to learn the
GNUstep API only once, and then you can use it both from Objective-C
and from Java in the same way! Moreover, JIGS can generate
automatically wrappers for your own Objective-C GNUstep libraries.

This package contains documentation for JIGS.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export JAVA_HOME=/usr/lib/jvm/java

%ifarch x86_64
JAVA_SERVER=$JAVA_HOME/jre/lib/amd64/server
%else
JAVA_SERVER=$JAVA_HOME/jre/lib/i386/server
%endif

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	JAVA_SERVER=$JAVA_SERVER
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

cp -fR Examples Testing %buildroot%_docdir/GNUstep/Developer/JIGS/

%files
%doc ChangeLog FAQ NEWS PACKAGING README TODO
%_bindir/*
%_libdir/GNUstep

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_datadir/GNUstep

%files docs
%_docdir/GNUstep

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1.4
- nmu: rebuild with new openjdk java

* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.2-alt1.3
- Rebuild with new icu

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1.2
- rebuild with java-1.6.0

* Sat Jun 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1.1
- rebuild with new openjdk java

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1
- Initial build for Sisyphus

