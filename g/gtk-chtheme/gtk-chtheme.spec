Name:     gtk-chtheme
Version:  0.3.1
Release:  alt1

Summary:  Gtk+ 2.0 Change Theme
License:  GPL
Group:    Graphical desktop/GNOME

Url:      http://plasmasturm.org/programs/gtk-chtheme/
Packager: Evgeny V Shishkov <shev@altlinux.org>

Source0:  %name-%version.tar.bz2
Source1:  %name.desktop
Patch1:   Makefile.20100422.patch

Summary(ru_RU.UTF8): Изменение темы Gtk+ 2.0 на лету

# Automatically added by buildreq on Thu Apr 22 2010
BuildRequires: libgtk+2-devel

%description
As the name suggests, this little program lets you change your Gtk+ 2.0 theme.
The aim is to make theme preview and selection as slick as possible. Themes
installed on the system are presented for selection and previewed on the fly.
A large variety of widgets provides a comprehensive demonstration.

%description -l ru_RU.UTF8
Как следует из названия, эта маленькая программа позволяет изменять темы Gtk+ 2.0.
Цель в том, чтобы сделать предварительный просмор возможностей темы. Темы,
установленные в системе, представлены для выбора и просмотра "на лету".
Большое разнообразие виджетов обеспечивает всестороннюю демонстрацию.

%prep
%setup
%patch1 -p1

%build
%make

%install
%make_install DESTDIR="%buildroot/" install
%__install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_man1dir/*
%_desktopdir/*
%doc COPYING ChangeLog

%changelog
* Thu Apr 22 2010 Evgeny V. Shishkov <shev@altlinux.org> 0.3.1-alt1
- initial build for ALT Linux
