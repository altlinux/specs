Group: Graphical desktop/Other
%define _libexecdir %_prefix/libexec
Name:           mate-icon-theme
Version:        1.6.0
Release:        alt1_1
Summary:        Icon theme for MATE Desktop
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  mate-common
BuildRequires:  icon-naming-utils

Provides: mate-icon-theme = %{version}-%{release}
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
%configure  --enable-icon-mapping

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS COPYING README
%{_datadir}/icons/mate
%{_datadir}/icons/menta

%files devel
%{_datadir}/pkgconfig/mate-icon-theme.pc


%changelog
* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

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

