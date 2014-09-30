Name:		luma
Version:	3.0.7
Release: 	alt1
Summary:	A graphical tool for managing LDAP servers

Group:		Networking/Other
License:	GPLv2
URL:		http://www.sourceforge.net/projects/luma
Source0:	http://prdownloads.sourceforge.net/luma/luma-%{version}.tar.gz
Patch1:		luma-3.0.7-desktop.patch

BuildArch:	noarch 

BuildRequires(pre): rpm-build-python
BuildRequires:	python-module-PyQt4-devel
BuildRequires:	python-module-ldap >= 2.3
BuildRequires:	python-module-smbpasswd
BuildRequires:  ImageMagick

Requires:	python-module-smbpasswd

%description
Luma - a graphical tool for accessing and managing LDAP
servers. It is written in Python, using PyQt and python-ldap.
Plugin-support is included and useful widgets with LDAP-
functionality for easy creation of plugins are delivered.

%prep
%setup
%patch1 -p2

# Remove tests
rm -f luma/runtests.py

%build
%python_build

%install
%python_install

# Add plugins/browser/templates
install -d %buildroot%python_sitelibdir/luma/plugins/browser/templates
cp -R luma/plugins/browser/templates/* \
   %buildroot%python_sitelibdir/luma/plugins/browser/templates

%files
%doc AUTHORS ChangeLog COPYING README TODO
%_bindir/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/*/apps/%name.png
%_pixmapsdir/%name.svg
%_desktopdir/%name.desktop
%doc %_man1dir/%name.*
%python_sitelibdir/*

%changelog
* Tue Sep 30 2014 Andrey Cherepanov <cas@altlinux.org> 3.0.7-alt1
- Initial build in Sisyphus from Fedora
- Remove tests
- Fix Russian translations of menu item
