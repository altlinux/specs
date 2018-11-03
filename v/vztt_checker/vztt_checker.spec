%define _libexecdir /usr/libexec

Summary: vztt_checker libraries for vzpkgenvs
Name: vztt_checker
Group: System/Configuration/Other
Url: http://openvz.org/
License: GPL
Version: 7.0.1
Release: alt1
Source: %name-%version.tar
Patch: %name-%version.patch

%description
vztt_checker libraries for vzpkgenvs

%prep
%setup -q
%patch -p1

%build
%make CFLAGS="%optflags"

%install
%makeinstall_std

%files
%_libexecdir/*.so

%changelog
* Mon Feb 26 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.1-alt1
- Initial build for ALT
