%define _unpackaged_files_terminate_build 1

Name: papirus-folders
Version: 1.12.1
Release: alt1
Summary: Allows to change the color of folders
License: MIT
Group: Other
Url: https://github.com/PapirusDevelopmentTeam/papirus-folders
Source: %name-%version.tar

BuildArch: noarch
Requires: bash >= 4.0

%description
Papirus-folders is a bash script that allows changing the color
of folders in Papirus icon theme and its forks (which based on
version 20171007 and newer).

%prep
%setup

%install
%makeinstall_std

%files
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/vendor-completions/_%name
%doc LICENSE README.md

%changelog
* Wed Feb 08 2023 Alexander Makeenkov <amakeenk@altlinux.org> 1.12.1-alt1
- Updated to version 1.12.1

* Sat May 14 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.12.0-alt1
- Updated to version 1.12.0

* Sat Nov 20 2021 Alexander Makeenkov <amakeenk@altlinux.org> 1.11.0-alt1
- Updated to version 1.11.0

* Fri May 28 2021 Alexander Makeenkov <amakeenk@altlinux.org> 1.9.0-alt1
- Updated to version 1.9.0

* Tue Nov 24 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.8.0-alt1
- Updated to version 1.8.0

* Thu May 14 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.0-alt1
- Updated to version 1.7.0

* Sat Dec 21 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.0-alt1
- New version

* Sun Oct 27 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.5.0-alt1
- New version

* Sun Oct 13 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.4.0-alt1
- Initial build for ALT
