%def_without test

Name: checksec
Version: 2.6.0
Release: alt1

Summary: Tool to check system for binary-hardening

License: BSD
Group: Development/Tools
Url: https://github.com/slimm609/%name.sh

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %url/archive/%version.tar.gz#/%name-%version.tar

BuildArch: noarch

%if_with test
BuildRequires: binutils
BuildRequires: file
BuildRequires: findutils
BuildRequires: gawk
BuildRequires: libxml2
BuildRequires: openssl
BuildRequires: procps-ng
BuildRequires: %_bindir/jsonlint
%endif

%filter_from_requires /^.etc.lsb-release/d
%filter_from_requires /^.etc.os-release/d

#Requires: binutils
#Requires: file
#Requires: findutils
#Requires: gawk
#Requires: which

%description
Modern Linux distributions offer some mitigation techniques to make it harder
to exploit software vulnerabilities reliably. Mitigations such as RELRO,
NoExecute (NX), Stack Canaries, Address Space Layout Randomization (ASLR) and
Position Independent Executables (PIE) have made reliably exploiting any
vulnerabilities that do exist far more challenging. The checksec script is
designed to test what *standard* Linux OS and PaX (http://pax.grsecurity.net/)
security features are being used.

The script also lists the status of various Linux kernel protection mechanisms.

%name can check binary-files and running processes for hardening features.

%prep
%setup
# fix missed PATH under root: sysctl: command not found
%__subst 's|.*SHLVL.*||' checksec

# Disable --update command.
%__subst 's/pkg_release=false/pkg_release=true/' checksec

%build
# noop

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
install -pm 0755 %name %buildroot%_bindir
install -pm 0644 extras/man/%name.1 %buildroot%_man1dir

%check
pushd tests
./xml-checks.sh || exit 2
./json-checks.sh || exit 2
popd

%files
%doc LICENSE.txt
%doc ChangeLog README.md
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Tue Jun 07 2022 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version 2.6.0 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt2
- fix PATH (thanks, andy@!)

* Sat Dec 18 2021 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

* Mon Jun 14 2021 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- initial build for ALT Sisyphus

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Qiyu Yan <yanqiyu@fedoraproject.org> - 2.4.0-1
- update to 2.4.0 upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Björn Esser <besser82@fedoraproject.org> - 2.2.2-1
- Release 2.2.2 (BZ#1840807)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.1.0-1
- Release 2.1.0 (BZ#1742252)
- Use 'sed' instead of a patch to disable --update command

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 Björn Esser <besser82@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1 (BZ#1693841)
- Section of man-page was moved to man1
- Add patch to disable --update command
- Add patch to fix shebang
- De-tabbify spec file

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.0-2
- Fix Linux 4.18 compitability (BZ#1632412)

* Sun Sep 23 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0 (BZ#1485319)

* Thu Aug 02 2018 Dan Horák <dan[at]danny.cz - 1.7.4-8
- which is Required

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Troy Dawson <tdawson@redhat.com> - 1.7.4-5
- Cleanup spec file conditionals

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 02 2016 Björn Esser <fedora@besser82.io> - 1.7.4-2
- Add manpage a Source1

* Sun Oct 02 2016 Björn Esser <fedora@besser82.io> - 1.7.4-1
- Update to forked version (rhbz 1240391)
- Added missing runtime-dependency on gawk (rhbz 1380950)

* Sun Oct 02 2016 Björn Esser <fedora@besser82.io> - 1.5-7
- Added missing runtime-dependencies (rhbz 1380950)
- Small improvements to spec-file
- Clean trailing whitespaces

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Björn Esser <bjoern.esser@gmail.com> - 1.5-2
- added stuff for el5-build

* Tue Jun 11 2013 Björn Esser <bjoern.esser@gmail.com> - 1.5-1
- Initial rpm release
