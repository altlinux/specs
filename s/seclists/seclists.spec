%define _unpackaged_files_terminate_build 1

Name: seclists
Version: 2025.3
Release: alt1.git93df3da7

Summary: Collection of multiple types of lists used during security assessments
License: MIT
Group: Security/Networking
Url: https://github.com/danielmiessler/SecLists
Vcs: https://github.com/danielmiessler/SecLists

BuildArch: noarch
AutoReqProv: no

Source: %name-%version.tar

%description
SecLists is the security tester's companion. It's a collection of
multiple types of lists used during security assessments,
collected in one place. List types include usernames, passwords, URLs,
sensitive data patterns, fuzzing payloads, web shells, and many more.
The goal is to enable a security tester to pull this repository onto
a new testing box and have access to every type of list that may be needed.

%prep
%setup

%install
cd SecLists
find . \( ! -iname "*.md" -a ! -iname ".git*" -a ! -name "LICENSE" \) -type f \
    -exec sh -c 'install -Dm644 "$1" "%buildroot/%_datadir/%name/${1#./}"' _ {} \;
find . \( -iname "*.md" -o -iname "LICENSE" \) -type f \
    -exec sh -c 'install -Dm644 "$1" "%buildroot/%_datadir/doc/%name-%version/${1#./}"' _ {} \;

%files
%_datadir/doc/%name-%version
%_datadir/%name

%changelog
* Wed Mar 04 2026 Denis Rastyogin <gerben@altlinux.org> 2025.3-alt1.git93df3da7
- Initial Build for Sisyphus.
