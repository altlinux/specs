%define _unpackaged_files_terminate_build 1
%add_python3_req_skip gpresult.Preferences.Preferences.Drive
%add_python3_req_skip gpresult.Preferences.Preferences.EnvVar
%add_python3_req_skip gpresult.Preferences.Preferences.File
%add_python3_req_skip gpresult.Preferences.Preferences.Folder
%add_python3_req_skip gpresult.Preferences.Preferences.Inifile
%add_python3_req_skip gpresult.Preferences.Preferences.Networkshare
%add_python3_req_skip gpresult.Preferences.Preferences.Shortcut

Name: gpresult
Version: 0.0.6
Release: alt1

Summary: Display applied policies
License: GPLv3+
Group: Other
Url: https://gitlab.basealt.space/alt/gpresult
BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3(wheel), python3(hatchling), python3(prettytable)
Requires: gpupdate >= 0.11.0

Source0: %name-%version.tar

%description
gpresult is used to get the result set of Group Policies that apply to a user and/or computer in domain.
The utility allows you to display a list of domain  (GPO) policies that apply to the computer and user.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%files -f %name.lang
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version.dist-info
%_bindir/%name
%_datadir/bash-completion/completions/%name

%changelog
* Wed Jan 28 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.0.6-alt1
- Fixed interpretation of '\' as an escape sequence (Closes: #57582)
- Compilation of translation files now runs at build time

* Tue May 06 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.5-alt2
- Removed libgvdb-gir dependency (automatic dependency lookup works)
- Translation files moved to /usr/share/locale/
- Repackaged translations and added bash-completions to pyproject-toml

* Fri Apr 11 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.5-alt1
- Fixed display of policy version (Closes: #53798)

* Fri Jan 31 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.0.4-alt1
- Added translations for argparse and fixed typos (Closes: #52282)
- Removed repetitions when using the -l and -lr options (Closes: #52878)
- Added --width key to bash completions

* Tue Dec 10 2024 Maria Alexeeva <alxvmr@altlinux.org> 0.0.3-alt1
- Added output about previous key values
- Added --previous key
- Added bash completion (thx skachedubov@altlinux.org)
- Added a key for setting the column width

* Mon Sep 16 2024 Maria Alexeeva <alxvmr@altlinux.org> 0.0.2-alt1
- Added output containing information about Preference
- Added analysis of policies that have no keys

* Mon Sep 02 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.0.1-alt2
- Initial build for Sisyphus

* Mon Aug 19 2024 Maria Alexeeva <alxvmr@altlinux.org> 0.0.1-alt1
- First build

