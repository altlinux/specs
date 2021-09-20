Name: libnss-altfiles
Version: 2.23.0
Release: alt2

Summary: NSS module which can read user information from files

License: LGPLv2.1
URL: https://github.com/aperezdc/nss-altfiles.git
Group: System/Libraries

Source: %name-%version.tar

%description
NSS module which can read user information from files in the same format as
/etc/passwd and /etc/group stored in an alternate location (/lib).

%prep
%setup

%build
./configure --datadir=/lib --libdir=/%_lib CFLAGS="%optflags"
%make_build

%install
%makeinstall_std

%files
/%_lib/*

%changelog
* Fri Sep 17 2021 Andrey Sokolov <keremet@altlinux.org> 2.23.0-alt2
- Change data directory to /lib
- Build for all architectures
- Change directory for library
- Use ./configure instead of macro

* Wed Sep 15 2021 Andrey Sokolov <keremet@altlinux.org> 2.23.0-alt1
- 2.23.0
