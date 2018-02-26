# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gtkdocize gcc-c++ imlib2-devel libGL-devel libXext-devel libaccounts-glib-devel libfreetype-devel pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define version 0.3.0
%define name libcaptury
%define captury_version 0.3.0

# Tarfile created using git
# git clone git://gitorious.org/libcaptury/mainline.git libcaptury
# cd libcaptury
# git-archive --format=tar --prefix=libcaptury-%{captury_version}/ %{git_version} | bzip2 > libcaptury-%{captury_version}-%{gitdate}.tar.bz2

%define gitdate 20080323
%define git_version cca4e3c

%define tarfile %{name}-%{captury_version}-%{gitdate}.tar.bz2
%define snapshot %{gitdate}git%{git_version}

Summary:        A library for X11/OpenGL video capturing framework
Name:           libcaptury
Version:        %{captury_version}
Release:        alt2_0.6.20080323gitcca4e3c
License:        GPLv2+
Group:          System/Libraries
URL:            http://gitorious.org/projects/libcaptury/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libcapseo-devel
BuildRequires:  libX11-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libogg-devel

# Fedora specific snapshot no upstream release (yet)
Source0:	%{tarfile}
Source44: import.info

%description
Captury is a realtime multimedia capturing framework for currently
OpenGL video (to be extended to XShm and audio/alsa soon). 
Its uses are e.g. for capturing video from external OpenGL applications
(via captury itself) and is currently also used by KDE's kwin
to record your desktop efficiently (VideoRecord plugin).

Captury supports full encoding as well as incremential(!) encoding
by only regions from the screen that have actually changed.
Window managers (like kwin) do know of such areas and can make use of it.

%package devel
Summary: Developer and header files for captury
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
Developer and header files for the captury movie capturing
framework.

%prep
%setup -q -n %{name}-%{version}
./autogen.sh

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}/%{_libdir}/*.la

%files
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%dir %{_includedir}/captury
%{_includedir}/captury/*.h
%{_libdir}/libcaptury.so
%{_libdir}/pkgconfig/libcaptury.pc

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_0.6.20080323gitcca4e3c
- update to new release by fcimport

* Sun Dec 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_0.5.20080323gitcca4e3c
- fixed build after mass spec cleanup

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_0.5.20080323gitcca4e3c
- initial import by fcimport

