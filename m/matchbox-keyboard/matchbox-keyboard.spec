# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libpng-devel
# END SourceDeps(oneline)
Name:           matchbox-keyboard
Version:        0.1
Release:        alt1_10
Summary:        On screen virtual keyboard
Group:          Accessibility
License:        GPLv2+
URL:            http://matchbox-project.org/
Source0:        %{name}-%{version}.tar.gz
Patch0:         matchbox-keyboard-0.1-fix-desktop.patch
Patch1:		matchbox-keyboard-0.1-libpng1.5.patch
Patch2:		matchbox-keyboard-0.1-link.patch
Patch3:		matchbox-keyboard-0.1-automake-1.13.patch
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libfakekey)
BuildRequires: pkgconfig(xft)
BuildRequires:  libXft-devel
BuildRequires:  libXrender-devel
BuildRequires:  libexpat-devel
BuildRequires:  desktop-file-utils
Source44: import.info

%description
Matchbox-keyboard is an on screen 'virtual' or 'software'
keyboard. It will hopefully work well on various touchscreen
devices from mobile phones to tablet PCs running X Windows.

It aims to 'just work' supporting localised, easy to write
XML layout configuration files.

%prep
%setup -q
%patch0 -p1 -b .fix-category
%patch1 -p0 -b .libpng
%patch2 -p0 -b .link
%patch3 -p1 -b .am
# for newer libtool
autoreconf -fi

%build
%configure --enable-gtk-im
%make

%install
%makeinstall_std

find %{buildroot} -name '*.la' | xargs rm

%files
%doc AUTHORS COPYING README
%{_bindir}/matchbox-keyboard
%{_datadir}/matchbox-keyboard
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_libdir}/gtk-2.0/2.10.0/immodules/libmb-im-invoker.so


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_10
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_9
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_8
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_7
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_6
- update by mgaimport

* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_3
- mageia import

