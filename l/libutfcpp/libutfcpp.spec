%define uglyver 2_3_4
Name: libutfcpp
Version: 3.1
Release: alt1

Summary: A library for handling UTF-8 encoded strings

License: BSL-1.0
Group: Development/C++
Url: http://sourceforge.net/projects/utfcpp/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://download.sourceforge.net/%name/utf8_v%uglyver.zip
Source: %name-%version.tar

%description
A library for handling UTF-8 encoded strings.

See https://github.com/ledger/utfcpp also.

%prep
%setup

%build

%install
cd source
install -d %buildroot/%_includedir/utf8
install -m0644 utf8.h %buildroot/%_includedir
install -m0644 utf8/{checked,unchecked,core}.h %buildroot/%_includedir/utf8

%package devel
Summary: A library for handling UTF-8 encoded strings
Group: Development/C++

%description devel
A library for handling UTF-8 encoded strings.

%files devel
%_includedir/utf8/
%_includedir/utf8.h

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version 3.1 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- initial build for ALT Linux Sisyphus

* Thu Jan 15 2015 jmatejka@suse.cz
- Initial package version 2.3.4
