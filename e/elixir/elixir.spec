Name: elixir
Version: 1.5.2
Release: alt1
Summary: A modern approach to programming for the Erlang VM

Group: Development/Other
# See LEGAL (provided by upstream) for explaination/breakdown.
License: ASL 2.0
Url: http://elixir-lang.org/

Packager: Denis Medvedev <nbr@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): erlang-otp-full erlang-otp-devel
BuildRequires(pre): erlang-common_test-debug erlang-common_test-common
BuildRequires(pre): erlang-otp-native  erlang-common_test-native erlang-common_test
BuildRequires: git

%description
Elixir is a programming language built on top of the Erlang VM.
As Erlang, it is a functional language built to support distributed,
fault-tolerant, non-stop applications with hot code swapping.

%prep
%setup
%__subst "s/time //g" Makefile
find -name '*.bat' -exec rm \{\} \;

# This contains a failing test. We want `make test` for most tests, but
# this deals with ANSI codes which rpmbuild strips.
#rm lib/elixir/test/elixir/io/ansi_test.exs

%build
make

%check
export LANG="en_US.UTF-8"
make test

%install
mkdir -p %buildroot/%_datadir/%name/%version
cp -ra bin lib %buildroot/%_datadir/%name/%version

mkdir -p %buildroot/%_bindir
ln -s %_datadir/%name/%version/bin/{elixir,elixirc,iex,mix} %buildroot/%_bindir/

%files
%doc LICENSE
%_bindir/elixir
%_bindir/elixirc
%_bindir/iex
%_bindir/mix
%_datadir/%name

%changelog
* Wed Nov 01 2017 Denis Medvedev <nbr@altlinux.org> 1.5.2-alt1
- new version.

* Wed Apr 12 2017 Denis Medvedev <nbr@altlinux.org> 1.4.2-alt1
- new version 1.4.2

* Mon Sep 19 2016 Denis Medvedev <nbr@altlinux.org> 1.3.3-alt1
- initial build for ALT Linux Sisyphus
