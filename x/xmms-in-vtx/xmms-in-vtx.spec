Name: xmms-in-vtx
Version: 0.9.1
Release: alt1

Summary: Plays VTX files containing music from the ZX Spectrum
License: GPL
Group: Sound
URL: http://sashnov.nm.ru/libayemu.html

Source0: xmms-vtx-%version.tar.gz

Patch0: xmms-vtx-0.9.1-alt-xmms.patch

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: xmms

# Automatically added by buildreq on Wed Mar 25 2009
BuildRequires: gcc-c++ libayemu-devel libxmms-devel

%description
libvtx is an XMMS input plugin. XMMS is a cross-platform multimedia
player. VTX - Vortex format for AY/YM music by Roman Scherbakov.  In
archive music_sample.tar.gz you can find 10 tunes in this format,
total time 31:15. More tunes could be found on http://vtx.microfor.ru

%prep
%setup -q -n xmms-vtx-%version
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc README ChangeLog NEWS TODO AUTHORS
%doc music_sample/
%xmms_inputdir/*.so
%exclude %xmms_inputdir/*.la

%changelog
* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 0.9.1-alt1
- 0.8.1 -> 0.9.1

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.8.1-alt3
- add xmms to Requires

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.8.1-alt2
- add Packager tag
- clean spec
- buildreq

* Tue May 23 2006 Igor Zubkov <icesik@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Mon May 22 2006 Igor Zubkov <icesik@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus
- based on spec file from Mandrake

* Wed Sep 10 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7-2mdk
- fix URL, I hope everybody understands Russian :-)

* Wed Sep 10 2003 Götz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- initial package

