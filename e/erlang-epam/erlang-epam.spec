%global realname epam

%set_verify_elf_method relaxed

Name: erlang-%realname
Version: 1.0.4
Release: alt1%ubt
Summary: Library for ejabberd for PAM authentication support
Group: Development/Erlang
License: Apache 2.0
Url: https://github.com/processone/epam

# https://github.com/processone/epam.git
Source: %name-%version.tar

# Load epam from this package rather than from ejabberd.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1337216 and
# https://github.com/processone/epam/issues/4
Patch1: erlang-epam-fedora-load-epam-from-the-package-s-own-path-rather-than-ej.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: libpam-devel

%description
An Erlang library for ejabberd that helps with PAM authentication.

%prep
%setup
%patch1 -p1

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
