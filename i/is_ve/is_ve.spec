Name: is_ve
Version: 0.0.1
Release: alt2
License: %gpl2plus

Url: http://sisyphus.ru/ru/srpm/Sisyphus/postgresql-common

Summary: Return '0' if started from OpenVZ VE

Group: System/Base

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildPreReq: rpm-build-licenses

Source: %name-%version.tar

%description
%summary

%prep
%setup 
%build
%make_build
%install
make install DESTDIR=%buildroot

%files
%attr(4711,root,root) %_bindir/is_ve

%changelog
* Sat Oct 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt2
- add Url tag

* Mon Oct 26 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus


