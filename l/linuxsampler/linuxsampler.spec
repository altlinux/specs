Name: linuxsampler
Version: 2.4.1
Release: alt1

Summary: A modular, streaming capable sampler
License: GPLv2
Group: Sound
Url: https://linuxsampler.org/

Source: %name-%version.tar

BuildRequires: flex gcc-c++ perl(XML/Parser.pm)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(gig)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(sqlite3)

%package -n liblinuxsampler
Summary: A modular, streaming capable sampler
Group: System/Libraries

%package -n lv2-linuxsampler-plugin
Summary: A modular, streaming capable sampler
Group: Sound

%package devel
Summary: A modular, streaming capable sampler
Group: Development/C

%define desc \
LinuxSampler is sampler backend, thus server-like console application. It\
provides a TCP based network interface with a custom ASCII based protocol\
called "LSCP" to control the sampler and manage sampler sessions. You either\
have to send commands manually to LinuxSampler, e.g. by connecting via\
'telnet' or by using 'netcat' or you might want to use a graphical user\
interface (frontend) like QSampler (C++/Qt based) or JSampler (Java based).\
For more information visit http://www.linuxsampler.org/documentation.html

%description %desc

%description -n liblinuxsampler %desc
This package contains linuxsampler shared library.

%description -n lv2-linuxsampler-plugin %desc
This package provides linuxsampler as LV2 plugin.

%description devel %desc
This package contains development part of linuxsampler.

%prep
%setup
sed -ri 's,"/usr/lib/ladspa","%_libdir/ladspa",' \
	src/effects/LadspaEffect.cpp \
	Documentation/lscp.xml

%build
%autoreconf
%configure --disable-static
make parser
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_libdir/linuxsampler/plugins

%files
%doc AUTHORS COPYING NEWS README
%_bindir/linuxsampler
%_bindir/ls_instr_script
%_bindir/lscp
%_libdir/linuxsampler/plugins
%_man1dir/linuxsampler.1*
%_man1dir/lscp.1*

%files -n liblinuxsampler
%_libdir/liblinuxsampler.so.*

%files -n lv2-linuxsampler-plugin
%_libdir/lv2/linuxsampler.lv2

%files devel
%_includedir/linuxsampler
%_libdir/liblinuxsampler.so
%_pkgconfigdir/linuxsampler.pc

%changelog
* Wed Nov 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.1-alt1
- 2.4.1 released

* Fri Jul 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.0-alt1
- 2.4.0 released
