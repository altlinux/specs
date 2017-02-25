Name: uperf
Version: 1.0.5
Release: alt1

Summary: A network performance tool

License: GPL
Group: Networking/Other
Url: http://uperf.org/

#source from: https://sourceforge.net/projects/uperf/files/uperf/
Source: %name-%version.tar
Patch0: uperf-1.0.5-alt-warnings.patch

BuildRequires: liblksctp-devel libssl-devel

%description
uperf is a network performance tool that supports modelling and replay of
various networking patterns.

%prep
%setup
%patch0 -p2

%build
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
* Wed Feb 25 2017 Oleg Solovyov <mcpain@altlinux.org> 1.0.5-alt1
- added .spec file
- fixed build warnings
