Name: PySolFC-Cardsets
Version: 3.1
Release: alt2

Summary: Various cardsets for PySolFC

License: GPLv2+
Group: Games/Cards
Url: https://github.com/shlomif/PySolFC-Cardsets

# Source-url: https://github.com/shlomif/PySolFC-Cardsets/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch

Requires: PySolFC >= %version

%description
This package contains various cardsets for PySolFC.

%prep
%setup

%build
%install
install -d -m755 %buildroot%_datadir/PySolFC
cp -a cardset-* %buildroot%_datadir/PySolFC

find %buildroot%_datadir/PySolFC -type f -name 'COPYRIGHT' -exec chmod 0644 '{}' \;

%files
%_datadir/PySolFC/cardset*

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt2
- ship all cardsets: PySolFC no longer includes standard ones (fix missing "Standard" cardset)

* Wed Apr 08 2026 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version (3.1)

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1.1
- Support PySolFC >= 2.0

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0

* Sat Sep 26 2009 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from FC

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 25 2007 Stewart Adam <s.adam@diffingo.com> 1.1-3
- Remove BR python-devel
- Add dot to %%description
- Remove preinstalled cardsets
- Use a dir PySolFC actually recognizes

* Wed Oct 24 2007 Stewart Adam <s.adam@diffingo.com> 1.1-2
- Own dirs we create
- Remove %%{?dist} tag
- Fix URL, description and summary
- Don't place any executable files in the RPM

* Sat Sep 29 2007 Stewart Adam <s.adam@diffingo.com> 1.1-1
- Initial release
