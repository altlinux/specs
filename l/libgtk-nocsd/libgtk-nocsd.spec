# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 0

Name: libgtk-nocsd
Version: 4.1
Release: alt1

Summary: An LD_PRELOAD library to disable CSD in GTK3/4

License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://codeberg.org/MorsMortium/GTK-NoCSD
VCS: https://codeberg.org/MorsMortium/GTK-NoCSD

Source: %name-%version.tar
Patch:  %name-%version-%release.patch

BuildRequires: libadwaita-devel

Requires: %name%sover = %EVR

%description
An LD_PRELOAD library to disable CSD in GTK3/4, LibHandy, and LibAdwaita apps.

%package -n %name%sover
Summary: An LD_PRELOAD library to disable CSD in GTK3/4
Group: Graphical desktop/Other

%description -n %name%sover
An LD_PRELOAD library to disable CSD in GTK3/4, LibHandy, and LibAdwaita apps.

%prep
%setup
%autopatch -p1

%build
%make_build CFLAGS_ADD="%optflags"	

%install
%makeinstall_std LIBDIR=%_libdir \
                 PREFIX=%prefix \
                 NODOC=1 \
                 NOOPT=1

rm -r %buildroot%prefix/share/licenses

sed -i 's|/usr/lib/|%_libdir/|' Source/gtk-nocsd.{,c}sh

install -pDm 755 Source/gtk-nocsd.sh \
	%buildroot%_sysconfdir/profile.d/gtk-nocsd.sh

install -pDm 755 Source/gtk-nocsd.csh \
	%buildroot%_sysconfdir/profile.d/gtk-nocsd.csh

%files
%doc *.md LICENSE
%_libdir/libgtk-nocsd.so
%_sysconfdir/profile.d/gtk-nocsd.csh
%_sysconfdir/profile.d/gtk-nocsd.sh

%files -n %name%sover
%_libdir/libgtk-nocsd.so.%sover

%changelog
* Wed Jun 17 2026 Anton Midyukov <antohami@altlinux.org> 4.1-alt1
- Initial build.
