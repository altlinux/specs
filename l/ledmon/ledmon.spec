%define optflags_lto %nil

Name:     ledmon
Version:  0.92
Release:  alt1

Summary:  This package contains the Enclosure LED Utilities
License:  LGPL-2.1-or-later
Group:    Other
Url:      https://github.com/intel/ledmon.git

Source:   %name-%version.tar
Patch: %name-%version.patch

BuildRequires: libsgutils-devel libudev-devel glibc-devel /usr/bin/pod2man

%description
This package contains the Enclosure LED Utilities

%prep
%setup
%patch -p1

%build
%remove_optflags -Wno-error
%add_optflags -Wno-error=address-of-packed-member -Wno-error=format-truncation
./autogen.sh
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_docdir/%name

%files
%doc README COPYING *.md
%_sbindir/*
%_man5dir/*
%_man8dir/*

%changelog
* Wed Sep 04 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.92-alt1
- Initial import for ALT
