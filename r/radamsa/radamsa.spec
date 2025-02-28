%define _unpackaged_files_terminate_build 1
%def_with check

Name: radamsa
Version: 0.7
Release: alt1

Summary: Radamsa is a test case generator for robustness testing, a.k.a. a fuzzer

License: MIT
Group: Development/Tools
Url: https://gitlab.com/akihe/radamsa
VCS: https://gitlab.com/akihe/radamsa

Source: %name-%version.tar
Source1: ol.c
Patch: %name-%version-alt.patch

%description
It is typically used to test how well a program can withstand malformed and
potentially malicious inputs. It works by reading sample files of valid data
and generating interestringly different outputs from them. The main selling
points of radamsa are that it has already found a slew of bugs in programs that
actually matter, it is easily scriptable and, easy to get up and running.

%prep
%setup
%patch -p1
install -v %SOURCE1 .

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std

%check
%make test

%files
%doc LICENCE README.md
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Feb 27 2025 Anastasia Doronina <swaggyglice@altlinux.org> 0.7-alt1
- Initial Build for Sisyphus.
