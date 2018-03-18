# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global __requires_exclude libkarma

%define major		0
%define libname		libkarma%{major}
%define develname	libkarma-devel

Summary:	Rio Karma tools
Name:		libkarma
Version:	0.1.2
Release:	alt1_9
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.freakysoft.de/html/libkarma/
Source0:	http://www.freakysoft.de/libkarma/libkarma-%{version}.tar.gz
Source2:	http://bobcopeland.com/karma/banshee/preferences.fdi
Source3:	http://bobcopeland.com/karma/banshee/multimedia-player-rio-karma.png
Source4:	karma-sharp.dll.config
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(zlib)
Requires:	%libname >= %version
Source44: import.info

%description
Rio Karma access library.

%package -n	%libname
Summary:	Rio Karma access library
Group:		System/Libraries

%description -n	%libname
Rio Karma access library.

%package -n	%develname
Summary:	Rio Karma development files
Group:		Development/C
Requires:	%libname = %version
Provides:	%name-devel = %version-%release
Obsoletes:	%name-devel < %version-%release
Obsoletes:	%{_lib}karma0-devel < %version-%release

%description -n	%develname
Rio Karma development files.


%package -n	karma-sharp
Summary:	Rio Karma C# bindings
Group:		Development/Other
Requires:	%name = %version

%description -n	karma-sharp
Rio Karma C# bindings.


%prep
%setup -q -n libkarma-%{version}
sed -i 's!gmcs!mcs!' karma-sharp/Makefile

%build

make PREFIX=$RPM_BUILD_ROOT/%_prefix

%install
mkdir -p $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/%_prefix CHOWNPROG=/bin/true CHGRPPROG=/bin/true
perl -pi -e "s^%buildroot^^" %buildroot%_prefix/lib/pkgconfig/karma-sharp.pc
%if %_lib != lib
mv %buildroot%_prefix/lib %buildroot%_libdir
perl -pi -e "s^/lib^/%_lib^" %buildroot%_libdir/pkgconfig/karma-sharp.pc
%endif


install -m 644 -D libkarma.fdi %buildroot%_sysconfdir/hal/fdi/information/20-rio-karma.fdi
install -m 644 -D %SOURCE2 %buildroot%_sysconfdir/hal/fdi/policy/preferences.fdi
install -m 644 -D %SOURCE3 %buildroot%_datadir/icons/hicolor/32x32/devices/multimedia-player-rio-karma.png

cat > README.urpmi << EOF
For automatic mounting, add the following line to your
/etc/fstab. Otherwise gnome-volume-manager will refuse to mount the
device, as it doesn't know about the Karma's proprietary filesystem.

/dev/disk/by-id/usb-Rio_Rio_Karma_0000000000000000-part2    /media/karma    omfs    user,noauto    0   0

EOF

install -m 644 %SOURCE4 %buildroot%_libdir/karma-sharp/karma-sharp.dll.config

%files
%doc THANKS TODO README.urpmi ChangeLog
%config(noreplace) %_sysconfdir/hal/fdi/information/20-rio-karma.fdi
%config(noreplace) %_sysconfdir/hal/fdi/policy/preferences.fdi
%_bindir/riocp
%_bindir/chprop
%_mandir/man1/*.1*
%attr(4711,root,root) %_bindir/karma_helper
%_datadir/icons/hicolor/32x32/devices/multimedia-player-rio-karma.png

%files -n %libname
%_libdir/libkarma.so.%{major}*

%files -n %develname
%_includedir/*
%_libdir/libkarma.a
%_libdir/libkarma.so

%files -n karma-sharp
%_libdir/karma-sharp/*
%_libdir/pkgconfig/karma-sharp.pc


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_9
- new version

