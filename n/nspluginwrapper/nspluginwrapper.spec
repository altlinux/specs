%global _hardened_build 1
%define _default_patch_fuzz 2

# Compile as a debug package
%define make_debug_package 	0

# What gecko we use
%define gecko_flavour		"mozilla"

%define plugin_config_version 1.9
%define plugin_config_name plugin-config-%{plugin_config_version}
%define plugin_config_binary plugin-config

# Excluded plugins (separated by ':')
%define exclude_list 	"libtotem*:libjavaplugin*:gecko-mediaplayer*:mplayerplug-in*:librhythmbox*:packagekit*:libnsISpicec*:libgnashplugin*:liblightsparkplugin*:npesteid*:mozplugger*"

# Target defines
%if "%{_target_cpu}" == "i386"
%define target_bits	32
%endif

%if "%{_target_cpu}" == "i586"
%define target_bits	32
%endif

%if "%{_target_cpu}" == "i686"
%define target_bits	32
%endif

%if "%{_target_cpu}" == "ppc"
%define target_bits	32
%endif

%if "%{_target_cpu}" == "armv5tel"
%define target_bits	32
%endif

%if "%{_target_cpu}" == "armv7hl"
%define target_bits	32
%endif

%if "%{_target_cpu}" == "x86_64"
%define target_bits	64
%endif

%if "%{_target_cpu}" == "ppc64"
%define target_bits	64
%endif

# Define libraries for 32/64 arches
%define lib32			lib
%define lib64			lib64
%define libdir32		/usr/lib
%define libdir64		/usr/lib64

# define nspluginswrapper libdir (invariant, including libdir)
%define pkgdir32		%{libdir32}/%{name}
%define pkgdir64		%{libdir64}/%{name}

# define mozilla plugin dir and back up dir for 32-bit browsers
%define pluginsourcedir32	%{libdir32}/browser-plugins
%define plugindir32 		%{libdir32}/browser-plugins-wrapped

# define mozilla plugin dir and back up dir for 64-bit browsers
%define pluginsourcedir64	%{libdir64}/browser-plugins
%define plugindir64 		%{libdir64}/browser-plugins-wrapped

%define build_dir 		objs-%{target_bits}

%if "%{target_bits}" == "32"
%define lib		%{lib32}
%define libdir  	%{libdir32}
%define pkgdir  	%{pkgdir32}
%define plugindir	%{plugindir32}
%define pluginsourcedir	%{pluginsourcedir32}
%else
%define lib	  	%{lib64}
%define libdir  	%{libdir64}
%define pkgdir  	%{pkgdir64}
%define plugindir	%{plugindir64}
%define pluginsourcedir	%{pluginsourcedir64}
%endif

%define svndate 928c322

Summary:	A compatibility layer for Netscape 4 plugins
Name:		nspluginwrapper
Version:	1.4.4
Release:	alt2
License:	GPLv2+
Group:		Networking/WWW
Url:		http://nspluginwrapper.org/
ExclusiveArch:	%{ix86} x86_64 ppc %{arm}

Source0:	http://nspluginwrapper.org/download/%name-%version.tar.gz
Source1:	%{plugin_config_name}.tar.gz
Source2:	plugin-config.sh.in
Source3:	%{name}.sh.in
Source4:	nspluginplayer.1.gz
Source5:        nspluginwrapper.1.gz

Patch1:		nspluginwrapper-1.4.4-make.patch
Patch3:		nspluginwrapper-1.3.0-directory.patch
Patch6:		nspluginwrapper-1.3.0-compiz.patch
Patch7:		nspluginwrapper-1.3.0-comp.patch
Patch10:	nspluginwrapper-pthread.patch
Patch11:	nspluginwrapper-arm.patch
Patch12:	nspluginwrapper-1.4.4-restart.patch
Patch100:	plugin-config-setuid.patch
Patch101:	plugin-config-umask.patch
Patch102:	plugin-config-print.patch
Patch103:	plugin-config-non-native.patch
Patch104:	plugin-config-time-check.patch
Patch105:	plugin-config-dlopen.patch
Patch106:	plugin-config-help.patch

Provides:	%{name} = %{version}-%{release}
BuildRequires:	pkgconfig gtk2-devel glib2-devel nspr-devel
BuildRequires:	libX11-devel libXt-devel libcairo-devel pango-devel libcurl-devel
#BuildRequires:	xulrunner-devel

%description
nspluginwrapper makes it possible to use Netscape 4 compatible plugins
compiled for i386 architecture (e.g. flash-plugin) into Mozilla for another 
architecture, e.g. x86_64.

This package consists in:
  * npviewer: the plugin viewer
  * npwrapper.so: the browser-side plugin
  * nspluginplayer: stand-alone NPAPI plugin player
  * mozilla-plugin-config: a tool to manage plugins installation and update

%prep
%setup  -q -a 1

# Installation & build patches
%patch1 -p1 -b .make
%patch3 -p1 -b .dir
%patch6 -p1 -b .compiz
%patch7 -p1 -b .comp
THREAD_LIBS=`pkg-config --libs gthread-2.0`
sed -e "s/__PTHREAD_LIBS__/$THREAD_LIBS/" %{P:%%PATCH10} > pthread.patch
%{__patch} -p1 -b --suffix .version --fuzz=0 < pthread.patch
%patch11 -p1 -b .arm
%patch12 -p1 -b .restart

# Plugin-config patches
pushd %plugin_config_name
%patch100 -p2
%patch101 -p2 -b .umask
%patch102 -p2 -b .print
%patch103 -p2 -b .non-native
%patch104 -p2 -b .time
%patch106 -p2 -b .help
popd
%patch105 -p1 -b .dlopen

# Set ALT-specific plugins place
subst 's,mozilla/plugins,browser-plugins,' \
	src/npw-config.c \
	plugin-config-1.9/src/plugin-path.h

%build
# Build wrapper

# set the propper built options
%if %{make_debug_package}
    %if "%{target_bits}" == "64"
	export CFLAGS="-g -m64 -DDEBUG"
    %else
	export CFLAGS="-g -m32 -DDEBUG"
    %endif
%else
    export CFLAGS="$RPM_OPT_FLAGS"
%endif

# set the propper built options
%ifnarch %{arm}
%if "%{target_bits}" == "64"
    export LDFLAGS="-m64 -L%{libdir64} -ldl" 
%else
    export LDFLAGS="-m32 -L%{libdir32} -ldl"
%endif
%else
    export LDFLAGS="-L%{libdir32} -ldl"
%endif
export LDFLAGS="$LDFLAGS -z now"

mkdir %{build_dir}
pushd %{build_dir}
../configure 					\
	    --prefix=%{_prefix} 		\
	    --target-cpu=%{_target_cpu}		\
	    --pkglibdir=%{pkgdir}	        \
	    --with-lib32=%{lib32}		\
	    --with-lib64=%{lib64}		\
	    --viewer-paths=%{pkgdir}		\
	    --enable-viewer			\
	    --viewer-paths="%{pkgdir32}:%{pkgdir64}"\
	    --disable-biarch

make
popd

#Build plugin configuration utility
pushd %{plugin_config_name}
./configure --prefix=%{_prefix} --libdir=%{_libdir} CFLAGS="$RPM_OPT_FLAGS"
make
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{plugindir}
mkdir -p $RPM_BUILD_ROOT%{pluginsourcedir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig

make -C %{build_dir} install DESTDIR=$RPM_BUILD_ROOT

ln -s %{pkgdir}/npwrapper.so $RPM_BUILD_ROOT/%{plugindir}/npwrapper.so

# Install plugin-config utility
pushd %{plugin_config_name}
DESTDIR=$RPM_BUILD_ROOT make install
popd

cd $RPM_BUILD_ROOT/usr/bin
mv %{plugin_config_binary} $RPM_BUILD_ROOT/%{pkgdir}
cd -

rm -rf $RPM_BUILD_ROOT/usr/doc/plugin-config

cat %{SOURCE2} > $RPM_BUILD_ROOT%{_bindir}/mozilla-plugin-config
chmod 755 $RPM_BUILD_ROOT%{_bindir}/mozilla-plugin-config

cat %{SOURCE3} | %{__sed} -e "s|EXCLUDE_LIST|%{exclude_list}|g" \
    > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

# set up nsplugin player starting script
cat > $RPM_BUILD_ROOT%{pkgdir}/nspluginplayer << EOF
export MOZ_PLUGIN_PATH=%{pluginsourcedir}
%{pkgdir}/npplayer "\$@"
EOF
chmod 755 $RPM_BUILD_ROOT%{pkgdir}/nspluginplayer

# Install man pages
mkdir -p %buildroot%_man1dir
cp %SOURCE4 %SOURCE5 %buildroot%_man1dir/

%post
/usr/bin/mozilla-plugin-config -i -f > /dev/null 2>&1 || :

%preun
if [ "$1" == "0" ]; then
    /usr/bin/mozilla-plugin-config -r > /dev/null 2>&1 || :
fi;

%files
%doc README COPYING NEWS
%dir %pkgdir
%dir %plugindir
%_man1dir/*.*

%_bindir/nsplugin*
%_bindir/mozilla-plugin-config
%pkgdir/%plugin_config_binary
%pkgdir/*
%plugindir/npwrapper.so
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}


%changelog
* Mon Mar 03 2014 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt2
- Restore nspluginwrapper and nspluginviewer in /usr/bin
- Add man pages from Debian
- Fix path to plugin directory
- Build without xulrunner

* Fri Feb 28 2014 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- Import to Sisyphus from Fedora (ALT #23877, #29244, #29246)
