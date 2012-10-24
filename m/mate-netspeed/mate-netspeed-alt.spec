# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libgtop-2.0)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-netspeed   
Version:        1.4.0
Release:        alt1_1.1
Summary:        MATE applet that shows traffic on a network device

Group:          Networking/Other
License:        GPLv2+
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:  gettext scrollkeeper intltool
BuildRequires:  libgtop2-devel
BuildRequires:  mate-panel-devel >= 1.1.0
BuildRequires:  mate-doc-utils
BuildRequires:  wireless-tools-devel
BuildRequires:  mate-common

Requires:       icon-theme-hicolor

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

Obsoletes: 		mate-netspeed-applet
Provides:  		mate-netspeed


# related to GNOME bz 600579 / Fedora #530920
Patch1: netspeed_applet-0.16-copy-qualpixbufs.patch
# related to GNOME bz 574462 / Fedora #647060
Patch3: netspeed_applet-0.16-details-bytes.patch

%description
netspeed is a little MATE applet that shows the traffic on a
specified network device (for example eth0) in kbytes/s.

%prep
%setup -q -n mate-netspeed-%{version}
%patch1 -p1 -b .copy-qualpixbufs
%patch3 -p1 -b .details-bytes
NOCONFIGURE=1 ./autogen.sh

%build
export 	LDFLAGS="-lm"
%configure \
	--disable-static \
	--disable-scrollkeeper



make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README TODO
# ChangeLog discontinued
%doc %{_datadir}/mate/help/mate_netspeed_applet/*
%{_libexecdir}/*
# wildcard _libexecdir/*
%exclude %_prefix/lib/debug
%{_libdir}/matecomponent/servers/*
%_iconsdir/hicolor/*/*/*
%{_datadir}/omf/mate_netspeed_applet/*


%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

