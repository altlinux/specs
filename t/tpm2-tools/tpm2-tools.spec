%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var

Name: tpm2-tools
Version: 5.5
Release: alt1
Summary: A bunch of TPM testing toolS build upon tpm2-tss
Group: System/Configuration/Other

License: BSD
Url: https://github.com/tpm2-software/tpm2-tools
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: autoconf-archive
BuildRequires: pandoc
BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(openssl) libssl-devel pkgconfig(libcrypto) >= 1.1.0
BuildRequires: pkgconfig(tss2-mu) >= 3.1.0
BuildRequires: pkgconfig(tss2-sys) >= 3.1.0
BuildRequires: pkgconfig(tss2-esys) >= 3.1.0
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(efivar)

Requires: libtpm2-tss0 >= 3.1.0

%description
tpm2-tools is a batch of tools for tpm2.0. It is based on tpm2-tss.

%prep
%setup
%patch -p1
echo %version > VERSION

%build
./bootstrap
#%%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc docs/LICENSE
%doc README.md docs/CHANGELOG.md
%_bindir/*
%_datadir/bash-completion/completions/*
%_man1dir/*

%changelog
* Sat Feb 18 2023 Alexey Shabalin <shaba@altlinux.org> 5.5-alt1
- new version 5.5

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 5.2-alt1
- new version 5.2

* Tue Aug 31 2021 Alexey Shabalin <shaba@altlinux.org> 5.1.1-alt2
- Up release for greater then in fedoraimport.

* Sat Aug 28 2021 Alexey Shabalin <shaba@altlinux.org> 5.1.1-alt1
- Initial build.

