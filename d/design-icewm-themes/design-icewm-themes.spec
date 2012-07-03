Name: design-icewm-themes
Version: 1.0
Release: alt3
Summary: Themes collection for IceWM
Summary(ru_RU.KOI8-R): Коллекция тем для IceWM
Group: Graphical desktop/Icewm
License: GPL
Source0: icewm-themes.tar.bz2
Requires:icewm-light
BuildArch: noarch
%description
Themes collection for IceWM

%description -l ru_RU.KOI8-R
Коллекция тем для IceWM

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%_x11datadir/X11/icewm/
tar xvfj %SOURCE0 -C $RPM_BUILD_ROOT%_x11datadir/X11/icewm/

find $RPM_BUILD_ROOT%_x11datadir/X11/icewm/themes -type f -print0 | 
	xargs -r0 chmod 0444
find $RPM_BUILD_ROOT%_x11datadir/X11/icewm/themes -type d -print0 | 
	xargs -r0 chmod 0755

# remove .xvpics
find $RPM_BUILD_ROOT%_x11datadir/X11/icewm/themes -type d -name .xvpics -print0 |
	xargs -r0 rm -rf
# remove *.bak
find $RPM_BUILD_ROOT%_x11datadir/X11/icewm/themes -type f -name '*.bak' -print0 |
	xargs -r0 rm -rf
(cd $RPM_BUILD_ROOT%_x11datadir ; find X11/icewm/themes ! -type d -printf "%_x11datadir/%%p\n") > other.list
(cd $RPM_BUILD_ROOT%_x11datadir ; find X11/icewm/themes   -type d -printf "%%%%dir %_x11datadir/%%p\n") >> other.list


%files -f other.list 

%changelog
* Sat Jun 10 2006 Damir Shayhutdinov <damir@altlinux.ru> 1.0-alt3
- Files relocated from %_x11libdir to %_x11datadir

* Mon Oct 21 2002 Rider <rider@altlinux.ru> 1.0-alt2
- fix permissons

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 1.0-alt1
- first build
