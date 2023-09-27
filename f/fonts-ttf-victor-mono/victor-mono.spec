%define _unpackaged_files_terminate_build 1
%define oname VictorMono
%define fname victor-mono

Name: fonts-ttf-%fname
Version: 1.5.5
Release: alt1

Summary: A free programming font with cursive italics and ligatures
License: OFL-1.1
Group: System/Fonts/True type
Url: https://rubjo.github.io/victor-mono
Vcs: https://github.com/rubjo/victor-mono

BuildArch: noarch

Source: VictorMonoAll.zip

Requires(pre): fontconfig
BuildRequires(pre): rpm-build-fonts
BuildRequires: unzip

%description
Victor Mono is an open-source monospaced font with optional semi-connected
cursive italics and programming symbol ligatures.

The typeface is slender, crisp and narrow, with a large x-height and clear
punctuation, making it legible and ideal for code. It comes in seven weights
and Roman, Italic and Oblique styles.

%prep
%setup -c -n %oname

%install
cd TTF
%ttf_fonts_install %fname

%files -f TTF/%fname.files
%doc LICENSE.txt

%changelog
* Wed Sep 27 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.5.5-alt1
- Initial build for ALT Sisyphus

