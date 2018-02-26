Name: catpkt
Version: 1.0
Release: alt4

Summary: FTS Packet Viewer
License: BSD-like
Group: Text tools
Packager: Igor Zubkov <icesik@altlinux.ru>

Source0: ftp://oskin.macomnet.ru/pub/linux/fido/%name-%version.tar.gz

Patch0: catpkt-1.0-alt-warnings.patch
Patch1: catpkt-1.0-alt-natspec.patch
Patch2: catpkt-1.0-alt-newld.patch
Patch3: catpkt-1.0-alt-gcc4.patch

# Automatically added by buildreq on Thu Sep 15 2005
BuildRequires: libnatspec-devel

%description
Viewer for out/in-bound ftn-packets. Execution catpkt with no parameters
will give you help. There is no point address support, maybe, because, I'm
a bit lazy for all this stuff. You can use and modify it for free, the one
thing I ask you for, is to e-mail me your diffs. Recoding from cp866 charset
to koi8-r included by default (you can change this).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make_build FLAGS="%optflags"

%install
%__mkdir_p %buildroot%_bindir/
%__install --mode=0755 catpkt %buildroot%_bindir/

%files
%doc CHANGES README README.1st README.mc TODO bsd-style-copyright
%_bindir/catpkt

%changelog
* Sat Jul 22 2006 Igor Zubkov <icesik@altlinux.ru> 1.0-alt4
- fix build with gcc4

* Wed Mar 08 2006 Igor Zubkov <icesik@altlinux.ru> 1.0-alt3
- fix build with new ld / -Wl,--as-needed

* Thu Sep 15 2005 Igor Zubkov <icesik@altlinux.ru> 1.0-alt2
- add natspec support

* Tue Jun 07 2005 Igor Zubkov <icesik@altlinux.ru> 1.0-alt1
- Initial build for Sisyphus.
