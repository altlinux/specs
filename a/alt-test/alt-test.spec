Name:    alt-test
Version: 1.0
Release: alt1

Summary: Test environment based on Tapper
License: GPLv3+
Group:   System/Libraries
URL:     http://altlinux.org/alt-test

Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: perl-Tapper-Cmd
Requires: perl-devel
Requires: libshell

Source:  %name-%version.tar

BuildArch: noarch

%description
Test environment based on Tapper

%prep
%setup

%install
install -m 0755 -D %name %buildroot%_bindir/%name
install -m 0755 -D %name-functions %buildroot%_bindir/%name-functions
mkdir -p %buildroot%_libexecdir/%name
cp -av tests/* %buildroot%_libexecdir/%name/

%files
%_bindir/%{name}*
%_libexecdir/%name

%changelog
* Thu Oct 03 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
