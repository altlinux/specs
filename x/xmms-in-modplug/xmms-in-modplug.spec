Name: xmms-in-modplug
Version: 2.05
Release: alt4

Summary: Xmms plugin based on libmodplug library.
License: GPL
Group: Sound

%define _progname modplugxmms

Url: http://modplug-xmms.sourceforge.net
Source: http://dl.sf.net/modplug-xmms/%_progname-%version.tar.gz
Patch: modplugxmms-2.05-alt-gcc43.patch
Packager: Michael Shigorin <mike@altlinux.org>

Obsoletes: %_progname

# Automatically added by buildreq on Thu May 15 2008
BuildRequires: gcc-c++ libmodplug-devel libxmms-devel

%description
This package contains xmms plugin for playing sound modules.
It is based on libmodplug library.

%package -n modplugplay
Summary: Console module player based on libmodplug library.
Group: Sound

%description -n modplugplay
This package contains console module player based on libmodplug library

%ifndef %xmms_inputdir
%define xmms_inputdir %(xmms-config --input-plugin-dir)
%endif

%prep
%setup -n %_progname-%version
%patch -p1

%build
%configure
%make_build

%install
%make \
	bindir=%buildroot%_bindir \
	plugindir=%buildroot%xmms_inputdir \
	install

%files
%xmms_inputdir/*.so
%doc AUTHORS README

%files -n modplugplay
%_bindir/*

%changelog
* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 2.05-alt4
- fixed build with gcc 4.3
- changed Packager: to myself

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 2.05-alt3
- buildreq
- minor spec cleanup

* Mon Dec 04 2006 Michael Shigorin <mike@altlinux.org> 2.05-alt1.2
- rebuild (undefined symbol: _ZN10CSoundFile13SetWaveConfigEmmmb)

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.05-alt1.1
- Rebuilt with libstdc++.so.6.

* Sat Dec 20 2003 Yury Aliaev <mutabor@altlinux.ru> 2.05-alt1
- Build with new name from modplugxmms
- Can use new xmms macros
- Added forgotten documentation
