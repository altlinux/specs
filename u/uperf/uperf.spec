Name: uperf
Version: 1.0.8
Release: alt1

Summary: A network performance tool

License: GPLv3
Group: Networking/Other
Url: http://uperf.org/

#source from: https://sourceforge.net/projects/uperf/files/uperf/
Source: %name-%version.tar

BuildRequires: liblksctp-devel libssl-devel

%description
uperf is a network performance tool that supports modelling and replay of
various networking patterns.

%prep
%setup

%build
%autoreconf
%configure --datadir=%_datadir/%name --enable-ssl
%make_build

%install
%makeinstall_std

%files
%doc NEWS COPYING AUTHORS README
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*.xml

%changelog
* Fri Mar 24 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.8-alt1
- Automatically updated to 1.0.8.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.7-alt1
- Build new version.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sat Feb 25 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.5-alt1
- added .spec file
- fixed build warnings
