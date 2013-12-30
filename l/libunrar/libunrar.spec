Name:		libunrar
Version:	5.0.14
Release:	alt1
Summary:	Library for extract *.rar format archives
Url:		http://www.rarlab.com/rar_add.htm

Source:		%name-%version.tar
License:	Freeware
Group:		System/Libraries
BuildRequires:  gcc-c++

%description
This library allows programs linking against it to decompress RAR v5 archives.

%prep
%setup -q

%build
make lib CXXFLAGS+="%optflags -fPIC -DSILENT" STRIP=true

%install
install -pD -m 644 libunrar.so %buildroot/%_libdir/libunrar.so

%files
%doc license.txt readme.txt
%_libdir/libunrar.so

%changelog
* Mon Dec 30 2013 Motsyo Gennadi <drool@altlinux.ru> 5.0.14-alt1
- build for Sisyphus (thank for src.rpm to Anatoly Chernov)

* Wed Oct 02 2013 Motsyo Gennadi <drool@altlinux.ru> 5.0.12-alt1
- build for Sisyphus (thank for src.rpm to Anatoly Chernov)
