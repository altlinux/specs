%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-firefox
Version: 5.5
Release: alt1

Summary: Firefox-specific ADMX policy templates
License: MPL-2.0
Group: System/Configuration/Other
Url: https://github.com/mozilla/policy-templates
BuildArch: noarch

BuildRequires: admx-lint

Source0: policy-templates.tar

%description
Firefox-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q -n policy-templates

%install
mkdir -p %buildroot%_datadir
cp -a windows/ %buildroot%_destdir
for file in %buildroot%_destdir/*.admx %buildroot%_destdir/*-*/*.adml; do
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns:xsd=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns:xsd="http:\/\/www.w3.org\/2001\/XMLSchema"/' "$file"
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns:xsi=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns:xsi="http:\/\/www.w3.org\/2001\/XMLSchema-instance"/' "$file"
    grep -q "^\(<policyDefinitions\|<policyDefinitionResources\) .*xmlns=" "$file" ||
        sed -i 's/^\(<policyDefinitions\|<policyDefinitionResources\)/\1 xmlns="http:\/\/schemas.microsoft.com\/GroupPolicy\/2006\/07\/PolicyDefinitions"/' "$file"
done

%check
for file in %buildroot%_destdir/*.admx %buildroot%_destdir/*-*/*.adml; do
    admx-lint --input_file "$file"
done

%files
%doc docs/index.md linux/policies.json
%dir %_destdir
%dir %_destdir/*-*/
%_destdir/*.admx
%_destdir/*/*.adml

%changelog
* Thu Nov 23 2023 Evgeny Sinelnikov <sin@altlinux.org> 5.5-alt1
- Update Policy templates for Firefox 120 and Firefox ESR 115.5
- Add "Enable or disable printing" policy support

* Fri Oct 20 2023 Evgeny Sinelnikov <sin@altlinux.org> 5.3-alt1
- Update Policy templates for Firefox 118 and Firefox ESR 115.3

* Fri Oct 20 2023 Evgeny Sinelnikov <sin@altlinux.org> 4.12-alt1
- Update Policy templates for Firefox 114 and Firefox ESR 102.12

* Tue Oct 25 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.4-alt1
- Update Policy templates for Firefox 106 and Firefox ESR 102.4
- This release contains some typo fixes and new Russian translations
  thanks to lepata@

* Wed Sep 14 2022 Evgeny Sinelnikov <sin@altlinux.org> 4.1-alt1
- Update Policy templates for Firefox 103 and Firefox ESR 102.1
- While these templates will work for Firefox ESR 91, they contain
  new policies that are not in Firefox ESR 91:
  + ExemptDomainFileTypePairsFromFileTypeDownloadWarnings
  + StartDownloadsInTempDirectory
  + UseSystemPrintDialog

* Mon Sep 06 2021 Alenka Glukhovskaya <alenka@altlinux.org> 3.0-alt1
- Update to new release

* Sun Jul 18 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.12-alt1
- Update to new release
- Add admx-lint check with special workaround:
  https://github.com/altlinux/admx-lint/issues/1

* Fri May 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.10-alt1
- Update to new release with russian translation
- Set right URL of upstream project

* Fri Apr 02 2021 Alenka Glukhovskaya <alenka@altlinux.org> 2.9-alt1
- Initial release 

