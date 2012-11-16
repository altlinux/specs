# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize
# END SourceDeps(oneline)
Group: Graphics
%define _libexecdir %_prefix/libexec
Name:		mate-backgrounds
Version:	1.5.0
Release:	alt1_2
Summary:	MATE Desktop backgrounds
License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildArch:	noarch
BuildRequires:	mate-common
Source44: import.info

%description
Backgrounds for MATE Desktop

%prep
%setup -q
# move to @datadir@/backgrounds as our gnome did.
# just in case, ask aris@ why.
sed -i -e s,/pixmaps/backgrounds/,/backgrounds/,g `grep -rl /pixmaps/backgrounds/ .`
NOCONFIGURE=1 ./autogen.sh


%build
%configure
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/mate-background-properties/
%{_datadir}/backgrounds/mate/

%changelog
* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- adapted alt patches

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

