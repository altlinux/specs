BuildRequires: desktop-file-utils
%def_disable gnome

Name: lekhonee
Version: 0.7
Release: alt1.qa1.1

Summary: A blog client
Group: Networking/Other
License: GPLv2
Url: http://fedorahosted.org/lekhonee

Source: https://fedorahosted.org/releases/l/e/lekhonee/%name-%version.tar.gz

BuildArch: noarch

BuildRequires: python-module-distutils-extra
Requires: python-module-%name = %version-%release

%description
A desktop wordpress client

%package gnome
Summary: Wordpress desktop client frontend for Gnome
Group: Networking/Other
Requires: %name = %version-%release
Requires: python-module-%name = %version-%release

%description gnome
Wordpress desktop client frontend for Gnome.

%package -n python-module-%name
Summary: The backend library for wordpress desktop client
Group: Development/Python

%description -n python-module-%name
The backend library for wordpress desktop client.

%prep
%setup -q

%build
%python_build

%install
%python_install
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=WebDevelopment \
	%buildroot%_desktopdir/lekhonee.desktop

%files
%_bindir/lekhonee
%_datadir/pixmaps/lekhonee.png
%_datadir/pixmaps/chotha/
%_datadir/applications/lekhonee.desktop
%python_sitelibdir/Chotha/*
%python_sitelibdir/*.egg-info
%doc docs/{README,ChangeLog}

%if_enabled gnome
%files gnome
%_bindir/lekhonee-gnome
%_datadir/chotha/gnome-frontend/*
%_datadir/pixmaps/lekhonee-gnome.png
%_datadir/applications/lekhonee-gnome*.desktop
%else
%exclude %_bindir/lekhonee-gnome
%exclude %_datadir/chotha/gnome-frontend/*
%exclude %_datadir/pixmaps/lekhonee-gnome.png
%exclude %_datadir/applications/lekhonee-gnome*.desktop
%endif

%files -n python-module-%name
%python_sitelibdir/lekhoneeblog/

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.qa1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.7-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for lekhonee

* Sat Feb 13 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- first build for Sisyphus

