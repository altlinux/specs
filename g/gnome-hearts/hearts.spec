Name: gnome-hearts
Version: 0.3
Release: alt3
Summary: Hearts for GNOME
License: GPL
Group: Games/Cards
Url: http://www.gnome-hearts.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: glib2-devel intltool libgnomeui-devel libgtk+2-devel
BuildPreReq: libglade-devel python-devel librarian

%py_provides player_api

%description
Gnome Hearts project, an implementation of the classic hearts card game
for the GNOME desktop, featuring configurable rulesets and editable
computer opponents to satisfy widely diverging playing styles.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-scrollkeeper

for i in $(egrep -R 'python.*\.a' ./ |awk -F : '{print $1}')
do
	sed -i 's|/usr.*libpython.*\.a|-lpython%_python_version|g' $i
done

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

install -d %buildroot%_liconsdir
ln -s %_pixmapsdir/%name.png %buildroot%_liconsdir/

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name
%_man6dir/*
%_pixmapsdir/*
%_liconsdir/*

%changelog
* Tue Jan 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Rebuilt with librarian

* Tue Jan 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Built without scrollkeeper

* Sun Jan 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

