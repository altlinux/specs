%global realname ezlib

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.4
Release: alt1%ubt
Summary: Native zlib driver for Erlang / Elixir
Group: Development/Erlang
License: Apache 2.0
Url: https://github.com/processone/ezlib

# https://github.com/processone/ezlib.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: zlib-devel

%description
Native zlib driver for Erlang / Elixir. This library focuses on compression / decompression of data streams.

%prep
%setup

%build
%autoreconf
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
* Wed Apr 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt1%ubt
- Initial build for ALT.
