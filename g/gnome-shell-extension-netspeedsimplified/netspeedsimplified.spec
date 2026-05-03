%define exID netspeedsimplified@prateekmedia.extension
%define nameU netspeedsimplified
%define nameS org.gnome.shell.extensions.netspeedsimplified

Name: gnome-shell-extension-netspeedsimplified
Version: 46
Release: alt1

Summary: Net speed Simplified

BuildArch: noarch

License:  GPL-3.0
Group:  Graphical desktop/GNOME
Url: https://github.com/prateekmedia/netspeedsimplified
VCS: https://github.com/prateekmedia/netspeedsimplified

Source: %nameU-%version.tar

Requires: gnome-shell >= 47.0

%description
A Net Speed monitor With Loads of Customization.

%prep
%setup -n %nameU-%version

#subst 's|"49"|"49", "50"|' metadata.json

%build
%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%exID/
install -D -p -m 0644 \
    schemas/%nameS.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%nameS.gschema.xml
cp -a *.js *.json *.css LICENSE %buildroot%_datadir/gnome-shell/extensions/%exID/

%files
%_datadir/gnome-shell/extensions/%exID/*
%_datadir/glib-2.0/schemas/*.xml
%doc *.md LICENSE 

%changelog
* Mon May 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 46-alt1
- 45 -> 46

* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 45-alt2
- fixed for GNOME 50

* Wed Nov 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 45-alt1
- 44 -> 45

* Fri Oct 31 2025 Aleksandr Shamaraev <shad@altlinux.org> 44-alt3
- update to git.2aae2ac

* Thu Oct 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 44-alt2
- fixed for GNOME 49

* Wed May 07 2025 Aleksandr Shamaraev <shad@altlinux.org> 44-alt1
- 43 -> 44

* Wed Mar 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 43-alt2
- fixed for GNOME 48

* Sun Dec 01 2024 Aleksandr Shamaraev <shad@altlinux.org> 43-alt1
- Initial build for Sisyphus.
