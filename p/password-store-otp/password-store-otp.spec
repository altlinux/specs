%define _unpackaged_files_terminate_build 1

%def_without check

Name:     password-store-otp
Version:  1.2.0
Release:  alt1

Summary:  A pass extension for managing one-time-password (OTP) tokens
License:  %gpl3plus
Group:    Text tools
Url:      https://github.com/tadfisher/pass-otp

Source:   %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

%if_with check
BuildRequires: /proc
BuildRequires: git
BuildRequires: expect
BuildRequires: oathtool
BuildRequires: qrencode
BuildRequires: password-store >= 1.7.0
%endif

Requires: password-store >= 1.7.0
Requires: qrencode
Requires: oathtool

%filter_from_requires /libxforms-demos/d

%description
pass-otp extends the pass utility with the otp command for adding OTP secrets,
generating OTP codes, and displaying secret key URIs using the standard
otpauth:// scheme.

%prep
%setup

%install
%makeinstall_std

mv %buildroot%_man1dir/pass-otp.1 %buildroot%_man1dir/%name.1
mkdir -p %buildroot%_datadir/bash-completion/completions/
mv %buildroot%_sysconfdir/bash_completion.d/pass-otp  %buildroot%_datadir/bash-completion/completions/pass-otp

%check
%make test

%files
%doc README.md CHANGELOG.md
%_libexecdir/password-store/extensions/otp.bash
%_datadir/bash-completion/completions/pass-otp
%_man1dir/%name.*

%changelog
* Mon May 26 2025 Andrey Limachko <liannnix@altlinux.org> 1.2.0-alt1
- Fix HOTP counter increases (thx Juan Orti Alcaine)
- Initial build
