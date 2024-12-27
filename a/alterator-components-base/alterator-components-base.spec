%define _unpackaged_files_terminate_build 1

Name: alterator-components-base
Version: 0.1.4
Release: alt1

Summary: Base set of Alterator components.
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-components-base

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: cmark

Requires: alterator-interface-component >= 0.1.6

%description
%summary.

%prep
%setup

%build
for d in components/*/ ; do
    find "$d" -type f -name "description*.md" -print0 | while IFS= read -r -d '' file; do
        cmark "$file" > "${file/%%md/html}"
    done
done

%install
mkdir -p "%buildroot%_datadir/alterator/backends"
mkdir -p "%buildroot%_datadir/alterator/components/categories"

for d in components/*/ ; do
    d="$(basename "$d")"
    mkdir -p "%buildroot%_datadir/alterator/components/$d"
    install -v -p -m 644 -D "components/$d/$d.backend" "%buildroot%_datadir/alterator/backends"
    install -v -p -m 644 -D "components/$d/$d.component" "%buildroot%_datadir/alterator/components/$d"
    
    find "components/$d" -name '*.png' -type f | while read -r file; do
	install -v -p -m 664 -D "$file" "%buildroot%_datadir/alterator/components/$d"
    done
    
    find "components/$d" -type f -name "description*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_datadir/alterator/components/$d"
    done
done

for d in categories/* ; do
    d="$(basename "$d")"
    install -v -p -m 644 -D "categories/$d" "%buildroot%_datadir/alterator/components/categories"
done

%files
%_datadir/alterator/backends/*
%_datadir/alterator/components/*

%changelog
* Tue Dec 24 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.4-alt1
- Add stdout_strings to components status method to get list of installed
  packages.

* Mon Dec 23 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.3-alt1
- Added sections for categories (thx Sergey Savelev)
- Added nested categories (thx Sergey Savelev)

* Tue Dec 17 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.2-alt1
- New components including some related to kde (thx Sergey Savelev, Elena
  Dyatlenko, Anna)
- Move categories into own dir

* Mon Nov 04 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt1
- A basic set of components for ALT Server.

* Thu Oct 17 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build with example components.
