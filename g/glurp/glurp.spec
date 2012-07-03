Name: glurp
Version: 0.12.3
Release: alt1

Summary: A GTK2-based graphical client for MPD with simple and clean interface.
License: GPL
Group: Sound

# git://git.musicpd.org/master/glurp.git
Url: https://sourceforge.net/projects/glurp/
Source: http://citkit.dl.sourceforge.net/sourceforge/%name/%name-%version.tar.gz

Summary(ru_RU.UTF8): Графический (Gtk2) клиент для Music Player Daemon с простым и понятным внешним видом.

BuildRequires: libmpd-devel >= 0.0.9.8
BuildRequires: libgtk+2-devel >= 2.4
BuildRequires: glib2-devel >= 2.4
#BuildRequires: libglade2-devel >= 2.3.6

%description
Glurp is a GTK+-2.x based graphical client for MPD media player

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%doc AUTHORS

%changelog
* Wed Feb 23 2011 Michael Shigorin <mike@altlinux.org> 0.12.3-alt1
- 0.12.3 (closes: #25137)
- minor spec cleanup

* Thu Oct 20 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.11.6-alt1
- Initial Sisyphus package.

