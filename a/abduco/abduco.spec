Summary:  Terminal multiplexer

Name: abduco
Version: 0.6.55.gae7dd80
Release: alt1
License: ISC
Group: Terminals
Url: https://github.com/legionus/abduco
Packager: Alexey Gladkov <legion@altlinux.org>

Source0: %name-%version.tar

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%description
abduco provides session management i.e. it allows programs to be run
independently from their controlling terminal. That is programs can be detached
- run in the background - and then later reattached.

%prep
%setup

%build
# non-autotools configure :(
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/*

%changelog
* Thu Dec 02 2021 Alexey Gladkov <legion@altlinux.ru> 0.6.55.gae7dd80-alt1
- First build for sisyphus.

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_8
- new version
