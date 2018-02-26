%define origname xmms_sndfile

Name: xmms-sndfile
Version: 1.2
Release: alt2

Summary: Input plugin for XMMS to use libsndfile
License: GPL
Group: Sound

Url: http://www.mega-nerd.com/xmms_sndfile
Source: %url/%origname-%version.tar.gz
Patch: %origname-memleak.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Dec 06 2008
BuildRequires: glibc-devel-static libsndfile-devel libxmms-devel

BuildRequires: libsndfile-devel >= 1.0.5

Summary(ru_RU.KOI8-R): Входной плагин для XMMS, использующий библиотеку libsndfile.

%description
Xmms_sndfile is an input plugin for XMMS (X multimedia system) allowing
XMMS to read any file format supported by libsndfile.

%description -l ru_RU.KOI8-R
Xmms_sndfile - это входной плагин для XMMS (Система Мультимедиа Х),
позволяющий XMMS проигрывать любой формат звукового файла, поддерживаемый
библиотекой libsndfile.

%define _xmms_input_plugin_dir %(xmms-config --input-plugin-dir)

%prep
%setup -n %origname-%version
%patch -p1

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_xmms_input_plugin_dir/*.so
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Sun Dec 07 2008 Michael Shigorin <mike@altlinux.org> 1.2-alt2
- adopted an orphan (xmms-minimal dependency)
- updated Url:
- spec cleanup
- buildreq

* Sat Jul 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2-alt1
- 1.2

* Sun May 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt1
- 1.1

* Thu Sep 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0pre6-alt4
- Rebuild with new libsndfile

* Wed Mar 06 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0pre6-alt3
- Rebuild with xmms-1.2.7
- Fixed "http" handling memory leak

* Fri Jun 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0pre6-alt2
- Rebuild with xmms-1.2.5
- Some spec cleanup

* Wed Apr 25 2001 Kostya Timoshenko <kt@altlinux.ru> 1.0pre6-alt1
- Build for ALT Linux

* Fri Jul 28 2000 Konstantin Volckov <goldhead@linux.ru.net>
  [xmms-sndfile-1.0pre6-1rus]
- Initial release.
