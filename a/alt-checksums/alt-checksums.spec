Name:     alt-checksums
Version:  0.5
Release:  alt3

Summary:  check of sums of executables
License:  MIT
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/genspec.git

BuildArch: noarch


Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar


%description
Counting and checking of checksums of binary files installed from RPMs

%prep
%setup

%install
mkdir -p %buildroot%_sbindir
install -Dm 0600  alt-gensum %buildroot%_sbindir/alt-gensum

mkdir -p %buildroot%_docdir
install -Dm 0600 README.md  %buildroot%_docdir
install -Dm 0600 COPYING.md  %buildroot%_docdir


%files
%_sbindir/*
%doc *.md

%changelog
* Fri Nov 13 2020 Denis Medvedev <nbr@altlinux.org> 0.5-alt3
- added option to optionaly generate a list, instead to work on a default one

* Fri Nov 13 2020 Denis Medvedev <nbr@altlinux.org> 0.5-alt2
- fixed group

* Wed Nov 11 2020 Denis Medvedev <nbr@altlinux.org> 0.5-alt1
Initial version
