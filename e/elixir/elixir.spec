%define _unpackaged_files_terminate_build 1

%def_with check

Name: elixir
Version: 1.14.2
Release: alt2
Summary: A modern approach to programming for the Erlang VM
License: Apache-2.0
Group: Development/Other
Url: http://elixir-lang.org/
VCS: https://github.com/elixir-lang/elixir.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel
BuildRequires: erlang-otp-devel
BuildRequires: rebar

%if_with check
BuildRequires: /dev/pts
BuildRequires: git
%endif

%description
Elixir is a programming language built on top of the Erlang VM.
As Erlang, it is a functional language built to support distributed,
fault-tolerant, non-stop applications with hot code swapping.

%prep
%setup
find -name '*.bat' -exec rm \{\} \;

# Fix build with make 4.4
# https://github.com/elixir-lang/elixir/pull/12244
sed -i '/.NOTPARALLEL/ s/ compile//' Makefile

%build
export LANG="en_US.UTF-8"
%make_build compile
%make_build build_man

%install
mkdir -p %buildroot/%_datadir/%name/%version
cp -ra bin lib %buildroot/%_datadir/%name/%version

mkdir -p %buildroot/%_bindir
ln -s %_datadir/%name/%version/bin/{elixir,elixirc,iex,mix} %buildroot/%_bindir/

mkdir -p %buildroot/%_mandir/man1
cp -a man/elixir.1 man/elixirc.1 man/iex.1 man/mix.1 %buildroot/%_mandir/man1

%check
export LANG="en_US.UTF-8"
%make_build test

%files
%doc LICENSE
%_bindir/elixir
%_bindir/elixirc
%_bindir/iex
%_bindir/mix
%_datadir/%name
%_mandir/man1/*

%changelog
* Mon Nov 21 2022 Egor Ignatov <egori@altlinux.org> 1.14.2-alt2
- Fix build with make 4.4

* Fri Nov 11 2022 Egor Ignatov <egori@altlinux.org> 1.14.2-alt1
- 1.14.2

* Tue Oct 25 2022 Egor Ignatov <egori@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Oct 12 2021 Egor Ignatov <egori@altlinux.org> 1.12.3-alt1
- 1.12.3

* Wed Mar 11 2020 Pavel Skrylev <majioa@altlinux.org> 1.10.2-alt1
- ^ 1.9.2 -> 1.10.2

* Mon Oct 28 2019 Pavel Skrylev <majioa@altlinux.org> 1.9.2-alt1
- update (^) 1.7.4 -> 1.9.2
- disable (-) tests

* Thu Nov 15 2018 Pavel Skrylev <majioa@altlinux.org> 1.7.4-alt1
- Bump to 1.7.4

* Wed Nov 01 2017 Denis Medvedev <nbr@altlinux.org> 1.5.2-alt1
- new version.

* Wed Apr 12 2017 Denis Medvedev <nbr@altlinux.org> 1.4.2-alt1
- new version 1.4.2

* Mon Sep 19 2016 Denis Medvedev <nbr@altlinux.org> 1.3.3-alt1
- initial build for ALT Linux Sisyphus
