Serial: 1
# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gtk+-2.0) automake
# END SourceDeps(oneline)
%define oldname gtk-smooth-engine
Summary: 	The Smooth engine for GTK+-2.0
Name: 		libgtk-engine-smooth
Version: 	2.14.3
Release: 	alt2_2
License:	LGPLv2+ and GPLv2+
URL: 		http://ftp.de.debian.org/debian/pool/main/g/gtk-smooth-engine
Source0: 	http://ftp.de.debian.org/debian/pool/main/g/gtk-smooth-engine/%{oldname}_%{version}+deb5.tar.gz
Group: 		Graphical desktop/Other

Patch0:     gtk-smooth-engine_automake.patch

Requires:	gtk2

BuildRequires: 	gtk2-devel >= 2.4.0
BuildRequires:	pango-devel >= 1.6.0
BuildRequires: 	glib2-devel >= 2.4.0
BuildRequires: 	libtool
BuildRequires: 	autoconf
Source44: import.info

%description
The Smooth engine for GTK+-2.0

%prep
%setup -q -n %{oldname}-%{version}+deb5
%patch0 -p1 -b .automake
NOCONFIGURE=1 ./autogen.sh


%build
%configure --disable-static
make %{?_smp_mflags}

%install
%{makeinstall_std}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libdir}/gtk-2.0/2.10.0/engines/libsmooth.so
%{_datadir}/gtk-engines/smooth.xml


%changelog
* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.14.3-alt2_2
- bumped serial to match 4.1 branch

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.14.3-alt1_2
- fc import

