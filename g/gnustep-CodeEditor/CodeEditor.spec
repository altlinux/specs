#set_verify_elf_method unresolved=strict

Name: gnustep-CodeEditor
Version: 0.4.4
Release: alt1
Summary: CodeEditor is a text and code editor
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.nongnu.org/codeeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-steptalk-devel

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
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles \
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

install -d %buildroot%_bindir
ln -s %_libdir/GNUstep/Applications/CodeEditor.app/CodeEditor \
	%buildroot%_bindir/

%files
%doc Changes README TODO Tutorial
%_bindir/*
%_libdir/GNUstep

%changelog
* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus

