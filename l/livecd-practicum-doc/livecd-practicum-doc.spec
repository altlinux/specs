Name: livecd-practicum-doc
Version: 1.0
Release: alt1

Summary: Provides practicum documentation icon
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://www.altlinux.org/practicum/practicum-xfce

BuildArch: noarch

Buildrequires: node-md2html
Buildrequires: livecd-cmdline-mount
Buildrequires: livecd-cmdline-password
Buildrequires: livecd-module-switcher
Buildrequires: livecd-netuser-services
Buildrequires: livecd-prac-style
Buildrequires: livecd-replace-localdomain

Source: %name-%version.tar

Requires(pre): shared-desktop-icons

%description
Desktop README for practicum featured changes.

%prep
%setup

%install
mkdir -p tmp_docs
i=1; find %_datadir/doc -name "README.practicum.md" \
	-print0 | while IFS= read -r -d '' file; \ 
	do cp "$file" "tmp_docs/${i}_README.md"; ((i++)); done
cp README.practicum.md tmp_docs/0_README.md
md2html -s tmp_docs/ -o README.html
install -pD -m644 README.desktop %buildroot%_datadir/applications/README.desktop

%files
%_datadir/applications/README.desktop
%doc README.html README.practicum.md

%changelog
* Sat Nov 22 2025 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
