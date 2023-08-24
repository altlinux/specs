%define _unpackaged_files_terminate_build 1
%define oname FantasqueSansMono
%define fname fantasque-sans-mono

Name: fonts-ttf-%fname
Version: 1.8.0
Release: alt1

Summary: A font family with a great monospaced variant for programmers
License: OFL-1.1
Group: System/Fonts/True type
Url: https://github.com/belluzj/fantasque-sans
Vcs: https://github.com/belluzj/fantasque-sans

BuildArch: noarch

Source0: %oname.tar
Source1: LICENSE.txt

Requires(pre): fontconfig
BuildRequires(pre): rpm-build-fonts

%description
A programming font, designed with functionality in mind, and with some
wibbly-wobbly handwriting-like fuzziness that makes it unassumingly cool.
Previously known as Cosmic Sans Neue Mono. It appeared that similar names
were already in use for other fonts, and that people tended to extend
their instinctive hatred of Comic Sans to this very font of mine (which
of course can only be loved).

%prep
%setup -n %oname
cp %SOURCE1 %_builddir/%oname/

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc LICENSE.txt

%changelog
* Thu Aug 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.8.0-alt1
- Initial build for ALT Sisyphus

