%define oname compsize

Name: btrfs-compsize
Version: 1.5
Release: alt1

Summary: Utility for measuring compression ratio of files on btrfs
License: GPLv2+
Group: File tools

Url: https://github.com/kilobyte/compsize

# Source-url: https://github.com/kilobyte/%name/archive/v%version/%oname-%version.tar.gz
Source: %name-%version.tar
Patch: %name.patch

BuildRequires: libbtrfs-devel

%description
compsize takes a list of files (given as arguments) on a btrfs filesystem and
measures used compression types and effective compression ratio, producing
a report.

%prep
%setup
%patch -p2

%build
%make_build "CFLAGS=%optflags"

%install
install -D -m 0755 %oname %buildroot%_bindir/%oname
install -D -m 0644 %oname.8 %buildroot%_man8dir/%oname.8

%files
%doc README.md
%doc LICENSE
%_bindir/%oname
%_man8dir/%oname.8*

%changelog
* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- initial build for ALT Sisyphus

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Juan Orti Alcaine <jortialc@redhat.com> - 1.5-1
- Version 1.5 (#1918100)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Juan Orti Alcaine <jortialc@redhat.com> - 1.4-1
- Version 1.4 (#1918100)

* Thu Aug 06 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.3-4
- Use set_build_flags macro

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Juan Orti Alcaine <jortialc@redhat.com> - 1.3-1
- Version 1.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1-1
- Initial release
