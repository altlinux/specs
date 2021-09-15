Name: libnss-altfiles
Version: 2.23.0
Release: alt1

Summary: NSS module which can read user information from files

License: LGPLv2.1
URL: https://github.com/aperezdc/nss-altfiles.git
Group: System/Libraries

ExcludeArch: armh i586

Source: %name-%version.tar

%description
NSS module which can read user information from files in the same format as
/etc/passwd and /etc/group stored in an alternate location (/usr/lib).

%prep
%setup

%build
%configure --datadir=/usr/lib
%make_build

%install
%makeinstall_std

%files
%_libdir/*

%changelog
* Wed Sep 15 2021 Andrey Sokolov <keremet@altlinux.org> 2.23.0-alt1
- 2.23.0
