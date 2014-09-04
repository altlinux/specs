Name: asciiquarium
Version: 1.1
Release: alt1

Summary: Aquarium/sea animation in ASCII art
License: GPL
Group: Toys
Url: http://www.robobunny.com/projects/asciiquarium/

Source: %url/%{name}_%version.tar.gz

BuildArch: noarch

BuildPreReq: perl-Curses perl-Term-Animation

%description
Asciiquarium is an aquarium/sea animation in ASCII art.

%prep
%setup -n %{name}_%version

%install
mkdir -p %buildroot%_bindir
install -p -m755 %name %buildroot%_bindir

%files
%_bindir/*
%doc CHANGES README

%changelog
* Thu Sep 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Version 1.1

* Mon Sep 19 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt1
- initial build
