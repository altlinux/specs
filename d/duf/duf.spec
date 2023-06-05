Name: duf
Version: 0.8.1
Release: alt1

Summary: Disk Usage/Free Utility - a better 'df' alternative

License: MIT and BSD
Group: File tools
Url: https://github.com/muesli/duf

# Source-url: https://github.com/muesli/duf/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded modules during update version with rpmgs from etersoft-build-utils
Source1: %name-development-%version.tar

BuildRequires: rpm-build-golang

%description
Disk Usage/Free Utility - a better 'df' alternative.

%prep
%setup -a1
chmod u+w -R *

%build
export GOPATH=$(pwd)/vendor
go build

%install
install -m 0755 -D duf %buildroot%_bindir/duf
install -m 0644 -D duf.1 %buildroot%_man1dir/duf.1

%files
%doc LICENSE README.md
%_bindir/duf
%_man1dir/duf.1*

%changelog
* Mon Jun 05 2023 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- initial build for ALT Sisyphus
