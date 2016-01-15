#set_verify_elf_method unresolved=strict

Name: gnustep-CodeEditor
Version: 0.4.4
Release: alt5.1
Summary: CodeEditor is a text and code editor
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/codeeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-steptalk-devel

Requires: gnustep-steptalk
Requires: gnustep-back

%description
The goal of CodeEditor is to be a good non-rich text code editor.
CodeEditorView offers a subclass of NSTextView and supports syntax
highlight, mark delimiters, etc. It can be used in other projects.

Features:

* Faster than ever
* Tab View: Don't need to open so many terminals again.
* Toolbar: Use "Alt (left) - t" to open/close a simple toolbar on the
  fly.
* Find (Regular Express support) and replace.
* File Inspector.
* Change font attributes and preference instantly without restart.
* Periodically or manually Highlight keyword with difference attributes
  according to the language.
* Automatically or manually find delimiter pair.
* Automatically indentation according to the preference.
* Support scripting (need StepTalk).

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	OBJCFLAGS="%optflags -DGNUSTEP" \
	USE_NONFRAGILE_ABI=no
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

install -d %buildroot%_bindir
ln -s %_libdir/GNUstep/Applications/CodeEditor.app/CodeEditor \
	%buildroot%_bindir/

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc Changes README TODO Tutorial
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt5.1
- NMU: Rebuild with libgnutls30.

* Sun Feb 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt5
- Built with clang

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt4
- Rebuilt

* Mon Feb 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt2
- Added Requires: gnustep-steptalk and Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus

