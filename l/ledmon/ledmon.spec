%define optflags_lto %nil

Name:     ledmon
Version:  0.97
Release:  alt1

Summary:  This package contains the Enclosure LED Utilities
License:  GPL-2.0-only AND LGPL-2.1-only
Group:    Other
Url:      https://github.com/intel/ledmon.git

Source:   %name-%version.tar
Patch: %name-%version.patch

BuildRequires: libsgutils-devel libudev-devel glibc-devel /usr/bin/pod2man
BuildRequires: libpci-devel

%description
This package contains the Enclosure LED Utilities

%prep
%setup
%patch -p1

%build
%add_optflags -Wno-error=enum-int-mismatch -Wno-error=address -Wno-error=format-truncation
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_docdir/%name

%files
%doc COPYING *.md
%_sbindir/*
%_man5dir/*
%_man8dir/*

%changelog
* Wed Feb 14 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.97-alt1
- 0.97

* Wed Sep 04 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.92-alt1
- Initial import for ALT
