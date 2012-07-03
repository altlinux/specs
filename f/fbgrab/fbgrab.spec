Name: fbgrab
Version: 1.0
Release: alt4

Summary: Framebuffer screenshot program
License: GCL
Group: Graphics
URL: http://hem.bredband.net/gmogmo/fbgrab/
Packager: Vadim V. Zhytnikov <vvzhy@altlinux.ru>

Source0: %name-%version.tar.gz

BuildRequires: libpng-devel

%description
FBGrab is a framebuffer screenshot program, capturing the linux
frambuffer and converting it to a png-picture.

%prep
%setup -q

%build
gcc %optflags fbgrab.c -lpng -lz -o fbgrab

%install
install -D -m755 fbgrab %buildroot%_bindir/fbgrab
install -D -m644 fbgrab.1.man %buildroot%_man1dir/fbgrab.1

%files
%_bindir/*
%_man1dir/f*

%changelog
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








