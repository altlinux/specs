Name:     todo.txt-cli
Version:  2.11.0
Release:  alt1

Summary:  A simple and extensible shell script for managing your todo.txt file
License:  GPL-3.0
Group:    Text tools
Url:      https://github.com/todotxt/todo.txt-cli.git

Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch

Source:   %name-%version.tar

BuildRequires: bash4

%description
%summary

%prep
%setup

%build

%install
make install prefix=%_prefix DESTDIR=%buildroot

sed -i -e 's,/usr/bin/env bash,/bin/sh4,' %buildroot/usr/bin/*
pushd %buildroot
mv usr/etc .
mv usr/share/bash_completion.d etc
popd

%files
%_bindir/*
%_sysconfdir/todo
%_sysconfdir/bash_completion.d/*
%doc *.md

%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 2.11.0-alt1
- Initial build for Sisyphus
