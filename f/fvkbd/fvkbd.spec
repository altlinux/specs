# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize pkgconfig(glib-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(libfakekey)
# END SourceDeps(oneline)
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name fvkbd
%define version 0.2.2
# Tarfile created using git
# git clone git://gitorious.org/fvkbd/fvkbd.git
# git archive --format=tar --prefix=fvkbd-%{version}/ %{git_version} | bzip2 > %{name}-%{version}.tar.bz2
%define git_version 348b3a9
%define tarfile %{name}-%{version}.tar.bz2

Name:          fvkbd
Version:       0.2.2
Release:       alt3_6
Summary:       Free Virtual Keyboard

Group:         System/Libraries
License:       LGPLv2
URL:           http://gitorious.org/fvkbd/pages/Home
# vc           http://gitorious.org/fvkbd/fvkbd/commits/master
Source0:       %{tarfile}
Patch0:        fvkbd-fixdesktop.patch
Patch1:        fvkbd-remove-unused.patch

BuildRequires: libclutter-devel
BuildRequires: gtk2-devel
BuildRequires: libfakekey-devel
BuildRequires: libxml2-devel
BuildRequires: libXtst-devel
BuildRequires: libunique-devel
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: gettext

# Require these because the git tarball doesn't have the configure built
BuildRequires: libtool
Source44: import.info

%description
A free virtual keyboard for use in Moblin Internet Devices from Phones to MIDs.

%package devel
Summary: Development package for %{name}
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
Files for development with %%{name}.

%prep
%setup -q
%patch0 -p1 -b .fixdesktop
%patch1 -p1 -b .remove_unused

# run autogen.sh until we have a proper release, but don't run configure twice.
sed -i '/configure/d' autogen.sh
./autogen.sh

%build
%configure --disable-static --enable-gtkdoc
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

desktop-file-validate %{buildroot}/%{_datadir}/applications/fvkbd-gtk.desktop

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Accessibility \
	%buildroot%_desktopdir/fvkbd-gtk.desktop

%files -f %{name}.lang
%doc COPYING AUTHORS
%{_bindir}/fvkbd-gtk
%{_libdir}/libfvkbd-0.2.so.*
%{_libdir}/libfvkbd-gtk-0.2.so.*
%{_datadir}/applications/fvkbd-gtk.desktop
%{_datadir}/pixmaps/fvkbd-gtk.png
%{_datadir}/fvkbd/

%files devel
%{_libdir}/libfvkbd-0.2.so
%{_libdir}/libfvkbd-gtk-0.2.so

%changelog
* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt3_6
- applied repocop patches

* Fri Dec 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt2_6
- restored in Sisyphus as fc import

* Tue Apr 12 2011 Egor Glukhov <kaman@altlinux.org> 0.2.2-alt1.git.e972f975
- Initial build for Sisyphus
