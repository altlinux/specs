# BEGIN SourceDeps(oneline):
# Automatically added by buildreq on Sun Dec 11 2016
# optimized out: cmake-modules fontconfig glib2-devel libaudiofile-devel libogg-devel libstdc++-devel libtqt3-devel pkg-config python-base python-modules tqt3 tqt3-dev-tools
BuildRequires: cmake gcc-c++ libalsa-devel libesd-devel libjack-devel libmad-devel libtqt4-devel libvorbis-devel perl(DB_File.pm) perl(Fcntl.pm) perl(Shell.pm) pkgconfig(audiofile) pkgconfig(glib-2.0) pkgconfig(gthread-2.0)
# END SourceDeps(oneline)
BuildRequires(pre):	rpm-macros-suse-compat
BuildRequires(pre):	rpm-macros-cmake
BuildRequires(pre): rpm-macros-trinity
#
# spec file for package arts (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.0.4
%endif
%define tde_pkg arts
%define tde_sbindir %{tde_prefix}/sbin
%define tde_tdeappdir %{tde_datadir}/applications/tde


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.5.10
Release:	alt1_14.0.4_1
Summary:	ARTS (analog realtime synthesizer) - the TDE sound system
Group:		System/Servers
URL:		http://www.trinitydesktop.org/

License:	GPL-2.0+

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar

# BuildRequires:	libtqt4-devel >= %{tde_epoch}:4.2.0
# BuildRequires:	trinity-filesystem >= %{tde_version}
# Requires:		trinity-filesystem >= %{tde_version}

# BuildRequires:	cmake >= 2.8
# BuildRequires:	gcc-c++
# BuildRequires:	pkgconfig

# BuildRequires:	audiofile-devel
# BuildRequires:	alsa-lib-devel
# BuildRequires:	glib2-devel
# BuildRequires:	gsl-devel
# BuildRequires:	libvorbis-devel

# ESOUND support
%define with_esound 1
# BuildRequires:	esound-devel

# JACK support
%define with_jack 1
%define jack_devel libjack-devel
# BuildRequires:	%{jack_devel}

# LIBTOOL
# BuildRequires:	libltdl-devel

# MAD support
%ifarch %{ix86} x86_64
%define with_libmad 1
%define mad_devel libmad-devel
# BuildRequires:		%{mad_devel}
%endif

# Pulseaudio config file
%define with_pulseaudio 1

# Requires:		libtqt4 >= %{tde_epoch}:4.2.0
# Requires:		audiofile

%if "%{?tde_prefix}" == "/usr"
Obsoletes:	arts
%endif
Source44: import.info

%description
arts (analog real-time synthesizer) is the sound system of TDE.

The principle of arts is to create/process sound using small modules which do
certain tasks. These may be create a waveform (oscillators), play samples,
filter data, add signals, perform effects like delay/flanger/chorus, or
output the data to the soundcard.

By connecting all those small modules together, you can perform complex
tasks like simulating a mixer, generating an instrument or things like
playing a wave file with some effects.

%files
%doc COPYING.LIB
%{tde_libdir}/lib*.so.*
%{tde_bindir}/artscat
%{tde_bindir}/artsd
%{tde_bindir}/artsdsp
%{tde_bindir}/artsplay
%{tde_bindir}/artsrec
%{tde_bindir}/artsshell
%{tde_bindir}/artswrapper
%{tde_bindir}/artsc-config
%{tde_bindir}/mcopidl

%dir %{tde_libdir}/mcop
%dir %{tde_libdir}/mcop/Arts
%dir %{tde_libdir}/mcop/Arts/Environment
%{tde_libdir}/mcop/Arts/*
%{tde_libdir}/mcop/*.mcopclass
%{tde_libdir}/mcop/*.mcoptype

# The '.la' files are needed for runtime, not devel !
#%%{tde_libdir}/lib*.la

##########

%package devel
Group:		Development/Other
Summary:	ARTS (analog realtime synthesizer) - the TDE sound system (Development files)
# Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%package devel-static
Group:		Development/Other
Summary:	ARTS (analog realtime synthesizer) - the TDE sound system (Development files)
# Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}


# Requires:	alsa-lib-devel
# Requires:	audiofile-devel
# Requires:	libvorbis-devel
# Requires:	esound-devel
%{?with_libmad:Requires: %{mad_devel}}
%{?with_jack:Requires: %{jack_devel}}

%description devel
arts (analog real-time synthesizer) is the sound system of TDE.

The principle of arts is to create/process sound using small modules which do
certain tasks. These may be create a waveform (oscillators), play samples,
filter data, add signals, perform effects like delay/flanger/chorus, or
output the data to the soundcard.

By connecting all those small modules together, you can perform complex
tasks like simulating a mixer, generating an instrument or things like
playing a wave file with some effects.


%description devel-static
arts (analog real-time synthesizer) is the sound system of TDE.

The principle of arts is to create/process sound using small modules which do
certain tasks. These may be create a waveform (oscillators), play samples,
filter data, add signals, perform effects like delay/flanger/chorus, or
output the data to the soundcard.

By connecting all those small modules together, you can perform complex
tasks like simulating a mixer, generating an instrument or things like
playing a wave file with some effects.


%files devel
# Arts includes are under 'tde' - this is on purpose !
%{tde_tdeincludedir}/arts/
# Artsc includes are not under 'tde'.
%{tde_includedir}/artsc/
%{tde_libdir}/lib*.so
%{tde_libdir}/pkgconfig/*.pc
%exclude %tde_includedir/include/*

%files devel-static
%{tde_libdir}/*.a
%{tde_libdir}/*.la


##########

%if 0%{?with_pulseaudio}

%package config-pulseaudio
Group:		System/Servers
Summary:	ARTS - Default configuration file for Pulseaudio
# Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description config-pulseaudio
This package contains a default ARTS configuration file, that is 
intended for systems running the Pulseaudio server.

%files config-pulseaudio
%{tde_confdir}/kcmartsrc

%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"


%{suse_cmake} \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_includedir}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}/arts" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  \
  -DWITH_ALSA=ON \
  -DWITH_AUDIOFILE=ON \
  -DWITH_VORBIS=ON \
  %{?with_libmad:-DWITH_MAD=ON} %{!?with_libmad:-DWITH_MAD=OFF} \
  %{?with_esound:-DWITH_ESOUND=ON} \
  %{?with_jack:-DWITH_JACK=ON} \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__make install -C build DESTDIR=%{?buildroot}

%__install -d -m 755 %{?buildroot}%{tde_datadir}/config
%__install -d -m 755 %{?buildroot}%{tde_datadir}/doc

%__install -d -m 755 %{?buildroot}%{tde_includedir}/artsc
%__install -D -m 644 %{?buildroot}%{tde_includedir}/include/artsc/*.h  %{?buildroot}%{tde_includedir}/artsc/


# Installs the Pulseaudio configuration file
%if 0%{?with_pulseaudio}
%__mkdir_p "%{?buildroot}%{tde_confdir}"
cat <<EOF >"%{?buildroot}%{tde_confdir}/kcmartsrc"
[Arts]
Arguments=\s-F 10 -S 4096 -a esd -n -s 1 -m artsmessage -c drkonqi -l 3 -f
NetworkTransparent=true
SuspendTime=1
EOF
chmod 644 "%{?buildroot}%{tde_confdir}/kcmartsrc"
%endif

# Add supplementary folders
%__install -d -m 755 "%{?buildroot}%{tde_libdir}/mcop/Arts/Environment"


%changelog
* Sun Dec 11 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:1.5.10-alt1_14.0.4_1
- converted for ALT Linux by srpmconvert tools
