Group: Graphical desktop/Other
%define _libexecdir %_prefix/libexec
Name:           mate-icon-theme
Version:        1.5.0
Release:        alt1_1
Summary:        Icon theme for MATE Desktop
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mate-common
BuildRequires:  icon-naming-utils

Provides: mate-icon-theme = %{version}-%{release}
Obsoletes: mate-icon-theme-legacy < %{version}-%{release}
Source44: import.info

%description
Icon theme for MATE Desktop

%package devel
Group: Graphical desktop/Other
Summary: Development files for mate-icon-theme

%description devel
Development files for mate-icon-theme

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure  --enable-icon-mapping \
            --disable-static
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

%post
/bin/touch --no-create %{_datadir}/icons/mate &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/mate &>/dev/null
fi

%files
%doc AUTHORS COPYING README
%{_datadir}/icons/mate/

%files devel
%{_datadir}/pkgconfig/mate-icon-theme.pc


%changelog
* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

