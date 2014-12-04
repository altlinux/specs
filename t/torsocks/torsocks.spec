Name: torsocks
Version: 2.0.0
Release: alt1

Summary: Use SOCKS-friendly applications with Tor
Group: Security/Networking
License: %gpl2only
Url: https://code.google.com/p/torsocks/
Packager: Vladimir Didenko <cow@altlinux.ru>

Source: %name-%version.tar
Source1: %name.bash_completion

BuildRequires(pre): rpm-build-licenses
BuildRequires: autoconf-archive
Requires: tor

%description
Torsocks allows you to use most SOCKS-friendly applications in a safe way
with Tor. It ensures that DNS requests are handled safely and explicitly
rejects UDP traffic from the application you are using.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

mkdir -p %buildroot/etc/bash_completion.d
install -p -m644 %SOURCE1 %buildroot%_sysconfdir/bash_completion.d/%name

%files
%doc ChangeLog gpl-2.0.txt LICENSE README.md
%{_bindir}/%name
%{_mandir}/man1/%name.1.*
%{_mandir}/man5/%name.conf.5.*
%{_mandir}/man8/%name.8.*
%dir %{_libdir}/%name
# %torsocks requires this file so it has not been placed in -devel subpackage
%{_libdir}/%name/lib%name.so
%{_libdir}/%name/lib%name.so.0*
%exclude %{_libdir}/%name/lib%name.a
%exclude %{_libdir}/%name/lib%name.la
%{_libdir}/%name/lib%name.so.0*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%name
%config(noreplace) %{_sysconfdir}/tor/%name.conf
%exclude %_datadir/doc/%name

%changelog
* Thu Dec 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
