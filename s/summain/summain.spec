%define _unpackaged_files_terminate_build 1

Name: summain
Version: 0.26.0
Release: alt1

Summary: File manifest generator
License: GPLv3+
Group: File tools
Url: https://doc.liw.fi/summain/

Source0: %name-%version.tar
Source1: vendor.tar
Source2: cargo_config.toml
Patch: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: /proc

%description
Produce a manifest of specified files. The manifest lists the files, and for
each file its important metadata, and if it's a regular file, the checksum of
the contents. The order in the output is deterministic: if the program is run
twice for the same file, and files haven't changed, the output is identical.

This is meant for testing that a backup has been restored correctly.

%prep
%setup -a1
%autopatch -p1

# point to vendored sources
export CARGO_HOME=${PWD}/.cargo
mkdir "$CARGO_HOME"
cp "%SOURCE2" "$CARGO_HOME/config.toml"

%build
export CARGO_HOME=${PWD}/.cargo
cargo build --offline --release

%install
export CARGO_HOME=${PWD}/.cargo
cargo install --offline --force --root %buildroot/%_usr --path ./ --no-track

%check
# requires Subplot: https://subplot.liw.fi/
# see 'check' file for details

%files
%doc *.md
%_bindir/summain

%changelog
* Fri Feb 04 2022 Stanislav Levin <slev@altlinux.org> 0.26.0-alt1
- 0.20 -> 0.26.0 (Python => Rust).

* Fri Jul 30 2021 Stanislav Levin <slev@altlinux.org> 0.20-alt3
- Fixed build on e2k (thanks to ilyakurdyukov@).

* Fri Mar 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.20-alt2
- Porting to python3.

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- new version 0.20 (with rpmrb script)

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt1
- initial build for ALT Linux Sisyphus

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 20 2014 Kevin Fenzi <kevin@scrye.com> - 0.19-4
- Rebuild for rpm bug 1131892

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Michel Salim <salimma@fedoraproject.org> - 0.19-1
- Update to 0.19

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Michel Salim <salimma@fedoraproject.org> - 0.18-1
- Update to 0.18

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 0.17-1
- Update to 0.17

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Michel Salim <salimma@fedoraproject.org> - 0.14-2.1
- When building for EL6, skip unavailable package checks

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Michel Salim <salimma@fedoraproject.org> - 0.14-1
- Update to 0.14

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.13-1
- Initial package
