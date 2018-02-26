Name: PySolFC-Cardsets
Version: 2.0
Release: alt1
Summary: Various cardsets for PySolFC
Group: Games/Cards
License: GPLv2+
Url: http://pysolfc.sourceforge.net/
Source: %name-%version.tar.bz2
BuildArch: noarch

Requires: PySolFC = %version

%description
This package contains various cardsets for PySolFC.

%prep
%setup

%build
%install
install -d -m755 %buildroot%_datadir/PySolFC
# remove cardsets included in PySolFC package
rm -rf cardset-2000 cardset-crystal-mahjongg cardset-dashavatara-ganjifa \
       cardset-dondorf cardset-gnome-mahjongg-1 cardset-hexadeck \
       cardset-kintengu cardset-matrix cardset-mughal-ganjifa cardset-oxymoron \
       cardset-standard cardset-tuxedo cardset-vienna-2k
cp -a cardset-* %buildroot%_datadir/PySolFC

find %buildroot%_datadir/PySolFC -type f -name 'COPYRIGHT' -exec chmod 0644 '{}' \;

%files
%_datadir/PySolFC/cardset*

%changelog
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
