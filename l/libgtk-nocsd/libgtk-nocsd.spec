# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define sover 0

Name: libgtk-nocsd
Version: 4.1
Release: alt2

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

%files
%doc *.md LICENSE Source/gtk-nocsd.csh Source/gtk-nocsd.sh
%_libdir/libgtk-nocsd.so

%files -n %name%sover
%_libdir/libgtk-nocsd.so.%sover

%changelog
* Thu Jun 18 2026 Anton Midyukov <antohami@altlinux.org> 4.1-alt2
- Don't pack /etc/profile.d. Copy yourself from doc or use for each application
  independently.

* Wed Jun 17 2026 Anton Midyukov <antohami@altlinux.org> 4.1-alt1
- Initial build.
