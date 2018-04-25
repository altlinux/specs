%global realname stringprep

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.11
Release: alt1%ubt
Summary: Fast Stringprep implementation for Erlang / Elixir
Group: Development/Erlang
License: Tcl/Tk and ASL 2.0
Url: https://github.com/processone/stringprep

# https://github.com/processone/stringprep.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils
BuildRequires: gcc-c++

%description
Stringprep is a framework for preparing Unicode test strings
in order to increase the likelihood that string input and string comparison work.

The principle are defined in RFC-3454: Preparation of Internationalized Strings.
This library is leverage Erlang native NIF mechanism to provide extremely fast and efficient processing.
The library includes support for several Stringprep profiles used in XMPP protocole like:
    Nodeprep
    Nameprep
    Resourceprep

%prep
%setup

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE.*
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.11-alt1%ubt
- Initial build for ALT.
