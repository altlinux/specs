%define _unpackaged_files_terminate_build 1

%global realname iconv

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.10
Release: alt1
Summary: Fast encoding conversion library for Erlang / Elixir
Group: Development/Erlang
License: ASL 2.0
Url: https://github.com/processone/iconv

# https://github.com/processone/iconv.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils

%description
Erlang bindings for libiconv.

%prep
%setup

%build
%configure
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit

%files
%doc LICENSE.txt
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Updated to upstream version 1.0.10.

* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt1
- Initial build for ALT.
