Name: fbgrab
Version: 1.2
Release: alt1

Summary: Framebuffer screenshot program
License: GCL
Group: Graphics
URL: http://fbgrab.monells.se/

Source0: %name-%version.tar.gz

BuildRequires: libpng-devel

%description
FBGrab is a framebuffer screenshot program, capturing the linux
frambuffer and converting it to a png-picture.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/f*

%changelog
* Sat Sep 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4.1
- Rebuilt with libpng15

* Fri Sep 21 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt4
- Remove Russian summary and description.

* Sun Oct 23 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt3
- Rebuild for x86_64.

* Sat Feb 19 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt2
- Rebuild with gcc 3.4.

* Sun May 09 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt1
- Rebuild with %optflags.

* Sat Mar 06 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt0.01
- First ALT Linux release.

