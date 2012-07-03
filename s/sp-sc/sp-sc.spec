%define oname sp-auth
Name: sp-sc
Version: 1.1.1
Release: alt1

Summary: Sopcast command line client

License: Distributable
Group: Video

Url: http://sopcast.org/download/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.sopcast.cn/download/%oname.tar.bz2
Source1: %name.LICENSE

ExclusiveArch: i586

BuildRequires: libstdc++3.3
Requires: libstdc++3.3
# due libc.so.6(GLIBC_PRIVATE)
AutoReq: no

%description
p2p TV sopcast command line client.
Example of using:
sp-sc sop://broker.sopcast.com:3912/6098 3908 8908
mplayer http://localhost:8908/tv.asf

%prep
%setup -n %oname

%build
./sp-sc-auth || :

%install
cp %SOURCE1 LICENSE
install -m755 -D sp-sc-auth %buildroot%_bindir/sp-sc-auth
ln -s sp-sc-auth %buildroot%_bindir/sp-sc

%files
%doc Readme LICENSE
%_bindir/sp-sc
%_bindir/sp-sc-auth

%changelog
* Sun Mar 09 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

