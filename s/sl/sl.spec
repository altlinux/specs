Name: sl
Version: 5.02
Release: alt1
Summary: Steam Locomotive in ASCII art
# The warranty claim is a bit different, but the rights are the same as in ISC
License: ISC
Group: Games/Other
Url: https://github.com/mtoyoda/sl
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://github.com/mtoyoda/%name/archive/%version/%name-%version.tar.gz
Patch0: update_to_master_at_923e7d7.patch
BuildRequires: libncurses-devel
Conflicts: python3-softlayer

%description
"sl" displays a steam locomotive running across the terminal.
It is a joke command intended to catch any mistypings of "ls".

%prep
%setup
%patch0 -p1

%build
make OPTFLAGS="%optflags" %{?_smp_mflags}

%install
install -d %buildroot%_bindir
install -d %buildroot%_man1dir
cp sl %buildroot%_bindir/sl
cp sl.1 %buildroot%_man1dir/sl.1

%files
%_man1dir/*
%_bindir/%name
%doc README.md
%doc LICENSE

%changelog
* Fri Feb 03 2023 Artyom Bystrov <arbars@altlinux.org> 5.02-alt1
- initial build for ALT Sisyphus

* Sat Aug 24 2019 Jan Engelhardt <jengelh@inai.de>
- Clarify description.
* Mon Jul 29 2019 Sebastian Wagner <sebix+novell.com@sebix.at>
- Add Conflict with python3-softlayer.
* Tue Jul  2 2019 Sebastian Wagner <sebix+novell.com@sebix.at>
- specfile: fix license, add license and readme file
* Thu Feb 21 2019 jannik.main@gmail.com
- Remove old patchfile.
* Thu Feb 21 2019 jannik.main@gmail.com
- Change patchname to reference upstream-commit.
* Thu Dec 27 2018 Matej Cepl <mcepl@suse.com>
- Initial packaging effort. Use verifiable 5.02 tarball,
  and patch update_to_master_at_923e7d7.patch which lifts the
  code up to the latest commit on the master branch now (commit
  ID 923e7d7).
