Name: hunspell-be
Summary: Belarusian hunspell dictionaries
Version: 1.1
Release: alt0.1
Source: http://extensions.services.openoffice.org/files/2412/1/dict-be-official.oxt
Group: Text tools
Url: http://extensions.services.openoffice.org/project/dict-be-official

License: GPL+ and LGPLv2+
BuildArch: noarch

Requires: libhunspell
Buildrequires: unzip

%description
Belarusian hunspell dictionaries.

%package -n hyphen-be
Requires: libhyphen
Summary: Belarusian hyphenation rules
Group: Text tools

%description -n hyphen-be
Belarusian hyphenation rules.

%prep
%setup -c -n hunspell-be

%build
subst "s/microsoft-cp1251/CP1251/g" be-official.aff hyph_be_BY.dic
tail -n +3 hyph_be_BY.dic| head -n 3 > README_hyph_be_BY

%install
mkdir -p %buildroot/%_datadir/myspell
cp -p be-official.aff %buildroot/%_datadir/myspell/be_BY.aff
cp -p be-official.dic %buildroot/%_datadir/myspell/be_BY.dic
mkdir -p %buildroot/%_datadir/hyphen
cp -p hyph_be_BY.dic %buildroot/%_datadir/hyphen/hyph_be_BY.dic

%files
%_datadir/myspell/*

%files -n hyphen-be
%doc README_hyph_be_BY
%_datadir/hyphen/*

%changelog
* Mon Apr 18 2011 L.A. Kostis <lakostis@altlinux.ru> 1.1-alt0.1
- Initial build for ALTLinux.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 23 2010 Caolán McNamara <caolanm@redhat.com> - 1.1-2
- add README_hyph_be_BY to subpackage

* Wed Sep 23 2009 Caolán McNamara <caolanm@redhat.com> - 1.1-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Caolán McNamara <caolanm@redhat.com> - 1.0.0-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 28 2008 Caolán McNamara <caolanm@redhat.com> - 0.1-1
- initial version
