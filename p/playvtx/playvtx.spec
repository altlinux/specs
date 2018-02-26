Name: playvtx
Version: 0.9.2
Release: alt1

Summary: VTX file format player based on AY/YM emulation library
Group: Sound
License: GPL
Url: http://sashnov.nm.ru/libayemu.html

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Wed Mar 25 2009
BuildRequires: libayemu-devel

%description
This is player for AY/YM sound chip music packed to VTX format.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%_bindir/playvtx

%changelog
* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 0.9.2-alt1
- 0.9.1 -> 0.9.2

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 0.9.1-alt2
- don't use obsolete macros

* Tue May 23 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.1-alt1
- Initial build for Sisyphus

* Thu Feb 10 2005 Alexander Sashnov <sashnov@ngs.ru>
- Start this spec file.
