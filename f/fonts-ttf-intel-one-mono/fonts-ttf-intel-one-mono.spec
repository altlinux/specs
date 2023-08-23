%define _unpackaged_files_terminate_build 1
%define oname IntelOneMono
%define fname intel-one-mono

Name: fonts-ttf-%fname
Version: 1.3.0
Release: alt1

Summary: Intel One Mono font
License: OFL-1.1
Group: System/Fonts/True type
Url: https://github.com/intel/intel-one-mono
Vcs: https://github.com/intel/intel-one-mono

BuildArch: noarch

Source: %oname.tar

Requires(pre): fontconfig
BuildRequires(pre): rpm-build-fonts

%description
Introducing Intel One Mono, an expressive monospaced font family
that's built with clarity, legibility, and the needs of developers
in mind.

It's easier to read, and available for free, with an open-source
font license.

Identifying the typographically underserved low-vision developer
audience, Frere-Jones Type designed the Intel One Mono typeface in
partnership with the Intel Brand Team and VMLY&R, for maximum
legibility to address developers' fatigue and eyestrain and reduce
coding errors. A panel of low-vision and legally blind developers
provided feedback at each stage of design.

Intel One Mono also covers a wide range of over 200 languages using
the Latin script. The Intel One Mono fonts are provided in four
weights - Light, Regular, Medium, and Bold - with matching italics,
and we are happy to share both an official release of fonts ready
to use as well as editable sources.

%prep
%setup -n %oname

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc OFL.txt

%changelog
* Wed Aug 23 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Built for ALT Sisyphus.

