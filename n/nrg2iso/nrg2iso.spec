Name:		nrg2iso
Summary:	Convert NRG images to ISO
Version:	0.4
Release:	alt1
License:	GPL
Group:		File tools
Source:		http://gregory.kokanosky.free.fr/v4/linux/%{name}-%{version}.tar.gz
Patch:		nrg2iso.patch
Url:		http://gregory.kokanosky.free.fr/v4/linux/nrg2iso.en.html
Packager:	Stanislav Yadykin <tosick@altlinux.ru>

%description
nrg2iso converts Images created by Nero Burning Rom to standard .iso (ISO9660) Files. 
Quite useful if you don't want to buy or start Windows and Burning Rom...

%prep
%setup -q
%patch -p0

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall

%files
%_bindir/nrg2iso
%doc gpl.txt CHANGELOG

%changelog
* Wed Aug 17 2005 Stanislav Yadykin <tosick@altlinux.ru> 0.4-alt1
- 0.4
- fixed build various target platforms

* Fri May 06 2005 Stanislav Yadykin <tosick@altlinux.ru> 0.2-alt1
- build for Sisyphus

