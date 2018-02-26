Name:       ibus-xkbc
Version:    1.3.3
Release:    alt1
Summary:    The XKBC engine for IBus input platform
License:    GPLv2
Group:      System/X11 
URL:        http://github.com/sun-im/ibus-xkbc/
Source0:    http://cloud.github.com/download/sun-im/ibus-xkbc/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  python-devel
BuildRequires:  pkgconfig
BuildRequires:  glib2-devel


%description
The XKBC engine for IBus platform. 
It provides keyboard layout emulation input method.

%prep
%setup -q

%build
sh autogen.sh
%configure --disable-static
# make -C po update-gmo
make 

%install
make DESTDIR=%buildroot install

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/ibus-xkbc
%{_datadir}/ibus/component/*
%{_datadir}/gnome/help/ibus-xkbc
%{_datadir}/omf/ibus-xkbc/

%changelog
* Tue Dec 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.3-alt1
- first build for sisyphus

* Wed Feb 04 2010 Peng Wu <pwu@redhat.com> - 1.2.0.20100115-3
- Correct home page url.

* Wed Feb 04 2010 Peng Wu <pwu@redhat.com> - 1.2.0.20100115-2
- Fixes koji build for F-13.

* Fri Oct 30 2009 Naoyuki Ishimura <naoyuki.ishimura@sun.com> - 0.1.0-1
- The first version.
