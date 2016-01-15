%set_verify_elf_method unresolved=strict

Name: gnustep-GTAMSAnalyzer
Version: 0.42
Release: alt5.1
Summary: GTAMS Analyzer is a complete coding and analysis package
License: GPL
Group: Graphical desktop/GNUstep
Url: http://tamsys.sourceforge.net/gtams/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
GTAMS Analyzer is a complete coding and analysis package. It is a "port"
of TAMS Analyzer for Macintosh OS X. Note, at some point the two
projects will have identical file formats, at which point  the initial G
(for GNUstep) will be dropped. GTAMS stands for GNUstep Text Analysis
Markup System, it is a convention for identifying themes in text. The
software offers a wide range of tools for applying themes to texts and
identifying patterns of themes within and between texts.

%package docs
Summary: Documentation for GTAMSAnalyzer
Group: Documentation
BuildArch: noarch

%description docs
GTAMS Analyzer is a complete coding and analysis package. It is a "port"
of TAMS Analyzer for Macintosh OS X. Note, at some point the two
projects will have identical file formats, at which point  the initial G
(for GNUstep) will be dropped. GTAMS stands for GNUstep Text Analysis
Markup System, it is a convention for identifying themes in text. The
software offers a wide range of tools for applying themes to texts and
identifying patterns of themes within and between texts.

This package contains documentation for GTAMSAnalyzer.

%prep
%setup

rm -f Source/obj

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build -C Source \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std -C Source GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_LOCAL_ROOT=%buildroot%_libdir/GNUstep

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ReadMe.* *.html
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files docs
%doc Documentation/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.42-alt5.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.42-alt5
- Built with clang

* Fri Feb 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.42-alt4
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.42-alt3
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.42-alt2
- Applied repocop patch

* Wed Jan 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.42-alt1
- Initial build for Sisyphus

