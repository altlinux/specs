Name: xorg-cf-files
Version: 1.0.4
Release: alt2
Summary: config files for Xorg build
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2

BuildRequires: xorg-util-macros xorg-font-utils 

%description
Config files for Xorg build

%prep
%setup

%build
%autoreconf
%configure \
	--with-config-dir=%_datadir/X11/config
%make

cat > host.def << EOF
#define XFree86CustomVersion	"ALT Linux build: 7.6.0"
#define BuilderString		"Build Host: %(hostname)\n"

#define XFree86RedHatCustom	YES
#define BootstrapCFlags		$RPM_OPT_FLAGS
#define DefaultGcc2i386Opt	$RPM_OPT_FLAGS -fno-strength-reduce GccAliasingArgs -pipe
#define DefaultGcc2x86_64Opt	$RPM_OPT_FLAGS -fno-strength-reduce GccAliasingArgs -pipe
#define DefaultGcc2AxpOpt	$RPM_OPT_FLAGS -Wa,-m21164a GccAliasingArgs -pipe
#define DefaultGcc2PpcOpt	$RPM_OPT_FLAGS GccAliasingArgs -pipe

#define ConfigDir		%_datadir/X11/config
#define X11ProjectRoot		%prefix
#define ProjectRoot		%prefix
#define XBinDir			%_bindir
#define BinDir			%_bindir
#define XUsrLibDirPath		%_libdir
#define UsrLibDir		%_libdir
#define LibDir			%_datadir/X11
#define IncRoot			%_includedir
#define ManDirectoryRoot	%_mandir
#define AdmDir			%_logdir
#define LbxproxyDir		%_sysconfdir/X11/lbxproxy
#define ProxyManagerDir		%_sysconfdir/X11/proxymngr
#define ServerConfigDir		%_sysconfdir/X11/xserver
#define XdmDir			%_sysconfdir/X11/xdm
#define XConfigDir		%_sysconfdir/X11
#define XinitDir		%_sysconfdir/X11/xinit
#define EtcX11Directory		%_sysconfdir/X11
#define XAppLoadDir		%_sysconfdir/X11/app-defaults
#define XPrintDir		%_sysconfdir/X11/xprint
#define DefaultRGBDatabase	%_datadir/X11/rgb
#define DefaultFSConfigFile	%_sysconfdir/X11/fs/config
#define FontDir			%_datadir/X11/fonts

#define XOrgNameString		ALTLinux X.Org Maintainer Team
#define XOrgWebSupportAddress	https://bugzilla.altlinux.org
#define BuilderEMailAddr	"xorg@packages.altlinux.org"

#define BuildHtmlManPages       NO
#define ManSuffix		1
#define LibManSuffix		3
#define DriverManSuffix		4
#define FileManSuffix		5
#define MiscManSuffix		7

EOF

%install
%make DESTDIR=%buildroot install

# XXX repocop suxx
mkdir -p %buildroot%_libdir/%name
for f in host.def linux.cf sgi.cf; do
  mv %buildroot%_datadir/X11/config/$f %buildroot%_libdir/%name/;
  ln -s `relative %buildroot%_libdir/%name/$f %buildroot%_datadir/X11/config/$f` %buildroot%_datadir/X11/config/$f
done

%files
%_datadir/X11/config
%_libdir/%name/*

%changelog
* Tue May 10 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt2
- This package is NOT noarch

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2.1
- Automatic buildreqfix
- Autobuild watchfile added

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- fixed build

* Fri Feb 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Feb 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt5
- set LibDir to %_datadir/X11 (fixed #9030)

* Tue Feb 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt4
- set DefaultFSConfigFile to %_sysconfdir/X11/fs/config, FontDir to %_datadir/X11/fonts (#9030)

* Tue Jan 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- set DefaultRGBDatabase to %_datadir/X11/rgb

* Tue Jan 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- set X11ProjectRoot to %prefix

* Thu Dec 29 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

