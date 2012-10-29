Name:		reaver
Version:	1.4
Release:	alt1
Group:		Security/Networking
License:	GPLv2
Summary:	Utility for audit wireless security against via WAP's and WPS pin
Url:		http://code.google.com/p/reaver-wps/
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source:		%name-%version.tar.gz

# Automatically added by buildreq on Mon Oct 29 2012 (-bi)
# optimized out: elfutils
BuildRequires: libpcap-devel libsqlite3-devel

%description
Reaver-WPS - is a utility for audit wireless security against via WAP's and WPS pin

%prep
%setup
pushd src
%configure
popd

%build
pushd src
%make_build
popd

%install
pushd docs
install -Dp -m 0644 %name.1.gz %buildroot%_mandir/man1/%name.1.gz
popd

pushd src
install -Dp -m 0644 %name.db %buildroot%_sysconfdir/%name/%name.db
install -Dp -m 0755 %name %buildroot/%_bindir/%name
install -Dp -m 0755 wash %buildroot/%_bindir/wash
popd

%files
%dir %_sysconfdir/%name
%doc ./docs/README*
%_bindir/*
%_sysconfdir/%name/*
%_man1dir/*

%changelog
* Mon Oct 29 2012 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt1
- initial build for ALT Linux
