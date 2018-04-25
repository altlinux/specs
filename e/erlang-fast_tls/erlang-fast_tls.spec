%global realname fast_tls

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.21
Release: alt1%ubt
Summary: TLS / SSL OpenSSL-based native driver for Erlang / Elixir
Group: Development/Erlang
License: ASL 2.0
Url: https://github.com/processone/fast_tls

# https://github.com/processone/fast_tls.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils
BuildRequires: openssl-devel

%description
Fast TLS is a native TLS / SSL driver for Erlang / Elixir.
It is based on OpenSSL, a proven and efficient TLS implementation.

It is designed for efficiency, speed and compliance.

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE.txt
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.21-alt1%ubt
- Initial build for ALT.
