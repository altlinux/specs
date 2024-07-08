%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-chromium
Version: 126.0
Release: alt1

Summary: Chromium-specific ADMX policy templates
License: CC-BY-2.5
Group: System/Configuration/Other
Url: https://www.chromium.org/administrators/policy-templates
BuildArch: noarch

BuildRequires: admx-lint
BuildRequires: iconv

Source0: policy_templates.tar

%description
Chromium-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q -n policy_templates

%install
mkdir -p %buildroot%_datadir
cp -a windows/admx/ %buildroot%_destdir
for file in %buildroot%_destdir/*.admx %buildroot%_destdir/*-*/*.adml; do
    if echo "$(basename "$file")" | grep -q "^chrome"; then
        mv "$file" "$file.utf16"
        iconv -f UTF-16 -t UTF-8 <"$file.utf16" >"$file"
        rm -f "$file.utf16"
    fi
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns:xsd=" "$file" ||
        sed -i 's/\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns:xsd="http:\/\/www.w3.org\/2001\/XMLSchema"/' "$file"
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns:xsi=" "$file" ||
        sed -i 's/\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns:xsi="http:\/\/www.w3.org\/2001\/XMLSchema-instance"/' "$file"
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns=" "$file" ||
        sed -i 's/\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns="http:\/\/schemas.microsoft.com\/GroupPolicy\/2006\/07\/PolicyDefinitions"/' "$file"
done

%check
for file in %buildroot%_destdir/*.admx %buildroot%_destdir/*-*/*.adml; do
    admx-lint --input_file "$file"
done

%files
%dir %_destdir
%dir %_destdir/*-*/
%_destdir/*.admx
%_destdir/*/*.adml

%changelog
* Mon Jul 08 2024 Valentin Sokolov <sova@altlinux.org> 126.0-alt1
- Update to latest release 126.0-6478.127

* Fri May 10 2024 Evgeny Sinelnikov <sin@altlinux.org> 124.0-alt1
- Update to latest release 124.0-6367.202

* Tue Mar 05 2024 Valentin Sokolov <sova@altlinux.org> 122.0-alt1
- Update to latest release 122.0-6261.95

* Tue Feb 20 2024 Valentin Sokolov <sova@altlinux.org> 121.0-alt1
- Update to latest release 121.0-6167.185

* Mon Dec 25 2023 Evgeny Sinelnikov <sin@altlinux.org> 120.0-alt1
- Update to latest release 120.0-6099.130

* Thu Nov 23 2023 Evgeny Sinelnikov <sin@altlinux.org> 119.0-alt1
- Update to latest release 119.0-6045.160

* Fri Oct 20 2023 Evgeny Sinelnikov <sin@altlinux.org> 118.0-alt1
- Update to latest release 118.0-5993.89

* Thu Dec 29 2022 Evgeny Sinelnikov <sin@altlinux.org> 108.0-alt1
- Update to latest release 108.0-5359.125

* Tue Oct 25 2022 Evgeny Sinelnikov <sin@altlinux.org> 106.0-alt1
- Update to latest release 106.0-5249.119

* Thu Sep 15 2022 Evgeny Sinelnikov <sin@altlinux.org> 105.0-alt1
- Update to latest release 105.0-5195.127

* Sun Jul 18 2021 Evgeny Sinelnikov <sin@altlinux.org> 91.0-alt1
- Update to latest release 91.0-4472.164
- Add admx-lint check with special workaround:
  https://github.com/altlinux/admx-lint/issues/1
- Convert UTF-16 chrome.adm files to UTF-8

* Fri May 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 90.0-alt1
- Update to latest release
- Fix installation to /usr/share/PolicyDefinitions
- Set right License and URL of upstream project

* Fri Apr 02 2021 Alenka Glukhovskaya <alenka@altlinux.org> 89.0-alt1
- Initial release

