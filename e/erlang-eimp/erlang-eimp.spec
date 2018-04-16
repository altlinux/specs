%global realname eimp

%set_verify_elf_method relaxed

# https://github.com/processone/eimp/issues/5
%def_disable check

Name: erlang-%realname
Version: 1.0.4
Release: alt1%ubt
Summary: Erlang Image Manipulation Process
Group: Development/Erlang
License: ASL 2.0
Url: https://github.com/processone/eimp

# https://github.com/processone/eimp.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-p1_utils
BuildRequires: libgd3-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libwebp-devel

%description
eimp is an Erlang/Elixir application for manipulating graphic images
using external C libraries. It supports WebP, JPEG, PNG and GIF.

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
* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt1%ubt
- Initial build for ALT.
