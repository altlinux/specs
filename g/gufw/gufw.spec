Name: gufw
Version: 24.04
Release: alt1
Summary: A graphical user interface for UFW
Group: System/Configuration/Networking

URL: https://github.com/costales/gufw
# https://abf.io/import/gufw/blob/rosa2021.1/gufw.spec
Source: %name-%version.tar
License: GPL-3.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-distutils-extra
BuildRequires: python3(gi)
BuildRequires: python3-module-netifaces
BuildRequires: intltool

%add_python3_req_skip gi.repository.Gdk
%add_python3_path %python3_sitelibdir/%name
%filter_from_provides /python3/d
#%%filter_from_requires /python3(gufw.*/d
%add_python3_self_prov_path %buildroot%python3_sitelibdir/gufw/gufw/

Provides: firewallgui
Provides: gui-ufw
Requires: icon-theme-hicolor
Requires: ufw
Requires: typelib(WebKit2) = 4.0

BuildArch: noarch

%description
An easy, intuitive, way to manage your Linux firewall. It supports common
tasks such as allowing or blocking pre-configured, common p2p, or individual
ports port(s), and many others!

%prep
%setup
sed -i 's|/usr/share/%name|%python3_sitelibdir|' bin/%name-pkexec

%build
#%%__python3 setup.py build
#%%pyproject_build

%install
%__python3 setup.py install --prefix=%_prefix --root %buildroot
#%%pyproject_install

%find_lang %name

install -D -m0644 build/share/applications/%name.desktop %buildroot%_datadir/applications/%name.desktop
install -D -m0644 data/icons/48x48/apps/%name.png %buildroot%_datadir/pixmaps/%name.png
install -D -m0644 data/icons/scalable/apps/%name.svg %buildroot%_datadir/pixmaps/%name.svg
chmod a+rx %buildroot%python3_sitelibdir/%name/%name.py
\rm -rf %buildroot%_docdir/%name

%files -f %name.lang
%doc COPYING.GPL3 README.md
%_sysconfdir/%name
%_bindir/%name
%_bindir/%name-pkexec
%python3_sitelibdir/%{name}*
%_datadir/applications/%name.desktop
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.*
%_datadir/pixmaps/%name.png
%_datadir/pixmaps/%name.svg
%_man8dir/%name.8.*
%_datadir/polkit-1/actions/com.ubuntu.pkexec.%name.policy

%changelog
* Thu Sep 05 2024 Andrew A. Vasilyev <andy@altlinux.org> 24.04-alt1
- Initial build for ALT.

