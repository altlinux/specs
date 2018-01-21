%define realname mokutil

Name: mokutil-0.5
Version: 0.5.0
Release: alt1
Summary: Tool to manage UEFI Secure Boot MoK Keys
License: GPLv3+
Url: https://github.com/lcp/mokutil
Group: System/Configuration/Hardware
BuildRequires: libefivar-devel libssl-devel
ExclusiveArch: %ix86 x86_64 aarch64
Source0: https://github.com/lcp/mokutil/archive/%{realname}-%{version}.tar.gz
Patch: %name-%version-%release.patch
Obsoletes: mokutil <= 0.4
Conflicts: mokutil

%description
mokutil provides a tool to manage keys for Secure Boot through the MoK
("Machine's Own Keys") mechanism.

%prep
%setup -n %realname-%version
%patch -p1

%build
%autoreconf
%configure \
	--with-bash-completion-dir=%_sysconfdir/bash_completion.d
%make

%install
make PREFIX=%_prefix LIBDIR=%_libdir DESTDIR=%buildroot install

%files
%doc README COPYING
%_bindir/%realname
%_man1dir/*
%_sysconfdir/bash_completion.d/%realname

%changelog
* Wed Jan 10 2018 L.A. Kostis <lakostis@altlinux.ru> 0.5.0-alt1
- Separate build from upstream sources (GIT e19adc5).
- Added Obsoletes for existing package build from shim sources.
