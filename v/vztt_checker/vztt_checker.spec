%define _libexecdir /usr/libexec

Summary: vztt_checker libraries for vzpkgenvs
Name: vztt_checker
Group: System/Configuration/Other
# git-vsc https://src.openvz.org/scm/ovzl/vztt_checker.git
Url: http://openvz.org/
License: GPLv2
Version: 7.0.2
Release: alt2
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
* Thu Dec 05 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.2-alt2
- fix License

* Fri Aug 23 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.2-alt1
- 7.0.2

* Mon Feb 26 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.1-alt1
- Initial build for ALT
