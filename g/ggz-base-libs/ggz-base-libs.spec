
Summary: Base libraries for GGZ gaming zone
Name:    ggz-base-libs
Version: 0.99.5
Release: alt2_10

License: LGPLv2+ and GPLv2+
Group:   System/Libraries
URL: http://www.ggzgamingzone.org/
#Source0: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/ggz-base-libs-snapshot-%{version}.tar.gz
Source0: http://mirrors.ibiblio.org/pub/mirrors/ggzgamingzone/ggz/snapshots/ggz-base-libs-snapshot-%{version}.tar.gz

# upstreamable patches, fix --with-tls=NSS
# https://bugs.ggzgamingzone.org/mantis/view.php?id=114
Patch50: ggz-base-libs-snapshot-0.99.5-tls_nss3.patch

Obsoletes: libggz < 1:0.99.5
Provides:  libggz = 1:%{version}-%{release}

Obsoletes: ggz-client-libs < 1:0.99.5
Provides:  ggz-client-libs = 1:%{version}-%{release}

Source1: ggz.modules
# see http://fedoraproject.org/wiki/PackagingDrafts/GGZ
Source2: macros.ggz

BuildRequires: libexpat-devel
BuildRequires: gettext
BuildRequires: libgcrypt-devel >= 1.4
BuildRequires: libnss-devel
Source44: import.info


%description
GGZ (which is a recursive acronym for GGZ Gaming Zone) develops libraries,
games and game-related applications for client-server online gaming. Player
rankings, game spectators, AI players and a chat bot are part of this effort.

%package devel
Summary: Development files for %{name}
Group: Development/C
Obsoletes: libggz-devel < 1:0.99.5
Obsoletes: ggz-client-libs-devel < 1:0.99.5
Provides: libggz-devel = 1:%{version}-%{release}
Provides: ggz-client-libs-devel = 1:%{version}-%{release}
Requires: %{name} = %{version}-%{release}
# %{_sysconfdir}/rpm ownership
Requires: rpm
%description devel
%{summary}.


%prep
%setup -q -n %{name}-snapshot-%{version}

%patch50 -p1 -b .tls_nss3

%if 0 
# some auto*/libtool love to quash rpaths
rm -f m4/libtool.m4 m4/lt*
#libtoolize -f --automake
#aclocal -Im4
autoreconf -i -f
%else
# avoid lib64 rpaths, quick-n-dirty
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif
%endif


%build
%configure \
  --disable-debug \
  --disable-static \
  --with-gcrypt \
  --with-tls=NSS

make %{?_smp_mflags}


%install

make install DESTDIR=%{buildroot}

# GGZCONFDIR stuff
install -D -m644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/ggz.modules
mkdir -p %{buildroot}%{_sysconfdir}/ggz.modules.d
# GGZDATADIR
mkdir -p %{buildroot}%{_datadir}/ggz
# GGZGAMEDIR
mkdir -p %{buildroot}%{_libdir}/ggz
# RPM macros
install -D -m644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/rpm/macros.ggz

%find_lang ggzcore_snapshot-%{version}
%find_lang ggz-config
cat ggz*.lang >> all.lang

# unpackaged files
rm -f %{buildroot}%{_libdir}/lib*.la


%check
make check ||:


%files -f all.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%verify(not size md5 mtime) %config(noreplace) %{_sysconfdir}/ggz.modules
%dir %{_sysconfdir}/ggz.modules.d
# GPLv2+
%{_bindir}/ggz-config
%dir %{_datadir}/ggz
%dir %{_libdir}/ggz
%{_libdir}/libggzmod.so.4*
%{_mandir}/man5/ggz.modules.5*
# LGPLv2+
%{_libdir}/libggz.so.2*
%{_libdir}/libggzcore.so.9*
%{_mandir}/man6/ggz*
%{_mandir}/man7/ggz*
%{_sysconfdir}/xdg/menus/applications-merged/ggz.merge.menu
%{_sysconfdir}/xdg/menus/ggz.menu
%{_datadir}/desktop-directories/ggz*.directory

%files devel
%{_sysconfdir}/rpm/macros.ggz
# GPLv2+
%{_includedir}/ggzmod.h
%{_libdir}/libggzmod.so
%{_libdir}/pkgconfig/ggzmod.pc
%{_mandir}/man3/ggzmod_h.3*
# LGPLv2+
%{_includedir}/ggz.h
%{_includedir}/ggz_*.h
%{_libdir}/libggz.so
%{_libdir}/pkgconfig/libggz.pc
%{_mandir}/man3/ggz*
%{_includedir}/ggzcore.h
%{_libdir}/libggzcore.so
%{_libdir}/pkgconfig/ggzcore.pc
%{_mandir}/man3/ggzcore_h.3*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.99.5-alt2_10
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.99.5-alt1_10
- update to new release by fcimport

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.99.5-alt1_8
- initial release by fcimport

