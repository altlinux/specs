Name: dex
Version: 0.8.0
Release: alt1.git.3.g9e96e39
Summary: DesktopEntry Execution
Url: http://e-jc.de/dex/
License: GPLv3
Group:  System/Base
# https://github.com/jceb/dex/archive/v0.8.0.tar.gz
Source: %name-%version.tar
Source44: %name.watch

BuildArch: noarch
BuildRequires: python3-module-sphinx

%description
dex, DesktopEntry Execution, is a program to generate and execute DesktopEntry
files of the Application type.

%prep
%setup -n %name-%version
subst 's/@sphinx-build/@py3_sphinx-build/' Makefile

%install
%makeinstall_std \
	PREFIX=%_prefix \
	MANPREFIX=%_mandir \

mv %buildroot%_docdir/%name doc2install

%files
%doc doc2install/*
%doc CHANGELOG*
%_bindir/%{name}*
%_man1dir/*

%changelog
* Wed Feb 14 2018 Ildar Mulyukov <ildar@altlinux.ru> 0.8.0-alt1.git.3.g9e96e39
- 1st version for Sisyphus
