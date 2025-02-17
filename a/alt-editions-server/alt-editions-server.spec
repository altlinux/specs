%define _unpackaged_files_terminate_build 1

Name: alt-editions-server
Version: 0.1.3
Release: alt1

Summary: Editions of BaseALT distribution ALT Server.
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alt-editions-server

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: alterator-entry >= 0.2.0
BuildRequires: cmark

Requires: alt-os-editions

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
find ./editions -name '*.edition' -type f -exec alterator-entry validate {} \+

%files
%dir %_alterator_datadir
%_alterator_datadir/editions

%changelog
* Mon Feb 17 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.1.3-alt1
- Added disks components and postgresql17 (thx Sergey Savelev)

* Thu Feb 13 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.1.2-alt1
- The initial basic set of components and components included in the domain
- editionhas been formed (thx Sergey Savelev)

* Thu Feb 13 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.1-alt2
- Remove alterator-interface-edition from requires.
- Fix bogus date in changelog.

* Mon Feb 10 2025 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.1.1-alt1
- The initial basic set of components and components included in the
  server edition has been formed (thx Sergey Savelev)

* Fri Jan 10 2025 Michael Chernigin <chernigin@altlinux.org> 0.1.0-alt1
- Initial build.
