%set_verify_elf_method unresolved=strict

Name: gnustep-Pantomime
Version: 1.2.0
Release: alt4
Summary: GNUMail framework
License: LGPL
Group: Graphical desktop/GNUstep
Url: http://wiki.gnustep.org/index.php/Pantomime
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel libssl-devel

Requires: lib%name = %EVR
Requires: gnustep-back
Requires: gnustep-GNUMail

%description
Pantomime provides a set of Objective-C classes that model a mail
system. Pantomime can be seen as a JavaMail 1.2 clone written in
Objective-C. Pantomime is almost entirely written in Objective-C. The C
language is only used where performance is critical. Pantomime uses a
little bit of ELM code. Pantomime is used in the project GNUMail.
Pantomime provides the following features:

* A full MIME encoder and decoder
* A 'folder view' to local mailboxes (Berkeley Format), POP3 accounts or
  IMAP mailboxes
* A powerful API to work on all aspects of Message objects
* A local mailer and a SMTP conduit for sending messages
* APOP and SMTP AUTH support
* IMAP and POP3 URL Scheme support
* iconv and Core Foundation support
* UNIX mbox and maildir support
* SSL/TLS support for IMAP, POP3 and SMTP and more!

%package -n lib%name
Summary: Shared libraries of GNUstep Pantomime
Group: System/Libraries

%description -n lib%name
Pantomime provides a set of Objective-C classes that model a mail
system. Pantomime can be seen as a JavaMail 1.2 clone written in
Objective-C. Pantomime is almost entirely written in Objective-C. The C
language is only used where performance is critical. Pantomime uses a
little bit of ELM code. Pantomime is used in the project GNUMail.

This package contains shared libraries of GNUstep Pantomime.

%package -n lib%name-devel
Summary: Development files of GNUstep Pantomime
Group: Development/Objective-C
Requires: lib%name = %EVR
Requires: %name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
Pantomime provides a set of Objective-C classes that model a mail
system. Pantomime can be seen as a JavaMail 1.2 clone written in
Objective-C. Pantomime is almost entirely written in Objective-C. The C
language is only used where performance is critical. Pantomime uses a
little bit of ELM code. Pantomime is used in the project GNUMail.

This package contains development files of GNUstep Pantomime.

%prep
%setup

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2 -lssl' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

pushd %buildroot%_libdir
for i in Pantomime; do
	lib=$(ls lib$i.so.*.*.*)
	for j in lib$i.so*; do
		rm -f $j
		mv GNUstep/Frameworks/$i.framework/Versions/1.2/$j ./
		ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/1.2/$j
	done
	rm -f GNUstep/Frameworks/$i.framework/Versions/1.2/$i
	ln -s %_libdir/$lib GNUstep/Frameworks/$i.framework/Versions/1.2/$i
done
popd

%files
%doc ChangeLog* README Documentation
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/*.framework/Headers
%exclude %_libdir/GNUstep/Frameworks/*.framework/Versions/1.2/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/*.framework/Headers
%_libdir/GNUstep/Frameworks/*.framework/Versions/1.2/Headers

%changelog
* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt4
- Added Requires: gnustep-back and Requires: gnustep-GNUMail

* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Rebuilt with new gnustep-gui

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added requirement on %name for lib%name-devel

* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

