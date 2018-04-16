%global realname proper

Name: erlang-%realname
Version: 1.2
Release: alt1%ubt
Summary: A QuickCheck-inspired property-based testing tool for Erlang
Group: Development/Erlang
License: GPLv3+
BuildArch: noarch
Url: https://github.com/manopapad/proper

# https://github.com/manopapad/proper.git
Source: %name-%version.tar

Patch1: erlang-proper-fedora-add-timeout-values-that-work-on-ARM.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar

%description
PropEr (PROPerty-based testing tool for ERlang) is a QuickCheck-inspired
open-source property-based testing tool for Erlang.

%prep
%setup
%patch1 -p1

%build
%rebar_compile

%install
%rebar_install %realname

%check
export ERL_LIBS=%buildroot%_erllibdir
%rebar_eunit -C rebar.test.config

%files
%doc COPYING
%doc doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1%ubt
- Initial build for ALT.
