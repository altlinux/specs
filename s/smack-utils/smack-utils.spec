Name:     smack-utils
Version:  1.3.1
Release:  alt1

Summary:  Utils for Simplified Mandatory Access Control Kernel
License:  LGPL v2.1
Group:    System/Configuration/Other
Url:      https://github.com/smack-team/smack/

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++ autoconf

%description
Utils for labeling and other console-based tasks for SMACK

%package devel
Summary: devel files for SMACK 
Group: Development/C

%description devel
Devel files for Simplified Mandatory Access Control Kernel



%prep
%setup

%build
autoreconf -fisv
%__autoconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%_bindir/*
%_man1dir/*
%_man8dir/*
%_libdir/*.so*

%doc  NEWS COPYING

%files devel
%_includedir/sys/*
%_libdir/pkgconfig/*.pc


%changelog
* Sat Jan 06 2018 Denis Medvedev <nbr@altlinux.org> 1.3.1-alt1
Initial Sisyphus release
