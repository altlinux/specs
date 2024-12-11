%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-thunderbird
Version: 0.1.0
Release: alt1

Summary: Thunderbird-specific ADMX policy templates
License: MPL-2.0
Group: System/Configuration/Other
Url: https://github.com/thunderbird/policy-templates
BuildArch: noarch

BuildRequires: admx-lint
Requires: admx-firefox

Source0: policy-templates.tar

%description
Thunderbird-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q -n policy-templates

%install
mkdir -p %buildroot%_datadir
cp -a templates/central/windows/ %buildroot%_destdir
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
%doc templates/central/README.md
%dir %_destdir
%dir %_destdir/*-*/
%_destdir/*.admx
%_destdir/*/*.adml

%changelog
* Mon Sep 16 2024 Valentin Sokolov <sova@altlinux.org> 0.1.0-alt1
- Initial build for Sysiphus

