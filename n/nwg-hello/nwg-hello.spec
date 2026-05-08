%define _unpackaged_files_terminate_build 1
%define _tmpfilesdir /lib/tmpfiles.d

Name: nwg-hello
Version: 0.4.5
Release: alt1

Summary: GTK3-based greeter for greetd written in python
License: MIT
Group: Graphical desktop/Other
URL: https://github.com/nwg-piotr/nwg-hello

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

Requires: greetd
Requires: typelib(GtkLayerShell)

BuildArch: noarch

Source: %name-%version.tar

%description
Nwg-hello is a GTK3-based greeter for the greetd daemon, written in
python. It is meant to work under a Wayland compositor, like sway or
Hyprland. The greeter has been developed for the nwg-iso project, but it
may be configured for standalone use.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

# installing additional files
install -Dm 644 %{name}-default.json %buildroot/%_sysconfdir/%name/%{name}-default.json
install -Dm 644 %{name}-default.css %buildroot/%_sysconfdir/%name/%{name}-default.css
install -Dm 644 hyprland.conf %buildroot/%_sysconfdir/%name/hyprland.conf
install -Dm 644 sway-config %buildroot/%_sysconfdir/%name/sway-config
install -Dm 644 img/* -t %buildroot/%_datadir/%name/
install -Dm 644 nwg.jpg %buildroot/%_datadir/%name/nwg.jpg
install -Dm 644 cache.json %buildroot/%_var/cache/%name/cache.json

cat <<EOF > %{name}.tmpfiles
d /var/cache/nwg-hello 0755 greeter greeter -
f /var/cache/nwg-hello/cache.json 0644 greeter greeter -
EOF
install -Dm 644 %{name}.tmpfiles %buildroot/%_tmpfilesdir/%{name}.conf

%files
%doc LICENSE README README.md
%python3_sitelibdir/nwg_hello/
%python3_sitelibdir/%{pyproject_distinfo nwg_hello}
%_bindir/*
%dir %_sysconfdir/%name/
%_sysconfdir/%name/*
%_tmpfilesdir/%{name}.conf
%dir %_datadir/%name/
%_datadir/%name/*
%_var/cache/%name/cache.json

%changelog
* Fri May 08 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.5-alt1
- New version 0.4.5.

* Fri Apr 03 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.4-alt1
- New version 0.4.4.

* Fri Feb 20 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.3-alt1
- New version 0.4.3.

* Wed Jan 07 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.2-alt1
- New version 0.4.2.

* Sat Jun 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt2
- Applied repocop fix for sisyphus_check

* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
