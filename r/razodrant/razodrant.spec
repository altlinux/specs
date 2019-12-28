Name:     razodrant
Version:  0.3
Release:  alt1

Summary:  Razodrant produces list of source RPMs which were used in the installer or livecd image for building corresponding RPMs
License:  GPLv2+
Group:    Other
Url:      http://git.altlinux.org/people/nbr/razodrant.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
Razodrant produces list of source RPMs which were used in
installer or livecd image for building corresponding RPMs.
No src rpms which were used to produce installer code
are mentioned - you better use image build logs for those.

%prep
%setup

%install
install -Dm 0755 razodrant.sh %buildroot%_bindir/razodrant

%files
%_bindir/*

%changelog
* Sat Dec 28 2019 Denis Medvedev <nbr@altlinux.org> 0.3-alt1
Initial release
