Name: thewidgetfactory
Summary: Test tool for GTK2 theme
Summary(ru_RU.UTF8): Утилита для тестирования созданной темы GTK2
Version: 0.2.1
Release: alt3
License: GPL
Group: Development/Other

Packager: Denis Koryavov <dkoryavov@altlinux.org>

Source0: %name-%version.tar.bz2
Source1: %name.16x16.png
Source2: %name.32x32.png
Source3: %name.48x48.png

# (from fedora)  add more widgets
Patch0: %name-newwidgets.patch
#patch the two makefile.in to avoid warnings of autoconf
Patch1: %name-fix-makefile-datadir.patch
Url: http://www.stellingwerff.com/?page_id=10

# Automatically added by buildreq on Fri May 29 2009
BuildRequires: gcc-c++ gcc-fortran libgtk+2-devel

%description
TheWidgetFactory is a showcase of GTK2 widgets, only useful to theme developers.

%description -l ru_RU.UTF8
TheWidgetFactory - фабрика элементов графического интерфейса ("виджетов") позволяющая
увидеть все виджеты в одном окне. Утилита будет очень полезна, если вы собираетесь
создать собственную тему GTK2.

%prep
%setup -q
%patch0 -p1 -b .newwidgets
%patch1 -p1 -b .fixmakefile

%build
# %undefine __libtoolize
libtoolize --force --copy
%configure
%make

%install
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%_datadir/applications
cat > $RPM_BUILD_ROOT%_datadir/applications/%name.desktop << EOF

[Desktop Entry]
Name=The Widget Factory
Name[ru]=Фабрика виджетов GTK2
Comment=A tool for previewing GTK widgets
Comment[ru] = Утилита для просмотра элементов графического интерфейса тем GTK2
Exec=%_bindir/twf
Icon=%name
Terminal=false
Type=Application
Categories=Development;GUIDesigner;
EOF

mkdir -p $RPM_BUILD_ROOT{%_liconsdir,%_niconsdir,%_miconsdir}
install -m 644 %SOURCE1 $RPM_BUILD_ROOT%_miconsdir/%name.png
install -m 644 %SOURCE2 $RPM_BUILD_ROOT%_niconsdir/%name.png
install -m 644 %SOURCE3 $RPM_BUILD_ROOT%_liconsdir/%name.png

%files
%doc ChangeLog README COPYING
%_bindir/twf
%_datadir/applications/%name.desktop
%_liconsdir/%name.png
%_miconsdir/%name.png
%_niconsdir/%name.png

%changelog
* Fri Nov 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.2.1-alt3
- Repocop warnings is taken into account.

* Fri May 29 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.2.1-alt2
- Build for Sisyphus


