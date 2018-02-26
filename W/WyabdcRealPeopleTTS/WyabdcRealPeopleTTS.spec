Name: WyabdcRealPeopleTTS
Version: 1.0
Release: alt1

Summary: Wyabdc RealPeople TTS

License: Public domain
Group: Sound
Url: http://www.openclipart.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar.bz2

BuildArch: noarch

%description
Wyabdc RealPeople TTS, contains many words's sound wave files.
It is used by StarDict and reciteword.

%prep
%setup -q -n %name

%install
%__mkdir -p %buildroot%_datadir
cd ..
cp -rf %name %buildroot%_datadir
#find -print0 | xargs -0 -i'{}' install -D -m0644 "{}" "%buildroot%_datadir/%name/{}"

%files
%_datadir/%name

%changelog
* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- first build for Sisyphus
