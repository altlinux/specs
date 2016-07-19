%define name wxGlade

Name: wxGlade
Summary: A GUI builder for wxWindows/wxPython
Version: 0.7.2
Release: alt1
License: MIT
Group: Development/Other
Url: http://wxglade.sourceforge.net/
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: http://heanet.dl.sourceforge.net/project/wxglade/wxglade/%version/%name-%version.tar.gz
Requires: python-base >= 2.3
Requires: python-module-wx >= 2.6
BuildRequires: ImageMagick-tools
BuildRequires: python-dev python-devel-static
BuildRequires: python-module-setuptools
BuildRequires: rpm-build-python
BuildArch: noarch

%description
wxGlade is a GUI designer written in Python with the popular GUI toolkit
wxPython, that helps you create wxWindows/wxPython user interfaces. At the
moment it can generate Python, C++ and XRC (wxWindows' XML resources) code.

As you can guess by the name, its model is Glade, the famous GTK+/GNOME
GUI builder, with which wxGlade shares the philosophy and the look & feel
(but not a line of code).

It is not (and will never be) a full featured IDE, but simply a "designer":
the generated code does nothing apart from displaying the created widgets.
If you are looking for a complete IDE, maybe Boa Constructor or PythonCard
is the right tool.

%prep
%setup
chmod a-x CREDITS.txt
chmod a-x LICENSE.txt
chmod a-x docs/src/manual.xml

%build
%python_build

%install
%__python setup.py install --prefix=%prefix -O1 --skip-build --root=%buildroot
# icons
mkdir -p %buildroot{%_iconsdir,%_miconsdir,%_liconsdir}
convert -resize 32x32 icons/icon.xpm %buildroot%_iconsdir/%name.png
convert -resize 16x16 icons/icon.xpm %buildroot%_miconsdir/%name.png
convert -resize 48x48 icons/icon.xpm %buildroot%_liconsdir/%name.png

# menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=%name
Comment=A GUI builder for wxWindows/wxPython
Exec=wxglade
Icon=%name
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-Tools;GUIDesigner;
EOF

# docs handled by doc section
rm -rf %buildroot%_docdir/wxglade

# fix attr
chmod a+x %buildroot%python_sitelibdir/wxglade/{xrc2wxg,wxglade,templates_ui,msgdialog}.py

%files
%doc docs CHANGES.txt README.txt TODO.txt CREDITS.txt LICENSE.txt
%_bindir/wxglade
%_man1dir/wxglade.1*
%python_sitelibdir/wxglade
%python_sitelibdir/%name-%version-py%__python_version.egg-info
%_desktopdir/%name.desktop
%_iconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_datadir/wxglade/icons/*
%_datadir/wxglade/templates/*

%changelog
* Tue Jul 19 2016 Konstantin Artyushkin <akv@altlinux.org> 0.7.2-alt1
- new version

* Tue Jul 19 2016 Konstantin Artyushkin <akv@altlinux.org> 0.6.8-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.6.8-2
+ Revision: 0083787
- MassBuild#464: Increase release tag


