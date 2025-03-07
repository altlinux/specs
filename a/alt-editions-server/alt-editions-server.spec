%define _unpackaged_files_terminate_build 1

%define alt_components_base_version 0.3.0

Name: alt-editions-server
Version: 0.2.1
Release: alt1

Summary: Editions of BaseALT distribution ALT Server.
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alt-editions-server

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: alterator-entry >= 0.2.4
BuildRequires: cmark

Requires: alt-os-editions
BuildRequires: alt-components-base >= %alt_components_base_version
Requires: alt-components-base >= %alt_components_base_version

%description
%summary.

%prep
%setup

%install
mkdir -p "%buildroot%_datadir/alterator/editions"

for d in editions/*/ ; do
    find "$d" -type f -name "description*.md" -print0 | while IFS= read -r -d '' file; do
        cmark "$file" > "${file/%%md/html}"
    done
done

for edition_dir in editions/*/; do
    edition="$(basename "$edition_dir")"

    mkdir -p "%buildroot%_alterator_datadir/editions/$edition"

    install -v -p -m 644 -D "$edition_dir/$edition.edition" "%buildroot%_alterator_datadir/editions/$edition"

    find "$edition_dir" -type f -name "description*.html" -print0 | while IFS= read -r -d '' file; do
        install -v -p -m 644 -D "$file" "%buildroot%_alterator_datadir/editions/$edition"
    done
done

%check
checkval=
for e in `find ./editions -name '*.edition' -type f`; do
    alterator-entry validate "$e"
    (alterator-entry get "$e" sections.base.components &&
           alterator-entry get "$e" sections.main.components) 2>/dev/null |
    while read c; do
        if ! test -f "/usr/share/alterator/components/$c/$c.component"; then
            echo "failed to locate component $c in edition $e"
            checkval=1
        fi
    done
done
[ -z "$checkval" ] || exit "$checkval"

%files
%dir %_alterator_datadir
%_alterator_datadir/editions

%changelog
* Sat Mar 08 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2.1-alt1
- fix: clean unused or absent gnome components
- fix: update typos in component names

* Fri Mar 07 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2.0-alt2
- Build with special alt-components-base version.

* Fri Mar 07 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.2.0-alt1
- Complete refactoring: update tree to refactored alt-components-base-0.3.0.

* Wed Feb 19 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.1.5-alt1
- The "network-manager-gtk" component has been removed from the server
  edition (thx Sergey Savelev)

* Tue Feb 18 2025 Evgeny Sinelnikov <sin@altlinux.org> 0.1.4-alt1
- Fix: domain edition: component disks renamed to disks-utilities-other.
- Update sections: rename Edition components to Main components.

* Mon Feb 17 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.1.3-alt1
- Added disks components and postgresql17 (thx Sergey Savelev)

* Thu Feb 13 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.1.2-alt1
- The initial basic set of components and components included in the domain
  edition has been formed (thx Sergey Savelev)

* Thu Feb 13 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt2
- Remove alterator-interface-edition from requires.
- Fix bogus date in changelog.

* Mon Feb 10 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.1.1-alt1
- The initial basic set of components and components included in the
  server edition has been formed (thx Sergey Savelev)

* Fri Jan 10 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
