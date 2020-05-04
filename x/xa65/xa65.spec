Name: xa65
Version: 2.3.5
Release: alt1

Summary: cross-assembler for the 6502 and 65816 CPUs

License: GPL-2.0-or-later
Group: Development/Other
Url: https://github.com/fachat/xa65

Source: %name-%version.tar

#BuildRequires:

%description
%summary

%prep
%setup

%build
pushd xa
%make_build
popd

%install
pushd xa
%make_install install DESTDIR=%buildroot%prefix
popd

%files
%_bindir/*
%_man1dir/*
%doc xa/README.1st

%changelog
* Mon May 04 2020 Anton Midyukov <antohami@altlinux.org> 2.3.5-alt1
- Initial build
